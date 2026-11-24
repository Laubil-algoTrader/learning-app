"""Read side, custom exercises, and attempt log for the Exercises section.

Built-in exercises live in code (backend/exercises); user-created exercises live in the
`custom_exercises` SQLite table. Both are merged seamlessly everywhere exercises are read.
"""

from __future__ import annotations

from datetime import timedelta
import json
import re
from typing import Any

from backend import fsrs
from backend.db import Database
from backend.exercises.registry import EXERCISES, EXERCISES_BY_ID, EXERCISES_BY_NODE

# A topic is flagged for re-reading once this many of its exercises have been
# attempted without ever being solved.
STRUGGLING_AFTER_UNSOLVED = 2


def _parse_custom_row(row) -> dict[str, Any]:
    return {
        "id": row["id"],
        "node": row["node_slug"],
        "kind": "problem",
        "title": row["title"],
        "level": int(row["level"] or 1),
        "minutes": int(row["minutes"] or 5),
        "statement": row["statement"],
        "parts": json.loads(row["parts_json"] or "[]"),
        "hints": json.loads(row["hints_json"] or "[]"),
        "solution": json.loads(row["solution_json"] or "[]"),
        "custom": True,
        "source": "",
    }


def load_custom_exercises(conn) -> list[dict[str, Any]]:
    rows = conn.execute("SELECT * FROM custom_exercises ORDER BY created_at ASC").fetchall()
    return [_parse_custom_row(r) for r in rows]


def all_exercises_by_id(conn) -> dict[str, dict[str, Any]]:
    merged = dict(EXERCISES_BY_ID)
    for ex in load_custom_exercises(conn):
        merged[ex["id"]] = ex
    return merged


def all_exercises_by_node(conn) -> dict[str, list[dict[str, Any]]]:
    merged: dict[str, list[dict[str, Any]]] = {k: list(v) for k, v in EXERCISES_BY_NODE.items()}
    for ex in load_custom_exercises(conn):
        merged.setdefault(ex["node"], []).append(ex)
    return merged


def _statuses(conn) -> dict[str, dict[str, Any]]:
    now = fsrs.utc_now()
    rows = conn.execute(
        """
        SELECT exercise_id,
               COUNT(*) AS attempts,
               SUM(CASE WHEN correct = 0 THEN 1 ELSE 0 END) AS fails,
               MAX(correct) AS solved,
               MAX(CASE WHEN correct = 1 AND saw_solution = 0 THEN 1 ELSE 0 END) AS solved_unaided,
               MAX(saw_solution) AS saw_solution,
               MAX(created_at) AS last_attempt_at
        FROM exercise_attempts
        GROUP BY exercise_id
        """
    ).fetchall()
    last_tags = {
        r["exercise_id"]: r["error_tag"]
        for r in conn.execute(
            """
            SELECT exercise_id, error_tag FROM exercise_attempts
            WHERE TRIM(error_tag) != '' ORDER BY id ASC
            """
        ).fetchall()
    }
    out: dict[str, dict[str, Any]] = {}
    for r in rows:
        solved_unaided = bool(r["solved_unaided"])
        solved = bool(r["solved"])
        last_at = r["last_attempt_at"]
        next_retry_at = None
        retry_due = False
        if not solved_unaided and last_at:
            dt = fsrs.parse_iso(last_at)
            if dt is not None:
                # Failed exercises resurface after 1 day; solution-assisted after 2 days
                delay_days = 2 if solved else 1
                due_dt = dt + timedelta(days=delay_days)
                next_retry_at = fsrs.to_iso(due_dt)
                retry_due = due_dt <= now
        out[r["exercise_id"]] = {
            "attempts": r["attempts"],
            "fails": int(r["fails"] or 0),
            "solved": solved,
            "solved_unaided": solved_unaided,
            "saw_solution": bool(r["saw_solution"]),
            "last_attempt_at": last_at,
            "next_retry_at": next_retry_at,
            "retry_due": retry_due,
            "error_tag": last_tags.get(r["exercise_id"], ""),
        }
    return out


_NEVER_TRIED = {
    "attempts": 0,
    "fails": 0,
    "solved": False,
    "solved_unaided": False,
    "saw_solution": False,
    "last_attempt_at": None,
    "next_retry_at": None,
    "retry_due": False,
    "error_tag": "",
}


def _status(statuses: dict[str, dict[str, Any]], exercise_id: str) -> dict[str, Any]:
    return dict(statuses.get(exercise_id, _NEVER_TRIED))


def count_for_node(node_slug: str, db: Database | None = None) -> int:
    """How many exercises a topic has (including custom exercises when db is provided)."""
    base = len(EXERCISES_BY_NODE.get(node_slug, []))
    if db is None:
        return base
    with db.connect() as conn:
        extra = conn.execute(
            "SELECT COUNT(*) FROM custom_exercises WHERE node_slug = ?", (node_slug,)
        ).fetchone()[0]
    return base + int(extra or 0)


def overview(db: Database) -> dict[str, Any]:
    """One entry per discipline that has exercises, with solved/total counts."""
    with db.connect() as conn:
        statuses = _statuses(conn)
        by_node = all_exercises_by_node(conn)
        domains = conn.execute("SELECT id, slug, name, lab_type FROM domains ORDER BY id ASC").fetchall()
        result = []
        for d in domains:
            slugs = [
                r["slug"]
                for r in conn.execute("SELECT slug FROM nodes WHERE domain_id = ?", (d["id"],)).fetchall()
            ]
            exercises = [e for slug in slugs for e in by_node.get(slug, [])]
            if not exercises:
                continue
            result.append(
                {
                    "slug": d["slug"],
                    "name": d["name"],
                    "lab_type": d["lab_type"],
                    "kind": "project" if all(e["kind"] == "project" for e in exercises) else "problem",
                    "total": len(exercises),
                    "solved": sum(1 for e in exercises if statuses.get(e["id"], {}).get("solved")),
                    "attempted": sum(1 for e in exercises if e["id"] in statuses),
                    "topics_with_exercises": sum(1 for slug in slugs if slug in by_node),
                    "topics_total": len(slugs),
                }
            )
    return {"domains": result}


def domain_exercises(db: Database, domain_slug: str) -> dict[str, Any]:
    """Every topic of a discipline that has exercises, each exercise with its status."""
    with db.connect() as conn:
        d = conn.execute("SELECT id, slug, name, lab_type FROM domains WHERE slug = ?", (domain_slug,)).fetchone()
        if not d:
            raise KeyError(f"Disciplina no encontrada: {domain_slug}")
        statuses = _statuses(conn)
        by_node = all_exercises_by_node(conn)
        nodes = conn.execute(
            """
            SELECT id, slug, title, order_index, metadata_json, lesson_completed_at
            FROM nodes WHERE domain_id = ? ORDER BY level ASC, order_index ASC, id ASC
            """,
            (d["id"],),
        ).fetchall()

    topics = []
    for n in nodes:
        exercises = by_node.get(n["slug"])
        if not exercises:
            continue
        items = [{**e, "status": _status(statuses, e["id"])} for e in exercises]
        unsolved_tried = sum(1 for e in items if e["status"]["attempts"] and not e["status"]["solved"])
        topics.append(
            {
                "node_id": n["id"],
                "slug": n["slug"],
                "title": n["title"],
                "order_index": n["order_index"],
                "section": json.loads(n["metadata_json"] or "{}").get("section", ""),
                "lesson_completed": bool(n["lesson_completed_at"]),
                "struggling": unsolved_tried >= STRUGGLING_AFTER_UNSOLVED,
                "solved": sum(1 for e in items if e["status"]["solved"]),
                "exercises": items,
            }
        )
    total = sum(len(t["exercises"]) for t in topics)
    return {
        "domain": dict(d),
        "topics": topics,
        "totals": {
            "total": total,
            "solved": sum(t["solved"] for t in topics),
            "topics_with_exercises": len(topics),
            "topics_total": len(nodes),
        },
    }


def list_retry_exercises(db: Database, domain_slug: str | None = None, due_only: bool = False) -> dict[str, Any]:
    """All attempted exercises not yet solved unaided, ordered with overdue/failed first."""
    with db.connect() as conn:
        statuses = _statuses(conn)
        by_id = all_exercises_by_id(conn)
        nodes_map = {
            r["slug"]: dict(r)
            for r in conn.execute(
                """
                SELECT n.id AS node_id, n.slug, n.title, d.slug AS domain_slug, d.name AS domain_name, d.lab_type
                FROM nodes n JOIN domains d ON d.id = n.domain_id
                """
            ).fetchall()
        }
    items = []
    for ex_id, st in statuses.items():
        if st["solved_unaided"]:
            continue
        if due_only and not st["retry_due"]:
            continue
        ex = by_id.get(ex_id)
        if not ex or ex.get("kind") != "problem":
            continue
        node = nodes_map.get(ex["node"])
        if not node:
            continue
        if domain_slug and node["domain_slug"] != domain_slug:
            continue
        items.append(
            {
                **ex,
                "status": st,
                "topic": {
                    "node_id": node["node_id"],
                    "slug": node["slug"],
                    "title": node["title"],
                    "domain_slug": node["domain_slug"],
                    "domain_name": node["domain_name"],
                    "lab_type": node["lab_type"],
                },
            }
        )
    items.sort(key=lambda x: (not x["status"]["retry_due"], x["status"]["solved"], -x["status"]["fails"]))
    return {"exercises": items, "total": len(items), "due_count": sum(1 for x in items if x["status"]["retry_due"])}


def create_custom_exercise(db: Database, payload: dict[str, Any]) -> dict[str, Any]:
    node_id = int(payload.get("node_id") or 0)
    title = str(payload.get("title") or "").strip()
    statement = str(payload.get("statement") or "").strip()
    if not node_id or not title or not statement:
        raise ValueError("Tema, título y enunciado son obligatorios.")
    parts = payload.get("parts") or []
    if not isinstance(parts, list) or not parts:
        raise ValueError("El ejercicio necesita al menos una pregunta con respuesta.")
    for p in parts:
        if not str(p.get("prompt") or "").strip() or not isinstance(p.get("check"), dict):
            raise ValueError("Cada inciso necesita consigna y criterio de corrección.")
    hints = [str(h).strip() for h in (payload.get("hints") or []) if str(h).strip()]
    solution = [str(s).strip() for s in (payload.get("solution") or []) if str(s).strip()]
    level = max(1, min(3, int(payload.get("level") or 1)))
    minutes = max(1, min(60, int(payload.get("minutes") or 5)))
    now_iso = fsrs.to_iso(fsrs.utc_now())

    with db.connect() as conn:
        row = conn.execute(
            "SELECT n.slug AS node_slug, d.slug AS domain_slug FROM nodes n JOIN domains d ON d.id = n.domain_id WHERE n.id = ?",
            (node_id,),
        ).fetchone()
        if not row:
            raise KeyError("Tema no encontrado.")
        base_slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:24] or "custom"
        count = conn.execute("SELECT COUNT(*) FROM custom_exercises WHERE node_slug = ?", (row["node_slug"],)).fetchone()[0]
        ex_id = f"custom-{row['node_slug']}-{base_slug}-{count + 1}"
        while conn.execute("SELECT 1 FROM custom_exercises WHERE id = ?", (ex_id,)).fetchone():
            count += 1
            ex_id = f"custom-{row['node_slug']}-{base_slug}-{count + 1}"
        conn.execute(
            """
            INSERT INTO custom_exercises(
                id, domain_slug, node_slug, title, level, minutes, statement,
                parts_json, hints_json, solution_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                ex_id,
                row["domain_slug"],
                row["node_slug"],
                title,
                level,
                minutes,
                statement,
                json.dumps(parts, ensure_ascii=False),
                json.dumps(hints, ensure_ascii=False),
                json.dumps(solution, ensure_ascii=False),
                now_iso,
            ),
        )
        created = conn.execute("SELECT * FROM custom_exercises WHERE id = ?", (ex_id,)).fetchone()
    return _parse_custom_row(created)


def delete_custom_exercise(db: Database, exercise_id: str) -> bool:
    with db.connect() as conn:
        cur = conn.execute("DELETE FROM custom_exercises WHERE id = ?", (exercise_id,))
        return cur.rowcount > 0


def log_attempt(db: Database, exercise_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Record one graded attempt (or a project marked as done) and return the new status."""
    with db.connect() as conn:
        exercise = all_exercises_by_id(conn).get(exercise_id)
        if exercise is None:
            raise KeyError(f"Ejercicio no encontrado: {exercise_id}")
        parts_total = len(exercise.get("parts") or exercise.get("done_when") or [])
        parts_ok = max(0, min(int(payload.get("parts_ok", 0)), parts_total))
        correct = bool(payload.get("correct")) and parts_ok == parts_total
        row = conn.execute(
            """
            SELECT d.slug AS domain_slug FROM nodes n JOIN domains d ON d.id = n.domain_id
            WHERE n.slug = ? ORDER BY d.id ASC LIMIT 1
            """,
            (exercise["node"],),
        ).fetchone()
        if not row:
            raise KeyError(f"El tema de este ejercicio ya no existe: {exercise['node']}")
        error_tag = str(payload.get("error_tag") or "").strip().lower()
        conn.execute(
            """
            INSERT INTO exercise_attempts(exercise_id, node_slug, domain_slug, correct, parts_ok, parts_total, saw_solution, error_tag, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                exercise_id,
                exercise["node"],
                row["domain_slug"],
                1 if correct else 0,
                parts_ok,
                parts_total,
                1 if payload.get("saw_solution") else 0,
                error_tag,
                fsrs.to_iso(fsrs.utc_now()),
            ),
        )
        status = _status(_statuses(conn), exercise_id)
    return {"exercise_id": exercise_id, "correct": correct, "status": status}

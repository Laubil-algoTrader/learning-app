"""Read side and attempt log for the Exercises section.

Exercises are static content (see backend/exercises); what the database holds is only
the learner's attempts. Everything here is derived from those two sources.
"""

from __future__ import annotations

import json
from typing import Any

from backend import fsrs
from backend.db import Database
from backend.exercises.registry import EXERCISES_BY_ID, EXERCISES_BY_NODE

# A topic is flagged for re-reading once this many of its exercises have been
# attempted without ever being solved.
STRUGGLING_AFTER_UNSOLVED = 2


def _statuses(conn) -> dict[str, dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT exercise_id,
               COUNT(*) AS attempts,
               MAX(correct) AS solved,
               MAX(CASE WHEN correct = 1 AND saw_solution = 0 THEN 1 ELSE 0 END) AS solved_unaided,
               MAX(created_at) AS last_attempt_at
        FROM exercise_attempts
        GROUP BY exercise_id
        """
    ).fetchall()
    return {
        r["exercise_id"]: {
            "attempts": r["attempts"],
            "solved": bool(r["solved"]),
            "solved_unaided": bool(r["solved_unaided"]),
            "last_attempt_at": r["last_attempt_at"],
        }
        for r in rows
    }


_NEVER_TRIED = {"attempts": 0, "solved": False, "solved_unaided": False, "last_attempt_at": None}


def _status(statuses: dict[str, dict[str, Any]], exercise_id: str) -> dict[str, Any]:
    return dict(statuses.get(exercise_id, _NEVER_TRIED))


def count_for_node(node_slug: str) -> int:
    """How many exercises a topic has (0 when none were written for it yet)."""
    return len(EXERCISES_BY_NODE.get(node_slug, []))


def overview(db: Database) -> dict[str, Any]:
    """One entry per discipline that has exercises, with solved/total counts."""
    with db.connect() as conn:
        statuses = _statuses(conn)
        domains = conn.execute("SELECT id, slug, name, lab_type FROM domains ORDER BY id ASC").fetchall()
        result = []
        for d in domains:
            slugs = [
                r["slug"]
                for r in conn.execute("SELECT slug FROM nodes WHERE domain_id = ?", (d["id"],)).fetchall()
            ]
            exercises = [e for slug in slugs for e in EXERCISES_BY_NODE.get(slug, [])]
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
                    "topics_with_exercises": sum(1 for slug in slugs if slug in EXERCISES_BY_NODE),
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
        nodes = conn.execute(
            """
            SELECT id, slug, title, order_index, metadata_json, lesson_completed_at
            FROM nodes WHERE domain_id = ? ORDER BY level ASC, order_index ASC, id ASC
            """,
            (d["id"],),
        ).fetchall()

    topics = []
    for n in nodes:
        exercises = EXERCISES_BY_NODE.get(n["slug"])
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


def log_attempt(db: Database, exercise_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Record one graded attempt (or a project marked as done) and return the new status."""
    exercise = EXERCISES_BY_ID.get(exercise_id)
    if exercise is None:
        raise KeyError(f"Ejercicio no encontrado: {exercise_id}")
    parts_total = len(exercise.get("parts") or exercise.get("done_when") or [])
    parts_ok = max(0, min(int(payload.get("parts_ok", 0)), parts_total))
    correct = bool(payload.get("correct")) and parts_ok == parts_total
    with db.connect() as conn:
        row = conn.execute(
            """
            SELECT d.slug AS domain_slug FROM nodes n JOIN domains d ON d.id = n.domain_id
            WHERE n.slug = ? ORDER BY d.id ASC LIMIT 1
            """,
            (exercise["node"],),
        ).fetchone()
        if not row:
            raise KeyError(f"El tema de este ejercicio ya no existe: {exercise['node']}")
        conn.execute(
            """
            INSERT INTO exercise_attempts(exercise_id, node_slug, domain_slug, correct, parts_ok, parts_total, saw_solution, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                exercise_id,
                exercise["node"],
                row["domain_slug"],
                1 if correct else 0,
                parts_ok,
                parts_total,
                1 if payload.get("saw_solution") else 0,
                fsrs.to_iso(fsrs.utc_now()),
            ),
        )
        status = _status(_statuses(conn), exercise_id)
    return {"exercise_id": exercise_id, "correct": correct, "status": status}

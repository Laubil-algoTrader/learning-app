"""Study platform services: mock exams, error bank, cheat sheets, notes, diagnostics, search and analytics."""

from __future__ import annotations

from collections import Counter
from datetime import date, timedelta
import json
import unicodedata
from typing import Any

from backend import exercise_store, fsrs, ingreso_uncuyo
from backend.db import Database, local_day
from backend.exercises.registry import EXERCISES_BY_ID, EXERCISES_BY_NODE
from backend.lessons_data import LESSONS_BY_SLUG

ERROR_TAGS = {
    "planteo": "Planteo / estrategia",
    "calculo": "Álgebra / cálculo",
    "formula": "Fórmula / propiedad",
    "unidades": "Unidades / cifras",
    "lectura": "Lectura de consigna",
}


def _resolve_lesson(slug: str, raw_lesson_json: str | None) -> dict[str, Any]:
    custom = json.loads(raw_lesson_json or "{}")
    return custom if custom.get("hook") else (LESSONS_BY_SLUG.get(slug) or {})


def _norm(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", str(text or ""))
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn").lower().strip()


# ---------- Today's study activity ----------


def get_today_activity(db: Database) -> dict[str, int]:
    today = local_day(fsrs.to_iso(fsrs.utc_now()))
    settings = db.get_settings()
    with db.connect() as conn:
        lessons = sum(
            1
            for r in conn.execute(
                "SELECT lesson_completed_at FROM nodes WHERE lesson_completed_at IS NOT NULL"
            ).fetchall()
            if local_day(r["lesson_completed_at"]) == today
        )
        ex_solved_today = len(
            {
                r["exercise_id"]
                for r in conn.execute(
                    "SELECT exercise_id, created_at FROM exercise_attempts WHERE correct = 1"
                ).fetchall()
                if local_day(r["created_at"]) == today
            }
        )
        review_rows = conn.execute("SELECT duration_sec, created_at FROM review_logs").fetchall()
        reviews_today = sum(1 for r in review_rows if local_day(r["created_at"]) == today)
        review_sec_today = sum(
            int(r["duration_sec"] or 0) for r in review_rows if local_day(r["created_at"]) == today
        )
        exam_sec_today = sum(
            int(r["duration_sec"] or 0)
            for r in conn.execute("SELECT duration_sec, created_at FROM exam_attempts").fetchall()
            if local_day(r["created_at"]) == today
        )
    return {
        "lessons": lessons,
        "exercises": ex_solved_today,
        "reviews": reviews_today,
        "study_seconds_today": review_sec_today + exam_sec_today,
        "lesson_goal": settings["daily_lesson_goal"],
        "exercise_goal": settings["daily_exercise_goal"],
    }


# ---------- Mock exams (simulacros) ----------


def list_exams(db: Database, domain_slug: str | None = None, limit: int = 30) -> dict[str, Any]:
    with db.connect() as conn:
        if domain_slug:
            rows = conn.execute(
                "SELECT * FROM exam_attempts WHERE domain_slug = ? ORDER BY created_at DESC LIMIT ?",
                (domain_slug, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM exam_attempts ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
    exams = []
    for r in rows:
        proc_score = r["procedure_score_pct"] if "procedure_score_pct" in r.keys() else None
        exams.append(
            {
                "id": r["id"],
                "domain_slug": r["domain_slug"],
                "mode": r["mode"],
                "title": r["title"],
                "units": json.loads(r["units_json"] or "[]"),
                "score_pct": r["score_pct"],
                "procedure_score_pct": proc_score,
                "effective_score_pct": proc_score if proc_score is not None else r["score_pct"],
                "passed": bool(r["passed"]),
                "correct_count": r["correct_count"],
                "total_count": r["total_count"],
                "duration_sec": r["duration_sec"],
                "time_limit_sec": r["time_limit_sec"],
                "details": json.loads(r["details_json"] or "[]"),
                "created_at": r["created_at"],
            }
        )
    scores = [e["effective_score_pct"] for e in exams]
    return {
        "exams": exams,
        "stats": {
            "count": len(exams),
            "passed": sum(1 for e in exams if e["passed"]),
            "best_score": max(scores) if scores else None,
            "avg_score": round(sum(scores) / len(scores)) if scores else None,
            "last_score": scores[0] if scores else None,
        },
    }


def log_exam(db: Database, payload: dict[str, Any]) -> dict[str, Any]:
    domain_slug = str(payload.get("domain_slug") or "").strip()
    if not domain_slug:
        raise ValueError("Falta domain_slug para guardar el simulacro.")
    total_count = max(1, int(payload.get("total_count") or 0))
    correct_count = max(0, min(int(payload.get("correct_count") or 0), total_count))
    score_pct = int(payload.get("score_pct", round(100 * correct_count / total_count)))
    score_pct = max(0, min(score_pct, 100))
    proc_raw = payload.get("procedure_score_pct")
    procedure_score_pct = max(0, min(100, int(proc_raw))) if proc_raw is not None else None
    effective_score = procedure_score_pct if procedure_score_pct is not None else score_pct
    passed = 1 if effective_score >= ingreso_uncuyo.COURSE["pass_mark"] else 0
    mode = str(payload.get("mode") or "ingreso")[:40]
    title = str(payload.get("title") or "Simulacro")[:140]
    units = [str(u) for u in (payload.get("units") or [])]
    details = payload.get("details") if isinstance(payload.get("details"), list) else []
    duration_sec = max(0, int(payload.get("duration_sec") or 0))
    time_limit_sec = max(0, int(payload.get("time_limit_sec") or 0))
    now_iso = fsrs.to_iso(fsrs.utc_now())

    with db.connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO exam_attempts(
                domain_slug, mode, title, units_json, score_pct, procedure_score_pct, passed,
                correct_count, total_count, duration_sec, time_limit_sec, details_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                domain_slug,
                mode,
                title,
                json.dumps(units, ensure_ascii=False),
                score_pct,
                procedure_score_pct,
                passed,
                correct_count,
                total_count,
                duration_sec,
                time_limit_sec,
                json.dumps(details, ensure_ascii=False),
                now_iso,
            ),
        )
        exam_id = cur.lastrowid
    return {
        "id": exam_id,
        "domain_slug": domain_slug,
        "mode": mode,
        "title": title,
        "units": units,
        "score_pct": score_pct,
        "procedure_score_pct": procedure_score_pct,
        "effective_score_pct": effective_score,
        "passed": bool(passed),
        "correct_count": correct_count,
        "total_count": total_count,
        "duration_sec": duration_sec,
        "time_limit_sec": time_limit_sec,
        "details": details,
        "created_at": now_iso,
    }


def update_exam(db: Database, exam_id: int, payload: dict[str, Any]) -> dict[str, Any]:
    """Update a saved mock exam with post-exam procedure self-evaluation."""
    with db.connect() as conn:
        row = conn.execute("SELECT * FROM exam_attempts WHERE id = ?", (int(exam_id),)).fetchone()
        if not row:
            raise KeyError("Simulacro no encontrado.")
        proc_raw = payload.get("procedure_score_pct")
        proc_score = max(0, min(100, int(proc_raw))) if proc_raw is not None else row["procedure_score_pct"]
        details = (
            json.dumps(payload["details"], ensure_ascii=False)
            if isinstance(payload.get("details"), list)
            else row["details_json"]
        )
        effective = proc_score if proc_score is not None else row["score_pct"]
        passed = 1 if effective >= ingreso_uncuyo.COURSE["pass_mark"] else 0
        conn.execute(
            """
            UPDATE exam_attempts
            SET procedure_score_pct = ?, passed = ?, details_json = ?
            WHERE id = ?
            """,
            (proc_score, passed, details, int(exam_id)),
        )
        updated = conn.execute("SELECT * FROM exam_attempts WHERE id = ?", (int(exam_id),)).fetchone()
    return {
        "id": updated["id"],
        "domain_slug": updated["domain_slug"],
        "mode": updated["mode"],
        "title": updated["title"],
        "units": json.loads(updated["units_json"] or "[]"),
        "score_pct": updated["score_pct"],
        "procedure_score_pct": updated["procedure_score_pct"],
        "effective_score_pct": updated["procedure_score_pct"] if updated["procedure_score_pct"] is not None else updated["score_pct"],
        "passed": bool(updated["passed"]),
        "correct_count": updated["correct_count"],
        "total_count": updated["total_count"],
        "duration_sec": updated["duration_sec"],
        "time_limit_sec": updated["time_limit_sec"],
        "details": json.loads(updated["details_json"] or "[]"),
        "created_at": updated["created_at"],
    }


# ---------- Exercise -> FSRS card & error tagging ----------


def exercise_to_card(db: Database, exercise_id: str) -> dict[str, Any]:
    with db.connect() as conn:
        ex = exercise_store.all_exercises_by_id(conn).get(exercise_id)
        if not ex:
            raise KeyError(f"Ejercicio no encontrado: {exercise_id}")
        node = conn.execute(
            "SELECT id, domain_id, slug FROM nodes WHERE slug = ? ORDER BY id ASC LIMIT 1",
            (ex["node"],),
        ).fetchone()
        if not node:
            raise KeyError(f"Tema no encontrado: {ex['node']}")
        title = f"Ejercicio: {ex['title']}"[:90]
        dup = conn.execute(
            "SELECT id FROM learning_items WHERE node_id = ? AND title = ?",
            (node["id"], title),
        ).fetchone()
        if dup:
            return {"created": False, "item_id": dup["id"], "already_exists": True}
        parts = ex.get("parts") or []
        first_part = parts[0] if parts else None
        prompt = ex["statement"]
        if first_part:
            prompt = f"{prompt}\n\n{first_part['prompt']}"
        answer_lines = [f"{p['prompt']} → {p['answer']}" for p in parts]
        sol_lines = ex.get("solution") or []
        answer = "\n".join(answer_lines) + (("\n\nResolución:\n• " + "\n• ".join(sol_lines)) if sol_lines else "")
        payload: dict[str, Any] = {"from_exercise": exercise_id}
        if first_part and len(parts) == 1:
            payload["check"] = first_part["check"]
        now_iso = fsrs.to_iso(fsrs.utc_now())
        cur = conn.execute(
            """
            INSERT INTO learning_items(
                node_id, domain_id, item_type, title, prompt, answer,
                hints_json, payload_json, state, due_at, created_at
            ) VALUES (?, ?, 'worked_example', ?, ?, ?, ?, ?, 'new', ?, ?)
            """,
            (
                node["id"],
                node["domain_id"],
                title,
                prompt,
                answer,
                json.dumps(ex.get("hints") or [], ensure_ascii=False),
                json.dumps(payload, ensure_ascii=False),
                now_iso,
                now_iso,
            ),
        )
        return {"created": True, "item_id": cur.lastrowid, "already_exists": False}


def tag_exercise_error(db: Database, exercise_id: str, error_tag: str) -> dict[str, Any]:
    tag = str(error_tag or "").strip().lower()
    if tag and tag not in ERROR_TAGS:
        raise ValueError(f"Tipo de error inválido: {tag}")
    with db.connect() as conn:
        if exercise_id not in exercise_store.all_exercises_by_id(conn):
            raise KeyError(f"Ejercicio no encontrado: {exercise_id}")
        row = conn.execute(
            "SELECT id FROM exercise_attempts WHERE exercise_id = ? ORDER BY id DESC LIMIT 1",
            (exercise_id,),
        ).fetchone()
        if not row:
            raise KeyError("Primero resolvé o intentá este ejercicio para etiquetar el error.")
        conn.execute("UPDATE exercise_attempts SET error_tag = ? WHERE id = ?", (tag, row["id"]))
    return {"exercise_id": exercise_id, "error_tag": tag, "label": ERROR_TAGS.get(tag, "")}


# ---------- Formula sheet / Cheat sheet ----------


def get_cheatsheet(db: Database, domain_slug: str, ingreso_only: bool = True) -> dict[str, Any]:
    roadmap = db.get_roadmap(domain_slug)
    domain = roadmap["domain"]
    nodes_by_slug = {n["slug"]: n for n in roadmap["nodes"]}

    with db.connect() as conn:
        lesson_rows = {
            r["slug"]: _resolve_lesson(r["slug"], r["lesson_json"])
            for r in conn.execute(
                "SELECT slug, lesson_json FROM nodes WHERE domain_id = ?", (domain["id"],)
            ).fetchall()
        }

    subject = next((s for s in ingreso_uncuyo.SUBJECTS if s["domain"] == domain_slug), None)
    groups: list[dict[str, Any]] = []

    if ingreso_only and subject:
        for idx, unit in enumerate(subject["units"], start=1):
            code, short_title = ingreso_uncuyo._split_unit_title(unit["title"], idx)
            entries = []
            for slug in unit["topics"]:
                node = nodes_by_slug.get(slug)
                if not node:
                    continue
                les = lesson_rows.get(slug) or {}
                concept = les.get("concept") or {}
                entries.append(
                    {
                        "node_id": node["id"],
                        "slug": slug,
                        "title": node["title"],
                        "summary": node.get("summary") or "",
                        "lesson_completed": node["lesson_completed"],
                        "key_rule": concept.get("key_rule") or "",
                        "pitfall": concept.get("pitfall") or "",
                        "points": (concept.get("points") or [])[:4],
                    }
                )
            if entries:
                groups.append({"code": code, "title": unit["title"], "short_title": short_title, "topics": entries})
    else:
        by_sec: dict[str, list[dict[str, Any]]] = {}
        for node in roadmap["nodes"]:
            sec = (node.get("metadata") or {}).get("section") or domain["name"]
            les = lesson_rows.get(node["slug"]) or {}
            concept = les.get("concept") or {}
            by_sec.setdefault(sec, []).append(
                {
                    "node_id": node["id"],
                    "slug": node["slug"],
                    "title": node["title"],
                    "summary": node.get("summary") or "",
                    "lesson_completed": node["lesson_completed"],
                    "key_rule": concept.get("key_rule") or "",
                    "pitfall": concept.get("pitfall") or "",
                    "points": (concept.get("points") or [])[:4],
                }
            )
        for idx, (sec, entries) in enumerate(by_sec.items(), start=1):
            groups.append({"code": f"S{idx}", "title": sec, "short_title": sec, "topics": entries})

    return {
        "domain": domain,
        "ingreso_only": bool(ingreso_only and subject),
        "groups": groups,
        "topics_total": sum(len(g["topics"]) for g in groups),
    }


# ---------- Error bank ("Banco de errores") ----------


def get_error_bank(db: Database, domain_slug: str | None = None, ingreso_only: bool = False) -> dict[str, Any]:
    program_slugs = ingreso_uncuyo.program_slugs() if ingreso_only else None
    with db.connect() as conn:
        statuses = exercise_store._statuses(conn)
        ex_by_id = exercise_store.all_exercises_by_id(conn)
        domains_map = {
            r["slug"]: dict(r)
            for r in conn.execute("SELECT id, slug, name, lab_type FROM domains").fetchall()
        }
        nodes_by_slug = {
            r["slug"]: dict(r)
            for r in conn.execute(
                "SELECT n.id, n.slug, n.title, d.slug AS domain_slug, d.name AS domain_name FROM nodes n JOIN domains d ON d.id = n.domain_id"
            ).fetchall()
        }
        att_rows = conn.execute(
            """
            SELECT exercise_id, node_slug, domain_slug, correct, saw_solution, error_tag, created_at
            FROM exercise_attempts
            ORDER BY id DESC
            """
        ).fetchall()

        weak_card_rows = conn.execute(
            """
            SELECT i.id, i.node_id, i.title, i.prompt, i.lapses, i.reps, i.difficulty,
                   n.slug AS node_slug, n.title AS node_title,
                   d.slug AS domain_slug, d.name AS domain_name, d.lab_type
            FROM learning_items i
            JOIN nodes n ON n.id = i.node_id
            JOIN domains d ON d.id = i.domain_id
            WHERE i.lapses >= 1 AND COALESCE(i.suspended, 0) = 0
            ORDER BY i.lapses DESC, i.difficulty DESC
            LIMIT 60
            """
        ).fetchall()

    # Aggregate error tags
    tag_counts: Counter[str] = Counter()
    seen_ex_ids: set[str] = set()
    for r in att_rows:
        if domain_slug and r["domain_slug"] != domain_slug:
            continue
        if program_slugs is not None and r["node_slug"] not in program_slugs:
            continue
        if r["error_tag"]:
            tag_counts[r["error_tag"]] += 1
        seen_ex_ids.add(r["exercise_id"])

    weak_exercises = []
    for ex_id in seen_ex_ids:
        st = statuses.get(ex_id)
        if not st or st["solved_unaided"]:
            continue
        ex = ex_by_id.get(ex_id)
        if not ex:
            continue
        node = nodes_by_slug.get(ex["node"])
        if not node:
            continue
        dom = domains_map.get(node["domain_slug"], {})
        weak_exercises.append(
            {
                "exercise_id": ex_id,
                "title": ex["title"],
                "source": ex.get("source") or "",
                "level": ex["level"],
                "node_id": node["id"],
                "node_slug": node["slug"],
                "node_title": node["title"],
                "domain_slug": node["domain_slug"],
                "domain_name": node["domain_name"],
                "lab_type": dom.get("lab_type", "generic"),
                "attempts": st["attempts"],
                "fails": st["fails"],
                "solved": st["solved"],
                "saw_solution": st["saw_solution"],
                "retry_due": st["retry_due"],
                "next_retry_at": st["next_retry_at"],
                "error_tag": st["error_tag"],
                "error_tag_label": ERROR_TAGS.get(st["error_tag"], ""),
                "last_attempt_at": st["last_attempt_at"],
            }
        )
    weak_exercises.sort(key=lambda x: (not x["retry_due"], x["solved"], -x["fails"], x["last_attempt_at"] or ""))

    weak_cards = []
    for r in weak_card_rows:
        if domain_slug and r["domain_slug"] != domain_slug:
            continue
        if program_slugs is not None and r["node_slug"] not in program_slugs:
            continue
        weak_cards.append(
            {
                "item_id": r["id"],
                "node_id": r["node_id"],
                "node_slug": r["node_slug"],
                "node_title": r["node_title"],
                "domain_slug": r["domain_slug"],
                "domain_name": r["domain_name"],
                "lab_type": r["lab_type"],
                "title": r["title"],
                "lapses": r["lapses"],
                "reps": r["reps"],
            }
        )

    return {
        "error_tags": ERROR_TAGS,
        "tag_counts": [{"tag": k, "label": ERROR_TAGS[k], "count": tag_counts[k]} for k in ERROR_TAGS],
        "weak_exercises": weak_exercises,
        "weak_cards": weak_cards,
        "totals": {
            "weak_exercises": len(weak_exercises),
            "due_retries": sum(1 for e in weak_exercises if e["retry_due"]),
            "unsolved_exercises": sum(1 for e in weak_exercises if not e["solved"]),
            "solution_assisted": sum(1 for e in weak_exercises if e["solved"] and e["saw_solution"]),
            "weak_cards": len(weak_cards),
        },
    }


# ---------- Study notebook & bookmarks ----------


def list_notes(
    db: Database, domain_slug: str | None = None, bookmarked_only: bool = False
) -> dict[str, Any]:
    with db.connect() as conn:
        # Backfill any legacy lesson Feynman notes into study_notes on read if absent
        legacy = conn.execute(
            """
            SELECT pm.node_id, d.slug AS domain_slug, pm.notes, pm.created_at
            FROM practice_metrics pm
            JOIN domains d ON d.id = pm.domain_id
            WHERE pm.metric_type = 'lesson_completed' AND pm.node_id IS NOT NULL AND TRIM(pm.notes) != ''
            ORDER BY pm.id ASC
            """
        ).fetchall()
        for r in legacy:
            conn.execute(
                """
                INSERT OR IGNORE INTO study_notes(node_id, domain_slug, content, bookmarked, updated_at)
                VALUES (?, ?, ?, 0, ?)
                """,
                (r["node_id"], r["domain_slug"], r["notes"].strip(), r["created_at"]),
            )

        rows = conn.execute(
            """
            SELECT sn.node_id, sn.domain_slug, sn.content, sn.bookmarked, sn.updated_at,
                   n.slug AS node_slug, n.title AS node_title, n.summary AS node_summary,
                   n.lesson_completed_at, d.name AS domain_name, d.lab_type
            FROM study_notes sn
            JOIN nodes n ON n.id = sn.node_id
            JOIN domains d ON d.id = n.domain_id
            ORDER BY sn.bookmarked DESC, sn.updated_at DESC
            """
        ).fetchall()

    notes = []
    for r in rows:
        if domain_slug and r["domain_slug"] != domain_slug:
            continue
        if bookmarked_only and not r["bookmarked"]:
            continue
        if not r["bookmarked"] and not (r["content"] or "").strip():
            continue
        notes.append(
            {
                "node_id": r["node_id"],
                "node_slug": r["node_slug"],
                "node_title": r["node_title"],
                "node_summary": r["node_summary"],
                "domain_slug": r["domain_slug"],
                "domain_name": r["domain_name"],
                "lab_type": r["lab_type"],
                "content": r["content"] or "",
                "bookmarked": bool(r["bookmarked"]),
                "lesson_completed": bool(r["lesson_completed_at"]),
                "updated_at": r["updated_at"],
            }
        )
    return {
        "notes": notes,
        "totals": {
            "total": len(notes),
            "bookmarked": sum(1 for n in notes if n["bookmarked"]),
        },
    }


def get_node_note(db: Database, node_id: int) -> dict[str, Any]:
    with db.connect() as conn:
        r = conn.execute(
            "SELECT content, bookmarked, updated_at FROM study_notes WHERE node_id = ?", (node_id,)
        ).fetchone()
    if not r:
        return {"node_id": node_id, "content": "", "bookmarked": False, "updated_at": None}
    return {
        "node_id": node_id,
        "content": r["content"] or "",
        "bookmarked": bool(r["bookmarked"]),
        "updated_at": r["updated_at"],
    }


def save_note(db: Database, node_id: int, payload: dict[str, Any]) -> dict[str, Any]:
    now_iso = fsrs.to_iso(fsrs.utc_now())
    with db.connect() as conn:
        row = conn.execute(
            "SELECT n.id, d.slug AS domain_slug FROM nodes n JOIN domains d ON d.id = n.domain_id WHERE n.id = ?",
            (node_id,),
        ).fetchone()
        if not row:
            raise KeyError("Tema no encontrado.")
        existing = conn.execute(
            "SELECT content, bookmarked FROM study_notes WHERE node_id = ?", (node_id,)
        ).fetchone()
        if "content" in payload:
            content = str(payload["content"] or "").strip()
        else:
            content = existing["content"] if existing else ""
        if "bookmarked" in payload:
            bookmarked = 1 if payload["bookmarked"] else 0
        else:
            bookmarked = int(existing["bookmarked"]) if existing else 0
        conn.execute(
            """
            INSERT INTO study_notes(node_id, domain_slug, content, bookmarked, updated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(node_id) DO UPDATE SET
                content = excluded.content,
                bookmarked = excluded.bookmarked,
                updated_at = excluded.updated_at
            """,
            (node_id, row["domain_slug"], content, bookmarked, now_iso),
        )
    return {
        "node_id": node_id,
        "domain_slug": row["domain_slug"],
        "content": content,
        "bookmarked": bool(bookmarked),
        "updated_at": now_iso,
    }


# ---------- Diagnostic assessment per entrance subject ----------


def get_diagnostic(db: Database, domain_slug: str) -> dict[str, Any]:
    """Build a multi-question-per-unit diagnostic using cards & exercises — never repeating lesson.check."""
    subject = next((s for s in ingreso_uncuyo.SUBJECTS if s["domain"] == domain_slug), None)
    if not subject:
        raise KeyError(f"No hay diagnóstico configurado para: {domain_slug}")
    roadmap = db.get_roadmap(domain_slug)
    nodes_by_slug = {n["slug"]: n for n in roadmap["nodes"]}

    with db.connect() as conn:
        card_rows = conn.execute(
            """
            SELECT i.id, n.slug AS node_slug, i.title, i.prompt, i.answer, i.payload_json
            FROM learning_items i
            JOIN nodes n ON n.id = i.node_id
            WHERE i.domain_id = ? AND COALESCE(i.suspended, 0) = 0
            ORDER BY i.id ASC
            """,
            (roadmap["domain"]["id"],),
        ).fetchall()
        ex_by_node = exercise_store.all_exercises_by_node(conn)

    cards_by_slug: dict[str, list[dict[str, Any]]] = {}
    for r in card_rows:
        pl = json.loads(r["payload_json"] or "{}")
        ck = pl.get("check")
        if isinstance(ck, dict) and ck.get("type") == "choice" and len(ck.get("options") or []) >= 2:
            cards_by_slug.setdefault(r["node_slug"], []).append(
                {
                    "id": f"diag-card-{r['id']}",
                    "source_kind": "card",
                    "question": r["prompt"],
                    "options": list(ck["options"]),
                    "correct": int(ck.get("correct") or 0),
                    "feedback": r["answer"] or "",
                }
            )

    def _collect_unit_pool(unit_topics: list[str]) -> list[tuple[str, dict[str, Any]]]:
        pool: list[tuple[str, dict[str, Any]]] = []
        # 1. Choice exercises (prefer concise single-part or clear statement + choice part)
        for slug in unit_topics:
            for ex in ex_by_node.get(slug, []):
                if ex.get("kind") != "problem":
                    continue
                for p_idx, part in enumerate(ex.get("parts") or []):
                    ck = part.get("check") or {}
                    if ck.get("type") != "choice" or len(ck.get("options") or []) < 2:
                        continue
                    stmt = str(ex.get("statement") or "").strip()
                    prompt = str(part.get("prompt") or "").strip()
                    # Avoid overly long multi-paragraph reading texts in quick diagnostic
                    if len(stmt) > 420:
                        continue
                    q_text = f"{stmt}\n\n{prompt}" if stmt and prompt not in stmt else (prompt or stmt)
                    pool.append(
                        (
                            slug,
                            {
                                "id": f"diag-ex-{ex['id']}-{p_idx}",
                                "source_kind": "exercise",
                                "question": q_text,
                                "options": list(ck["options"]),
                                "correct": int(ck.get("correct") or 0),
                                "feedback": part.get("answer") or "",
                            },
                        )
                    )
                    break  # at most 1 part per exercise
        # 2. Choice cards (FSRS items — distinct from lesson.check)
        for slug in unit_topics:
            for c in cards_by_slug.get(slug, []):
                pool.append((slug, c))
        return pool

    # Always at least 2 questions per unit (so a single lucky guess can never unlock a unit)
    per_unit_target = 2 if len(subject["units"]) >= 6 else (2 if len(subject["units"]) >= 4 else 3)
    questions: list[dict[str, Any]] = []

    for u_idx, unit in enumerate(subject["units"], start=1):
        code, short_title = ingreso_uncuyo._split_unit_title(unit["title"], u_idx)
        pool = _collect_unit_pool(unit["topics"])
        picked: list[tuple[str, dict[str, Any]]] = []
        used_slugs: set[str] = set()
        used_q: set[str] = set()

        # First pass: spread across distinct topics in the unit (prefer card_choice + exercise_choice mix)
        for slug, q in pool:
            if len(picked) >= per_unit_target:
                break
            if slug in used_slugs or q["question"] in used_q:
                continue
            used_slugs.add(slug)
            used_q.add(q["question"])
            picked.append((slug, q))

        # Second pass: allow a second distinct question from the same topic (e.g. U0 has 1 topic)
        for slug, q in pool:
            if len(picked) >= per_unit_target:
                break
            if q["question"] in used_q:
                continue
            used_q.add(q["question"])
            picked.append((slug, q))

        for slug, q in picked:
            node = nodes_by_slug.get(slug)
            if not node:
                continue
            questions.append(
                {
                    "id": q["id"],
                    "source_kind": q["source_kind"],
                    "unit_code": code,
                    "unit_title": short_title,
                    "node_id": node["id"],
                    "node_slug": slug,
                    "node_title": node["title"],
                    "question": q["question"],
                    "options": q["options"],
                    "correct": q["correct"],
                    "feedback": q["feedback"],
                }
            )

    return {
        "subject_key": subject["key"],
        "subject_name": subject["name"],
        "domain": roadmap["domain"],
        "per_unit_target": per_unit_target,
        "questions": questions,
    }


def apply_diagnostic(db: Database, domain_slug: str, payload: dict[str, Any]) -> dict[str, Any]:
    subject = next((s for s in ingreso_uncuyo.SUBJECTS if s["domain"] == domain_slug), None)
    if not subject:
        raise KeyError(f"Materia no encontrada: {domain_slug}")
    results = payload.get("results") or []
    # Unlocking is opt-in by default so the learner reviews the unit map before skipping ahead
    unlock_strong = bool(payload.get("unlock_strong", False))
    save_metric = bool(payload.get("save_metric", True))
    now_iso = fsrs.to_iso(fsrs.utc_now())

    by_unit: dict[str, list[bool]] = {}
    for r in results:
        code = str(r.get("unit_code") or "")
        if code:
            by_unit.setdefault(code, []).append(bool(r.get("correct")))

    unit_report = []
    strong_codes: set[str] = set()
    for idx, unit in enumerate(subject["units"], start=1):
        code, short_title = ingreso_uncuyo._split_unit_title(unit["title"], idx)
        arr = by_unit.get(code) or []
        ok = sum(1 for x in arr if x)
        tot = len(arr)
        pct = round(100 * ok / tot) if tot else 0
        # Require >= 2 questions and >= 75% accuracy to classify a unit as strong
        level = "strong" if tot >= 2 and pct >= 75 else ("medium" if tot > 0 and pct >= 50 else "weak")
        if level == "strong":
            strong_codes.add(code)
        unit_report.append(
            {"code": code, "short_title": short_title, "correct": ok, "total": tot, "pct": pct, "level": level}
        )

    unlocked_count = 0
    total_q = len(results)
    total_ok = sum(1 for r in results if r.get("correct"))
    score_pct = round(100 * total_ok / total_q) if total_q else 0

    with db.connect() as conn:
        dom = conn.execute("SELECT id FROM domains WHERE slug = ?", (domain_slug,)).fetchone()
        if dom:
            if save_metric:
                conn.execute(
                    """
                    INSERT INTO practice_metrics(domain_id, node_id, metric_type, label, value, unit, notes, created_at)
                    VALUES (?, NULL, 'diagnostic', ?, ?, '%', ?, ?)
                    """,
                    (
                        dom["id"],
                        f"Diagnóstico {subject['name']}",
                        score_pct,
                        json.dumps({"units": unit_report}, ensure_ascii=False),
                        now_iso,
                    ),
                )
            if unlock_strong and strong_codes:
                for idx, unit in enumerate(subject["units"], start=1):
                    code, _ = ingreso_uncuyo._split_unit_title(unit["title"], idx)
                    if code not in strong_codes:
                        continue
                    for slug in unit["topics"]:
                        cur = conn.execute(
                            "UPDATE nodes SET manual_unlocked = 1 WHERE domain_id = ? AND slug = ? AND manual_unlocked = 0",
                            (dom["id"], slug),
                        )
                        unlocked_count += cur.rowcount

    first_weak = next((u for u in unit_report if u["level"] == "weak"), None) or next(
        (u for u in unit_report if u["level"] == "medium"), None
    )
    return {
        "domain_slug": domain_slug,
        "score_pct": score_pct,
        "correct": total_ok,
        "total": total_q,
        "units": unit_report,
        "strong_units_count": len(strong_codes),
        "unlocked_topics": unlocked_count,
        "recommended_unit": first_weak["code"] if first_weak else (unit_report[0]["code"] if unit_report else None),
    }


# ---------- Full-text content search (Ctrl+K) ----------


def search_content(db: Database, query: str, limit: int = 24) -> dict[str, Any]:
    q = _norm(query)
    if len(q) < 2:
        return {"query": query, "results": []}

    results: list[dict[str, Any]] = []

    def _snippet(text: str, max_len: int = 110) -> str:
        raw = " ".join(str(text or "").split())
        if len(raw) <= max_len:
            return raw
        idx = _norm(raw).find(q)
        if idx < 0:
            return raw[:max_len] + "…"
        start = max(0, idx - 35)
        end = min(len(raw), start + max_len)
        prefix = "…" if start > 0 else ""
        suffix = "…" if end < len(raw) else ""
        return f"{prefix}{raw[start:end]}{suffix}"

    with db.connect() as conn:
        nodes = conn.execute(
            """
            SELECT n.id, n.slug, n.title, n.summary, n.lesson_json,
                   d.slug AS domain_slug, d.name AS domain_name, d.icon AS domain_icon, d.lab_type
            FROM nodes n JOIN domains d ON d.id = n.domain_id
            ORDER BY d.id ASC, n.level ASC, n.order_index ASC
            """
        ).fetchall()
        node_by_slug = {r["slug"]: dict(r) for r in nodes}

        # 1. Lessons (title, summary, key_rule, pitfall, concept points)
        for r in nodes:
            les = _resolve_lesson(r["slug"], r["lesson_json"])
            concept = les.get("concept") or {}
            key_rule = concept.get("key_rule") or ""
            pitfall = concept.get("pitfall") or ""
            points_txt = " ".join(concept.get("points") or [])
            haystack = _norm(f"{r['title']} {r['summary']} {key_rule} {pitfall} {points_txt}")
            if q in haystack:
                score = 3 if q in _norm(r["title"]) else (2 if q in _norm(key_rule) else 1)
                snip = _snippet(key_rule if q in _norm(key_rule) else (pitfall if q in _norm(pitfall) else (points_txt if q in _norm(points_txt) else r["summary"])))
                results.append(
                    {
                        "kind": "lesson",
                        "score": score,
                        "label": r["title"],
                        "meta": f"Lección · {r['domain_name']}",
                        "snippet": snip,
                        "ico": r["domain_icon"] or r["lab_type"] or "book",
                        "hash": f"#/learn/{r['id']}",
                    }
                )

        # 2. Study notes
        note_rows = conn.execute(
            """
            SELECT sn.node_id, sn.content, n.title AS node_title, d.name AS domain_name
            FROM study_notes sn
            JOIN nodes n ON n.id = sn.node_id
            JOIN domains d ON d.id = n.domain_id
            WHERE TRIM(sn.content) != ''
            """
        ).fetchall()
        for r in note_rows:
            if q in _norm(f"{r['node_title']} {r['content']}"):
                results.append(
                    {
                        "kind": "note",
                        "score": 2,
                        "label": f"Apunte: {r['node_title']}",
                        "meta": f"Cuaderno · {r['domain_name']}",
                        "snippet": _snippet(r["content"]),
                        "ico": "pen",
                        "hash": "#/cuaderno",
                    }
                )

        # 3. Exercises (built-in + custom)
        all_ex = list(exercise_store.all_exercises_by_id(conn).values())
        for ex in all_ex:
            node = node_by_slug.get(ex["node"])
            if not node:
                continue
            hay = _norm(f"{ex['title']} {ex.get('statement', '')} {ex.get('source', '')}")
            if q in hay:
                score = 2 if q in _norm(ex["title"]) or q in _norm(ex.get("source", "")) else 1
                results.append(
                    {
                        "kind": "exercise",
                        "score": score,
                        "label": ex["title"],
                        "meta": f"Ejercicio · {node['domain_name']}" + (f" · {ex['source']}" if ex.get("source") else ""),
                        "snippet": _snippet(ex.get("statement", "")),
                        "ico": "target",
                        "hash": f"#/ejercicios/{node['domain_slug']}/{node['slug']}?e={ex['id']}",
                    }
                )

        # 4. FSRS cards
        card_rows = conn.execute(
            """
            SELECT i.id, i.node_id, i.title, i.prompt, d.name AS domain_name
            FROM learning_items i
            JOIN domains d ON d.id = i.domain_id
            WHERE COALESCE(i.suspended, 0) = 0
            """
        ).fetchall()
        for r in card_rows:
            if q in _norm(f"{r['title']} {r['prompt']}"):
                results.append(
                    {
                        "kind": "card",
                        "score": 1,
                        "label": r["title"],
                        "meta": f"Tarjeta · {r['domain_name']}",
                        "snippet": _snippet(r["prompt"]),
                        "ico": "brain",
                        "hash": f"#/review?node={r['node_id']}",
                    }
                )

    results.sort(key=lambda x: (-x["score"], x["kind"] != "lesson", x["label"]))
    return {"query": query, "results": results[:limit]}


# ---------- Real mastery, study time, topic accuracy & mock exam trend ----------


def get_analytics(db: Database) -> dict[str, Any]:
    ov = ingreso_uncuyo.overview(db)
    exams = list_exams(db, limit=30)
    errors = get_error_bank(db, ingreso_only=True)

    today_str = local_day(fsrs.to_iso(fsrs.utc_now()))
    week_cutoff = (date.fromisoformat(today_str) - timedelta(days=6)).isoformat()

    with db.connect() as conn:
        statuses = exercise_store._statuses(conn)
        ex_by_node = exercise_store.all_exercises_by_node(conn)

        # Study time from review_logs + exam_attempts
        rev_rows = conn.execute(
            """
            SELECT rl.node_id, rl.rating, rl.duration_sec, rl.created_at,
                   n.slug AS node_slug, n.title AS node_title,
                   d.slug AS domain_slug, d.name AS domain_name
            FROM review_logs rl
            JOIN nodes n ON n.id = rl.node_id
            JOIN domains d ON d.id = rl.domain_id
            """
        ).fetchall()
        exam_dur_rows = conn.execute("SELECT duration_sec, created_at FROM exam_attempts").fetchall()
        att_rows = conn.execute(
            """
            SELECT ea.node_slug, ea.domain_slug, ea.correct,
                   n.id AS node_id, n.title AS node_title, d.name AS domain_name
            FROM exercise_attempts ea
            JOIN nodes n ON n.slug = ea.node_slug
            JOIN domains d ON d.id = n.domain_id
            """
        ).fetchall()

    today_sec = 0
    week_sec = 0
    total_sec = 0
    topic_stats: dict[str, dict[str, Any]] = {}

    for r in rev_rows:
        dur = int(r["duration_sec"] or 0)
        day = local_day(r["created_at"])
        total_sec += dur
        if day >= week_cutoff:
            week_sec += dur
        if day == today_str:
            today_sec += dur
        ts = topic_stats.setdefault(
            r["node_slug"],
            {
                "node_id": r["node_id"],
                "node_slug": r["node_slug"],
                "node_title": r["node_title"],
                "domain_slug": r["domain_slug"],
                "domain_name": r["domain_name"],
                "ok": 0,
                "total": 0,
            },
        )
        ts["total"] += 1
        if int(r["rating"] or 0) >= 3:
            ts["ok"] += 1

    for r in exam_dur_rows:
        dur = int(r["duration_sec"] or 0)
        day = local_day(r["created_at"])
        total_sec += dur
        if day >= week_cutoff:
            week_sec += dur
        if day == today_str:
            today_sec += dur

    for r in att_rows:
        ts = topic_stats.setdefault(
            r["node_slug"],
            {
                "node_id": r["node_id"],
                "node_slug": r["node_slug"],
                "node_title": r["node_title"],
                "domain_slug": r["domain_slug"],
                "domain_name": r["domain_name"],
                "ok": 0,
                "total": 0,
            },
        )
        ts["total"] += 1
        if r["correct"]:
            ts["ok"] += 1

    topic_accuracy = []
    for ts in topic_stats.values():
        if ts["total"] <= 0:
            continue
        topic_accuracy.append(
            {
                **ts,
                "accuracy_pct": round(100 * ts["ok"] / ts["total"]),
            }
        )
    # Weakest practiced topics first so learner knows what needs attention
    topic_accuracy.sort(key=lambda x: (x["accuracy_pct"], -x["total"]))

    subject_breakdown = []
    for s in ov["subjects"]:
        units_data = []
        sub_unaided = 0
        sub_assisted = 0
        sub_unsolved_tried = 0
        sub_not_started = 0
        for u in s["units"]:
            u_unaided = 0
            u_assisted = 0
            u_tried = 0
            u_not_started = 0
            for t in u["topics"]:
                for ex in ex_by_node.get(t["slug"], []):
                    st = statuses.get(ex["id"])
                    if not st:
                        u_not_started += 1
                    elif st["solved_unaided"]:
                        u_unaided += 1
                    elif st["solved"]:
                        u_assisted += 1
                    else:
                        u_tried += 1
            u_total = u_unaided + u_assisted + u_tried + u_not_started
            sub_unaided += u_unaided
            sub_assisted += u_assisted
            sub_unsolved_tried += u_tried
            sub_not_started += u_not_started
            units_data.append(
                {
                    "code": u["code"],
                    "short_title": u["short_title"],
                    "progress_pct": u["progress_pct"],
                    "total": u_total,
                    "unaided": u_unaided,
                    "assisted": u_assisted,
                    "unsolved_tried": u_tried,
                    "not_started": u_not_started,
                }
            )
        subject_breakdown.append(
            {
                "key": s["key"],
                "name": s["name"],
                "domain": s["domain"],
                "lab_type": s["lab_type"],
                "progress_pct": s["progress_pct"],
                "unaided": sub_unaided,
                "assisted": sub_assisted,
                "unsolved_tried": sub_unsolved_tried,
                "not_started": sub_not_started,
                "total": sub_unaided + sub_assisted + sub_unsolved_tried + sub_not_started,
                "units": units_data,
            }
        )

    exam_trend = [
        {
            "id": e["id"],
            "date": (e["created_at"] or "")[:10],
            "domain_slug": e["domain_slug"],
            "title": e["title"],
            "score_pct": e["score_pct"],
            "procedure_score_pct": e["procedure_score_pct"],
            "effective_score_pct": e["effective_score_pct"],
            "passed": e["passed"],
        }
        for e in reversed(exams["exams"][:12])
    ]

    return {
        "today": get_today_activity(db),
        "study_time": {
            "today_sec": today_sec,
            "week_sec": week_sec,
            "total_sec": total_sec,
        },
        "topic_accuracy": topic_accuracy[:12],
        "exam_trend": exam_trend,
        "subjects": subject_breakdown,
        "exams": exams,
        "error_tags": errors["tag_counts"],
        "error_totals": errors["totals"],
    }


def compute_exam_pace(
    exam_date_str: str | None,
    lessons_remaining: int,
    exercises_remaining: int,
) -> dict[str, Any]:
    """Calculate countdown and recommended daily pace leaving a 14-day mock-exam buffer when possible."""
    if not exam_date_str:
        return {
            "exam_date": None,
            "days_left": None,
            "recommended_lessons_per_day": None,
            "recommended_exercises_per_day": None,
            "pace_status": "unset",
        }
    try:
        target = date.fromisoformat(exam_date_str)
    except ValueError:
        return {
            "exam_date": None,
            "days_left": None,
            "recommended_lessons_per_day": None,
            "recommended_exercises_per_day": None,
            "pace_status": "unset",
        }
    today = date.today()
    days_left = (target - today).days
    if days_left < 0:
        return {
            "exam_date": exam_date_str,
            "days_left": days_left,
            "recommended_lessons_per_day": 0,
            "recommended_exercises_per_day": 0,
            "pace_status": "past",
        }
    study_days = max(1, days_left - 14) if days_left > 21 else max(1, days_left)
    rec_lessons = round(lessons_remaining / study_days, 1) if lessons_remaining > 0 else 0
    rec_exercises = round(exercises_remaining / study_days, 1) if exercises_remaining > 0 else 0
    if lessons_remaining == 0 and exercises_remaining == 0:
        status = "ready"
    elif rec_lessons <= 1.5 and rec_exercises <= 7:
        status = "on_track"
    else:
        status = "tight"
    return {
        "exam_date": exam_date_str,
        "days_left": days_left,
        "recommended_lessons_per_day": rec_lessons,
        "recommended_exercises_per_day": rec_exercises,
        "pace_status": status,
    }

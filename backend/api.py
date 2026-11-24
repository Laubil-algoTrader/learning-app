"""REST API routing and request handling for AprendeLab."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import parse_qs, urlparse

from backend import exercise_store, ingreso_uncuyo, study_tools
from backend.db import Database


class APIError(Exception):
    def __init__(self, status: int, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.message = message


def handle_api_request(
    db: Database,
    method: str,
    raw_path: str,
    body_bytes: bytes = b"",
) -> tuple[int, dict[str, Any]]:
    """Route /api/* requests and return (HTTP status, JSON-serializable dict)."""
    parsed = urlparse(raw_path)
    path = parsed.path.rstrip("/")
    query = parse_qs(parsed.query)
    parts = [p for p in path.split("/") if p]

    payload: dict[str, Any] = {}
    if body_bytes:
        try:
            payload = json.loads(body_bytes.decode("utf-8"))
            if not isinstance(payload, dict):
                raise APIError(400, "El cuerpo JSON debe ser un objeto.")
        except json.JSONDecodeError as exc:
            raise APIError(400, f"JSON inválido: {exc}") from exc

    try:
        # GET /api/dashboard
        if method == "GET" and parts == ["api", "dashboard"]:
            return 200, db.get_dashboard()

        # GET /api/search-index  ·  GET /api/search?q=...
        if method == "GET" and parts == ["api", "search-index"]:
            return 200, db.get_search_index()
        if method == "GET" and parts == ["api", "search"]:
            q = query.get("q", [""])[0]
            limit = int(query.get("limit", ["24"])[0])
            return 200, study_tools.search_content(db, q, limit=limit)

        # GET / POST /api/domains
        if parts == ["api", "domains"]:
            if method == "GET":
                return 200, {"domains": db.list_domains()}
            if method == "POST":
                return 201, {"domain": db.create_domain(payload)}

        # DELETE /api/domains/<id>
        if len(parts) == 3 and parts[:2] == ["api", "domains"] and method == "DELETE":
            deleted = db.delete_domain(int(parts[2]))
            if not deleted:
                raise APIError(404, "Disciplina no encontrada.")
            return 200, {"deleted": True}

        # GET /api/domains/<slug>/roadmap
        if (
            len(parts) == 4
            and parts[:2] == ["api", "domains"]
            and parts[3] == "roadmap"
            and method == "GET"
        ):
            return 200, db.get_roadmap(parts[2])

        # POST /api/nodes  ·  PUT/DELETE /api/nodes/<id>
        if parts == ["api", "nodes"] and method == "POST":
            return 201, {"node": db.create_node(payload)}
        if len(parts) == 3 and parts[:2] == ["api", "nodes"]:
            node_id = int(parts[2])
            if method == "PUT":
                return 200, {"node": db.update_node(node_id, payload)}
            if method == "DELETE":
                ok = db.delete_node(node_id)
                if not ok:
                    raise APIError(404, "Nodo no encontrado.")
                return 200, {"deleted": True}

        # POST /api/nodes/<id>/unlock
        if (
            len(parts) == 4
            and parts[:2] == ["api", "nodes"]
            and parts[3] == "unlock"
            and method == "POST"
        ):
            ok = db.unlock_node(int(parts[2]))
            if not ok:
                raise APIError(404, "Nodo no encontrado.")
            return 200, {"unlocked": True}

        # GET /api/nodes/<id>/lesson
        if (
            len(parts) == 4
            and parts[:2] == ["api", "nodes"]
            and parts[3] == "lesson"
            and method == "GET"
        ):
            data = db.get_node_lesson(int(parts[2]))
            data["exercise_count"] = exercise_store.count_for_node(data["node"]["slug"], db)
            data["note"] = study_tools.get_node_note(db, int(parts[2]))
            return 200, data

        # POST /api/nodes/<id>/lesson/complete
        if (
            len(parts) == 5
            and parts[:2] == ["api", "nodes"]
            and parts[3] == "lesson"
            and parts[4] == "complete"
            and method == "POST"
        ):
            return 200, db.complete_node_lesson(int(parts[2]), payload)

        # POST /api/items
        if parts == ["api", "items"] and method == "POST":
            return 201, {"item": db.create_item(payload)}

        # GET /api/items/suspended
        if parts == ["api", "items", "suspended"] and method == "GET":
            return 200, {"items": db.list_suspended_items()}

        # PUT / DELETE /api/items/<id>
        if len(parts) == 3 and parts[:2] == ["api", "items"]:
            item_id = int(parts[2])
            if method == "PUT":
                return 200, {"item": db.update_item(item_id, payload)}
            if method == "DELETE":
                ok = db.delete_item(item_id)
                if not ok:
                    raise APIError(404, "Ítem no encontrado.")
                return 200, {"deleted": True}

        # POST /api/reviews/undo
        if parts == ["api", "reviews", "undo"] and method == "POST":
            raw_id = payload.get("review_log_id")
            return 200, db.undo_last_review(int(raw_id) if raw_id is not None else None)

        # GET /api/reviews/due
        if parts == ["api", "reviews", "due"] and method == "GET":
            domain_slug = query.get("domain", [None])[0]
            node_raw = query.get("node", [None])[0]
            node_id = int(node_raw) if node_raw is not None and node_raw != "" else None
            limit = int(query.get("limit", ["20"])[0])
            include_new = query.get("include_new", ["true"])[0].lower() != "false"
            practice_all = query.get("mode", [""])[0] == "practice_all"
            return 200, db.get_review_queue(
                domain_slug=domain_slug,
                node_id=node_id,
                limit=limit,
                include_new=include_new,
                practice_all=practice_all,
            )

        # POST /api/reviews/<item_id>
        if len(parts) == 3 and parts[:2] == ["api", "reviews"] and method == "POST":
            return 200, db.submit_review(int(parts[2]), payload)

        # POST /api/sessions/generate
        if parts == ["api", "sessions", "generate"] and method == "POST":
            duration = int(payload.get("duration_minutes", 25))
            domains = payload.get("domains") or None
            return 200, db.generate_smart_session(duration_minutes=duration, domain_slugs=domains)

        # GET / POST /api/metrics
        if parts == ["api", "metrics"]:
            if method == "GET":
                domain_slug = query.get("domain", [None])[0]
                metric_type = query.get("type", [None])[0]
                limit = int(query.get("limit", ["50"])[0])
                return 200, {
                    "metrics": db.list_metrics(
                        domain_slug=domain_slug, metric_type=metric_type, limit=limit
                    )
                }
            if method == "POST":
                return 201, {"metric": db.log_metric(payload)}

        # GET / PUT /api/settings
        if parts == ["api", "settings"]:
            if method == "GET":
                return 200, {"settings": db.get_settings()}
            if method == "PUT":
                return 200, {"settings": db.update_settings(payload)}

        # GET /api/ingreso — the entrance-course syllabus with progress per topic
        if parts == ["api", "ingreso"] and method == "GET":
            return 200, ingreso_uncuyo.overview(db)

        # GET /api/exercises  ·  GET /api/exercises/retries  ·  POST /api/exercises/custom
        if parts == ["api", "exercises"] and method == "GET":
            return 200, exercise_store.overview(db)
        if parts == ["api", "exercises", "retries"] and method == "GET":
            domain_slug = query.get("domain", [None])[0]
            due_only = query.get("due_only", ["0"])[0] == "1"
            return 200, exercise_store.list_retry_exercises(db, domain_slug=domain_slug, due_only=due_only)
        if parts == ["api", "exercises", "custom"] and method == "POST":
            return 201, {"exercise": exercise_store.create_custom_exercise(db, payload)}
        if len(parts) == 4 and parts[:3] == ["api", "exercises", "custom"] and method == "DELETE":
            ok = exercise_store.delete_custom_exercise(db, parts[3])
            if not ok:
                raise APIError(404, "Ejercicio personalizado no encontrado.")
            return 200, {"deleted": True}
        if len(parts) == 3 and parts[:2] == ["api", "exercises"] and method == "GET":
            return 200, exercise_store.domain_exercises(db, parts[2])

        # POST /api/exercises/<exercise_id>/attempts
        if (
            len(parts) == 4
            and parts[:2] == ["api", "exercises"]
            and parts[3] == "attempts"
            and method == "POST"
        ):
            return 201, exercise_store.log_attempt(db, parts[2], payload)

        # POST /api/exercises/<exercise_id>/to-card
        if (
            len(parts) == 4
            and parts[:2] == ["api", "exercises"]
            and parts[3] == "to-card"
            and method == "POST"
        ):
            return 201, study_tools.exercise_to_card(db, parts[2])

        # POST /api/exercises/<exercise_id>/error-tag
        if (
            len(parts) == 4
            and parts[:2] == ["api", "exercises"]
            and parts[3] == "error-tag"
            and method == "POST"
        ):
            return 200, study_tools.tag_exercise_error(db, parts[2], payload.get("error_tag", ""))

        # GET / POST /api/exams  ·  PUT /api/exams/<id>
        if parts == ["api", "exams"]:
            if method == "GET":
                domain_slug = query.get("domain", [None])[0]
                limit = int(query.get("limit", ["30"])[0])
                return 200, study_tools.list_exams(db, domain_slug=domain_slug, limit=limit)
            if method == "POST":
                return 201, {"exam": study_tools.log_exam(db, payload)}
        if len(parts) == 3 and parts[:2] == ["api", "exams"] and method == "PUT":
            return 200, {"exam": study_tools.update_exam(db, int(parts[2]), payload)}

        # GET / POST /api/reports  ·  DELETE /api/reports/<id>
        if parts == ["api", "reports"]:
            if method == "GET":
                return 200, {"reports": db.list_reports()}
            if method == "POST":
                return 201, {"report": db.create_report(payload)}
        if len(parts) == 3 and parts[:2] == ["api", "reports"] and method == "DELETE":
            ok = db.delete_report(int(parts[2]))
            if not ok:
                raise APIError(404, "Reporte no encontrado.")
            return 200, {"deleted": True}

        # GET /api/backup/auto
        if parts == ["api", "backup", "auto"] and method == "GET":
            return 200, {"backups": db.list_auto_backups()}

        # GET /api/cheatsheet/<domain_slug>
        if len(parts) == 3 and parts[:2] == ["api", "cheatsheet"] and method == "GET":
            ingreso_only = query.get("ingreso", ["1"])[0] != "0"
            return 200, study_tools.get_cheatsheet(db, parts[2], ingreso_only=ingreso_only)

        # GET /api/errors
        if parts == ["api", "errors"] and method == "GET":
            domain_slug = query.get("domain", [None])[0]
            ingreso_only = query.get("ingreso", ["0"])[0] == "1"
            return 200, study_tools.get_error_bank(db, domain_slug=domain_slug, ingreso_only=ingreso_only)

        # GET /api/notes  ·  PUT /api/notes/<node_id>
        if parts == ["api", "notes"] and method == "GET":
            domain_slug = query.get("domain", [None])[0]
            bookmarked = query.get("bookmarked", ["0"])[0] == "1"
            return 200, study_tools.list_notes(db, domain_slug=domain_slug, bookmarked_only=bookmarked)
        if len(parts) == 3 and parts[:2] == ["api", "notes"] and method == "PUT":
            return 200, {"note": study_tools.save_note(db, int(parts[2]), payload)}

        # GET /api/diagnostic/<domain_slug>  ·  POST /api/diagnostic/<domain_slug>/apply
        if len(parts) == 3 and parts[:2] == ["api", "diagnostic"] and method == "GET":
            return 200, study_tools.get_diagnostic(db, parts[2])
        if (
            len(parts) == 4
            and parts[:2] == ["api", "diagnostic"]
            and parts[3] == "apply"
            and method == "POST"
        ):
            return 200, study_tools.apply_diagnostic(db, parts[2], payload)

        # GET /api/analytics
        if parts == ["api", "analytics"] and method == "GET":
            return 200, study_tools.get_analytics(db)

        # GET /api/export
        if parts == ["api", "export"] and method == "GET":
            return 200, db.export_json()

        # POST /api/import
        if parts == ["api", "import"] and method == "POST":
            return 200, {"imported": db.import_module(payload)}

        # POST /api/backup/restore
        if parts == ["api", "backup", "restore"] and method == "POST":
            return 200, {"restored": db.restore_backup(payload)}

        raise APIError(404, f"Endpoint no encontrado: {method} {path}")

    except APIError:
        raise
    except KeyError as exc:
        raise APIError(404, str(exc).strip("'")) from exc
    except (ValueError, TypeError) as exc:
        raise APIError(400, str(exc)) from exc

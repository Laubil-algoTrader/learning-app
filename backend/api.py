"""REST API routing and request handling for AprendeLab."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import parse_qs, urlparse

from backend import exercise_store, ingreso_uncuyo
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

        # GET /api/search-index
        if method == "GET" and parts == ["api", "search-index"]:
            return 200, db.get_search_index()

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

        # POST /api/nodes
        if parts == ["api", "nodes"] and method == "POST":
            return 201, {"node": db.create_node(payload)}

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
            data["exercise_count"] = exercise_store.count_for_node(data["node"]["slug"])
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

        # GET /api/exercises  ·  GET /api/exercises/<domain_slug>
        if parts == ["api", "exercises"] and method == "GET":
            return 200, exercise_store.overview(db)
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

        # GET /api/export
        if parts == ["api", "export"] and method == "GET":
            return 200, db.export_json()

        # POST /api/import
        if parts == ["api", "import"] and method == "POST":
            return 200, {"imported": db.import_module(payload)}

        raise APIError(404, f"Endpoint no encontrado: {method} {path}")

    except APIError:
        raise
    except KeyError as exc:
        raise APIError(404, str(exc).strip("'")) from exc
    except (ValueError, TypeError) as exc:
        raise APIError(400, str(exc)) from exc

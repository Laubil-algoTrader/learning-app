"""SQLite persistence, Mastery Graph evaluation, and Interleaved Session builder."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import sqlite3
from typing import Any, Iterator

from backend import fsrs
from backend.lessons_data import LESSONS_BY_SLUG
from backend.seed_data import RETIRED_SEED_NODE_SLUGS, SEED_DOMAINS, SEED_TITLE_RENAMES

DEFAULT_SETTINGS = {
    "desired_retention": "0.90",
    "default_session_minutes": "25",
    "theme": "light",
    "new_per_day": "8",
    "ui_state": "{}",
}

# Bump when seed_data.py gains new nodes / cards / auto-check payloads so existing
# databases receive them once (without touching the learner's FSRS progress).
SEED_CONTENT_VERSION = 24
SCHEMA_VERSION = 2

# An item counts as mastered when FSRS predicts it will survive ~3 weeks AND it
# has been recalled on at least 3 separate reviews (one lucky "Bien" is not mastery).
MASTERY_STABILITY_DAYS = 21.0
MASTERY_MIN_REPS = 3
LEGACY_MASTERY_THRESHOLD = 3.0
# Share of a prerequisite's cards that must have been recalled at least once
# (plus its lesson completed) before the next node unlocks.
UNLOCK_PRACTICED_PCT = 60


def local_day(ts: str | None) -> str:
    """Calendar day (learner's local timezone) of a stored UTC ISO timestamp."""
    dt = fsrs.parse_iso(ts)
    if dt is None:
        return ""
    return dt.astimezone().date().isoformat()


def item_progress(stability: float, reps: int, threshold: float = MASTERY_STABILITY_DAYS) -> float:
    """0..1 mastery progress of one card (durability x repeated successful recall)."""
    if reps <= 0 or stability <= 0:
        return 0.0
    durability = min(1.0, stability / max(threshold, 0.1))
    repetition = min(1.0, reps / MASTERY_MIN_REPS)
    return durability * repetition

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    icon TEXT NOT NULL DEFAULT 'book',
    color TEXT NOT NULL DEFAULT '#296a6c',
    domain_type TEXT NOT NULL DEFAULT 'mixed',
    lab_type TEXT NOT NULL DEFAULT 'generic',
    description TEXT NOT NULL DEFAULT '',
    config_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    slug TEXT NOT NULL,
    title TEXT NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    order_index INTEGER NOT NULL DEFAULT 1,
    summary TEXT NOT NULL DEFAULT '',
    prerequisites_json TEXT NOT NULL DEFAULT '[]',
    mastery_threshold REAL NOT NULL DEFAULT 21.0,
    manual_unlocked INTEGER NOT NULL DEFAULT 0,
    lesson_completed_at TEXT,
    lesson_json TEXT NOT NULL DEFAULT '{}',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    UNIQUE(domain_id, slug)
);

CREATE TABLE IF NOT EXISTS learning_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    node_id INTEGER NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    item_type TEXT NOT NULL DEFAULT 'recall',
    title TEXT NOT NULL,
    prompt TEXT NOT NULL,
    answer TEXT NOT NULL,
    hints_json TEXT NOT NULL DEFAULT '[]',
    payload_json TEXT NOT NULL DEFAULT '{}',
    state TEXT NOT NULL DEFAULT 'new',
    stability REAL NOT NULL DEFAULT 0.0,
    difficulty REAL NOT NULL DEFAULT 0.0,
    reps INTEGER NOT NULL DEFAULT 0,
    lapses INTEGER NOT NULL DEFAULT 0,
    due_at TEXT,
    last_review_at TEXT,
    suspended INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS review_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL REFERENCES learning_items(id) ON DELETE CASCADE,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    node_id INTEGER NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL,
    confidence_before TEXT DEFAULT '',
    elapsed_days REAL NOT NULL DEFAULT 0.0,
    duration_sec INTEGER NOT NULL DEFAULT 0,
    feynman_note TEXT NOT NULL DEFAULT '',
    prev_state_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS practice_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    node_id INTEGER REFERENCES nodes(id) ON DELETE SET NULL,
    metric_type TEXT NOT NULL,
    label TEXT NOT NULL DEFAULT '',
    value REAL NOT NULL,
    unit TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Attempts at exercises and projects. Their content lives in code (backend/exercises),
-- so they are referenced by their stable string ids rather than by foreign keys.
CREATE TABLE IF NOT EXISTS exercise_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_id TEXT NOT NULL,
    node_slug TEXT NOT NULL,
    domain_slug TEXT NOT NULL,
    correct INTEGER NOT NULL,
    parts_ok INTEGER NOT NULL DEFAULT 0,
    parts_total INTEGER NOT NULL DEFAULT 0,
    saw_solution INTEGER NOT NULL DEFAULT 0,
    error_tag TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS exam_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_slug TEXT NOT NULL,
    mode TEXT NOT NULL DEFAULT 'general',
    title TEXT NOT NULL DEFAULT '',
    units_json TEXT NOT NULL DEFAULT '[]',
    score_pct INTEGER NOT NULL,
    procedure_score_pct INTEGER,
    passed INTEGER NOT NULL DEFAULT 0,
    correct_count INTEGER NOT NULL,
    total_count INTEGER NOT NULL,
    duration_sec INTEGER NOT NULL DEFAULT 0,
    time_limit_sec INTEGER NOT NULL DEFAULT 0,
    details_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS study_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    node_id INTEGER NOT NULL UNIQUE REFERENCES nodes(id) ON DELETE CASCADE,
    domain_slug TEXT NOT NULL,
    content TEXT NOT NULL DEFAULT '',
    bookmarked INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS content_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL,
    target_id TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    message TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS custom_exercises (
    id TEXT PRIMARY KEY,
    domain_slug TEXT NOT NULL,
    node_slug TEXT NOT NULL,
    title TEXT NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    minutes INTEGER NOT NULL DEFAULT 5,
    statement TEXT NOT NULL,
    parts_json TEXT NOT NULL DEFAULT '[]',
    hints_json TEXT NOT NULL DEFAULT '[]',
    solution_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_items_domain_due ON learning_items(domain_id, due_at);
CREATE INDEX IF NOT EXISTS idx_items_node ON learning_items(node_id);
CREATE INDEX IF NOT EXISTS idx_logs_created ON review_logs(created_at);
CREATE INDEX IF NOT EXISTS idx_metrics_domain ON practice_metrics(domain_id, metric_type);
CREATE INDEX IF NOT EXISTS idx_attempts_exercise ON exercise_attempts(exercise_id);
CREATE INDEX IF NOT EXISTS idx_exams_domain ON exam_attempts(domain_slug, created_at);
CREATE INDEX IF NOT EXISTS idx_notes_domain ON study_notes(domain_slug);
CREATE INDEX IF NOT EXISTS idx_custom_ex_node ON custom_exercises(node_slug);
"""


def slugify(text: str) -> str:
    clean = text.lower().strip()
    replacements = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u", "ñ": "n"
    }
    for src, dst in replacements.items():
        clean = clean.replace(src, dst)
    clean = re.sub(r"[^a-z0-9]+", "-", clean).strip("-")
    return clean or "item"


class Database:
    def __init__(self, db_path: str | Path) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.init_db()

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def init_db(self) -> None:
        with self.connect() as conn:
            conn.executescript(SCHEMA_SQL)
            # Non-destructive schema migration for existing SQLite databases
            cols = {r["name"] for r in conn.execute("PRAGMA table_info(nodes)").fetchall()}
            if "lesson_completed_at" not in cols:
                conn.execute("ALTER TABLE nodes ADD COLUMN lesson_completed_at TEXT")
            if "lesson_json" not in cols:
                conn.execute("ALTER TABLE nodes ADD COLUMN lesson_json TEXT NOT NULL DEFAULT '{}'")
            for key, val in DEFAULT_SETTINGS.items():
                conn.execute(
                    "INSERT OR IGNORE INTO settings(key, value) VALUES (?, ?)",
                    (key, val),
                )
            self._seed_if_empty(conn)
            self._run_migrations(conn)
            self._sync_seed_content(conn)

    def _get_raw_setting(self, conn: sqlite3.Connection, key: str, default: str = "") -> str:
        row = conn.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
        return row["value"] if row else default

    def _set_raw_setting(self, conn: sqlite3.Connection, key: str, value: str) -> None:
        conn.execute("INSERT OR REPLACE INTO settings(key, value) VALUES (?, ?)", (key, value))

    def get_or_create_lan_pin(self) -> str:
        """6-digit PIN other devices on the Wi-Fi must enter once (stable across restarts)."""
        import secrets

        with self.connect() as conn:
            pin = self._get_raw_setting(conn, "lan_pin", "")
            if not pin:
                pin = f"{secrets.randbelow(1_000_000):06d}"
                self._set_raw_setting(conn, "lan_pin", pin)
        return pin

    def _run_migrations(self, conn: sqlite3.Connection) -> None:
        version = int(self._get_raw_setting(conn, "schema_version", "1") or 1)
        if version < 2:
            # Mastery used to mean "stability >= 3 days" (one "Bien" was enough).
            conn.execute(
                "UPDATE nodes SET mastery_threshold = ? WHERE mastery_threshold = ?",
                (MASTERY_STABILITY_DAYS, LEGACY_MASTERY_THRESHOLD),
            )
            # Completing a lesson used to insert a fake "Bien / confianza media" review
            # just to store the Feynman note (the note also lives in practice_metrics).
            conn.execute(
                """
                DELETE FROM review_logs
                WHERE duration_sec = 0 AND elapsed_days = 0.0 AND rating = 3
                  AND confidence_before = 'media' AND TRIM(feynman_note) != ''
                  AND EXISTS (
                      SELECT 1 FROM practice_metrics pm
                      WHERE pm.node_id = review_logs.node_id
                        AND pm.metric_type = 'lesson_completed'
                        AND pm.notes = review_logs.feynman_note
                  )
                """
            )
            self._set_raw_setting(conn, "schema_version", str(SCHEMA_VERSION))
        # Safe additive columns on existing databases
        attempt_cols = {r[1] for r in conn.execute("PRAGMA table_info(exercise_attempts)").fetchall()}
        if "error_tag" not in attempt_cols:
            conn.execute("ALTER TABLE exercise_attempts ADD COLUMN error_tag TEXT NOT NULL DEFAULT ''")
        item_cols = {r[1] for r in conn.execute("PRAGMA table_info(learning_items)").fetchall()}
        if "suspended" not in item_cols:
            conn.execute("ALTER TABLE learning_items ADD COLUMN suspended INTEGER NOT NULL DEFAULT 0")
        log_cols = {r[1] for r in conn.execute("PRAGMA table_info(review_logs)").fetchall()}
        if "prev_state_json" not in log_cols:
            conn.execute("ALTER TABLE review_logs ADD COLUMN prev_state_json TEXT NOT NULL DEFAULT '{}'")
        exam_cols = {r[1] for r in conn.execute("PRAGMA table_info(exam_attempts)").fetchall()}
        if "procedure_score_pct" not in exam_cols:
            conn.execute("ALTER TABLE exam_attempts ADD COLUMN procedure_score_pct INTEGER")

    def _sync_seed_content(self, conn: sqlite3.Connection) -> None:
        """Add new built-in nodes, cards and auto-check payloads once per content version.

        Never touches learner progress (FSRS state, reps, lapses, lesson completion or
        user-created nodes/cards).
        """
        current = int(self._get_raw_setting(conn, "content_version", "1") or 1)
        if current >= SEED_CONTENT_VERSION:
            return
        now = fsrs.to_iso(fsrs.utc_now())
        # Remove explicitly retired built-in nodes (never touches user-created nodes)
        for domain_slug, retired_slugs in RETIRED_SEED_NODE_SLUGS.items():
            if not retired_slugs:
                continue
            drow = conn.execute("SELECT id FROM domains WHERE slug = ?", (domain_slug,)).fetchone()
            if not drow:
                continue
            ph = ",".join("?" for _ in retired_slugs)
            conn.execute(
                f"DELETE FROM nodes WHERE domain_id = ? AND slug IN ({ph})",
                (drow["id"], *retired_slugs),
            )
        # Renamed built-in cards keep their row (and FSRS progress): rename before matching by title
        seed_slugs = [d["slug"] for d in SEED_DOMAINS]
        marks = ",".join("?" for _ in seed_slugs)
        for old_title, new_title in SEED_TITLE_RENAMES.items():
            conn.execute(
                f"""
                UPDATE learning_items SET title = ?
                WHERE title = ?
                  AND domain_id IN (SELECT id FROM domains WHERE slug IN ({marks}))
                  AND NOT EXISTS (
                      SELECT 1 FROM learning_items x
                      WHERE x.node_id = learning_items.node_id AND x.title = ?
                  )
                """,
                (new_title, old_title, *seed_slugs, new_title),
            )
        for d in SEED_DOMAINS:
            drow = conn.execute("SELECT id FROM domains WHERE slug = ?", (d["slug"],)).fetchone()
            if not drow:
                continue  # learner deleted this built-in discipline: respect that
            conn.execute(
                "UPDATE domains SET description = ?, config_json = ? WHERE id = ?",
                (
                    d["description"],
                    json.dumps(d.get("config", {}), ensure_ascii=False),
                    drow["id"],
                ),
            )
            for n in d["nodes"]:
                nrow = conn.execute(
                    "SELECT id FROM nodes WHERE domain_id = ? AND slug = ?", (drow["id"], n["slug"])
                ).fetchone()
                if not nrow:
                    ncur = conn.execute(
                        """
                        INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, prerequisites_json, metadata_json, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            drow["id"],
                            n["slug"],
                            n["title"],
                            n["level"],
                            n["order_index"],
                            n["summary"],
                            json.dumps(n.get("prerequisites", []), ensure_ascii=False),
                            json.dumps(n.get("metadata", {}), ensure_ascii=False),
                            now,
                        ),
                    )
                    node_id = ncur.lastrowid
                else:
                    node_id = nrow["id"]
                    conn.execute(
                        """
                        UPDATE nodes
                        SET title = ?, level = ?, order_index = ?, summary = ?,
                            prerequisites_json = ?, metadata_json = ?
                        WHERE id = ?
                        """,
                        (
                            n["title"],
                            n["level"],
                            n["order_index"],
                            n["summary"],
                            json.dumps(n.get("prerequisites", []), ensure_ascii=False),
                            json.dumps(n.get("metadata", {}), ensure_ascii=False),
                            node_id,
                        ),
                    )
                existing = {
                    r["title"]: r
                    for r in conn.execute(
                        "SELECT id, title, prompt, answer, hints_json, payload_json FROM learning_items WHERE node_id = ?",
                        (node_id,),
                    ).fetchall()
                }
                for item in n["items"]:
                    seed_payload = item.get("payload", {}) or {}
                    seed_hints = json.dumps(item.get("hints", []), ensure_ascii=False)
                    row = existing.get(item["title"])
                    if row is None:
                        conn.execute(
                            """
                            INSERT INTO learning_items(
                                node_id, domain_id, item_type, title, prompt, answer,
                                hints_json, payload_json, state, due_at, created_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'new', ?, ?)
                            """,
                            (
                                node_id, drow["id"], item["item_type"], item["title"],
                                item["prompt"], item["answer"],
                                seed_hints,
                                json.dumps(seed_payload, ensure_ascii=False),
                                now, now,
                            ),
                        )
                        continue
                    payload = json.loads(row["payload_json"] or "{}")
                    changed = (
                        row["prompt"] != item["prompt"]
                        or row["answer"] != item["answer"]
                        or row["hints_json"] != seed_hints
                    )
                    for key in ("check", "lab_metric", "lab_link"):
                        if key in seed_payload and payload.get(key) != seed_payload[key]:
                            payload[key] = seed_payload[key]
                            changed = True
                    if changed:
                        conn.execute(
                            """
                            UPDATE learning_items
                            SET payload_json = ?, prompt = ?, answer = ?, hints_json = ?
                            WHERE id = ?
                            """,
                            (
                                json.dumps(payload, ensure_ascii=False),
                                item["prompt"],
                                item["answer"],
                                seed_hints,
                                row["id"],
                            ),
                        )
        self._set_raw_setting(conn, "content_version", str(SEED_CONTENT_VERSION))

    def _seed_if_empty(self, conn: sqlite3.Connection) -> None:
        """Idempotently seed all built-in domains (adds new built-in subjects like Física on upgrade)."""
        existing_slugs = {
            r["slug"] for r in conn.execute("SELECT slug FROM domains").fetchall()
        }
        now = fsrs.to_iso(fsrs.utc_now())
        for d in SEED_DOMAINS:
            if d["slug"] in existing_slugs:
                continue
            cur = conn.execute(
                """
                INSERT INTO domains(slug, name, icon, color, domain_type, lab_type, description, config_json, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    d["slug"],
                    d["name"],
                    d["icon"],
                    d["color"],
                    d["domain_type"],
                    d["lab_type"],
                    d["description"],
                    json.dumps(d.get("config", {}), ensure_ascii=False),
                    now,
                ),
            )
            domain_id = cur.lastrowid
            for n in d["nodes"]:
                ncur = conn.execute(
                    """
                    INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, prerequisites_json, metadata_json, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        domain_id,
                        n["slug"],
                        n["title"],
                        n["level"],
                        n["order_index"],
                        n["summary"],
                        json.dumps(n.get("prerequisites", []), ensure_ascii=False),
                        json.dumps(n.get("metadata", {}), ensure_ascii=False),
                        now,
                    ),
                )
                node_id = ncur.lastrowid
                for item in n["items"]:
                    conn.execute(
                        """
                        INSERT INTO learning_items(
                            node_id, domain_id, item_type, title, prompt, answer,
                            hints_json, payload_json, state, due_at, created_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'new', ?, ?)
                        """,
                        (
                            node_id,
                            domain_id,
                            item["item_type"],
                            item["title"],
                            item["prompt"],
                            item["answer"],
                            json.dumps(item.get("hints", []), ensure_ascii=False),
                            json.dumps(item.get("payload", {}), ensure_ascii=False),
                            now,
                            now,
                        ),
                    )

    # ---------- Settings ----------

    def get_settings(self) -> dict[str, Any]:
        with self.connect() as conn:
            rows = conn.execute("SELECT key, value FROM settings").fetchall()
        raw = {r["key"]: r["value"] for r in rows}
        try:
            ui_state = json.loads(raw.get("ui_state") or "{}")
        except json.JSONDecodeError:
            ui_state = {}
        try:
            exam_dates = json.loads(raw.get("exam_dates") or "{}")
        except json.JSONDecodeError:
            exam_dates = {}
        return {
            "desired_retention": float(raw.get("desired_retention", 0.90)),
            "default_session_minutes": int(raw.get("default_session_minutes", 25)),
            "theme": raw.get("theme", "light"),
            "new_per_day": int(raw.get("new_per_day", 8)),
            "daily_lesson_goal": int(raw.get("daily_lesson_goal", 1)),
            "daily_exercise_goal": int(raw.get("daily_exercise_goal", 4)),
            "ingreso_focus_mode": raw.get("ingreso_focus_mode", "false") == "true",
            "exam_dates": exam_dates if isinstance(exam_dates, dict) else {},
            "ui_state": ui_state if isinstance(ui_state, dict) else {},
        }

    def update_settings(self, updates: dict[str, Any]) -> dict[str, Any]:
        with self.connect() as conn:
            if "desired_retention" in updates:
                val = fsrs.clamp(float(updates["desired_retention"]), 0.75, 0.97)
                conn.execute(
                    "INSERT OR REPLACE INTO settings(key, value) VALUES ('desired_retention', ?)",
                    (f"{val:.2f}",),
                )
            if "default_session_minutes" in updates:
                mins = int(fsrs.clamp(float(updates["default_session_minutes"]), 10, 90))
                conn.execute(
                    "INSERT OR REPLACE INTO settings(key, value) VALUES ('default_session_minutes', ?)",
                    (str(mins),),
                )
            if "theme" in updates and updates["theme"] in ("dark", "light", "system"):
                conn.execute(
                    "INSERT OR REPLACE INTO settings(key, value) VALUES ('theme', ?)",
                    (updates["theme"],),
                )
            if "new_per_day" in updates:
                per_day = int(fsrs.clamp(float(updates["new_per_day"]), 0, 40))
                self._set_raw_setting(conn, "new_per_day", str(per_day))
            if "daily_lesson_goal" in updates:
                val = int(fsrs.clamp(float(updates["daily_lesson_goal"]), 1, 10))
                self._set_raw_setting(conn, "daily_lesson_goal", str(val))
            if "daily_exercise_goal" in updates:
                val = int(fsrs.clamp(float(updates["daily_exercise_goal"]), 1, 30))
                self._set_raw_setting(conn, "daily_exercise_goal", str(val))
            if "ingreso_focus_mode" in updates:
                self._set_raw_setting(conn, "ingreso_focus_mode", "true" if updates["ingreso_focus_mode"] else "false")
            if isinstance(updates.get("exam_dates"), dict):
                try:
                    merged_dates = json.loads(self._get_raw_setting(conn, "exam_dates", "{}") or "{}")
                except json.JSONDecodeError:
                    merged_dates = {}
                for k, v in updates["exam_dates"].items():
                    s_val = str(v or "").strip()
                    if not s_val:
                        merged_dates.pop(str(k), None)
                    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", s_val):
                        merged_dates[str(k)] = s_val
                self._set_raw_setting(conn, "exam_dates", json.dumps(merged_dates, ensure_ascii=False))
            if isinstance(updates.get("ui_state"), dict):
                # Shallow-merge small UI state blobs (e.g. project checklists) so they sync across devices
                try:
                    merged = json.loads(self._get_raw_setting(conn, "ui_state", "{}") or "{}")
                except json.JSONDecodeError:
                    merged = {}
                merged.update(updates["ui_state"])
                self._set_raw_setting(conn, "ui_state", json.dumps(merged, ensure_ascii=False))
        return self.get_settings()

    # ---------- Helpers ----------

    def _row_to_card(self, row: sqlite3.Row) -> fsrs.CardState:
        return fsrs.CardState(
            state=row["state"],
            stability=row["stability"],
            difficulty=row["difficulty"],
            reps=row["reps"],
            lapses=row["lapses"],
            last_review_at=row["last_review_at"],
            due_at=row["due_at"],
        )

    @staticmethod
    def _due_label(state: str, due_dt: datetime | None, now: datetime) -> str:
        """Plain-language scheduling status (no FSRS jargon) for lists."""
        if state == "new":
            return "Nuevo"
        if due_dt is None:
            return "Sin fecha"
        delta_days = (due_dt - now).total_seconds() / 86400.0
        if delta_days <= 0:
            return "Toca repasar"
        return f"Próximo repaso en {fsrs.format_interval_es(delta_days)}"

    def _learnable_node_ids(self, conn: sqlite3.Connection) -> set[int]:
        """Nodes whose NEW cards may enter the review queue.

        Built-in nodes (and custom ones with an authored lesson) require the guided
        lesson to be completed first, so the queue never quizzes untaught material.
        Custom nodes without an authored lesson are always learnable.
        """
        learnable: set[int] = set()
        for r in conn.execute("SELECT id, slug, lesson_completed_at, lesson_json FROM nodes").fetchall():
            if r["lesson_completed_at"]:
                learnable.add(r["id"])
                continue
            has_custom = bool(json.loads(r["lesson_json"] or "{}").get("hook"))
            if r["slug"] not in LESSONS_BY_SLUG and not has_custom:
                learnable.add(r["id"])
        return learnable

    def _new_introduced_today(self, conn: sqlite3.Connection) -> int:
        today = fsrs.utc_now().astimezone().date().isoformat()
        rows = conn.execute(
            "SELECT item_id, MIN(created_at) AS first_at FROM review_logs GROUP BY item_id"
        ).fetchall()
        return sum(1 for r in rows if local_day(r["first_at"]) == today)

    def _new_remaining_today(self, conn: sqlite3.Connection) -> int:
        per_day = int(self._get_raw_setting(conn, "new_per_day", "8") or 8)
        return max(0, per_day - self._new_introduced_today(conn))

    def _serialize_item(
        self,
        row: sqlite3.Row,
        now: datetime,
        desired_retention: float,
        include_previews: bool = False,
    ) -> dict[str, Any]:
        card = self._row_to_card(row)
        retr = fsrs.current_retrievability(card, now)
        due_dt = fsrs.parse_iso(row["due_at"])
        is_due = row["state"] == "new" or (due_dt is not None and due_dt <= now)
        data: dict[str, Any] = {
            "id": row["id"],
            "node_id": row["node_id"],
            "domain_id": row["domain_id"],
            "item_type": row["item_type"],
            "title": row["title"],
            "prompt": row["prompt"],
            "answer": row["answer"],
            "hints": json.loads(row["hints_json"] or "[]"),
            "payload": json.loads(row["payload_json"] or "{}"),
            "state": row["state"],
            "stability": round(row["stability"], 2),
            "difficulty": round(row["difficulty"], 2),
            "reps": row["reps"],
            "lapses": row["lapses"],
            "due_at": row["due_at"],
            "last_review_at": row["last_review_at"],
            "suspended": bool(row["suspended"]) if "suspended" in row.keys() else False,
            "retrievability": retr,
            "is_due": is_due,
            "due_label": self._due_label(row["state"], due_dt, now),
            "mastered": row["stability"] >= MASTERY_STABILITY_DAYS and row["reps"] >= MASTERY_MIN_REPS,
        }
        if "domain_name" in row.keys():
            data["domain_name"] = row["domain_name"]
            data["domain_slug"] = row["domain_slug"]
            data["domain_icon"] = row["domain_icon"]
            data["domain_color"] = row["domain_color"]
        if "node_title" in row.keys():
            data["node_title"] = row["node_title"]
            data["node_slug"] = row["node_slug"]
        if include_previews:
            data["interval_previews"] = fsrs.preview_intervals(
                card, now, desired_retention
            )
        return data

    # ---------- Domains & Roadmap ----------

    def list_domains(self) -> list[dict[str, Any]]:
        now = fsrs.utc_now()
        with self.connect() as conn:
            domains = conn.execute("SELECT * FROM domains ORDER BY id ASC").fetchall()
            learnable = self._learnable_node_ids(conn)
            result = []
            for d in domains:
                items = conn.execute(
                    "SELECT * FROM learning_items WHERE domain_id = ?", (d["id"],)
                ).fetchall()
                nodes = conn.execute(
                    "SELECT id, lesson_completed_at FROM nodes WHERE domain_id = ?", (d["id"],)
                ).fetchall()
                due_count = 0
                new_count = 0
                locked_new_count = 0
                reviewed_retr = []
                mastered_items = 0
                progress_sum = 0.0
                for it in items:
                    if it["suspended"]:
                        continue
                    card = self._row_to_card(it)
                    due_dt = fsrs.parse_iso(it["due_at"])
                    if it["state"] == "new":
                        if it["node_id"] in learnable:
                            new_count += 1
                        else:
                            locked_new_count += 1
                    elif due_dt is not None and due_dt <= now:
                        due_count += 1
                    r = fsrs.current_retrievability(card, now)
                    if r is not None:
                        reviewed_retr.append(r)
                    progress_sum += item_progress(it["stability"], it["reps"])
                    if it["stability"] >= MASTERY_STABILITY_DAYS and it["reps"] >= MASTERY_MIN_REPS:
                        mastered_items += 1
                avg_retr = (
                    round(sum(reviewed_retr) / len(reviewed_retr) * 100)
                    if reviewed_retr
                    else None
                )
                result.append(
                    {
                        "id": d["id"],
                        "slug": d["slug"],
                        "name": d["name"],
                        "icon": d["icon"],
                        "color": d["color"],
                        "domain_type": d["domain_type"],
                        "lab_type": d["lab_type"],
                        "description": d["description"],
                        "config": json.loads(d["config_json"] or "{}"),
                        "node_count": len(nodes),
                        "item_count": len(items),
                        "due_count": due_count,
                        "new_count": new_count,
                        "locked_new_count": locked_new_count,
                        "lessons_completed": sum(1 for n in nodes if n["lesson_completed_at"]),
                        "mastered_items": mastered_items,
                        "progress_pct": round(progress_sum / len(items) * 100) if items else 0,
                        "memory_health_pct": avg_retr,
                    }
                )
            return result

    def create_domain(self, payload: dict[str, Any]) -> dict[str, Any]:
        name = (payload.get("name") or "").strip()
        if not name:
            raise ValueError("El nombre de la disciplina es obligatorio.")
        slug = slugify(payload.get("slug") or name)
        now = fsrs.to_iso(fsrs.utc_now())
        with self.connect() as conn:
            existing = conn.execute(
                "SELECT id FROM domains WHERE slug = ?", (slug,)
            ).fetchone()
            if existing:
                slug = f"{slug}-{int(fsrs.utc_now().timestamp()) % 1000}"
            cur = conn.execute(
                """
                INSERT INTO domains(slug, name, icon, color, domain_type, lab_type, description, config_json, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    slug,
                    name,
                    (payload.get("icon") or "book").strip() or "book",
                    (payload.get("color") or "#296a6c").strip(),
                    payload.get("domain_type") or "mixed",
                    payload.get("lab_type") or "generic",
                    (payload.get("description") or "").strip(),
                    json.dumps(payload.get("config") or {}, ensure_ascii=False),
                    now,
                ),
            )
            domain_id = cur.lastrowid
            # Optionally create starter node if requested
            if payload.get("create_starter_node", True):
                conn.execute(
                    """
                    INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, prerequisites_json, created_at)
                    VALUES (?, ?, ?, 1, 1, ?, '[]', ?)
                    """,
                    (
                        domain_id,
                        f"{slug}-fundamentos",
                        "1. Fundamentos iniciales",
                        f"Primer bloque práctico para arrancar en {name}.",
                        now,
                    ),
                )
        return next(d for d in self.list_domains() if d["id"] == domain_id)

    def delete_domain(self, domain_id: int) -> bool:
        with self.connect() as conn:
            cur = conn.execute("DELETE FROM domains WHERE id = ?", (domain_id,))
            return cur.rowcount > 0

    def get_roadmap(self, domain_slug: str) -> dict[str, Any]:
        now = fsrs.utc_now()
        settings = self.get_settings()
        with self.connect() as conn:
            d = conn.execute(
                "SELECT * FROM domains WHERE slug = ?", (domain_slug,)
            ).fetchone()
            if not d:
                raise KeyError(f"Disciplina no encontrada: {domain_slug}")
            nodes_rows = conn.execute(
                "SELECT * FROM nodes WHERE domain_id = ? ORDER BY level ASC, order_index ASC, id ASC",
                (d["id"],),
            ).fetchall()
            items_rows = conn.execute(
                "SELECT * FROM learning_items WHERE domain_id = ? ORDER BY id ASC",
                (d["id"],),
            ).fetchall()

        items_by_node: dict[int, list[dict[str, Any]]] = {}
        for r in items_rows:
            items_by_node.setdefault(r["node_id"], []).append(
                self._serialize_item(r, now, settings["desired_retention"], include_previews=True)
            )

        # First pass: compute per-node mastery score
        node_stats: dict[str, dict[str, Any]] = {}
        raw_nodes: list[dict[str, Any]] = []
        for n in nodes_rows:
            n_items = items_by_node.get(n["id"], [])
            threshold = float(n["mastery_threshold"] or MASTERY_STABILITY_DAYS)
            if n_items:
                progress_vals = []
                total_lapses = 0
                total_reps = 0
                practiced = 0
                for it in n_items:
                    total_lapses += it["lapses"]
                    total_reps += it["reps"]
                    progress_vals.append(item_progress(it["stability"], it["reps"], threshold))
                    # "Practiced" = recalled successfully at least once (reached long-term review)
                    if it["reps"] > 0 and (it["state"] == "review" or it["reps"] > it["lapses"] + 1):
                        practiced += 1
                mastery_pct = round(sum(progress_vals) / len(progress_vals) * 100)
                practiced_pct = round(practiced / len(n_items) * 100)
                started = total_reps > 0
            else:
                mastery_pct = 0
                practiced_pct = 100
                total_lapses = 0
                total_reps = 0
                started = False
            lesson_done = bool(n["lesson_completed_at"])
            has_lesson = n["slug"] in LESSONS_BY_SLUG or bool(json.loads(n["lesson_json"] or "{}").get("hook"))

            node_obj = {
                "id": n["id"],
                "domain_id": n["domain_id"],
                "slug": n["slug"],
                "title": n["title"],
                "level": n["level"],
                "order_index": n["order_index"],
                "summary": n["summary"],
                "prerequisites": json.loads(n["prerequisites_json"] or "[]"),
                "mastery_threshold": threshold,
                "manual_unlocked": bool(n["manual_unlocked"]),
                "lesson_completed": bool(n["lesson_completed_at"]),
                "lesson_completed_at": n["lesson_completed_at"],
                "metadata": json.loads(n["metadata_json"] or "{}"),
                "mastery_pct": mastery_pct,
                "practiced_pct": practiced_pct,
                "has_lesson": has_lesson,
                "due_count": sum(1 for it in n_items if it["state"] != "new" and it["is_due"] and not it.get("suspended")),
                "total_reps": total_reps,
                "total_lapses": total_lapses,
                "started": started,
                "items": n_items,
            }
            node_stats[n["slug"]] = node_obj
            raw_nodes.append(node_obj)

        # Second pass: resolve prerequisite unlock status & remediation hints
        remediation_hints: list[dict[str, Any]] = []
        for node in raw_nodes:
            prereq_slugs = node["prerequisites"]
            unmet = []
            weak_prereqs = []
            for pslug in prereq_slugs:
                pnode = node_stats.get(pslug)
                if not pnode:
                    continue
                # Unlocking is about having learned + practiced the base once, not about
                # long-term mastery (which takes weeks and would stall the roadmap).
                lesson_missing = pnode["has_lesson"] and not pnode["lesson_completed"]
                if lesson_missing or pnode["practiced_pct"] < UNLOCK_PRACTICED_PCT:
                    unmet.append(
                        {
                            "slug": pslug,
                            "title": pnode["title"],
                            "mastery_pct": pnode["mastery_pct"],
                            "practiced_pct": pnode["practiced_pct"],
                            "lesson_completed": pnode["lesson_completed"],
                        }
                    )
                if pnode["mastery_pct"] < 50:
                    weak_prereqs.append({"slug": pslug, "title": pnode["title"], "mastery_pct": pnode["mastery_pct"]})

            if node["mastery_pct"] >= 80:
                status = "mastered"
            elif node["started"] or node["lesson_completed"]:
                status = "in_progress"
            elif not unmet or node["manual_unlocked"]:
                status = "available"
            else:
                status = "locked"

            node["status"] = status
            node["unmet_prerequisites"] = unmet
            if node["total_lapses"] >= 2 and weak_prereqs:
                remediation_hints.append(
                    {
                        "node_title": node["title"],
                        "node_slug": node["slug"],
                        "suggested_prereqs": weak_prereqs,
                        "reason": (
                            f"Tuviste {node['total_lapses']} fallos en '{node['title']}'. "
                            f"Reforzar la base previa acelera el dominio."
                        ),
                    }
                )

        return {
            "domain": {
                "id": d["id"],
                "slug": d["slug"],
                "name": d["name"],
                "icon": d["icon"],
                "color": d["color"],
                "domain_type": d["domain_type"],
                "lab_type": d["lab_type"],
                "description": d["description"],
                "config": json.loads(d["config_json"] or "{}"),
            },
            "nodes": raw_nodes,
            "remediation_hints": remediation_hints,
        }

    def unlock_node(self, node_id: int) -> bool:
        with self.connect() as conn:
            cur = conn.execute(
                "UPDATE nodes SET manual_unlocked = 1 WHERE id = ?", (node_id,)
            )
            return cur.rowcount > 0

    # ---------- Guided Step-by-Step Lessons (Modo Aprender) ----------

    def get_node_lesson(self, node_id: int) -> dict[str, Any]:
        with self.connect() as conn:
            row = conn.execute(
                """
                SELECT n.*, d.slug AS domain_slug, d.name AS domain_name,
                       d.icon AS domain_icon, d.lab_type AS domain_lab_type
                FROM nodes n
                JOIN domains d ON d.id = n.domain_id
                WHERE n.id = ?
                """,
                (node_id,),
            ).fetchone()
            if not row:
                raise KeyError("Nodo no encontrado.")
            siblings = conn.execute(
                "SELECT id, slug, title, lesson_completed_at FROM nodes WHERE domain_id = ? ORDER BY level ASC, order_index ASC, id ASC",
                (row["domain_id"],),
            ).fetchall()
            items = conn.execute(
                "SELECT id, title, item_type, prompt, answer, hints_json, payload_json FROM learning_items WHERE node_id = ? ORDER BY id ASC",
                (node_id,),
            ).fetchall()

        custom_lesson = json.loads(row["lesson_json"] or "{}")
        lesson = custom_lesson if custom_lesson.get("hook") else LESSONS_BY_SLUG.get(row["slug"])
        if not lesson:
            # Synthesize a clean guided lesson automatically for user-created custom nodes
            first_item = items[0] if items else None
            points = [row["summary"] or f"Comprendé los fundamentos de {row['title']} paso a paso."]
            for it in items[:4]:
                points.append(f"{it['title']}: {it['answer']}")
            lesson = {
                "hook": {
                    "question": f"¿Qué problema concreto te permite resolver '{row['title']}'?",
                    "intuition": row["summary"] or "Construir un modelo mental claro antes de practicar acelera la retención y evita la memorización mecánica.",
                },
                "concept": {
                    "points": points,
                    "key_rule": first_item["title"] if first_item else row["title"],
                    "pitfall": "Pasar directo a repetir sin comprender el 'por qué' genera conocimiento frágil.",
                },
                "example": {
                    "title": first_item["title"] if first_item else f"Aplicación práctica de {row['title']}",
                    "steps": [
                        first_item["prompt"] if first_item else "Identificá un caso concreto del tema.",
                        first_item["answer"] if first_item else "Aplicá la regla principal paso a paso y verificá el resultado.",
                    ],
                    "lab_link": None,
                    "lab_cta": None,
                },
                "check": {
                    "question": "¿Cuál es la mejor manera de consolidar esta lección justo después de leerla?",
                    "options": [
                        {"text": "Explicarla con tus propias palabras y practicarla con Active Recall (FSRS-5)", "ok": True, "feedback": "Exacto: recuperar activamente el concepto recién aprendido fortalece las conexiones neuronales."},
                        {"text": "Releerla pasivamente 5 veces seguidas", "ok": False, "feedback": "La relectura pasiva genera ilusión de competencia sin memoria duradera."},
                    ],
                },
                "takeaway_prompt": f"Resumí en 1 o 2 frases lo más importante de '{row['title']}' con tus propias palabras.",
            }

        sib_list = [dict(s) for s in siblings]
        pos = next((i for i, s in enumerate(sib_list) if s["id"] == node_id), 0)
        prev_node = sib_list[pos - 1] if pos > 0 else None
        next_node = sib_list[pos + 1] if pos + 1 < len(sib_list) else None

        return {
            "node": {
                "id": row["id"],
                "slug": row["slug"],
                "title": row["title"],
                "level": row["level"],
                "summary": row["summary"],
                "lesson_completed": bool(row["lesson_completed_at"]),
                "lesson_completed_at": row["lesson_completed_at"],
                "item_count": len(items),
                "position": pos + 1,
                "total_nodes": len(sib_list),
            },
            "domain": {
                "id": row["domain_id"],
                "slug": row["domain_slug"],
                "name": row["domain_name"],
                "icon": row["domain_icon"],
                "lab_type": row["domain_lab_type"],
            },
            "lesson": lesson,
            "prev_node": prev_node,
            "next_node": next_node,
        }

    def complete_node_lesson(self, node_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        now_iso = fsrs.to_iso(fsrs.utc_now())
        feynman_note = (payload.get("feynman_note") or "").strip()
        with self.connect() as conn:
            row = conn.execute(
                "SELECT id, domain_id, title FROM nodes WHERE id = ?", (node_id,)
            ).fetchone()
            if not row:
                raise KeyError("Nodo no encontrado.")
            conn.execute(
                "UPDATE nodes SET lesson_completed_at = ? WHERE id = ?",
                (now_iso, node_id),
            )
            conn.execute(
                """
                INSERT INTO practice_metrics(domain_id, node_id, metric_type, label, value, unit, notes, created_at)
                VALUES (?, ?, 'lesson_completed', ?, 1, 'lección', ?, ?)
                """,
                (row["domain_id"], node_id, row["title"], feynman_note, now_iso),
            )
            if feynman_note:
                dom = conn.execute("SELECT slug FROM domains WHERE id = ?", (row["domain_id"],)).fetchone()
                conn.execute(
                    """
                    INSERT INTO study_notes(node_id, domain_slug, content, bookmarked, updated_at)
                    VALUES (?, ?, ?, 0, ?)
                    ON CONFLICT(node_id) DO UPDATE SET content = excluded.content, updated_at = excluded.updated_at
                    """,
                    (node_id, dom["slug"] if dom else "", feynman_note, now_iso),
                )
            # Each comprehension question the learner missed becomes a spaced-repetition card
            created_cards = 0
            for miss in (payload.get("missed_checks") or [])[:6]:
                question = (miss.get("question") or "").strip()
                options = [str(o) for o in (miss.get("options") or []) if str(o).strip()]
                correct = miss.get("correct")
                if not question or not isinstance(correct, int) or not (0 <= correct < len(options)):
                    continue
                title = f"Comprobación: {question[:70]}"
                dup = conn.execute(
                    "SELECT id FROM learning_items WHERE node_id = ? AND title = ?", (node_id, title)
                ).fetchone()
                if dup:
                    continue
                answer = options[correct]
                feedback = (miss.get("feedback") or "").strip()
                if feedback:
                    answer = f"{answer}\n\n{feedback}"
                conn.execute(
                    """
                    INSERT INTO learning_items(
                        node_id, domain_id, item_type, title, prompt, answer,
                        hints_json, payload_json, state, due_at, created_at
                    ) VALUES (?, ?, 'recall', ?, ?, ?, '[]', ?, 'new', ?, ?)
                    """,
                    (
                        node_id, row["domain_id"], title, question, answer,
                        json.dumps(
                            {"check": {"type": "choice", "options": options, "correct": correct}, "from_lesson": True},
                            ensure_ascii=False,
                        ),
                        now_iso, now_iso,
                    ),
                )
                created_cards += 1
        return {
            "completed": True,
            "node_id": node_id,
            "lesson_completed_at": now_iso,
            "created_cards": created_cards,
        }

    # ---------- Nodes & Items CRUD ----------

    def create_node(self, payload: dict[str, Any]) -> dict[str, Any]:
        domain_id = int(payload["domain_id"])
        title = (payload.get("title") or "").strip()
        if not title:
            raise ValueError("El título del nodo es obligatorio.")
        slug = slugify(payload.get("slug") or title)
        now = fsrs.to_iso(fsrs.utc_now())
        with self.connect() as conn:
            max_order = conn.execute(
                "SELECT COALESCE(MAX(order_index), 0) FROM nodes WHERE domain_id = ?",
                (domain_id,),
            ).fetchone()[0]
            existing = conn.execute(
                "SELECT id FROM nodes WHERE domain_id = ? AND slug = ?",
                (domain_id, slug),
            ).fetchone()
            if existing:
                slug = f"{slug}-{max_order + 1}"
            cur = conn.execute(
                """
                INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, prerequisites_json, metadata_json, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    domain_id,
                    slug,
                    title,
                    int(payload.get("level") or 1),
                    int(payload.get("order_index") or (max_order + 1)),
                    (payload.get("summary") or "").strip(),
                    json.dumps(payload.get("prerequisites") or [], ensure_ascii=False),
                    json.dumps(payload.get("metadata") or {}, ensure_ascii=False),
                    now,
                ),
            )
            row = conn.execute("SELECT * FROM nodes WHERE id = ?", (cur.lastrowid,)).fetchone()
        return {
            "id": row["id"],
            "domain_id": row["domain_id"],
            "slug": row["slug"],
            "title": row["title"],
            "level": row["level"],
            "order_index": row["order_index"],
            "summary": row["summary"],
            "prerequisites": json.loads(row["prerequisites_json"] or "[]"),
        }

    def update_node(self, node_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        with self.connect() as conn:
            row = conn.execute("SELECT * FROM nodes WHERE id = ?", (node_id,)).fetchone()
            if not row:
                raise KeyError("Nodo no encontrado.")
            title = (payload.get("title", row["title"]) or "").strip()
            if not title:
                raise ValueError("El título del nodo es obligatorio.")
            summary = (payload.get("summary", row["summary"]) or "").strip()
            level = max(1, min(20, int(payload.get("level", row["level"]) or 1)))
            prereqs_json = (
                json.dumps(payload["prerequisites"], ensure_ascii=False)
                if "prerequisites" in payload
                else row["prerequisites_json"]
            )
            lesson_json = row["lesson_json"]
            if isinstance(payload.get("lesson"), dict):
                lesson_json = json.dumps(payload["lesson"], ensure_ascii=False)
            conn.execute(
                """
                UPDATE nodes
                SET title = ?, summary = ?, level = ?, prerequisites_json = ?, lesson_json = ?
                WHERE id = ?
                """,
                (title, summary, level, prereqs_json, lesson_json, node_id),
            )
            updated = conn.execute("SELECT * FROM nodes WHERE id = ?", (node_id,)).fetchone()
        return {
            "id": updated["id"],
            "domain_id": updated["domain_id"],
            "slug": updated["slug"],
            "title": updated["title"],
            "level": updated["level"],
            "order_index": updated["order_index"],
            "summary": updated["summary"],
            "prerequisites": json.loads(updated["prerequisites_json"] or "[]"),
            "lesson": json.loads(updated["lesson_json"] or "{}"),
        }

    def delete_node(self, node_id: int) -> bool:
        with self.connect() as conn:
            row = conn.execute("SELECT slug FROM nodes WHERE id = ?", (node_id,)).fetchone()
            if not row:
                return False
            conn.execute("DELETE FROM custom_exercises WHERE node_slug = ?", (row["slug"],))
            cur = conn.execute("DELETE FROM nodes WHERE id = ?", (node_id,))
            return cur.rowcount > 0

    def create_item(self, payload: dict[str, Any]) -> dict[str, Any]:
        node_id = int(payload["node_id"])
        title = (payload.get("title") or "").strip()
        prompt = (payload.get("prompt") or "").strip()
        answer = (payload.get("answer") or "").strip()
        if not title or not prompt or not answer:
            raise ValueError("Título, pregunta/consigna y respuesta son obligatorios.")
        now = fsrs.utc_now()
        now_iso = fsrs.to_iso(now)
        with self.connect() as conn:
            node = conn.execute("SELECT domain_id FROM nodes WHERE id = ?", (node_id,)).fetchone()
            if not node:
                raise KeyError("Nodo no encontrado.")
            cur = conn.execute(
                """
                INSERT INTO learning_items(
                    node_id, domain_id, item_type, title, prompt, answer,
                    hints_json, payload_json, state, due_at, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'new', ?, ?)
                """,
                (
                    node_id,
                    node["domain_id"],
                    payload.get("item_type") or "recall",
                    title,
                    prompt,
                    answer,
                    json.dumps(payload.get("hints") or [], ensure_ascii=False),
                    json.dumps(payload.get("payload") or {}, ensure_ascii=False),
                    now_iso,
                    now_iso,
                ),
            )
            row = conn.execute(
                "SELECT * FROM learning_items WHERE id = ?", (cur.lastrowid,)
            ).fetchone()
        return self._serialize_item(row, now, self.get_settings()["desired_retention"], True)

    def update_item(self, item_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        now = fsrs.utc_now()
        with self.connect() as conn:
            row = conn.execute(
                "SELECT * FROM learning_items WHERE id = ?", (item_id,)
            ).fetchone()
            if not row:
                raise KeyError("Ítem no encontrado.")
            title = (payload.get("title", row["title"]) or "").strip()
            prompt = (payload.get("prompt", row["prompt"]) or "").strip()
            answer = (payload.get("answer", row["answer"]) or "").strip()
            item_type = payload.get("item_type", row["item_type"])
            hints_json = (
                json.dumps(payload["hints"], ensure_ascii=False)
                if "hints" in payload
                else row["hints_json"]
            )
            payload_json = row["payload_json"]
            if isinstance(payload.get("payload"), dict):
                merged = json.loads(row["payload_json"] or "{}")
                for k, v in payload["payload"].items():
                    if v is None:
                        merged.pop(k, None)
                    else:
                        merged[k] = v
                payload_json = json.dumps(merged, ensure_ascii=False)
            suspended = (
                (1 if payload["suspended"] else 0)
                if "suspended" in payload
                else int(row["suspended"] or 0)
            )
            conn.execute(
                """
                UPDATE learning_items
                SET title = ?, prompt = ?, answer = ?, item_type = ?, hints_json = ?, payload_json = ?, suspended = ?
                WHERE id = ?
                """,
                (title, prompt, answer, item_type, hints_json, payload_json, suspended, item_id),
            )
            updated = conn.execute(
                "SELECT * FROM learning_items WHERE id = ?", (item_id,)
            ).fetchone()
        return self._serialize_item(updated, now, self.get_settings()["desired_retention"], True)

    def list_suspended_items(self) -> list[dict[str, Any]]:
        now = fsrs.utc_now()
        ret = self.get_settings()["desired_retention"]
        with self.connect() as conn:
            rows = conn.execute(
                """
                SELECT li.*, d.name AS domain_name, d.slug AS domain_slug,
                       d.icon AS domain_icon, d.color AS domain_color,
                       n.title AS node_title, n.slug AS node_slug
                FROM learning_items li
                JOIN domains d ON d.id = li.domain_id
                JOIN nodes n ON n.id = li.node_id
                WHERE COALESCE(li.suspended, 0) = 1
                ORDER BY li.id DESC
                """
            ).fetchall()
        return [self._serialize_item(r, now, ret, False) for r in rows]

    def delete_item(self, item_id: int) -> bool:
        with self.connect() as conn:
            cur = conn.execute("DELETE FROM learning_items WHERE id = ?", (item_id,))
            return cur.rowcount > 0

    # ---------- Reviews & FSRS ----------

    def get_due_items(
        self,
        domain_slug: str | None = None,
        node_id: int | None = None,
        limit: int = 20,
        include_new: bool = True,
        practice_all: bool = False,
    ) -> list[dict[str, Any]]:
        return self.get_review_queue(domain_slug, node_id, limit, include_new, practice_all)["items"]

    def get_review_queue(
        self,
        domain_slug: str | None = None,
        node_id: int | None = None,
        limit: int = 20,
        include_new: bool = True,
        practice_all: bool = False,
    ) -> dict[str, Any]:
        """Today's queue: every due review + a capped number of NEW cards from learned lessons.

        - Normal mode: due cards first (most overdue first), then new cards in roadmap
          order, limited by the daily new-card budget. New cards of lessons the learner
          has not completed never appear.
        - node_id: explicit practice of one node (all its cards, no gating).
        - practice_all: voluntary extra practice over already-reviewed cards, weakest first.
        """
        now = fsrs.utc_now()
        now_iso = fsrs.to_iso(now)
        settings = self.get_settings()
        query = """
            SELECT li.*, d.name AS domain_name, d.slug AS domain_slug,
                   d.icon AS domain_icon, d.color AS domain_color,
                   n.title AS node_title, n.slug AS node_slug,
                   n.level AS node_level, n.order_index AS node_order,
                   (
                       SELECT rl.feynman_note
                       FROM review_logs rl
                       WHERE rl.item_id = li.id AND TRIM(rl.feynman_note) != ''
                       ORDER BY rl.id DESC
                       LIMIT 1
                   ) AS last_feynman_note
            FROM learning_items li
            JOIN domains d ON d.id = li.domain_id
            JOIN nodes n ON n.id = li.node_id
            WHERE COALESCE(li.suspended, 0) = 0
        """
        params: list[Any] = []
        if domain_slug:
            query += " AND d.slug = ?"
            params.append(domain_slug)
        if node_id is not None:
            query += " AND li.node_id = ?"
            params.append(int(node_id))
        with self.connect() as conn:
            rows = conn.execute(query, params).fetchall()
            learnable = self._learnable_node_ids(conn)
            new_remaining = self._new_remaining_today(conn)

        roadmap_key = lambda r: (r["node_level"], r["node_order"], r["id"])  # noqa: E731
        due_rows = [r for r in rows if r["state"] != "new" and (r["due_at"] or "") <= now_iso]
        new_rows = [r for r in rows if r["state"] == "new"]
        learnable_new = sorted((r for r in new_rows if r["node_id"] in learnable), key=roadmap_key)
        locked_new = len(new_rows) - len(learnable_new)

        if node_id is not None:
            picked = sorted(due_rows, key=lambda r: r["due_at"] or "")
            picked += sorted(new_rows, key=roadmap_key)
            picked += sorted(
                (r for r in rows if r["state"] != "new" and (r["due_at"] or "") > now_iso),
                key=lambda r: r["stability"],
            )
        elif practice_all:
            reviewed = [r for r in rows if r["state"] != "new"]
            picked = sorted(reviewed, key=lambda r: (-r["lapses"], r["stability"], roadmap_key(r)))
        else:
            picked = sorted(due_rows, key=lambda r: r["due_at"] or "")
            if include_new:
                picked += learnable_new[:new_remaining]
        picked = picked[: max(1, int(limit))]

        items = []
        for r in picked:
            item_dict = self._serialize_item(r, now, settings["desired_retention"], include_previews=True)
            item_dict["last_feynman_note"] = r["last_feynman_note"] or ""
            items.append(item_dict)
        return {
            "items": items,
            "meta": {
                "due_total": len(due_rows),
                "new_available": len(learnable_new),
                "new_remaining_today": new_remaining,
                "new_per_day": settings["new_per_day"],
                "locked_new": locked_new,
            },
        }

    def get_search_index(self) -> dict[str, Any]:
        with self.connect() as conn:
            domains = [
                dict(r)
                for r in conn.execute(
                    "SELECT id, slug, name, icon, lab_type, domain_type FROM domains ORDER BY id ASC"
                ).fetchall()
            ]
            nodes = [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT n.id, n.slug, n.title, n.level, d.slug AS domain_slug, d.name AS domain_name, d.icon AS domain_icon, d.lab_type
                    FROM nodes n
                    JOIN domains d ON d.id = n.domain_id
                    ORDER BY d.id ASC, n.level ASC, n.order_index ASC
                    """
                ).fetchall()
            ]
        return {"domains": domains, "nodes": nodes}

    def submit_review(self, item_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        rating = int(payload.get("rating", 0))
        if rating not in fsrs.VALID_RATINGS:
            raise ValueError("Rating inválido (debe ser 1=Otra vez, 2=Difícil, 3=Bien, 4=Fácil).")
        now = fsrs.utc_now()
        settings = self.get_settings()
        with self.connect() as conn:
            row = conn.execute(
                "SELECT * FROM learning_items WHERE id = ?", (item_id,)
            ).fetchone()
            if not row:
                raise KeyError("Ítem no encontrado.")
            card = self._row_to_card(row)
            prev_snapshot = {
                "state": row["state"],
                "stability": float(row["stability"] or 0.0),
                "difficulty": float(row["difficulty"] or 0.0),
                "reps": int(row["reps"] or 0),
                "lapses": int(row["lapses"] or 0),
                "due_at": row["due_at"],
                "last_review_at": row["last_review_at"],
            }
            sched = fsrs.schedule_review(
                card, rating, now=now, desired_retention=settings["desired_retention"]
            )
            conn.execute(
                """
                UPDATE learning_items
                SET state = ?, stability = ?, difficulty = ?, reps = ?, lapses = ?,
                    due_at = ?, last_review_at = ?
                WHERE id = ?
                """,
                (
                    sched["state"],
                    sched["stability"],
                    sched["difficulty"],
                    sched["reps"],
                    sched["lapses"],
                    sched["due_at"],
                    sched["last_review_at"],
                    item_id,
                ),
            )
            cur = conn.execute(
                """
                INSERT INTO review_logs(
                    item_id, domain_id, node_id, rating, confidence_before,
                    elapsed_days, duration_sec, feynman_note, prev_state_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item_id,
                    row["domain_id"],
                    row["node_id"],
                    rating,
                    (payload.get("confidence_before") or "").strip(),
                    sched["elapsed_days"],
                    max(0, int(payload.get("duration_sec") or 0)),
                    (payload.get("feynman_note") or "").strip(),
                    json.dumps(prev_snapshot, ensure_ascii=False),
                    fsrs.to_iso(now),
                ),
            )
            log_id = cur.lastrowid
            updated = conn.execute(
                "SELECT * FROM learning_items WHERE id = ?", (item_id,)
            ).fetchone()
        return {
            "review_log_id": log_id,
            "item": self._serialize_item(updated, now, settings["desired_retention"], True),
            "schedule": sched,
        }

    def undo_last_review(self, log_id: int | None = None) -> dict[str, Any]:
        """Undo a review (the given log_id or the most recent one) restoring prior FSRS state."""
        now = fsrs.utc_now()
        settings = self.get_settings()
        with self.connect() as conn:
            if log_id is not None:
                log = conn.execute("SELECT * FROM review_logs WHERE id = ?", (int(log_id),)).fetchone()
            else:
                log = conn.execute("SELECT * FROM review_logs ORDER BY id DESC LIMIT 1").fetchone()
            if not log:
                raise KeyError("No hay ningún repaso reciente para deshacer.")
            prev = json.loads(log["prev_state_json"] or "{}")
            if not prev:
                raise ValueError("Este repaso no tiene estado previo guardado para deshacer.")
            conn.execute(
                """
                UPDATE learning_items
                SET state = ?, stability = ?, difficulty = ?, reps = ?, lapses = ?,
                    due_at = ?, last_review_at = ?
                WHERE id = ?
                """,
                (
                    prev.get("state", "new"),
                    float(prev.get("stability") or 0.0),
                    float(prev.get("difficulty") or 0.0),
                    int(prev.get("reps") or 0),
                    int(prev.get("lapses") or 0),
                    prev.get("due_at"),
                    prev.get("last_review_at"),
                    log["item_id"],
                ),
            )
            conn.execute("DELETE FROM review_logs WHERE id = ?", (log["id"],))
            restored = conn.execute(
                """
                SELECT li.*, d.name AS domain_name, d.slug AS domain_slug,
                       d.icon AS domain_icon, d.color AS domain_color,
                       n.title AS node_title, n.slug AS node_slug
                FROM learning_items li
                JOIN domains d ON d.id = li.domain_id
                JOIN nodes n ON n.id = li.node_id
                WHERE li.id = ?
                """,
                (log["item_id"],),
            ).fetchone()
        return {
            "undone_log_id": log["id"],
            "item": self._serialize_item(restored, now, settings["desired_retention"], True) if restored else None,
        }

    # ---------- Content error reports ----------

    def create_report(self, payload: dict[str, Any]) -> dict[str, Any]:
        kind = str(payload.get("kind") or "other").strip()[:32]
        target_id = str(payload.get("target_id") or "").strip()[:120]
        title = str(payload.get("title") or "").strip()[:160]
        message = str(payload.get("message") or "").strip()
        if not message:
            raise ValueError("Describí brevemente el error encontrado.")
        now_iso = fsrs.to_iso(fsrs.utc_now())
        with self.connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO content_reports(kind, target_id, title, message, status, created_at)
                VALUES (?, ?, ?, ?, 'open', ?)
                """,
                (kind, target_id, title, message, now_iso),
            )
            row = conn.execute("SELECT * FROM content_reports WHERE id = ?", (cur.lastrowid,)).fetchone()
        return dict(row)

    def list_reports(self) -> list[dict[str, Any]]:
        with self.connect() as conn:
            return [
                dict(r)
                for r in conn.execute(
                    "SELECT * FROM content_reports ORDER BY created_at DESC, id DESC LIMIT 100"
                ).fetchall()
            ]

    def delete_report(self, report_id: int) -> bool:
        with self.connect() as conn:
            cur = conn.execute("DELETE FROM content_reports WHERE id = ?", (int(report_id),))
            return cur.rowcount > 0

    # ---------- Smart Interleaved Session Generator ----------

    def generate_smart_session(
        self, duration_minutes: int = 25, domain_slugs: list[str] | None = None
    ) -> dict[str, Any]:
        """Build a 4-phase evidence-based session:
        1. Warm-up & FSRS Spaced Review
        2. Deliberate Practice (highest-lapse / hardest active bottleneck)
        3. Interleaved Rotation (round-robin across selected domains/nodes)
        4. Overlearning & Feynman Consolidation
        """
        duration_minutes = int(fsrs.clamp(duration_minutes, 10, 60))
        target_items = max(4, min(14, round(duration_minutes / 3.5)))
        now = fsrs.utc_now()
        now_iso = fsrs.to_iso(now)
        settings = self.get_settings()

        with self.connect() as conn:
            query = """
                SELECT li.*, d.name AS domain_name, d.slug AS domain_slug,
                       d.icon AS domain_icon, d.color AS domain_color,
                       n.title AS node_title, n.slug AS node_slug,
                       n.level AS node_level, n.order_index AS node_order
                FROM learning_items li
                JOIN domains d ON d.id = li.domain_id
                JOIN nodes n ON n.id = li.node_id
                WHERE COALESCE(li.suspended, 0) = 0
            """
            params: list[Any] = []
            if domain_slugs:
                placeholders = ",".join("?" for _ in domain_slugs)
                query += f" AND d.slug IN ({placeholders})"
                params.extend(domain_slugs)
            rows = conn.execute(query, params).fetchall()
            learnable = self._learnable_node_ids(conn)
            new_remaining = self._new_remaining_today(conn)

        # Never quiz material whose lesson has not been learned; cap brand-new cards per day
        eligible_rows = []
        new_budget = new_remaining
        for r in sorted(rows, key=lambda x: (x["node_level"], x["node_order"], x["id"])):
            if r["state"] != "new":
                eligible_rows.append(r)
            elif r["node_id"] in learnable and new_budget > 0:
                eligible_rows.append(r)
                new_budget -= 1
        locked_new = sum(1 for r in rows if r["state"] == "new" and r["node_id"] not in learnable)
        rows = eligible_rows

        all_items = [
            self._serialize_item(r, now, settings["desired_retention"], include_previews=True)
            for r in rows
        ]
        # Attach roadmap ordering for sorting
        order_map = {r["id"]: (r["node_level"], r["node_order"]) for r in rows}

        used_ids: set[int] = set()
        blocks: list[dict[str, Any]] = []

        # Phase 1: Overdue FSRS reviews (Warm-up)
        overdue = [
            it for it in all_items
            if it["state"] != "new" and (it["due_at"] or "") <= now_iso
        ]
        overdue.sort(key=lambda x: (x["retrievability"] if x["retrievability"] is not None else 1.0))
        warmup_cap = max(1, target_items // 3)
        for it in overdue[:warmup_cap]:
            used_ids.add(it["id"])
            blocks.append(
                {
                    "phase": "warmup",
                    "phase_label": "1. Calentamiento y Repaso FSRS",
                    "phase_tip": "Intentá recuperar la respuesta sin mirar antes de revelar.",
                    "suggested_minutes": 3,
                    "item": it,
                }
            )

        # Phase 2: Deliberate Practice bottleneck (most lapses / highest difficulty or first fresh item)
        bottlenecks = [
            it for it in all_items
            if it["id"] not in used_ids and (it["lapses"] > 0 or it["difficulty"] >= 6.0)
        ]
        bottlenecks.sort(key=lambda x: (-x["lapses"], -x["difficulty"]))
        if not bottlenecks:
            # Pick the earliest unstarted drill/worked_example as deliberate practice focus
            fresh = [it for it in all_items if it["id"] not in used_ids]
            fresh.sort(key=lambda x: (0 if x["item_type"] in ("drill", "worked_example", "debug") else 1, order_map[x["id"]]))
            bottlenecks = fresh[:2]

        for it in bottlenecks[:2]:
            if len(blocks) >= target_items:
                break
            used_ids.add(it["id"])
            blocks.append(
                {
                    "phase": "deliberate",
                    "phase_label": "2. Práctica Deliberada (Cuello de Botella)",
                    "phase_tip": "Bajá la velocidad: buscá 0 errores antes de acelerar o avanzar.",
                    "suggested_minutes": 5,
                    "item": it,
                }
            )

        # Phase 3: Interleaved Rotation (round-robin across domains so consecutive items differ)
        by_domain: dict[str, list[dict[str, Any]]] = {}
        remaining = [it for it in all_items if it["id"] not in used_ids]
        remaining.sort(key=lambda x: (0 if x["state"] == "new" else 1, order_map[x["id"]]))
        for it in remaining:
            by_domain.setdefault(it["domain_slug"], []).append(it)

        domain_keys = list(by_domain.keys())
        interleave_items: list[dict[str, Any]] = []
        idx = 0
        while domain_keys and len(blocks) + len(interleave_items) < max(target_items - 1, 2):
            key = domain_keys[idx % len(domain_keys)]
            bucket = by_domain[key]
            if bucket:
                picked = bucket.pop(0)
                used_ids.add(picked["id"])
                interleave_items.append(picked)
            if not bucket:
                domain_keys.remove(key)
            else:
                idx += 1

        for it in interleave_items:
            blocks.append(
                {
                    "phase": "interleave",
                    "phase_label": "3. Rotación Intercalada (Interleaving)",
                    "phase_tip": "Cambiar de habilidad obliga al cerebro a reconstruir la estrategia desde cero.",
                    "suggested_minutes": 4,
                    "item": it,
                }
            )

        # Phase 4: Consolidation / Overlearning (revisit the deliberate practice anchor or a remaining item)
        consolidation_item = None
        if blocks:
            deliberate_blocks = [b["item"] for b in blocks if b["phase"] == "deliberate"]
            if deliberate_blocks:
                consolidation_item = deliberate_blocks[0]
            else:
                consolidation_item = blocks[0]["item"]

        if consolidation_item and len(blocks) >= 2:
            blocks.append(
                {
                    "phase": "consolidation",
                    "phase_label": "4. Consolidación (Overlearning + Feynman)",
                    "phase_tip": "Hacé 3 repeticiones limpias o explicá el concepto en 2 frases simples antes de cerrar.",
                    "suggested_minutes": 3,
                    "is_overlearning": True,
                    # Already rated earlier in this session: this block reinforces, it must not
                    # reschedule the card a second time on the same day.
                    "no_schedule": True,
                    "item": consolidation_item,
                }
            )

        return {
            "duration_minutes": duration_minutes,
            "total_blocks": len(blocks),
            "domains_included": sorted({b["item"]["domain_slug"] for b in blocks}),
            "blocks": blocks,
            "locked_new": locked_new,
        }

    # ---------- Metrics & Dashboard ----------

    def log_metric(self, payload: dict[str, Any]) -> dict[str, Any]:
        domain_id = payload.get("domain_id")
        domain_slug = payload.get("domain_slug")
        now_iso = fsrs.to_iso(fsrs.utc_now())
        with self.connect() as conn:
            if not domain_id and domain_slug:
                row = conn.execute(
                    "SELECT id FROM domains WHERE slug = ?", (domain_slug,)
                ).fetchone()
                if not row:
                    raise KeyError("Disciplina no encontrada.")
                domain_id = row["id"]
            if not domain_id:
                raise ValueError("Se requiere domain_id o domain_slug.")
            cur = conn.execute(
                """
                INSERT INTO practice_metrics(domain_id, node_id, metric_type, label, value, unit, notes, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    int(domain_id),
                    payload.get("node_id"),
                    (payload.get("metric_type") or "generic").strip(),
                    (payload.get("label") or "").strip(),
                    float(payload["value"]),
                    (payload.get("unit") or "").strip(),
                    (payload.get("notes") or "").strip(),
                    now_iso,
                ),
            )
            saved = conn.execute(
                "SELECT * FROM practice_metrics WHERE id = ?", (cur.lastrowid,)
            ).fetchone()
        return dict(saved)

    def list_metrics(
        self, domain_slug: str | None = None, metric_type: str | None = None, limit: int = 50
    ) -> list[dict[str, Any]]:
        query = """
            SELECT pm.*, d.slug AS domain_slug, d.name AS domain_name
            FROM practice_metrics pm
            JOIN domains d ON d.id = pm.domain_id
            WHERE 1=1
        """
        params: list[Any] = []
        if domain_slug:
            query += " AND d.slug = ?"
            params.append(domain_slug)
        if metric_type:
            query += " AND pm.metric_type = ?"
            params.append(metric_type)
        query += " ORDER BY pm.created_at DESC, pm.id DESC LIMIT ?"
        params.append(limit)
        with self.connect() as conn:
            rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def get_dashboard(self) -> dict[str, Any]:
        domains = self.list_domains()
        now = fsrs.utc_now()
        local_today = now.astimezone().date()
        today_str = local_today.isoformat()

        # Heatmap for last 56 days (8 weeks), bucketed by the learner's local calendar day
        start_day = local_today - timedelta(days=55)
        heatmap_counts: dict[str, int] = {}
        for i in range(56):
            heatmap_counts[(start_day + timedelta(days=i)).isoformat()] = 0

        with self.connect() as conn:
            window_start = (start_day - timedelta(days=1)).isoformat()
            logs = conn.execute(
                "SELECT created_at, rating FROM review_logs WHERE created_at >= ?",
                (window_start,),
            ).fetchall()
            metrics = conn.execute(
                "SELECT created_at FROM practice_metrics WHERE created_at >= ?",
                (window_start,),
            ).fetchall()
            new_remaining = self._new_remaining_today(conn)
            lessons_completed = conn.execute(
                "SELECT COUNT(*) FROM nodes WHERE lesson_completed_at IS NOT NULL"
            ).fetchone()[0]
            total_reviews = conn.execute("SELECT COUNT(*) FROM review_logs").fetchone()[0]
            due_rows = conn.execute(
                "SELECT state, due_at FROM learning_items WHERE state != 'new' AND due_at IS NOT NULL AND COALESCE(suspended, 0) = 0"
            ).fetchall()
            recent_metrics = [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT pm.id, pm.metric_type, pm.label, pm.value, pm.unit, pm.created_at,
                           d.name AS domain_name, d.slug AS domain_slug, d.icon AS domain_icon, d.lab_type
                    FROM practice_metrics pm
                    JOIN domains d ON d.id = pm.domain_id
                    WHERE pm.metric_type NOT IN ('lesson_completed', 'clean_reps')
                    ORDER BY pm.created_at DESC, pm.id DESC
                    LIMIT 6
                    """
                ).fetchall()
            ]
            feynman_journal = [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT rl.id, rl.feynman_note, rl.rating, rl.created_at,
                           li.title AS item_title, d.name AS domain_name, d.slug AS domain_slug
                    FROM review_logs rl
                    JOIN learning_items li ON li.id = rl.item_id
                    JOIN domains d ON d.id = rl.domain_id
                    WHERE TRIM(rl.feynman_note) != ''
                    ORDER BY rl.id DESC
                    LIMIT 5
                    """
                ).fetchall()
            ]
            # Lesson takeaways are stored with the lesson_completed metric (not as fake reviews)
            feynman_journal += [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT pm.id, pm.notes AS feynman_note, NULL AS rating, pm.created_at,
                           pm.label AS item_title, d.name AS domain_name, d.slug AS domain_slug
                    FROM practice_metrics pm
                    JOIN domains d ON d.id = pm.domain_id
                    WHERE pm.metric_type = 'lesson_completed' AND TRIM(pm.notes) != ''
                    ORDER BY pm.id DESC
                    LIMIT 5
                    """
                ).fetchall()
            ]
            feynman_journal.sort(key=lambda f: f["created_at"], reverse=True)
            feynman_journal = feynman_journal[:5]
            calib_rows = conn.execute(
                """
                SELECT confidence_before, rating
                FROM review_logs
                WHERE TRIM(confidence_before) != ''
                """
            ).fetchall()

        # Metacognitive calibration (detect illusion of competence)
        calib_total = len(calib_rows)
        overconfident = 0
        well_calibrated = 0
        for cr in calib_rows:
            conf = cr["confidence_before"].lower()
            rat = cr["rating"]
            if conf == "alta" and rat == 1:
                overconfident += 1
            elif (conf == "alta" and rat >= 3) or (conf == "media" and rat >= 2) or (conf == "baja" and rat <= 2):
                well_calibrated += 1
        calibration = {
            "total_checked": calib_total,
            "overconfident_lapses": overconfident,
            "calibrated_pct": round(well_calibrated / calib_total * 100) if calib_total else None,
        }

        # 14-day FSRS due forecast (day 0 = today/overdue, days 1..13 = upcoming)
        forecast_counts: dict[str, int] = {}
        today_date = local_today
        for offset in range(14):
            forecast_counts[(today_date + timedelta(days=offset)).isoformat()] = 0
        for dr in due_rows:
            due_dt = fsrs.parse_iso(dr["due_at"])
            if not due_dt:
                continue
            d_date = due_dt.astimezone().date()
            if d_date <= today_date:
                forecast_counts[today_date.isoformat()] += 1
            else:
                key = d_date.isoformat()
                if key in forecast_counts:
                    forecast_counts[key] += 1

        today_reviews = 0
        for log in logs:
            day = local_day(log["created_at"])
            if day in heatmap_counts:
                heatmap_counts[day] += 1
            if day == today_str:
                today_reviews += 1
        for m in metrics:
            day = local_day(m["created_at"])
            if day in heatmap_counts:
                heatmap_counts[day] += 1

        # Active days streak
        streak = 0
        cursor_day = local_today
        while True:
            key = cursor_day.isoformat()
            if heatmap_counts.get(key, 0) > 0:
                streak += 1
                cursor_day -= timedelta(days=1)
            elif cursor_day == local_today:
                # Allow checking yesterday if user hasn't studied yet today
                cursor_day -= timedelta(days=1)
            else:
                break

        remediation_alerts = []
        next_steps: dict[str, dict[str, Any]] = {}
        for d in domains:
            rm = self.get_roadmap(d["slug"])
            for hint in rm["remediation_hints"]:
                remediation_alerts.append(
                    {
                        "domain_slug": d["slug"],
                        "domain_name": d["name"],
                        "domain_icon": d["icon"],
                        **hint,
                    }
                )
            # Pick the most actionable next node: first unlearned available, else first in_progress, else first available
            pick = next(
                (n for n in rm["nodes"] if n["status"] in ("available", "in_progress") and not n["lesson_completed"]),
                None,
            )
            if not pick:
                pick = next((n for n in rm["nodes"] if n["status"] == "in_progress"), None)
            if not pick:
                pick = next((n for n in rm["nodes"] if n["status"] == "available"), None)
            if not pick and rm["nodes"]:
                pick = rm["nodes"][0]
            if pick:
                next_steps[d["slug"]] = {
                    "node_id": pick["id"],
                    "node_title": pick["title"],
                    "status": pick["status"],
                    "mastery_pct": pick["mastery_pct"],
                    "lesson_completed": pick["lesson_completed"],
                    "est_minutes": (pick.get("metadata") or {}).get("est_minutes"),
                    "position": rm["nodes"].index(pick) + 1,
                    "total_nodes": len(rm["nodes"]),
                }

        health_vals = [d["memory_health_pct"] for d in domains if d["memory_health_pct"] is not None]
        overall_health = round(sum(health_vals) / len(health_vals)) if health_vals else None

        return {
            "domains": domains,
            "summary": {
                "total_due": sum(d["due_count"] for d in domains),
                "total_new": sum(d["new_count"] for d in domains),
                # What the learner will actually be asked today (due + capped new cards)
                "new_today": min(new_remaining, sum(d["new_count"] for d in domains)),
                "new_remaining_today": new_remaining,
                "locked_new": sum(d["locked_new_count"] for d in domains),
                "lessons_completed": lessons_completed,
                "total_lessons": sum(d["node_count"] for d in domains),
                "is_first_run": total_reviews == 0 and lessons_completed == 0,
                "total_items": sum(d["item_count"] for d in domains),
                "today_reviews": today_reviews,
                "total_reviews": total_reviews,
                "streak_days": streak,
                "overall_memory_health_pct": overall_health,
            },
            "heatmap": [
                {"date": k, "count": v} for k, v in sorted(heatmap_counts.items())
            ],
            "forecast_14d": [
                {"date": k, "count": v} for k, v in sorted(forecast_counts.items())
            ],
            "recent_metrics": recent_metrics,
            "feynman_journal": feynman_journal,
            "calibration": calibration,
            "next_steps": next_steps,
            "remediation_alerts": remediation_alerts[:5],
            "settings": self.get_settings(),
        }

    # ---------- Export / Import JSON & Automatic / SQLite Backups ----------

    def create_auto_backup(self, max_keep: int = 7) -> Path | None:
        """Create a safe online SQLite daily backup under <db_dir>/backups/ and rotate old ones."""
        if not self.db_path.exists():
            return None
        backup_dir = self.db_path.parent / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        day_tag = datetime.now().strftime("%Y-%m-%d")
        dest = backup_dir / f"aprendelab-{day_tag}.db"
        if not dest.exists():
            tmp = backup_dir / f".tmp-{day_tag}.db"
            src_conn = sqlite3.connect(self.db_path)
            dst_conn = sqlite3.connect(tmp)
            try:
                src_conn.backup(dst_conn)
            finally:
                dst_conn.close()
                src_conn.close()
            tmp.replace(dest)
        # Rotate keeping the newest `max_keep` daily snapshots
        snapshots = sorted(backup_dir.glob("aprendelab-*.db"), reverse=True)
        for old in snapshots[max_keep:]:
            try:
                old.unlink()
            except OSError:
                pass
        return dest

    def list_auto_backups(self) -> list[dict[str, Any]]:
        backup_dir = self.db_path.parent / "backups"
        if not backup_dir.exists():
            return []
        out = []
        for p in sorted(backup_dir.glob("*.db"), reverse=True)[:14]:
            st = p.stat()
            out.append(
                {
                    "name": p.name,
                    "size_kb": max(1, round(st.st_size / 1024)),
                    "modified_at": datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(),
                }
            )
        return out

    def restore_sqlite_file(self, raw_bytes: bytes) -> dict[str, Any]:
        """Validate an uploaded SQLite .db file, snapshot the current DB, and replace it atomically."""
        if not raw_bytes or not raw_bytes.startswith(b"SQLite format 3\x00"):
            raise ValueError("El archivo no es una base de datos SQLite válida (.db).")
        backup_dir = self.db_path.parent / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        tmp = backup_dir / f".upload-{int(datetime.now().timestamp())}.db"
        tmp.write_bytes(raw_bytes)
        try:
            check_conn = sqlite3.connect(tmp)
            try:
                integrity = check_conn.execute("PRAGMA integrity_check").fetchone()
                if not integrity or integrity[0] != "ok":
                    raise ValueError("El archivo SQLite está dañado (falló integrity_check).")
                tables = {
                    r[0]
                    for r in check_conn.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    ).fetchall()
                }
                required = {"domains", "nodes", "learning_items", "review_logs"}
                if not required.issubset(tables):
                    raise ValueError("El archivo SQLite no parece ser un respaldo de AprendeLab.")
                counts = {
                    "domains": check_conn.execute("SELECT COUNT(*) FROM domains").fetchone()[0],
                    "nodes": check_conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0],
                    "reviews": check_conn.execute("SELECT COUNT(*) FROM review_logs").fetchone()[0],
                }
            finally:
                check_conn.close()

            # Save a pre-restore safety snapshot of the current database
            if self.db_path.exists():
                safety = backup_dir / f"pre-restore-{datetime.now().strftime('%Y%m%d-%H%M%S')}.db"
                s_src = sqlite3.connect(self.db_path)
                s_dst = sqlite3.connect(safety)
                try:
                    s_src.backup(s_dst)
                finally:
                    s_dst.close()
                    s_src.close()

            tmp.replace(self.db_path)
            self.init_db()
            return {"ok": True, **counts}
        except Exception:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
            raise

    def export_json(self) -> dict[str, Any]:
        with self.connect() as conn:
            domains = [dict(r) for r in conn.execute("SELECT * FROM domains ORDER BY id").fetchall()]
            nodes = [dict(r) for r in conn.execute("SELECT * FROM nodes ORDER BY id").fetchall()]
            items = [dict(r) for r in conn.execute("SELECT * FROM learning_items ORDER BY id").fetchall()]
            metrics = [dict(r) for r in conn.execute("SELECT * FROM practice_metrics ORDER BY id").fetchall()]
            review_logs = [dict(r) for r in conn.execute("SELECT * FROM review_logs ORDER BY id").fetchall()]
            exercise_attempts = [dict(r) for r in conn.execute("SELECT * FROM exercise_attempts ORDER BY id").fetchall()]
            exam_attempts = [dict(r) for r in conn.execute("SELECT * FROM exam_attempts ORDER BY id").fetchall()]
            study_notes = [dict(r) for r in conn.execute("SELECT * FROM study_notes ORDER BY id").fetchall()]
            custom_exercises = [dict(r) for r in conn.execute("SELECT * FROM custom_exercises ORDER BY created_at").fetchall()]
            content_reports = [dict(r) for r in conn.execute("SELECT * FROM content_reports ORDER BY id").fetchall()]
        return {
            "app": "AprendeLab",
            "version": 2,
            "exported_at": fsrs.to_iso(fsrs.utc_now()),
            "settings": self.get_settings(),
            "domains": domains,
            "nodes": nodes,
            "learning_items": items,
            "practice_metrics": metrics,
            "review_logs": review_logs,
            "exercise_attempts": exercise_attempts,
            "exam_attempts": exam_attempts,
            "study_notes": study_notes,
            "custom_exercises": custom_exercises,
            "content_reports": content_reports,
        }

    def restore_backup(self, bundle: dict[str, Any]) -> dict[str, int]:
        """Restore complete learner progress (settings, FSRS state, review history, metrics, attempts, exams, notes, custom exercises)."""
        res = self.import_module(bundle)
        restored_nodes = 0
        restored_items = 0
        restored_reviews = 0
        restored_metrics = 0
        restored_attempts = 0
        restored_exams = 0
        restored_notes = 0
        restored_custom_ex = 0

        if isinstance(bundle.get("settings"), dict):
            self.update_settings(bundle["settings"])

        with self.connect() as conn:
            domain_by_slug = {
                r["slug"]: r["id"]
                for r in conn.execute("SELECT id, slug FROM domains").fetchall()
            }
            old_domain_slug: dict[Any, str] = {}
            for d in bundle.get("domains") or []:
                dslug = d.get("slug") or slugify(d.get("name") or "")
                if dslug in domain_by_slug:
                    old_domain_slug[d.get("id")] = dslug

            node_by_slug = {
                r["slug"]: (r["id"], r["domain_id"])
                for r in conn.execute("SELECT id, domain_id, slug FROM nodes").fetchall()
            }
            old_node_slug: dict[Any, str] = {}
            for n in bundle.get("nodes") or []:
                slug = n.get("slug")
                if not slug or slug not in node_by_slug:
                    continue
                old_node_slug[n.get("id")] = slug
                nid = node_by_slug[slug][0]
                completed_at = n.get("lesson_completed_at")
                unlocked = int(n.get("manual_unlocked") or 0)
                lesson_j = n.get("lesson_json") if isinstance(n.get("lesson_json"), str) else None
                has_custom_lesson = bool(lesson_j and lesson_j.strip() not in ("", "{}"))
                if completed_at or unlocked or has_custom_lesson:
                    conn.execute(
                        """
                        UPDATE nodes
                        SET lesson_completed_at = COALESCE(?, lesson_completed_at),
                            manual_unlocked = CASE WHEN ? = 1 THEN 1 ELSE manual_unlocked END,
                            lesson_json = CASE WHEN ? IS NOT NULL AND TRIM(?) NOT IN ('', '{}') THEN ? ELSE lesson_json END
                        WHERE id = ?
                        """,
                        (completed_at, unlocked, lesson_j, lesson_j or "", lesson_j or "{}", nid),
                    )
                    restored_nodes += 1

            # Map old learning_item ids -> current learning_item rows so review_logs can be restored accurately
            old_item_to_cur: dict[Any, tuple[int, int, int]] = {}
            for it in bundle.get("learning_items") or []:
                slug = old_node_slug.get(it.get("node_id"))
                if not slug or slug not in node_by_slug:
                    continue
                nid, did = node_by_slug[slug]
                title = it.get("title") or ""
                cur_row = conn.execute(
                    "SELECT id FROM learning_items WHERE node_id = ? AND title = ?",
                    (nid, title),
                ).fetchone()
                if cur_row:
                    old_item_to_cur[it.get("id")] = (cur_row["id"], did, nid)
                suspended = int(it.get("suspended") or 0)
                if int(it.get("reps") or 0) > 0 or (it.get("state") or "new") != "new" or suspended:
                    cur = conn.execute(
                        """
                        UPDATE learning_items
                        SET state = ?, stability = ?, difficulty = ?, reps = ?, lapses = ?,
                            due_at = ?, last_review_at = ?, suspended = ?
                        WHERE node_id = ? AND title = ?
                        """,
                        (
                            it.get("state", "new"),
                            float(it.get("stability") or 0.0),
                            float(it.get("difficulty") or 0.0),
                            int(it.get("reps") or 0),
                            int(it.get("lapses") or 0),
                            it.get("due_at"),
                            it.get("last_review_at"),
                            suspended,
                            nid,
                            title,
                        ),
                    )
                    restored_items += cur.rowcount

            # Restore full review_logs history (drives total_reviews, streak_days, heatmap, calibration, study time)
            existing_logs = {
                (r["item_id"], r["created_at"])
                for r in conn.execute("SELECT item_id, created_at FROM review_logs").fetchall()
            }
            for rl in bundle.get("review_logs") or []:
                mapped = old_item_to_cur.get(rl.get("item_id"))
                created_at = rl.get("created_at")
                if not mapped or not created_at:
                    continue
                cur_item_id, cur_dom_id, cur_node_id = mapped
                if (cur_item_id, created_at) in existing_logs:
                    continue
                conn.execute(
                    """
                    INSERT INTO review_logs(
                        item_id, domain_id, node_id, rating, confidence_before,
                        elapsed_days, duration_sec, feynman_note, prev_state_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cur_item_id,
                        cur_dom_id,
                        cur_node_id,
                        int(rl.get("rating") or 3),
                        str(rl.get("confidence_before") or ""),
                        float(rl.get("elapsed_days") or 0.0),
                        int(rl.get("duration_sec") or 0),
                        str(rl.get("feynman_note") or ""),
                        str(rl.get("prev_state_json") or "{}"),
                        created_at,
                    ),
                )
                existing_logs.add((cur_item_id, created_at))
                restored_reviews += 1

            # Restore practice_metrics (lab scores, lesson completions, diagnostic logs, streak activity)
            existing_metrics = {
                (r["domain_id"], r["metric_type"], r["label"], r["created_at"])
                for r in conn.execute(
                    "SELECT domain_id, metric_type, label, created_at FROM practice_metrics"
                ).fetchall()
            }
            for pm in bundle.get("practice_metrics") or []:
                dslug = old_domain_slug.get(pm.get("domain_id"))
                if not dslug or dslug not in domain_by_slug:
                    continue
                cur_dom_id = domain_by_slug[dslug]
                nslug = old_node_slug.get(pm.get("node_id")) if pm.get("node_id") is not None else None
                cur_node_id = node_by_slug[nslug][0] if nslug and nslug in node_by_slug else None
                created_at = pm.get("created_at")
                mtype = str(pm.get("metric_type") or "")
                label = str(pm.get("label") or "")
                if not created_at or not mtype:
                    continue
                mkey = (cur_dom_id, mtype, label, created_at)
                if mkey in existing_metrics:
                    continue
                conn.execute(
                    """
                    INSERT INTO practice_metrics(domain_id, node_id, metric_type, label, value, unit, notes, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cur_dom_id,
                        cur_node_id,
                        mtype,
                        label,
                        float(pm.get("value") or 0.0),
                        str(pm.get("unit") or ""),
                        str(pm.get("notes") or ""),
                        created_at,
                    ),
                )
                existing_metrics.add(mkey)
                restored_metrics += 1

            existing_attempts = {
                (r["exercise_id"], r["created_at"])
                for r in conn.execute("SELECT exercise_id, created_at FROM exercise_attempts").fetchall()
            }
            for att in bundle.get("exercise_attempts") or []:
                key = (att.get("exercise_id"), att.get("created_at"))
                if not key[0] or not key[1] or key in existing_attempts:
                    continue
                conn.execute(
                    """
                    INSERT INTO exercise_attempts(
                        exercise_id, node_slug, domain_slug, correct, parts_ok, parts_total,
                        saw_solution, error_tag, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        att["exercise_id"],
                        att.get("node_slug", ""),
                        att.get("domain_slug", ""),
                        int(att.get("correct") or 0),
                        int(att.get("parts_ok") or 0),
                        int(att.get("parts_total") or 0),
                        int(att.get("saw_solution") or 0),
                        att.get("error_tag", ""),
                        att["created_at"],
                    ),
                )
                existing_attempts.add(key)
                restored_attempts += 1

            existing_exams = {
                (r["domain_slug"], r["created_at"])
                for r in conn.execute("SELECT domain_slug, created_at FROM exam_attempts").fetchall()
            }
            for ex in bundle.get("exam_attempts") or []:
                key = (ex.get("domain_slug"), ex.get("created_at"))
                if not key[0] or not key[1] or key in existing_exams:
                    continue
                conn.execute(
                    """
                    INSERT INTO exam_attempts(
                        domain_slug, mode, title, units_json, score_pct, procedure_score_pct, passed,
                        correct_count, total_count, duration_sec, time_limit_sec, details_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        ex["domain_slug"],
                        ex.get("mode", "general"),
                        ex.get("title", ""),
                        ex.get("units_json") if isinstance(ex.get("units_json"), str) else json.dumps(ex.get("units") or [], ensure_ascii=False),
                        int(ex.get("score_pct") or 0),
                        ex.get("procedure_score_pct"),
                        int(ex.get("passed") or 0),
                        int(ex.get("correct_count") or 0),
                        int(ex.get("total_count") or 0),
                        int(ex.get("duration_sec") or 0),
                        int(ex.get("time_limit_sec") or 0),
                        ex.get("details_json") if isinstance(ex.get("details_json"), str) else json.dumps(ex.get("details") or [], ensure_ascii=False),
                        ex["created_at"],
                    ),
                )
                existing_exams.add(key)
                restored_exams += 1

            for note in bundle.get("study_notes") or []:
                slug = old_node_slug.get(note.get("node_id"))
                if not slug or slug not in node_by_slug:
                    continue
                nid = node_by_slug[slug][0]
                conn.execute(
                    """
                    INSERT INTO study_notes(node_id, domain_slug, content, bookmarked, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(node_id) DO UPDATE SET
                        content = CASE WHEN TRIM(excluded.content) != '' THEN excluded.content ELSE study_notes.content END,
                        bookmarked = MAX(study_notes.bookmarked, excluded.bookmarked),
                        updated_at = excluded.updated_at
                    """,
                    (
                        nid,
                        note.get("domain_slug", ""),
                        note.get("content", ""),
                        int(note.get("bookmarked") or 0),
                        note.get("updated_at") or fsrs.to_iso(fsrs.utc_now()),
                    ),
                )
                restored_notes += 1

            for cex in bundle.get("custom_exercises") or []:
                cid = cex.get("id")
                if not cid:
                    continue
                cur = conn.execute(
                    """
                    INSERT OR IGNORE INTO custom_exercises(
                        id, domain_slug, node_slug, title, level, minutes, statement,
                        parts_json, hints_json, solution_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cid,
                        cex.get("domain_slug", ""),
                        cex.get("node_slug", ""),
                        cex.get("title", ""),
                        int(cex.get("level") or 1),
                        int(cex.get("minutes") or 5),
                        cex.get("statement", ""),
                        cex.get("parts_json") if isinstance(cex.get("parts_json"), str) else json.dumps(cex.get("parts") or [], ensure_ascii=False),
                        cex.get("hints_json") if isinstance(cex.get("hints_json"), str) else json.dumps(cex.get("hints") or [], ensure_ascii=False),
                        cex.get("solution_json") if isinstance(cex.get("solution_json"), str) else json.dumps(cex.get("solution") or [], ensure_ascii=False),
                        cex.get("created_at") or fsrs.to_iso(fsrs.utc_now()),
                    ),
                )
                restored_custom_ex += cur.rowcount

        return {
            **res,
            "restored_nodes": restored_nodes,
            "restored_items": restored_items,
            "restored_reviews": restored_reviews,
            "restored_metrics": restored_metrics,
            "restored_attempts": restored_attempts,
            "restored_exams": restored_exams,
            "restored_notes": restored_notes,
            "restored_custom_exercises": restored_custom_ex,
        }

    def import_module(self, bundle: dict[str, Any]) -> dict[str, int]:
        """Import one or more domains with their nodes and items without clobbering existing data."""
        domains_in = bundle.get("domains") or []
        nodes_in = bundle.get("nodes") or []
        items_in = bundle.get("learning_items") or []
        now = fsrs.to_iso(fsrs.utc_now())

        added_domains = 0
        added_nodes = 0
        added_items = 0
        domain_id_map: dict[Any, int] = {}
        node_id_map: dict[Any, int] = {}

        with self.connect() as conn:
            for d in domains_in:
                slug = slugify(d.get("slug") or d.get("name") or "modulo")
                existing = conn.execute("SELECT id FROM domains WHERE slug = ?", (slug,)).fetchone()
                if existing:
                    domain_id_map[d.get("id", slug)] = existing["id"]
                else:
                    cfg = d.get("config_json") if isinstance(d.get("config_json"), str) else json.dumps(d.get("config") or {}, ensure_ascii=False)
                    cur = conn.execute(
                        """
                        INSERT INTO domains(slug, name, icon, color, domain_type, lab_type, description, config_json, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            slug,
                            d.get("name") or slug,
                            d.get("icon") or "book",
                            d.get("color") or "#296a6c",
                            d.get("domain_type") or "mixed",
                            d.get("lab_type") or "generic",
                            d.get("description") or "",
                            cfg,
                            now,
                        ),
                    )
                    domain_id_map[d.get("id", slug)] = cur.lastrowid
                    added_domains += 1

            for n in nodes_in:
                target_domain = domain_id_map.get(n.get("domain_id"))
                if not target_domain:
                    continue
                nslug = slugify(n.get("slug") or n.get("title") or "nodo")
                existing = conn.execute(
                    "SELECT id FROM nodes WHERE domain_id = ? AND slug = ?",
                    (target_domain, nslug),
                ).fetchone()
                if existing:
                    node_id_map[n.get("id", nslug)] = existing["id"]
                else:
                    prereqs = n.get("prerequisites_json") if isinstance(n.get("prerequisites_json"), str) else json.dumps(n.get("prerequisites") or [], ensure_ascii=False)
                    meta = n.get("metadata_json") if isinstance(n.get("metadata_json"), str) else json.dumps(n.get("metadata") or {}, ensure_ascii=False)
                    cur = conn.execute(
                        """
                        INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, prerequisites_json, metadata_json, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            target_domain,
                            nslug,
                            n.get("title") or nslug,
                            int(n.get("level") or 1),
                            int(n.get("order_index") or 1),
                            n.get("summary") or "",
                            prereqs,
                            meta,
                            now,
                        ),
                    )
                    node_id_map[n.get("id", nslug)] = cur.lastrowid
                    added_nodes += 1

            for it in items_in:
                target_node = node_id_map.get(it.get("node_id"))
                target_domain = domain_id_map.get(it.get("domain_id"))
                if not target_node or not target_domain:
                    continue
                existing = conn.execute(
                    "SELECT id FROM learning_items WHERE node_id = ? AND title = ?",
                    (target_node, it.get("title") or ""),
                ).fetchone()
                if existing:
                    continue
                hints = it.get("hints_json") if isinstance(it.get("hints_json"), str) else json.dumps(it.get("hints") or [], ensure_ascii=False)
                payload_j = it.get("payload_json") if isinstance(it.get("payload_json"), str) else json.dumps(it.get("payload") or {}, ensure_ascii=False)
                conn.execute(
                    """
                    INSERT INTO learning_items(
                        node_id, domain_id, item_type, title, prompt, answer,
                        hints_json, payload_json, state, stability, difficulty,
                        reps, lapses, due_at, last_review_at, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        target_node,
                        target_domain,
                        it.get("item_type") or "recall",
                        it.get("title") or "Ítem",
                        it.get("prompt") or "",
                        it.get("answer") or "",
                        hints,
                        payload_j,
                        it.get("state") or "new",
                        float(it.get("stability") or 0.0),
                        float(it.get("difficulty") or 0.0),
                        int(it.get("reps") or 0),
                        int(it.get("lapses") or 0),
                        it.get("due_at") or now,
                        it.get("last_review_at"),
                        now,
                    ),
                )
                added_items += 1

        return {
            "added_domains": added_domains,
            "added_nodes": added_nodes,
            "added_items": added_items,
        }

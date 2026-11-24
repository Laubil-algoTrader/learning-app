"""Comprehensive regression tests for study tools, bug fixes, full backup/restore, diagnostics, search, review undo/suspend, editor CRUD & analytics."""

from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
import unittest

from backend import study_tools
from backend.api import handle_api_request
from backend.db import Database
from backend.lessons_data import LESSONS_BY_SLUG


class StudyToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.db_path = Path(self._tmp.name) / "test.db"
        self.db = Database(self.db_path)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_save_note_content_only_without_bookmarked_key(self) -> None:
        """Regression test for the 404 KeyError bug when saving content without 'bookmarked'."""
        _, rm = handle_api_request(self.db, "GET", "/api/domains/fisica/roadmap")
        node_id = rm["nodes"][0]["id"]

        # 1) Create note with ONLY content (no 'bookmarked' key!)
        st1, res1 = handle_api_request(
            self.db,
            "PUT",
            f"/api/notes/{node_id}",
            json.dumps({"content": "Recordar convertir km/h a m/s dividiendo por 3,6."}).encode(),
        )
        self.assertEqual(st1, 200)
        self.assertEqual(res1["note"]["content"], "Recordar convertir km/h a m/s dividiendo por 3,6.")
        self.assertFalse(res1["note"]["bookmarked"])

        # 2) Toggle bookmark ONLY (no 'content' key!) -> keeps content intact
        st2, res2 = handle_api_request(
            self.db,
            "PUT",
            f"/api/notes/{node_id}",
            json.dumps({"bookmarked": True}).encode(),
        )
        self.assertEqual(st2, 200)
        self.assertTrue(res2["note"]["bookmarked"])
        self.assertIn("3,6", res2["note"]["content"])

        # 3) Update content ONLY again -> keeps bookmarked=True intact
        st3, res3 = handle_api_request(
            self.db,
            "PUT",
            f"/api/notes/{node_id}",
            json.dumps({"content": "Apunte editado en cuaderno."}).encode(),
        )
        self.assertEqual(st3, 200)
        self.assertTrue(res3["note"]["bookmarked"])
        self.assertEqual(res3["note"]["content"], "Apunte editado en cuaderno.")

    def test_mock_exams_and_procedure_self_evaluation(self) -> None:
        st1, d1 = handle_api_request(
            self.db,
            "POST",
            "/api/exams",
            json.dumps(
                {
                    "domain_slug": "matematicas",
                    "mode": "p1",
                    "title": "Simulacro · Parcial 1",
                    "units": ["U0", "U1", "U2", "U3"],
                    "correct_count": 4,
                    "total_count": 8,
                    "duration_sec": 1800,
                    "time_limit_sec": 3600,
                }
            ).encode(),
        )
        self.assertEqual(st1, 201)
        self.assertEqual(d1["exam"]["score_pct"], 50)
        self.assertFalse(d1["exam"]["passed"])

        # Learner self-evaluates procedure (e.g. arithmetic mistakes on well-set-up problems -> 75%)
        exam_id = d1["exam"]["id"]
        st_up, up = handle_api_request(
            self.db,
            "PUT",
            f"/api/exams/{exam_id}",
            json.dumps({"procedure_score_pct": 75, "details": [{"exercise_id": "x", "procedure_rating": 0.5}]}).encode(),
        )
        self.assertEqual(st_up, 200)
        self.assertEqual(up["exam"]["procedure_score_pct"], 75)
        self.assertTrue(up["exam"]["passed"])

        st_hist, hist = handle_api_request(self.db, "GET", "/api/exams?domain=matematicas")
        self.assertEqual(st_hist, 200)
        self.assertEqual(hist["stats"]["best_score"], 75)
        self.assertEqual(hist["stats"]["passed"], 1)

    def test_exercise_to_card_error_bank_and_auto_retries(self) -> None:
        st, dom = handle_api_request(self.db, "GET", "/api/exercises/matematicas")
        self.assertEqual(st, 200)
        ex = dom["topics"][0]["exercises"][0]
        ex_id = ex["id"]
        parts_len = len(ex["parts"])

        st_att, att = handle_api_request(
            self.db,
            "POST",
            f"/api/exercises/{ex_id}/attempts",
            json.dumps({"correct": False, "parts_ok": 0, "saw_solution": False}).encode(),
        )
        self.assertEqual(st_att, 201)
        self.assertIsNotNone(att["status"]["next_retry_at"])

        # Appears automatically in retry queue
        st_ret, retries = handle_api_request(self.db, "GET", "/api/exercises/retries?domain=matematicas")
        self.assertEqual(st_ret, 200)
        self.assertTrue(any(e["id"] == ex_id for e in retries["exercises"]))

        # Error tagging + error bank
        st_tag, tag_res = handle_api_request(
            self.db,
            "POST",
            f"/api/exercises/{ex_id}/error-tag",
            json.dumps({"error_tag": "planteo"}).encode(),
        )
        self.assertEqual(st_tag, 200)
        self.assertEqual(tag_res["error_tag"], "planteo")

        st_err, err_data = handle_api_request(self.db, "GET", "/api/errors?domain=matematicas")
        self.assertEqual(st_err, 200)
        self.assertTrue(any(e["exercise_id"] == ex_id for e in err_data["weak_exercises"]))

        # Convert to FSRS card + dedup
        st_c1, c1 = handle_api_request(self.db, "POST", f"/api/exercises/{ex_id}/to-card", b"{}")
        self.assertEqual(st_c1, 201)
        self.assertTrue(c1["created"])
        st_c2, c2 = handle_api_request(self.db, "POST", f"/api/exercises/{ex_id}/to-card", b"{}")
        self.assertEqual(st_c2, 201)
        self.assertTrue(c2["already_exists"])

        # Solving unaided removes it from retries & weak exercises
        handle_api_request(
            self.db,
            "POST",
            f"/api/exercises/{ex_id}/attempts",
            json.dumps({"correct": True, "parts_ok": parts_len, "saw_solution": False}).encode(),
        )
        _, err_after = handle_api_request(self.db, "GET", "/api/errors?domain=matematicas")
        self.assertFalse(any(e["exercise_id"] == ex_id for e in err_after["weak_exercises"]))
        _, ret_after = handle_api_request(self.db, "GET", "/api/exercises/retries?domain=matematicas")
        self.assertFalse(any(e["id"] == ex_id for e in ret_after["exercises"]))

    def test_cheatsheet_returns_units_and_rules(self) -> None:
        for slug in ("matematicas", "fisica", "comprension-problemas"):
            st, cs = handle_api_request(self.db, "GET", f"/api/cheatsheet/{slug}?ingreso=1")
            self.assertEqual(st, 200)
            self.assertTrue(cs["ingreso_only"])
            self.assertGreater(len(cs["groups"]), 0)
            self.assertTrue(cs["groups"][0]["topics"][0]["key_rule"])

    def test_diagnostic_multi_question_per_unit_non_lesson_and_opt_in_unlock(self) -> None:
        """Diagnostic must ask >=2 questions per unit, never repeat lesson.check[0], and not silently unlock."""
        for slug, expected_units in (("matematicas", 8), ("fisica", 5), ("comprension-problemas", 3)):
            st, diag = handle_api_request(self.db, "GET", f"/api/diagnostic/{slug}")
            self.assertEqual(st, 200)
            by_unit: dict[str, int] = {}
            for q in diag["questions"]:
                by_unit[q["unit_code"]] = by_unit.get(q["unit_code"], 0) + 1
                les = LESSONS_BY_SLUG.get(q["node_slug"]) or {}
                first_check_q = (les.get("check") or {}).get("question", "")
                self.assertNotEqual(q["question"], first_check_q, f"Diagnostic repeated lesson.check in {q['node_slug']}")
            self.assertEqual(len(by_unit), expected_units)
            for code, cnt in by_unit.items():
                self.assertGreaterEqual(cnt, 2, f"{slug} {code} only has {cnt} question(s)")

        # Apply without unlock_strong -> does NOT unlock anything silently
        _, diag_m = handle_api_request(self.db, "GET", "/api/diagnostic/matematicas")
        results = [
            {"unit_code": q["unit_code"], "node_slug": q["node_slug"], "correct": q["unit_code"] == "U1", "skipped": q["unit_code"] != "U1"}
            for q in diag_m["questions"]
        ]
        st_no, rep_no = handle_api_request(
            self.db,
            "POST",
            "/api/diagnostic/matematicas/apply",
            json.dumps({"results": results}).encode(),
        )
        self.assertEqual(st_no, 200)
        self.assertEqual(rep_no["unlocked_topics"], 0)
        self.assertEqual(rep_no["strong_units_count"], 1)

        # Explicit opt-in unlock -> unlocks U1 topics
        st_yes, rep_yes = handle_api_request(
            self.db,
            "POST",
            "/api/diagnostic/matematicas/apply",
            json.dumps({"results": results, "unlock_strong": True, "save_metric": False}).encode(),
        )
        self.assertEqual(st_yes, 200)
        self.assertGreater(rep_yes["unlocked_topics"], 0)

    def test_review_undo_suspend_and_content_reports(self) -> None:
        _, rm = handle_api_request(self.db, "GET", "/api/domains/fisica/roadmap")
        nid = rm["nodes"][0]["id"]
        handle_api_request(self.db, "POST", f"/api/nodes/{nid}/lesson/complete", b"{}")
        _, queue = handle_api_request(self.db, "GET", f"/api/reviews/due?node={nid}")
        item = queue["items"][0]

        # Submit a review, verify total_reviews increases, then UNDO it
        st_rev, rev = handle_api_request(
            self.db,
            "POST",
            f"/api/reviews/{item['id']}",
            json.dumps({"rating": 3, "confidence_before": "media", "duration_sec": 45}).encode(),
        )
        self.assertEqual(st_rev, 200)
        self.assertEqual(rev["item"]["reps"], 1)
        log_id = rev["review_log_id"]

        st_undo, undo = handle_api_request(
            self.db, "POST", "/api/reviews/undo", json.dumps({"review_log_id": log_id}).encode()
        )
        self.assertEqual(st_undo, 200)
        self.assertEqual(undo["item"]["reps"], 0)
        self.assertEqual(undo["item"]["state"], "new")

        # Suspend item -> disappears from queue and appears in /api/items/suspended
        st_sus, sus = handle_api_request(
            self.db, "PUT", f"/api/items/{item['id']}", json.dumps({"suspended": True}).encode()
        )
        self.assertEqual(st_sus, 200)
        self.assertTrue(sus["item"]["suspended"])

        _, q_after = handle_api_request(self.db, "GET", f"/api/reviews/due?node={nid}")
        self.assertFalse(any(x["id"] == item["id"] for x in q_after["items"]))

        _, sus_list = handle_api_request(self.db, "GET", "/api/items/suspended")
        self.assertTrue(any(x["id"] == item["id"] for x in sus_list["items"]))

        # Content reports CRUD
        st_rep, rep = handle_api_request(
            self.db,
            "POST",
            "/api/reports",
            json.dumps({"kind": "card", "target_id": str(item["id"]), "title": item["title"], "message": "Typo en unidad"}).encode(),
        )
        self.assertEqual(st_rep, 201)
        _, reps = handle_api_request(self.db, "GET", "/api/reports")
        self.assertEqual(len(reps["reports"]), 1)
        st_del, _ = handle_api_request(self.db, "DELETE", f"/api/reports/{rep['report']['id']}")
        self.assertEqual(st_del, 200)

    def test_full_content_search_and_editor_crud(self) -> None:
        # Full-text search matches lesson rules, exercises, cards and notes
        _, rm = handle_api_request(self.db, "GET", "/api/domains/fisica/roadmap")
        nid = rm["nodes"][0]["id"]
        handle_api_request(
            self.db,
            "PUT",
            f"/api/notes/{nid}",
            json.dumps({"content": "Clave secreta xyz987 de prueba."}).encode(),
        )
        st_s1, s1 = handle_api_request(self.db, "GET", "/api/search?q=xyz987")
        self.assertEqual(st_s1, 200)
        self.assertTrue(any(r["kind"] == "note" for r in s1["results"]))

        st_s2, s2 = handle_api_request(self.db, "GET", "/api/search?q=atwood")
        self.assertEqual(st_s2, 200)
        self.assertTrue(any(r["kind"] == "exercise" for r in s2["results"]))

        # Edit custom node + lesson + create & delete custom exercise + delete node
        dom_id = rm["domain"]["id"]
        st_cn, cn = handle_api_request(
            self.db,
            "POST",
            "/api/nodes",
            json.dumps({"domain_id": dom_id, "title": "Tema Propio", "summary": "Resumen inicial"}).encode(),
        )
        self.assertEqual(st_cn, 201)
        new_nid = cn["node"]["id"]

        st_un, un = handle_api_request(
            self.db,
            "PUT",
            f"/api/nodes/{new_nid}",
            json.dumps(
                {
                    "title": "Tema Propio Editado",
                    "summary": "Resumen actualizado",
                    "lesson": {"hook": {"question": "?", "intuition": "Idea"}, "concept": {"points": ["P1"], "key_rule": "ReglaX", "pitfall": "Ojo"}},
                }
            ).encode(),
        )
        self.assertEqual(st_un, 200)
        self.assertEqual(un["node"]["title"], "Tema Propio Editado")

        st_ce, ce = handle_api_request(
            self.db,
            "POST",
            "/api/exercises/custom",
            json.dumps(
                {
                    "node_id": new_nid,
                    "title": "Ejercicio Propio 1",
                    "statement": "Calculá 2 + 2.",
                    "parts": [{"prompt": "Resultado", "answer": "4", "check": {"type": "numeric", "value": 4, "tolerance": 0}}],
                    "hints": ["Sumá"],
                    "solution": ["2 + 2 = 4"],
                }
            ).encode(),
        )
        self.assertEqual(st_ce, 201)
        cex_id = ce["exercise"]["id"]

        # Attempt on custom exercise works seamlessly
        st_ca, _ = handle_api_request(
            self.db,
            "POST",
            f"/api/exercises/{cex_id}/attempts",
            json.dumps({"correct": True, "parts_ok": 1, "saw_solution": False}).encode(),
        )
        self.assertEqual(st_ca, 201)

        st_dce, _ = handle_api_request(self.db, "DELETE", f"/api/exercises/custom/{cex_id}")
        self.assertEqual(st_dce, 200)

        st_dn, _ = handle_api_request(self.db, "DELETE", f"/api/nodes/{new_nid}")
        self.assertEqual(st_dn, 200)

    def test_complete_json_restore_preserves_reviews_streak_metrics_and_sqlite_restore(self) -> None:
        """Restoring JSON must preserve review_logs (total_reviews + streak), metrics, attempts, exams & notes."""
        _, rm = handle_api_request(self.db, "GET", "/api/domains/matematicas/roadmap")
        nid = rm["nodes"][0]["id"]
        handle_api_request(
            self.db,
            "POST",
            f"/api/nodes/{nid}/lesson/complete",
            json.dumps({"feynman_note": "Nota importante para respaldo."}).encode(),
        )
        _, q = handle_api_request(self.db, "GET", f"/api/reviews/due?node={nid}")
        item_id = q["items"][0]["id"]
        handle_api_request(
            self.db,
            "POST",
            f"/api/reviews/{item_id}",
            json.dumps({"rating": 3, "confidence_before": "alta", "duration_sec": 90}).encode(),
        )
        handle_api_request(
            self.db,
            "POST",
            "/api/metrics",
            json.dumps({"domain_id": rm["domain"]["id"], "metric_type": "math_drill", "label": "Drill", "value": 95, "unit": "%"}).encode(),
        )
        handle_api_request(
            self.db,
            "POST",
            "/api/exams",
            json.dumps({"domain_slug": "matematicas", "title": "Global Backup Test", "correct_count": 7, "total_count": 10, "duration_sec": 600}).encode(),
        )

        # Verify analytics study time & topic accuracy on source DB
        st_an, an = handle_api_request(self.db, "GET", "/api/analytics")
        self.assertEqual(st_an, 200)
        self.assertGreaterEqual(an["study_time"]["today_sec"], 690)
        self.assertGreaterEqual(len(an["topic_accuracy"]), 1)

        # Export JSON v2 and restore into fresh DB2
        _, bundle = handle_api_request(self.db, "GET", "/api/export")
        db2_path = Path(self._tmp.name) / "restored.db"
        db2 = Database(db2_path)
        st_res, res = handle_api_request(db2, "POST", "/api/backup/restore", json.dumps(bundle).encode())
        self.assertEqual(st_res, 200)
        self.assertGreaterEqual(res["restored"]["restored_reviews"], 1)
        self.assertGreaterEqual(res["restored"]["restored_metrics"], 1)
        self.assertGreaterEqual(res["restored"]["restored_exams"], 1)

        _, dash2 = handle_api_request(db2, "GET", "/api/dashboard")
        self.assertEqual(dash2["summary"]["total_reviews"], 1)
        self.assertGreaterEqual(dash2["summary"]["streak_days"], 1)

        # Auto-backup + raw SQLite .db restore into fresh DB3
        auto_path = self.db.create_auto_backup()
        self.assertIsNotNone(auto_path)
        self.assertTrue(auto_path.exists())
        self.assertGreaterEqual(len(self.db.list_auto_backups()), 1)

        db3 = Database(Path(self._tmp.name) / "restored_sqlite.db")
        with self.assertRaises(ValueError):
            db3.restore_sqlite_file(b"not a sqlite file")
        sqlite_res = db3.restore_sqlite_file(self.db_path.read_bytes())
        self.assertTrue(sqlite_res["ok"])
        self.assertEqual(sqlite_res["reviews"], 1)
        _, dash3 = handle_api_request(db3, "GET", "/api/dashboard")
        self.assertEqual(dash3["summary"]["total_reviews"], 1)


if __name__ == "__main__":
    unittest.main()

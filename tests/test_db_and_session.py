"""Tests for SQLite persistence, Mastery Graph, Interleaved Sessions, and Export/Import."""

from pathlib import Path
import tempfile
import unittest

from backend.db import Database
from backend.seed_data import SEED_DOMAINS


class TestDatabaseAndSession(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmp.name) / "test.db"
        self.db = Database(self.db_path)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_idempotent_seed_integrity(self) -> None:
        domains = self.db.list_domains()
        self.assertEqual(len(domains), len(SEED_DOMAINS))
        slugs = {d["slug"] for d in domains}
        self.assertEqual(slugs, {d["slug"] for d in SEED_DOMAINS})
        for d in domains:

            expected_nodes = next(len(x["nodes"]) for x in SEED_DOMAINS if x["slug"] == d["slug"])
            self.assertEqual(d["node_count"], expected_nodes)
            self.assertGreaterEqual(d["item_count"], 16)

        # Re-initializing must not duplicate seed rows
        db2 = Database(self.db_path)
        self.assertEqual(len(db2.list_domains()), len(SEED_DOMAINS))

    def _complete_lessons(self, slug: str, count: int) -> list[dict]:
        nodes = self.db.get_roadmap(slug)["nodes"][:count]
        for n in nodes:
            self.db.complete_node_lesson(n["id"], {})
        return nodes

    def test_unlock_needs_lesson_and_practice_but_mastery_takes_time(self) -> None:
        rm = self.db.get_roadmap("matematicas")
        node1 = rm["nodes"][0]
        self.assertEqual(node1["status"], "available")
        self.assertEqual(rm["nodes"][1]["status"], "locked")

        # Practising without having completed the lesson does not unlock the next node
        for it in node1["items"]:
            self.db.submit_review(it["id"], {"rating": 3, "confidence_before": "media"})
        self.assertEqual(self.db.get_roadmap("matematicas")["nodes"][1]["status"], "locked")

        self.db.complete_node_lesson(node1["id"], {})
        rm_after = self.db.get_roadmap("matematicas")
        self.assertEqual(rm_after["nodes"][1]["status"], "available")
        # One good review is practice, not mastery
        self.assertEqual(rm_after["nodes"][0]["status"], "in_progress")
        self.assertLess(rm_after["nodes"][0]["mastery_pct"], 50)
        self.assertEqual(self.db.list_domains()[2]["mastered_items"], 0)

    def test_queue_only_contains_taught_material_and_caps_new_cards(self) -> None:
        # Fresh database: nothing learned yet -> nothing to review
        queue = self.db.get_review_queue(limit=50)
        self.assertEqual(queue["items"], [])
        self.assertGreater(queue["meta"]["locked_new"], 60)

        nodes = self._complete_lessons("guitarra", 3)
        learned_node_ids = {n["id"] for n in nodes}
        self.db.update_settings({"new_per_day": 5})
        queue = self.db.get_review_queue(limit=50)
        self.assertEqual(len(queue["items"]), 5)
        self.assertTrue(all(it["node_id"] in learned_node_ids for it in queue["items"]))

        # Reviewing new cards consumes today's budget
        for it in queue["items"][:2]:
            self.db.submit_review(it["id"], {"rating": 3})
        queue2 = self.db.get_review_queue(limit=50)
        self.assertEqual(queue2["meta"]["new_remaining_today"], 3)
        self.assertEqual(len(queue2["items"]), 3)

        # Explicit node practice ignores the gate
        locked_node = self.db.get_roadmap("fisica")["nodes"][4]
        self.assertGreaterEqual(len(self.db.get_due_items(node_id=locked_node["id"])), 1)

    def test_again_in_same_sitting_does_not_inflate_lapses(self) -> None:
        node = self._complete_lessons("fisica", 1)[0]
        item_id = node["items"][0]["id"]
        self.db.submit_review(item_id, {"rating": 3})
        first = self.db.submit_review(item_id, {"rating": 1})
        self.assertEqual(first["item"]["lapses"], 1)
        again = self.db.submit_review(item_id, {"rating": 1})
        self.assertEqual(again["item"]["lapses"], 1)

    def test_lesson_completion_does_not_fake_a_review_and_missed_checks_become_cards(self) -> None:
        node = self.db.get_roadmap("electronica")["nodes"][0]
        before = len(node["items"])
        res = self.db.complete_node_lesson(
            node["id"],
            {
                "feynman_note": "La corriente es el caudal, el voltaje la presión.",
                "missed_checks": [
                    {"question": "¿Qué mide el voltaje?", "options": ["Caudal", "Presión eléctrica"], "correct": 1, "feedback": "Es la diferencia de potencial."}
                ],
            },
        )
        self.assertEqual(res["created_cards"], 1)
        dash = self.db.get_dashboard()
        self.assertEqual(dash["summary"]["total_reviews"], 0)
        self.assertEqual(dash["calibration"]["total_checked"], 0)
        self.assertEqual(len(dash["feynman_journal"]), 1)
        after = self.db.get_roadmap("electronica")["nodes"][0]
        self.assertEqual(len(after["items"]), before + 1)
        created = after["items"][-1]
        self.assertEqual(created["payload"]["check"]["type"], "choice")
        # Same miss twice must not duplicate the card
        self.db.complete_node_lesson(node["id"], {"missed_checks": [{"question": "¿Qué mide el voltaje?", "options": ["Caudal", "Presión eléctrica"], "correct": 1}]})
        self.assertEqual(len(self.db.get_roadmap("electronica")["nodes"][0]["items"]), before + 1)

    def test_interleaved_session_mixes_domains_and_phases(self) -> None:
        empty = self.db.generate_smart_session(duration_minutes=25)
        self.assertEqual(empty["total_blocks"], 0)

        for slug in ("guitarra", "electronica", "matematicas"):
            self._complete_lessons(slug, 2)
        self.db.update_settings({"new_per_day": 20})
        sess = self.db.generate_smart_session(
            duration_minutes=25, domain_slugs=["guitarra", "electronica", "matematicas"]
        )
        self.assertGreaterEqual(sess["total_blocks"], 4)
        self.assertGreaterEqual(len(sess["domains_included"]), 2)
        phases = [b["phase"] for b in sess["blocks"]]
        self.assertIn("deliberate", phases)
        self.assertIn("interleave", phases)
        self.assertEqual(phases[-1], "consolidation")
        self.assertTrue(sess["blocks"][-1]["no_schedule"])

    def test_seed_content_sync_adds_checks_without_touching_progress(self) -> None:
        import json
        import sqlite3

        node = self.db.get_roadmap("matematicas")["nodes"][0]
        item = node["items"][0]
        self.db.submit_review(item["id"], {"rating": 3})
        conn = sqlite3.connect(self.db_path)
        conn.execute("UPDATE settings SET value = '1' WHERE key = 'content_version'")
        conn.execute("UPDATE learning_items SET payload_json = '{}' WHERE id = ?", (item["id"],))
        conn.execute("DELETE FROM learning_items WHERE id = ?", (node["items"][-1]["id"],))
        conn.commit()
        conn.close()

        db2 = Database(self.db_path)
        after = db2.get_roadmap("matematicas")["nodes"][0]
        self.assertEqual(len(after["items"]), len(node["items"]))
        same = next(i for i in after["items"] if i["id"] == item["id"])
        self.assertEqual(same["reps"], 1)
        for key in ("check", "lab_metric"):
            self.assertEqual(
                json.dumps(same["payload"].get(key), sort_keys=True),
                json.dumps(item["payload"].get(key), sort_keys=True),
            )

    def test_seed_content_sync_adds_new_physics_nodes_without_losing_progress(self) -> None:
        import sqlite3

        from backend.physics_content import PHYSICS_DOMAIN

        phys_before = self.db.get_roadmap("fisica")["nodes"]
        self.assertEqual(len(phys_before), len(PHYSICS_DOMAIN["nodes"]))
        self.assertEqual(phys_before[0]["slug"], "f-intro-fisica")
        # Progress on an existing node (f-magnitudes-vectores) must survive upgrading from v2 -> v4
        existing_node = next(n for n in phys_before if n["slug"] == "f-magnitudes-vectores")
        existing_item = existing_node["items"][0]
        self.db.complete_node_lesson(existing_node["id"], {"feynman_note": "Vector tiene dirección."})
        self.db.submit_review(existing_item["id"], {"rating": 3})

        # Simulate an older v2 database that only had the original 8 Physics nodes
        new_slugs = (
            "f-intro-fisica",
            "f-circular-gravitacion", "f-momento-choques", "f-torque-rotacion", "f-fluidos",
            "f-ondas-em", "f-optica-luz", "f-relatividad", "f-cuantica-nuclear",
        )
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute(
            f"DELETE FROM nodes WHERE slug IN ({','.join('?' for _ in new_slugs)})",
            new_slugs,
        )
        conn.execute("UPDATE settings SET value = '2' WHERE key = 'content_version'")
        conn.commit()
        conn.close()

        # Reopening Database upgrades the content version and restores every Physics node
        upgraded = Database(self.db_path)
        phys_after = upgraded.get_roadmap("fisica")["nodes"]
        self.assertEqual(len(phys_after), len(PHYSICS_DOMAIN["nodes"]))
        self.assertEqual(phys_after[0]["slug"], "f-intro-fisica")
        self.assertEqual(phys_after[0]["status"], "available")
        preserved_node = next(n for n in phys_after if n["slug"] == "f-magnitudes-vectores")
        self.assertTrue(preserved_node["lesson_completed"])
        preserved = next(i for i in preserved_node["items"] if i["id"] == existing_item["id"])
        self.assertEqual(preserved["reps"], 1)
        # Every new node has realistic auto-checked items and a guided lesson with 3 checks
        for node in phys_after:
            lesson = upgraded.get_node_lesson(node["id"])["lesson"]
            self.assertIn("hook", lesson)
            self.assertIn("real_world", lesson["concept"])
            self.assertEqual(1 + len(lesson.get("checks") or []), 3)
            self.assertGreaterEqual(len(node["items"]), 6)

    def test_custom_domain_crud_and_export_import_roundtrip(self) -> None:
        dom = self.db.create_domain(
            {
                "name": "Inglés",
                "icon": "🗣️",
                "color": "#ec4899",
                "domain_type": "conceptual",
                "description": "Listening y vocabulario con FSRS.",
            }
        )
        rm = self.db.get_roadmap(dom["slug"])
        starter_node_id = rm["nodes"][0]["id"]
        created_item = self.db.create_item(
            {
                "node_id": starter_node_id,
                "item_type": "recall",
                "title": "Phrasal verb: figure out",
                "prompt": "¿Qué significa 'figure out' en contexto técnico?",
                "answer": "Descubrir, deducir o resolver cómo funciona algo.",
                "hints": ["Se usa mucho al debuggear."],
            }
        )
        self.assertEqual(created_item["title"], "Phrasal verb: figure out")

        bundle = self.db.export_json()
        self.assertEqual(len(bundle["domains"]), len(SEED_DOMAINS) + 1)

        # Import into a brand new DB
        other_db = Database(Path(self.tmp.name) / "other.db")
        stats = other_db.import_module(bundle)
        self.assertEqual(stats["added_domains"], 1)
        self.assertEqual(stats["added_items"], 1)
        self.assertEqual(len(other_db.list_domains()), len(SEED_DOMAINS) + 1)

    def test_guided_lessons_for_all_32_nodes_and_custom_nodes(self) -> None:
        for slug in ("guitarra", "electronica", "matematicas", "fisica"):
            rm = self.db.get_roadmap(slug)
            for node in rm["nodes"]:
                lesson_data = self.db.get_node_lesson(node["id"])
                self.assertIn("hook", lesson_data["lesson"])
                self.assertIn("concept", lesson_data["lesson"])
                self.assertIn("example", lesson_data["lesson"])
                self.assertIn("check", lesson_data["lesson"])

        # Complete a Physics lesson and check state update
        phys_rm = self.db.get_roadmap("fisica")
        n1_id = phys_rm["nodes"][0]["id"]
        res = self.db.complete_node_lesson(n1_id, {"feynman_note": "Vector tiene magnitud y dirección."})
        self.assertTrue(res["completed"])
        phys_rm_after = self.db.get_roadmap("fisica")
        self.assertTrue(phys_rm_after["nodes"][0]["lesson_completed"])

    def test_renamed_builtin_cards_keep_their_progress(self) -> None:
        import sqlite3

        from backend.seed_data import SEED_TITLE_RENAMES

        old_title, new_title = next(iter(SEED_TITLE_RENAMES.items()))
        conn = sqlite3.connect(self.db_path)
        item_id, node_id = conn.execute(
            "SELECT id, node_id FROM learning_items WHERE title = ?", (new_title,)
        ).fetchone()
        count_before = conn.execute("SELECT COUNT(*) FROM learning_items").fetchone()[0]
        # Simulate a database created before the rename, with progress on that card
        conn.execute("UPDATE learning_items SET title = ? WHERE id = ?", (old_title, item_id))
        conn.execute("UPDATE settings SET value = '4' WHERE key = 'content_version'")
        conn.commit()
        conn.close()
        self.db.submit_review(item_id, {"rating": 3})

        Database(self.db_path)  # re-open: content sync runs
        conn = sqlite3.connect(self.db_path)
        title, reps = conn.execute("SELECT title, reps FROM learning_items WHERE id = ?", (item_id,)).fetchone()
        same_node = conn.execute(
            "SELECT COUNT(*) FROM learning_items WHERE node_id = ? AND title IN (?, ?)",
            (node_id, old_title, new_title),
        ).fetchone()[0]
        count_after = conn.execute("SELECT COUNT(*) FROM learning_items").fetchone()[0]
        conn.close()
        self.assertEqual(title, new_title)
        self.assertEqual(reps, 1)
        self.assertEqual(same_node, 1)
        self.assertEqual(count_after, count_before)

    def test_seed_content_sync_replaces_retired_math_nodes_with_arithmetic(self) -> None:
        import sqlite3

        from backend.math_content import RETIRED_MATH_NODE_SLUGS

        # Add a custom user node inside Matemáticas to ensure migration NEVER deletes user content
        math_dom = next(d for d in self.db.list_domains() if d["slug"] == "matematicas")
        custom = self.db.create_node({"domain_id": math_dom["id"], "title": "Mi nota personal", "level": 1})

        # Simulate an older v6 DB having the retired m-* nodes and none of the new a-*/p-*/al-*/g-*/a2-*/t-*/pc-*/c1-*/c2-*/mv-*/de-*/la-* nodes
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute(
            "DELETE FROM nodes WHERE domain_id = ? AND (slug LIKE 'a-%' OR slug LIKE 'p-%' OR slug LIKE 'al-%' OR slug LIKE 'g-%' OR slug LIKE 'a2-%' OR slug LIKE 't-%' OR slug LIKE 'pc-%' OR slug LIKE 'c1-%' OR slug LIKE 'c2-%' OR slug LIKE 'mv-%' OR slug LIKE 'de-%' OR slug LIKE 'la-%')",
            (math_dom["id"],),
        )
        for i, slug in enumerate(RETIRED_MATH_NODE_SLUGS, 1):
            conn.execute(
                """
                INSERT INTO nodes(domain_id, slug, title, level, order_index, summary, created_at)
                VALUES (?, ?, ?, 1, ?, '', '2026-01-01T00:00:00Z')
                """,
                (math_dom["id"], slug, f"{i}. Old {slug}", i),
            )
        conn.execute("UPDATE settings SET value = '6' WHERE key = 'content_version'")
        conn.commit()
        conn.close()

        upgraded = Database(self.db_path)
        math_nodes = upgraded.get_roadmap("matematicas")["nodes"]
        slugs = [n["slug"] for n in math_nodes]
        for old_slug in RETIRED_MATH_NODE_SLUGS:
            self.assertNotIn(old_slug, slugs)
        self.assertIn(custom["slug"], slugs)
        arith_nodes = [n for n in math_nodes if n["slug"].startswith("a-")]
        prealg_nodes = [n for n in math_nodes if n["slug"].startswith("p-")]
        alg1_nodes = [n for n in math_nodes if n["slug"].startswith("al-")]
        geom_nodes = [n for n in math_nodes if n["slug"].startswith("g-")]
        alg2_nodes = [n for n in math_nodes if n["slug"].startswith("a2-")]
        trig_nodes = [n for n in math_nodes if n["slug"].startswith("t-")]
        precalc_nodes = [n for n in math_nodes if n["slug"].startswith("pc-")]
        calc1_nodes = [n for n in math_nodes if n["slug"].startswith("c1-")]
        calc2_nodes = [n for n in math_nodes if n["slug"].startswith("c2-")]
        mv_nodes = [n for n in math_nodes if n["slug"].startswith("mv-")]
        de_nodes = [n for n in math_nodes if n["slug"].startswith("de-")]
        la_nodes = [n for n in math_nodes if n["slug"].startswith("la-")]
        # Every built-in math topic made it into the database, prefix by prefix.
        from backend.math_content import MATH_DOMAIN

        for prefix, found in [
            ("a-", arith_nodes), ("p-", prealg_nodes), ("al-", alg1_nodes), ("g-", geom_nodes),
            ("a2-", alg2_nodes), ("t-", trig_nodes), ("pc-", precalc_nodes), ("c1-", calc1_nodes),
            ("c2-", calc2_nodes), ("mv-", mv_nodes), ("de-", de_nodes), ("la-", la_nodes),
        ]:
            expected = sum(1 for n in MATH_DOMAIN["nodes"] if n["slug"].startswith(prefix))
            self.assertEqual(len(found), expected, prefix)
        self.assertEqual(arith_nodes[0]["slug"], "a-valor-posicional")
        self.assertEqual(arith_nodes[0]["status"], "available")
        self.assertEqual(arith_nodes[0]["metadata"]["section"], "Aritmética")
        self.assertEqual(prealg_nodes[0]["metadata"]["section"], "Preálgebra")
        self.assertEqual(alg1_nodes[0]["metadata"]["section"], "Álgebra 1")
        self.assertEqual(geom_nodes[0]["metadata"]["section"], "Geometría")
        self.assertEqual(alg2_nodes[0]["metadata"]["section"], "Álgebra 2")
        self.assertEqual(trig_nodes[0]["metadata"]["section"], "Trigonometría")
        self.assertEqual(precalc_nodes[0]["metadata"]["section"], "Precálculo")
        self.assertEqual(calc1_nodes[0]["metadata"]["section"], "Cálculo 1")
        self.assertEqual(calc2_nodes[0]["metadata"]["section"], "Cálculo 2")
        self.assertEqual(mv_nodes[0]["metadata"]["section"], "Cálculo multivariable")
        self.assertEqual(de_nodes[0]["metadata"]["section"], "Ecuaciones diferenciales")
        self.assertEqual(la_nodes[0]["metadata"]["section"], "Álgebra lineal")
        for n in arith_nodes + prealg_nodes + alg1_nodes + geom_nodes + alg2_nodes + trig_nodes + precalc_nodes + calc1_nodes + calc2_nodes + mv_nodes + de_nodes + la_nodes:
            les = upgraded.get_node_lesson(n["id"])["lesson"]
            self.assertEqual(len(les["concept"]["real_world"]), 3)
            self.assertEqual(1 + len(les.get("checks") or []), 3)

        # Every built-in discipline exposes curated multi-stage sections for the roadmap UI

        expected_section_counts = {
            d["slug"]: len({n["metadata"]["section"] for n in d["nodes"]}) for d in SEED_DOMAINS
        }
        for slug, expected_count in expected_section_counts.items():
            rm = upgraded.get_roadmap(slug)
            seen = []
            for node in rm["nodes"]:
                if slug == "matematicas" and node["slug"] == custom["slug"]:
                    continue
                sec = node["metadata"].get("section")
                self.assertTrue(sec, f"Missing section on {slug}/{node['slug']}")
                if sec not in seen:
                    seen.append(sec)
            self.assertEqual(len(seen), expected_count, f"{slug}: {seen}")


if __name__ == "__main__":
    unittest.main()

"""End-to-end HTTP API & static serving tests against an ephemeral server."""

import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from app import create_server
from backend.seed_data import SEED_DOMAINS


class TestHTTPAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmp.name) / "api_test.db"
        self.server = create_server(host="127.0.0.1", port=0, db_path=self.db_path, quiet=True)
        self.port = self.server.server_address[1]
        self.base_url = f"http://127.0.0.1:{self.port}"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        self.tmp.cleanup()

    def _req(self, method: str, path: str, body: dict | None = None) -> tuple[int, dict]:
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = Request(
            self.base_url + path,
            data=data,
            method=method,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urlopen(req, timeout=5) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except HTTPError as err:
            with err:
                return err.code, json.loads(err.read().decode("utf-8"))

    def test_static_frontend_and_pwa_assets(self) -> None:
        for path, needle in [
            ("/", "AprendeLab"),
            ("/manifest.json", "AprendeLab"),
            ("/js/main.js", "renderGuitarLab"),
            ("/css/styles.css", "--accent"),
        ]:
            with urlopen(self.base_url + path, timeout=5) as resp:
                self.assertEqual(resp.status, 200)
                text = resp.read().decode("utf-8")
                self.assertIn(needle, text)

    def test_full_learning_workflow_over_http(self) -> None:
        # 1. Dashboard loads seeded domains (4 incl. Física) + 14-day forecast + search index
        st, dash = self._req("GET", "/api/dashboard")
        self.assertEqual(st, 200)
        self.assertEqual(len(dash["domains"]), len(SEED_DOMAINS))
        self.assertGreater(dash["summary"]["total_items"], 60)
        self.assertEqual(len(dash["forecast_14d"]), 14)

        st, idx = self._req("GET", "/api/search-index")
        self.assertEqual(st, 200)
        self.assertEqual(len(idx["domains"]), len(SEED_DOMAINS))

        self.assertEqual(len(idx["nodes"]), sum(len(d["nodes"]) for d in SEED_DOMAINS))

        # 1b. Guided lesson endpoint & completion
        first_phys_node = next(n for n in idx["nodes"] if n["domain_slug"] == "fisica")
        st, lesson_res = self._req("GET", f"/api/nodes/{first_phys_node['id']}/lesson")
        self.assertEqual(st, 200)
        self.assertIn("hook", lesson_res["lesson"])
        self.assertIn("check", lesson_res["lesson"])
        st, done_res = self._req(
            "POST",
            f"/api/nodes/{first_phys_node['id']}/lesson/complete",
            {"feynman_note": "Escalar es solo magnitud; vector agrega dirección."},
        )
        self.assertEqual(st, 200)
        self.assertTrue(done_res["completed"])

        # 2. Due reviews (by domain & by single node) + submit FSRS review
        st, due = self._req("GET", "/api/reviews/due?domain=guitarra&limit=5")
        self.assertEqual(st, 200)
        self.assertEqual(due["items"], [])  # no guitar lesson learned yet
        for n in [n for n in idx["nodes"] if n["domain_slug"] == "guitarra"][:3]:
            self._req("POST", f"/api/nodes/{n['id']}/lesson/complete", {})
        st, due = self._req("GET", "/api/reviews/due?domain=guitarra&limit=5")
        self.assertEqual(st, 200)
        self.assertEqual(len(due["items"]), 5)
        self.assertIn("new_remaining_today", due["meta"])
        item_id = due["items"][0]["id"]
        node_id = due["items"][0]["node_id"]

        st, node_due = self._req("GET", f"/api/reviews/due?node={node_id}&limit=10")
        self.assertEqual(st, 200)
        self.assertTrue(all(it["node_id"] == node_id for it in node_due["items"]))

        st, rev = self._req(
            "POST",
            f"/api/reviews/{item_id}",
            {"rating": 3, "confidence_before": "media", "duration_sec": 18, "feynman_note": "E A D G B E"},
        )
        self.assertEqual(st, 200)
        self.assertEqual(rev["item"]["reps"], 1)
        self.assertGreater(rev["schedule"]["stability"], 1.0)

        # Verify Feynman journal (1 from Physics lesson + 1 from Guitar review), calibration & next_steps
        st, dash2 = self._req("GET", "/api/dashboard")
        self.assertEqual(st, 200)
        self.assertEqual(len(dash2["feynman_journal"]), 2)
        self.assertEqual(dash2["calibration"]["total_checked"], 1)  # the lesson is not a review
        self.assertEqual(dash2["summary"]["total_reviews"], 1)
        self.assertIn("guitarra", dash2["next_steps"])
        self.assertIn("fisica", dash2["next_steps"])

        st, extra = self._req("GET", "/api/reviews/due?mode=practice_all&limit=5")
        self.assertEqual(st, 200)
        self.assertEqual(len(extra["items"]), 1)  # extra practice only covers reviewed cards

        # 3. Log practice metric (Guitar BPM)
        st, met = self._req(
            "POST",
            "/api/metrics",
            {"domain_slug": "guitarra", "metric_type": "bpm_clean", "label": "Em-Am", "value": 70, "unit": "BPM"},
        )
        self.assertEqual(st, 201)
        self.assertEqual(met["metric"]["value"], 70.0)

        # 4. Generate smart interleaved session
        st, sess = self._req("POST", "/api/sessions/generate", {"duration_minutes": 20})
        self.assertEqual(st, 200)
        self.assertGreaterEqual(sess["total_blocks"], 3)

        # 5. Create & delete custom domain
        st, created = self._req("POST", "/api/domains", {"name": "Dibujo", "icon": "✏️"})
        self.assertEqual(st, 201)
        dom_id = created["domain"]["id"]
        st, deleted = self._req("DELETE", f"/api/domains/{dom_id}")
        self.assertEqual(st, 200)
        self.assertTrue(deleted["deleted"])

        # 6. Error handling on invalid rating / missing route
        st, err = self._req("POST", f"/api/reviews/{item_id}", {"rating": 99})
        self.assertEqual(st, 400)
        self.assertIn("error", err)

        st, nf = self._req("GET", "/api/does-not-exist")
        self.assertEqual(st, 404)
        self.assertIn("error", nf)


class TestLanPin(unittest.TestCase):
    """With a PIN configured, non-loopback clients are locked out of the API until they enter it."""

    def test_pin_gate_and_cookie(self) -> None:
        import app as app_module

        tmp = tempfile.TemporaryDirectory()
        server = create_server(host="127.0.0.1", port=0, db_path=Path(tmp.name) / "pin.db", quiet=True, pin="246810")
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_address[1]}"
        original_loopback = set(app_module.LOOPBACK)
        app_module.LOOPBACK.clear()  # pretend the test client is another device on the Wi-Fi
        try:
            def call(method: str, path: str, body: dict | None = None, cookie: str | None = None):
                headers = {"Content-Type": "application/json"}
                if cookie:
                    headers["Cookie"] = cookie
                req = Request(base + path, data=json.dumps(body).encode() if body is not None else None, method=method, headers=headers)
                try:
                    with urlopen(req, timeout=5) as resp:
                        return resp.status, json.loads(resp.read().decode()), resp.headers.get("Set-Cookie")
                except HTTPError as err:
                    with err:
                        return err.code, json.loads(err.read().decode()), None

            st, data, _ = call("GET", "/api/domains")
            self.assertEqual(st, 401)
            self.assertTrue(data["pin_required"])
            with urlopen(base + "/", timeout=5) as resp:  # the app shell itself still loads
                self.assertEqual(resp.status, 200)

            st, _, _ = call("POST", "/api/auth", {"pin": "000000"})
            self.assertEqual(st, 401)
            st, _, set_cookie = call("POST", "/api/auth", {"pin": "246810"})
            self.assertEqual(st, 200)
            cookie = set_cookie.split(";")[0]
            st, data, _ = call("GET", "/api/domains", cookie=cookie)
            self.assertEqual(st, 200)
            self.assertEqual(len(data["domains"]), len(SEED_DOMAINS))
        finally:
            app_module.LOOPBACK.update(original_loopback)
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()

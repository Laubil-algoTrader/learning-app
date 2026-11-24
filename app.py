#!/usr/bin/env python3
"""AprendeLab — Zero-dependency local web/PWA learning server."""

from __future__ import annotations

import argparse
import hashlib
import hmac
from http import HTTPStatus
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import shutil
import socket
import ssl
import subprocess
import sys
import time
import traceback
from urllib.parse import urlparse

from backend.api import APIError, handle_api_request
from backend.db import Database

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DEFAULT_DB_PATH = BASE_DIR / "data" / "aprendelab.db"
CERT_DIR = BASE_DIR / "data" / "certs"
LOOPBACK = {"127.0.0.1", "::1", "::ffff:127.0.0.1"}
MAX_PIN_FAILURES = 5
PIN_LOCK_SECONDS = 60


def pin_token(pin: str) -> str:
    """Cookie value proving the device entered the PIN (stable while the PIN is)."""
    return hashlib.sha256(f"aprendelab:{pin}".encode("utf-8")).hexdigest()

# Ensure modern web MIME types are registered
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("image/svg+xml", ".svg")


def detect_lan_ip() -> str | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return None


def make_handler(db: Database, frontend_dir: Path = FRONTEND_DIR, pin: str | None = None):
    failures: dict[str, list[float]] = {}

    class AprendeLabHandler(BaseHTTPRequestHandler):
        server_version = "AprendeLab/1.1"

        # ----- LAN access control: other devices must enter the PIN once -----
        def _is_local(self) -> bool:
            return self.client_address[0] in LOOPBACK

        def _has_valid_cookie(self) -> bool:
            jar = SimpleCookie(self.headers.get("Cookie", ""))
            morsel = jar.get("al_session")
            return bool(morsel) and hmac.compare_digest(morsel.value, pin_token(pin or ""))

        def _authorized(self) -> bool:
            return pin is None or self._is_local() or self._has_valid_cookie()

        def _handle_auth(self, body: bytes) -> None:
            ip = self.client_address[0]
            now = time.time()
            recent = [t for t in failures.get(ip, []) if now - t < PIN_LOCK_SECONDS]
            if len(recent) >= MAX_PIN_FAILURES:
                self._send_json(429, {"error": "Demasiados intentos. Esperá un minuto."})
                return
            try:
                given = str(json.loads(body.decode("utf-8") or "{}").get("pin", "")).strip()
            except (json.JSONDecodeError, AttributeError):
                given = ""
            if pin is None or hmac.compare_digest(given, pin):
                failures.pop(ip, None)
                raw = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(raw)))
                self.send_header(
                    "Set-Cookie",
                    f"al_session={pin_token(pin or '')}; Path=/; Max-Age=2592000; HttpOnly; SameSite=Strict",
                )
                self.end_headers()
                self.wfile.write(raw)
                return
            recent.append(now)
            failures[ip] = recent
            self._send_json(401, {"error": "PIN incorrecto.", "pin_required": True})

        def log_message(self, format: str, *args) -> None:  # noqa: A002
            # Keep terminal output tidy during normal usage
            if getattr(self.server, "quiet", False):
                return
            super().log_message(format, *args)

        def _send_json(self, status: int, data: dict) -> None:
            raw = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)

        def _read_body(self, max_bytes: int = 5 * 1024 * 1024) -> bytes:
            length = int(self.headers.get("Content-Length", "0") or "0")
            if length > max_bytes:
                raise APIError(413, f"Payload demasiado grande (máx {max_bytes // (1024 * 1024)}MB).")
            return self.rfile.read(length) if length > 0 else b""

        def _serve_static(self, raw_path: str) -> None:
            parsed = urlparse(raw_path)
            rel = parsed.path.lstrip("/") or "index.html"
            target = (frontend_dir / rel).resolve()
            # Prevent directory traversal outside frontend_dir
            if not str(target).startswith(str(frontend_dir.resolve())):
                self.send_error(HTTPStatus.FORBIDDEN, "Acceso denegado")
                return
            if not target.exists() or target.is_dir():
                target = frontend_dir / "index.html"
            if not target.exists():
                self.send_error(HTTPStatus.NOT_FOUND, "Archivo no encontrado")
                return
            content = target.read_bytes()
            mime, _ = mimetypes.guess_type(str(target))
            if not mime:
                mime = "application/octet-stream"
            if mime.startswith("text/") or mime in ("application/javascript", "application/json"):
                mime = f"{mime}; charset=utf-8"
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(content)))
            if target.name == "sw.js":
                self.send_header("Service-Worker-Allowed", "/")
            self.end_headers()
            self.wfile.write(content)

        def _dispatch(self, method: str) -> None:
            if self.path.startswith("/api/"):
                try:
                    clean_path = urlparse(self.path).path.rstrip("/")
                    max_size = 25 * 1024 * 1024 if clean_path == "/api/backup/restore-db" else 5 * 1024 * 1024
                    body = self._read_body(max_bytes=max_size)
                    if clean_path == "/api/auth" and method == "POST":
                        self._handle_auth(body)
                        return
                    if not self._authorized():
                        self._send_json(401, {"error": "Ingresá el PIN.", "pin_required": True})
                        return
                    if clean_path == "/api/backup/db" and method == "GET":
                        raw_db = Path(db.db_path).read_bytes()
                        fname = f"aprendelab-backup-{time.strftime('%Y-%m-%d')}.db"
                        self.send_response(200)
                        self.send_header("Content-Type", "application/x-sqlite3")
                        self.send_header("Content-Disposition", f'attachment; filename="{fname}"')
                        self.send_header("Content-Length", str(len(raw_db)))
                        self.send_header("Cache-Control", "no-store")
                        self.end_headers()
                        self.wfile.write(raw_db)
                        return
                    if clean_path == "/api/backup/restore-db" and method == "POST":
                        try:
                            result = db.restore_sqlite_file(body)
                        except ValueError as exc:
                            raise APIError(400, str(exc)) from exc
                        self._send_json(200, {"restored": result})
                        return
                    status, data = handle_api_request(db, method, self.path, body)
                    self._send_json(status, data)
                except APIError as exc:
                    self._send_json(exc.status, {"error": exc.message})
                except Exception:  # pragma: no cover - safety net
                    # Details go to the server console, not to whoever made the request
                    traceback.print_exc(file=sys.stderr)
                    self._send_json(500, {"error": "Error interno del servidor. Mirá la consola de AprendeLab."})
            elif method == "GET":
                self._serve_static(self.path)
            else:
                self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

        def do_GET(self) -> None:
            self._dispatch("GET")

        def do_POST(self) -> None:
            self._dispatch("POST")

        def do_PUT(self) -> None:
            self._dispatch("PUT")

        def do_DELETE(self) -> None:
            self._dispatch("DELETE")

    return AprendeLabHandler


def create_server(
    host: str = "127.0.0.1",
    port: int = 8000,
    db_path: str | Path = DEFAULT_DB_PATH,
    quiet: bool = False,
    pin: str | None = None,
    certfile: str | Path | None = None,
    keyfile: str | Path | None = None,
) -> ThreadingHTTPServer:
    db = Database(db_path)
    try:
        db.create_auto_backup()
    except Exception:
        pass
    handler = make_handler(db, FRONTEND_DIR, pin=pin)
    server = ThreadingHTTPServer((host, port), handler)
    if certfile and keyfile:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(certfile=str(certfile), keyfile=str(keyfile))
        server.socket = ctx.wrap_socket(server.socket, server_side=True)
    server.quiet = quiet  # type: ignore[attr-defined]
    server.db = db  # type: ignore[attr-defined]
    return server


def ensure_self_signed_cert(lan_ip: str | None) -> tuple[Path, Path]:
    """Create (once) a self-signed certificate so phones get HTTPS on the LAN."""
    CERT_DIR.mkdir(parents=True, exist_ok=True)
    cert, key = CERT_DIR / "aprendelab.crt", CERT_DIR / "aprendelab.key"
    marker = CERT_DIR / "ip.txt"
    if cert.exists() and key.exists() and marker.exists() and marker.read_text().strip() == (lan_ip or ""):
        return cert, key
    if not shutil.which("openssl"):
        raise SystemExit("--https necesita el comando 'openssl' instalado (o usá --cert y --key con tu propio certificado).")
    san = "DNS:localhost,IP:127.0.0.1" + (f",IP:{lan_ip}" if lan_ip else "")
    subprocess.run(
        [
            "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "825",
            "-keyout", str(key), "-out", str(cert),
            "-subj", "/CN=AprendeLab", "-addext", f"subjectAltName={san}",
        ],
        check=True,
        capture_output=True,
    )
    marker.write_text(lan_ip or "")
    return cert, key


def main() -> None:
    parser = argparse.ArgumentParser(description="Servidor local AprendeLab")
    parser.add_argument("--host", default=None, help="Host (default: 127.0.0.1, o 0.0.0.0 con --lan)")
    parser.add_argument("--port", type=int, default=8000, help="Puerto (default: 8000)")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="Ruta a SQLite DB")
    parser.add_argument("--lan", action="store_true", help="Permitir acceso desde otros dispositivos de tu Wi-Fi (pide PIN)")
    parser.add_argument("--pin", default=None, help="PIN para --lan (default: uno de 6 dígitos guardado en la base)")
    parser.add_argument("--https", action="store_true", help="Servir por HTTPS con un certificado autofirmado (micrófono en el celular)")
    parser.add_argument("--cert", default=None, help="Certificado TLS propio (PEM), por ejemplo de mkcert")
    parser.add_argument("--key", default=None, help="Clave privada del certificado (PEM)")
    args = parser.parse_args()

    host = args.host or ("0.0.0.0" if args.lan else "127.0.0.1")
    exposed = host not in ("127.0.0.1", "localhost", "::1")
    lan_ip = detect_lan_ip() if exposed else None

    pin = None
    if exposed:
        pin = args.pin or Database(args.db).get_or_create_lan_pin()

    certfile, keyfile = args.cert, args.key
    if args.https and not (certfile and keyfile):
        certfile, keyfile = ensure_self_signed_cert(lan_ip)
    scheme = "https" if certfile and keyfile else "http"

    server = create_server(host=host, port=args.port, db_path=args.db, pin=pin, certfile=certfile, keyfile=keyfile)
    lines = [f"En esta PC : {scheme}://localhost:{args.port}"]
    if exposed and lan_ip:
        lines.append(f"En tu Wi-Fi: {scheme}://{lan_ip}:{args.port}")
        lines.append(f"PIN        : {pin}")
    elif not exposed:
        lines.append("Solo esta PC. Para el celular: --lan")
    lines.append(f"Base       : {Path(args.db).name}")
    width = max(len(line) for line in lines) + 2
    print("\n╔" + "═" * width + "╗")
    print("║ " + "AprendeLab".ljust(width - 1) + "║")
    print("╠" + "═" * width + "╣")
    for line in lines:
        print("║ " + line.ljust(width - 1) + "║")
    print("╚" + "═" * width + "╝")
    print("Ctrl+C para detener.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDeteniendo AprendeLab...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

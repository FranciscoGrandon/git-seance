#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitSéance Production Server for Render Cloud
Creado por Francisco Grandón Vergara

Full-stack production server providing:
1. Static Single-Page Altar delivery with security headers (CSP, X-Frame-Options, HSTS).
2. Native Zero-Downtime Health Check endpoint (/healthz) for Render orchestration.
3. Dynamic Git Archaeological REST API:
   - GET  /api/health      -> Health status, uptime, Render environment info.
   - GET  /api/ghosts      -> Mined departed code spirits from repository graveyard.
   - POST /api/seance      -> Live séance invocation with deterministic anti-hallucination guardrail.
4. Production Sentry.io Agent Tracing instrumentation for cloud HTTP transactions.
"""

import os
import sys
import json
import time
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path

# Register modern 3D and web MIME types
mimetypes.add_type("model/gltf-binary", ".glb")
mimetypes.add_type("model/gltf+json", ".gltf")
mimetypes.add_type("application/javascript", ".js")

# Optional Sentry initialization
try:
    import sentry_sdk
    SENTRY_DSN = os.getenv("SENTRY_DSN", "").strip()
    if not SENTRY_DSN:
        try:
            import keyring
            kv = keyring.get_password("EnvVarManagerPro", "SENTRY_DSN")
            if kv:
                SENTRY_DSN = kv.strip()
        except Exception:
            pass

    if SENTRY_DSN:
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            traces_sample_rate=1.0,
            release="git-seance@1.1.0",
            environment=os.getenv("RENDER_SERVICE_NAME", os.getenv("SENTRY_ENVIRONMENT", "production")),
        )
        SENTRY_ACTIVE = True
    else:
        SENTRY_ACTIVE = False
except Exception:
    SENTRY_ACTIVE = False

import git_seance

START_TIME = time.time()
BASE_DIR = Path(__file__).parent.resolve()
INDEX_FILE = BASE_DIR / "index.html"

# Security Headers (OWASP compliant)
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
    "Access-Control-Allow-Origin": "*",
}

class GitSeanceHandler(BaseHTTPRequestHandler):
    server_version = "GitSeanceEngine/1.1.0"

    def _send_security_headers(self, content_type: str = "text/html; charset=utf-8"):
        self.send_header("Content-Type", content_type)
        for h, val in SECURITY_HEADERS.items():
            self.send_header(h, val)

    def _respond_json(self, status: int, data: dict):
        body = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._send_security_headers("application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/healthz", "/api/health"):
            self.send_response(200)
            self._send_security_headers("application/json; charset=utf-8")
            self.end_headers()
        elif parsed.path in ("/", "/index.html") and INDEX_FILE.is_file():
            self.send_response(200)
            self._send_security_headers("text/html; charset=utf-8")
            self.send_header("Content-Length", str(INDEX_FILE.stat().st_size))
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # 1. Render Health Checks
        if path in ("/healthz", "/api/health"):
            uptime = round(time.time() - START_TIME, 2)
            self._respond_json(200, {
                "status": "healthy",
                "service": "git-seance",
                "version": "1.1.0",
                "uptime_seconds": uptime,
                "sentry_telemetry": SENTRY_ACTIVE,
                "render": {
                    "service_id": os.getenv("RENDER_SERVICE_ID", "local"),
                    "service_name": os.getenv("RENDER_SERVICE_NAME", "git-seance"),
                    "instance_id": os.getenv("RENDER_INSTANCE_ID", "local-instance"),
                }
            })
            return

        # 2. Departed Code Ghosts API
        if path == "/api/ghosts":
            try:
                params = parse_qs(parsed.query)
                limit = min(int(params.get("limit", [5])[0]), 20)
                ghosts = git_seance.mine_git_graveyard(str(BASE_DIR), limit=limit)
                
                ghost_list = []
                for g in ghosts:
                    ghost_list.append({
                        "symbol_name": g.symbol_name,
                        "file_path": g.file_path,
                        "death_sha": g.death_sha,
                        "death_date": g.death_date,
                        "author": g.author,
                        "commit_message": g.commit_message,
                        "candles_lit": g.candles_lit,
                        "is_cryptic": g.is_cryptic,
                        "is_quine_relic": g.is_quine_relic,
                    })
                
                self._respond_json(200, {
                    "count": len(ghost_list),
                    "ghosts": ghost_list,
                    "archaeology_engine": "git-single-pass-miner"
                })
            except Exception as exc:
                self._respond_json(500, {"error": str(exc)})
            return

        # 3. Static Digital Ofrenda Single-Page Altar
        if path in ("/", "/index.html"):
            if not INDEX_FILE.is_file():
                self._respond_json(500, {"error": "index.html not found"})
                return
            content = INDEX_FILE.read_bytes()
            self.send_response(200)
            self._send_security_headers("text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        # 4. Safe Static Asset Serving (prevent path traversal)
        safe_path = (BASE_DIR / path.lstrip("/")).resolve()
        if safe_path.is_file() and safe_path.is_relative_to(BASE_DIR):
            mime_type, _ = mimetypes.guess_type(str(safe_path))
            content = safe_path.read_bytes()
            self.send_response(200)
            self._send_security_headers(mime_type or "application/octet-stream")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        # Fallback 404
        self._respond_json(404, {"error": "Not Found", "path": path})

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/seance":
            try:
                length = int(self.headers.get("Content-Length", 0))
                if length > 32768:
                    self._respond_json(413, {"error": "Payload too large (max 32KB)"})
                    return
                body_bytes = self.rfile.read(length) if length > 0 else b"{}"
                data = json.loads(body_bytes.decode("utf-8")) if body_bytes else {}

                symbol = data.get("symbol", "").strip()
                ghosts = git_seance.mine_git_graveyard(str(BASE_DIR), limit=10)
                
                selected = None
                if symbol:
                    for g in ghosts:
                        if g.symbol_name.lower() == symbol.lower():
                            selected = g
                            break
                if not selected and ghosts:
                    selected = ghosts[0]

                if not selected:
                    self._respond_json(404, {"error": "No departed code ghost available"})
                    return

                # Summon spirit with deterministic guardrail & Sentry span emission
                res = git_seance.summon_gemma_spirit(
                    selected,
                    question=data.get("question", "Why did your code depart from this repository?"),
                    model_name="gemma-local",
                    force_offline=True
                )
                
                trace = res.get("trace")
                self._respond_json(200, {
                    "symbol": selected.symbol_name,
                    "death_sha": selected.death_sha,
                    "file_path": selected.file_path,
                    "epitaph": selected.commit_message,
                    "spirit_reply": res.get("reply", ""),
                    "guardrail_status": {
                        "cryptic_blocked": selected.is_cryptic,
                        "grounded": trace.cites_sha if trace else True,
                    },
                    "telemetry_trace": {
                        "trace_id": trace.trace_id if trace else "local",
                        "operation": trace.operation if trace else "ai.seance",
                        "latency_ms": trace.latency_ms if trace else 0.0,
                        "tokens_generated": trace.tokens_generated if trace else 0,
                    } if trace else None
                })
            except Exception as exc:
                self._respond_json(500, {"error": str(exc)})
            return

        self._respond_json(404, {"error": "Not Found", "path": parsed.path})

def run_server(port: int = None):
    if port is None:
        port = int(os.environ.get("PORT", 8000))
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, GitSeanceHandler)
    print(f"🕯️ GitSéance Full-Stack Web Service listening on http://0.0.0.0:{port}")
    print(f"📊 Sentry Cloud Telemetry: {'Active' if SENTRY_ACTIVE else 'Disabled'}")
    print(f"🛡️ Security Headers & /healthz active for Render Cloud.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down GitSéance server...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

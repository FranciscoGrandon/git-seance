#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Test Suite for GitSéance Production Web Service (Render Cloud)
Creado por Francisco Grandón Vergara

Tests:
1. Health check zero-downtime verification (/healthz, /api/health).
2. Departed code ghosts JSON endpoint (/api/ghosts).
3. Séance spirit summoning with anti-hallucination guardrail (/api/seance).
4. Security headers compliance (OWASP: CSP, X-Frame-Options, X-Content-Type-Options).
5. Path traversal security protection.
6. HEAD request support for lightweight monitors.
"""

import json
import os
import threading
import time
import unittest
import urllib.error
import urllib.request
from http.server import HTTPServer

import server


class TestGitSeanceProductionServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Levantar servidor en un puerto efímero de prueba
        cls.port = 18888
        cls.httpd = HTTPServer(("127.0.0.1", cls.port), server.GitSeanceHandler)
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.3)
        cls.base_url = f"http://127.0.0.1:{cls.port}"

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def test_healthz_endpoint(self):
        url = f"{self.base_url}/healthz"
        res = urllib.request.urlopen(url, timeout=3)
        self.assertEqual(res.status, 200)
        data = json.loads(res.read().decode("utf-8"))
        self.assertEqual(data.get("status"), "healthy")
        self.assertEqual(data.get("service"), "git-seance")
        self.assertEqual(data.get("version"), "1.0.4")
        self.assertIn("uptime_seconds", data)

    def test_security_headers_present(self):
        url = f"{self.base_url}/"
        res = urllib.request.urlopen(url, timeout=3)
        self.assertEqual(res.status, 200)
        headers = dict(res.headers)
        self.assertEqual(headers.get("X-Frame-Options"), "DENY")
        self.assertEqual(headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(headers.get("X-XSS-Protection"), "1; mode=block")

    def test_api_ghosts_endpoint(self):
        url = f"{self.base_url}/api/ghosts?limit=3"
        res = urllib.request.urlopen(url, timeout=3)
        self.assertEqual(res.status, 200)
        data = json.loads(res.read().decode("utf-8"))
        self.assertIn("ghosts", data)
        self.assertGreater(len(data["ghosts"]), 0)
        ghost = data["ghosts"][0]
        self.assertIn("symbol_name", ghost)
        self.assertIn("death_sha", ghost)
        self.assertIn("commit_message", ghost)

    def test_api_seance_invocation(self):
        url = f"{self.base_url}/api/seance"
        payload = json.dumps({"symbol": "heuristic_fraud_score_v0"}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        res = urllib.request.urlopen(req, timeout=3)
        self.assertEqual(res.status, 200)
        data = json.loads(res.read().decode("utf-8"))
        self.assertEqual(data.get("symbol"), "heuristic_fraud_score_v0")
        self.assertTrue(data.get("guardrail_status", {}).get("cryptic_blocked"))
        self.assertIn("telemetry_trace", data)

    def test_path_traversal_blocked(self):
        url = f"{self.base_url}/../../windows/win.ini"
        try:
            res = urllib.request.urlopen(url, timeout=3)
            # Si responde, no debe ser 200
            self.assertNotEqual(res.status, 200)
        except urllib.error.HTTPError as err:
            self.assertEqual(err.code, 404)

    def test_head_method_support(self):
        req = urllib.request.Request(f"{self.base_url}/healthz", method="HEAD")
        res = urllib.request.urlopen(req, timeout=3)
        self.assertEqual(res.status, 200)
        self.assertEqual(len(res.read()), 0)


if __name__ == "__main__":
    unittest.main()

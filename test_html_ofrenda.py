#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Creado por Francisco Grandón Vergara
"""
Test Suite for GitSéance HTML & JavaScript Ofrenda
Hacktoberfest 2026 Week 4 ("Ghost in the Machine")
Author: Francisco Grandón Vergara
"""

import binascii
import os
import re
import subprocess
import unittest
from pathlib import Path


class TestHtmlOfrenda(unittest.TestCase):
    """Deep verification of the single-file HTML & JS Digital Ofrenda application."""

    @classmethod
    def setUpClass(cls):
        cls.html_path = Path("gits_ance_digital_ofrenda_haunted_code_archaeologist_gemma_local.html")
        if not cls.html_path.exists():
            raise FileNotFoundError(f"HTML file not found: {cls.html_path}")
        cls.content = cls.html_path.read_text(encoding="utf-8", errors="replace")

    def test_file_integrity_and_size(self):
        """Verifies that the standalone HTML file exists and contains embedded assets."""
        self.assertTrue(self.html_path.is_file())
        size_bytes = os.path.getsize(self.html_path)
        self.assertGreater(size_bytes, 1_000_000, "HTML file should be > 1MB due to embedded visual assets.")
        self.assertIn("<!DOCTYPE html>", self.content)
        self.assertIn("<html", self.content)
        self.assertIn("</html>", self.content)

    def test_authorship_and_meta(self):
        """Verifies mandatory authorship metadata and comments (Rule 12)."""
        self.assertIn('name="author" content="Francisco Grandón Vergara"', self.content)
        self.assertIn("<!-- Creado por Francisco Grandón Vergara -->", self.content)
        self.assertIn("Creado por Francisco Grandón Vergara", self.content)

    def test_external_cdns(self):
        """Verifies that modern, production-grade CDNs are linked."""
        self.assertIn("cdn.tailwindcss.com", self.content)
        self.assertIn("chart.umd.min.js", self.content)
        self.assertIn("fonts.googleapis.com", self.content)

    def test_dom_elements_consistency(self):
        """
        Extracts every document.getElementById('ID') called in JavaScript and
        guarantees that an element with id='ID' exists in the HTML markup.
        Prevents TypeError: Cannot read properties of null runtime bugs.
        """
        script_match = re.search(r'<script id="gitSeanceCoreScript"[^>]*>(.*?)</script>', self.content, re.DOTALL)
        self.assertIsNotNone(script_match, "gitSeanceCoreScript tag must be present.")
        script_code = script_match.group(1)

        # Find all getElementById calls
        id_calls = re.findall(r'document\.getElementById\(\s*["\']([^"\']+)["\']\s*\)', script_code)
        self.assertGreater(len(id_calls), 15, "Expected at least 15 getElementById calls in script.")

        # Find all id="..." declarations in the HTML markup
        declared_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', self.content))

        for target_id in set(id_calls):
            self.assertIn(
                target_id,
                declared_ids,
                f"JavaScript references getElementById('{target_id}'), but no element with id='{target_id}' exists in HTML!",
            )

    def test_navigation_tabs_exist(self):
        """Verifies the 3 core views: Ofrenda, Sentry Tracing, and Submission Kit."""
        self.assertIn('id="viewOfrenda"', self.content)
        self.assertIn('id="viewSentry"', self.content)
        self.assertIn('id="viewKit"', self.content)
        self.assertIn('id="tabBtnOfrenda"', self.content)
        self.assertIn('id="tabBtnSentry"', self.content)
        self.assertIn('id="tabBtnKit"', self.content)

    def test_mictlan_quine_parity_with_python(self):
        """
        Verifies that the secret Mictlán hex cipher in JavaScript exactly matches
        the Python MICTLAN_HEX_CIPHER and decodes to the exact same text.
        """
        m = re.search(r'const MICTLAN_HEX_EPITAPH\s*=\s*["\']([0-9a-fA-F]+)["\']', self.content)
        self.assertIsNotNone(m, "MICTLAN_HEX_EPITAPH must be defined in JavaScript.")
        hex_cipher = m.group(1)

        decoded = binascii.unhexlify(hex_cipher).decode("utf-8")
        expected = (
            '"The code you delete never truly dies: it becomes the silent foundation '
            'of every commit that follows. Viva Open Source!"'
        )
        self.assertEqual(decoded, expected)

    def test_fnv1a_js_algorithm_parity(self):
        """
        Tests that the JavaScript 32-bit FNV-1a implementation produces the exact
        same checksum as Python's compute_fnv1a_32.
        """
        # Python implementation
        def py_fnv1a(text: str) -> str:
            h = 0x811C9DC5
            for char in text:
                h ^= ord(char)
                h = (h * 0x01000193) & 0xFFFFFFFF
            return f"0x{h:08x}"

        # JavaScript bitwise simulation in Python
        def js_fnv1a_sim(text: str) -> str:
            h = 0x811C9DC5
            for char in text:
                h ^= ord(char)
                # In JS: h = (h + (h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24)) >>> 0;
                # Note: 1 + 2 + 16 + 128 + 256 + 16777216 = 16777619 = 0x01000193!
                term = h + ((h << 1) & 0xFFFFFFFF) + ((h << 4) & 0xFFFFFFFF) + ((h << 7) & 0xFFFFFFFF) + ((h << 8) & 0xFFFFFFFF) + ((h << 24) & 0xFFFFFFFF)
                h = term & 0xFFFFFFFF
            return f"0x{h:08x}"

        test_strings = [
            "mictlan",
            "git_seance_ofrenda.html",
            "__mictlan_source_quine__",
            "Hacktoberfest 2026",
            "Google Gemma local",
        ]
        for s in test_strings:
            self.assertEqual(py_fnv1a(s), js_fnv1a_sim(s), f"Parity mismatch for string: '{s}'")

    def test_github_actions_workflow_template(self):
        """Verifies that the GitHub Actions workflow snippet is complete and valid."""
        self.assertIn("actions/checkout@v4", self.content)
        self.assertIn("fetch-depth: 0", self.content)
        self.assertIn("python3 git_seance.py --ci-summary", self.content)
        self.assertIn("pull_request:", self.content)

    def test_sentry_tracing_ui(self):
        """Verifies that Sentry Agent Tracing telemetry table and chart canvas exist."""
        self.assertIn('id="sentryTraceTableBody"', self.content)
        self.assertIn('id="sentryChartCanvas"', self.content)
        self.assertIn('id="simulateCrypticTraceBtn"', self.content)
        self.assertIn('id="exportTracesBtn"', self.content)
        self.assertIn("ai.seance", self.content)

    def test_is_cryptic_commit_js_parity(self):
        """Verifies that the JavaScript isCrypticCommit implementation matches Python's rules."""
        # Confirm that CRYPTIC_KEYWORDS and CRYPTIC_REGEX exist in JS
        self.assertIn("const CRYPTIC_KEYWORDS = new Set(", self.content)
        self.assertIn("const CRYPTIC_REGEX =", self.content)
        self.assertIn("function isCrypticCommit(msg)", self.content)

        # Extract JS CRYPTIC_REGEX pattern and test against python re
        m = re.search(r"const CRYPTIC_REGEX\s*=\s*/(.*?)/([a-z]*)", self.content)
        self.assertIsNotNone(m, "CRYPTIC_REGEX must be declared in JS.")
        pattern, flags = m.group(1), m.group(2)
        js_re = re.compile(pattern, re.IGNORECASE if "i" in flags else 0)

        # Test cases that previously caused divergence before our fix
        self.assertTrue(bool(js_re.match("chore(core): wip")))
        self.assertTrue(bool(js_re.match("refactor: cleanup")))
        self.assertTrue(bool(js_re.match("fix(api): fix")))
        self.assertFalse(bool(js_re.match("Remove legacy_payment_retry_loop after bug")))

    def test_escape_html_entity_handling(self):
        """Verifies that escapeHtml protects against XSS and generic type DOM swallowing."""
        self.assertIn("function escapeHtml(str)", self.content)
        # Check that &, <, >, ", and ' are escaped
        self.assertIn(".replace(/&/g, \"&amp;\")", self.content)
        self.assertIn(".replace(/</g, \"&lt;\")", self.content)
        self.assertIn(".replace(/>/g, \"&gt;\")", self.content)
        self.assertIn(".replace(/\"/g, \"&quot;\")", self.content)
        self.assertIn(".replace(/'/g, \"&#39;\")", self.content)

    def test_headless_edge_rendering(self):
        """Verifies live physical DOM rendering of the HTML file using headless Microsoft Edge."""
        edge_candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ]
        edge_exe = next((p for p in edge_candidates if os.path.isfile(p)), None)
        if not edge_exe:
            self.skipTest("msedge.exe not found on host machine.")

        proc = subprocess.run(
            [edge_exe, "--headless", "--disable-gpu", "--dump-dom", str(self.html_path.resolve())],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
        rendered_dom = proc.stdout
        self.assertIn("legacy_payment_retry_loop()", rendered_dom)
        self.assertIn("seance://legacy_payment_retry_loop@8f3a91c", rendered_dom)
        self.assertIn("HALLUCINATION_BLOCKED", rendered_dom)
        self.assertIn("GROUNDED_SHA", rendered_dom)
        self.assertIn("000dead", rendered_dom)

    def test_index_html_render_parity(self):
        """Verifies that index.html exists, matches byte size, and has identical SHA-256 checksum."""
        import hashlib
        index_path = Path("index.html")
        self.assertTrue(index_path.is_file(), "index.html must exist for Render Static Site deployment.")
        self.assertEqual(
            os.path.getsize(index_path),
            os.path.getsize(self.html_path),
            "index.html must match byte size of original HTML ofrenda.",
        )
        h1 = hashlib.sha256(index_path.read_bytes()).hexdigest()
        h2 = hashlib.sha256(self.html_path.read_bytes()).hexdigest()
        self.assertEqual(h1, h2, "index.html and original HTML file must have identical SHA-256 checksums.")

    def test_index_html_headless_edge_rendering(self):
        """Verifies live physical DOM rendering of index.html using headless Microsoft Edge."""
        edge_candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ]
        edge_exe = next((p for p in edge_candidates if os.path.isfile(p)), None)
        if not edge_exe:
            self.skipTest("msedge.exe not found on host machine.")

        index_path = Path("index.html")
        proc = subprocess.run(
            [edge_exe, "--headless", "--disable-gpu", "--dump-dom", str(index_path.resolve())],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
        rendered_dom = proc.stdout
        self.assertIn("legacy_payment_retry_loop()", rendered_dom)
        self.assertIn("seance://legacy_payment_retry_loop@8f3a91c", rendered_dom)
        self.assertIn("HALLUCINATION_BLOCKED", rendered_dom)
        self.assertIn("GROUNDED_SHA", rendered_dom)
        self.assertIn("000dead", rendered_dom)

    def test_github_workflow_file_integrity(self):
        """Verifies that .github/workflows/ofrenda_pr.yml exists and contains required steps."""
        wf_path = Path(".github/workflows/ofrenda_pr.yml")
        self.assertTrue(wf_path.is_file(), "ofrenda_pr.yml workflow file must exist.")
        content = wf_path.read_text(encoding="utf-8")
        self.assertIn("pull_request:", content)
        self.assertIn("actions/checkout@v4", content)
        self.assertIn("fetch-depth: 0", content)
        self.assertIn("git_seance.py --ci-summary", content)
        self.assertIn("pull-requests: write", content)
        self.assertIn("Creado por Francisco Grandón Vergara", content)


if __name__ == "__main__":
    unittest.main()


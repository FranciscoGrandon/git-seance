#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Creado por Francisco Grandón Vergara
"""
Test Suite for GitSéance (git_seance.py)
Hacktoberfest 2026 Week 4 ("Ghost in the Machine")
Author: Francisco Grandón Vergara
"""

import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict
from unittest.mock import patch

import git_seance


class TestGitSeanceCore(unittest.TestCase):
    """Deep verification of pure functions, data structures, and edge cases in git_seance.py."""

    def test_fnv1a_hash_vectors(self):
        """Verifies 32-bit FNV-1a checksum calculation against known test vectors."""
        # Test empty input: offset basis 0x811C9DC5
        self.assertEqual(git_seance.compute_fnv1a_32(b""), "0x811c9dc5")
        # Test ASCII input determinism
        h1 = git_seance.compute_fnv1a_32(b"mictlan")
        h2 = git_seance.compute_fnv1a_32(b"mictlan")
        self.assertEqual(h1, h2)
        self.assertTrue(h1.startswith("0x"))
        self.assertEqual(len(h1), 10)  # 0x + 8 hex digits

    def test_inspect_own_source_quine(self):
        """Verifies the self-aware AST Quine introspection over its own source code."""
        meta = git_seance.inspect_own_source_quine()
        self.assertIsInstance(meta, dict)
        required_keys = {
            "byte_length",
            "line_count",
            "fnv1a_checksum",
            "sha256_prefix",
            "ast_fingerprint",
            "ast_node_count",
            "ast_functions",
            "ast_classes",
            "decoded_epitaph",
            "quine_preview",
        }
        for k in required_keys:
            self.assertIn(k, meta, f"Missing key in quine metadata: {k}")

        self.assertGreater(meta["byte_length"], 1000)
        self.assertGreater(meta["line_count"], 500)
        self.assertGreater(meta["ast_node_count"], 1000)
        self.assertIn("inspect_own_source_quine", meta["ast_functions"])
        self.assertIn("DepartedCodeGhost", meta["ast_classes"])
        self.assertEqual(
            meta["decoded_epitaph"],
            "\"The code you delete never truly dies: it becomes the silent foundation of every commit that follows. Viva Open Source!\"",
        )
        self.assertIn("MICTLAN_HEX_CIPHER", meta["quine_preview"])

    def test_build_quine_ghost(self):
        """Verifies construction of the __mictlan_source_quine__ ghost."""
        ghost = git_seance.build_quine_ghost()
        self.assertEqual(ghost.symbol_name, "__mictlan_source_quine__")
        self.assertEqual(ghost.death_sha, "000dead")
        self.assertTrue(ghost.is_quine_relic)
        self.assertEqual(ghost.candles_lit, 99)
        self.assertFalse(ghost.is_cryptic)

    def test_cryptic_commit_detection(self):
        """Verifies boundary cases for cryptic commit epitaph guardrails."""
        # 1. Obvious cryptic messages
        for msg in ["wip", "wip cleanup", "fix", "fixes", "clean up", "refactor", "update", "temp", "lint"]:
            ghost = git_seance.DepartedCodeGhost(
                symbol_name="test_func",
                file_path="src/test.py",
                death_sha="a1b2c3d",
                death_date="2026-10-28",
                author="Test Author",
                commit_message=msg,
                removed_lines="- def test_func(): pass",
            )
            self.assertTrue(ghost.is_cryptic, f"Expected '{msg}' to be detected as cryptic.")

        # 2. Conventional commit variations on cryptic tokens
        for msg in ["chore: wip", "fix(core): fix", "style: lint", "refactor: cleanup", "chore(api): update"]:
            ghost = git_seance.DepartedCodeGhost(
                symbol_name="test_func",
                file_path="src/test.py",
                death_sha="a1b2c3d",
                death_date="2026-10-28",
                author="Test Author",
                commit_message=msg,
                removed_lines="- def test_func(): pass",
            )
            self.assertTrue(ghost.is_cryptic, f"Expected conventional commit '{msg}' to be detected as cryptic.")

        # 3. Short messages (<12 chars)
        short_ghost = git_seance.DepartedCodeGhost(
            symbol_name="test_func",
            file_path="src/test.py",
            death_sha="a1b2c3d",
            death_date="2026-10-28",
            author="Test Author",
            commit_message="done now",
            removed_lines="- def test_func(): pass",
        )
        self.assertTrue(short_ghost.is_cryptic, "Short message should be cryptic.")

        # 4. Descriptive, meaningful commit messages (MUST NOT be cryptic)
        meaningful_ghost = git_seance.DepartedCodeGhost(
            symbol_name="legacy_payment_retry_loop",
            file_path="src/billing/retry.py",
            death_sha="8f3a91c",
            death_date="2026-10-14",
            author="Elena Vance",
            commit_message="Remove legacy_payment_retry_loop after double-charging bug on webhook timeout",
            removed_lines="- def legacy_payment_retry_loop(): pass",
        )
        self.assertFalse(meaningful_ghost.is_cryptic, "Detailed commit message must NOT be cryptic.")

        # 5. Quine relic is never cryptic
        quine_ghost = git_seance.DepartedCodeGhost(
            symbol_name="__mictlan_source_quine__",
            file_path="git_seance.py",
            death_sha="000dead",
            death_date="2026-10-31",
            author="Quine",
            commit_message="wip",
            removed_lines="",
            is_quine_relic=True,
        )
        self.assertFalse(quine_ghost.is_cryptic, "Quine relic must never be marked cryptic.")

    def test_extract_symbol_name_polyglot(self):
        """Tests extraction of function, class, and method symbols across languages."""
        cases = [
            ("def calculate_total(a, b):", "calculate_total"),
            ("async def fetch_user_data(uid):", "fetch_user_data"),
            ("class DatabaseConnectionPool:", "DatabaseConnectionPool"),
            ("function renderAltarView(data) {", "renderAltarView"),
            ("export const authenticateUser = async () => {", "authenticateUser"),
            ("let processOrder = (order) => {", "processOrder"),
            ("pub fn verify_signature(bytes: &[u8]) -> bool {", "verify_signature"),
            ("func HandleWebhook(w http.ResponseWriter, r *http.Request) {", "HandleWebhook"),
            ("x = 10", None),
            ("return True", None),
            ("# Just a comment", None),
            ("// Another comment", None),
        ]
        for line, expected in cases:
            res = git_seance._extract_symbol_name(line)
            self.assertEqual(res, expected, f"Failed on line: {line}")

    def test_extract_python_ast_symbols(self):
        """Tests AST symbol extraction from clean and partial Python diffs."""
        # Clean diff hunk
        diff_lines = [
            "- def old_helper():",
            "-     return 42",
            "- class OldClass:",
            "-     pass",
        ]
        syms = git_seance._extract_python_ast_symbols(diff_lines)
        self.assertIn("old_helper", syms)
        self.assertIn("OldClass", syms)

        # Broken partial diff syntax (fallback should return empty set without throwing)
        broken_lines = ["- def incomplete_func(", "-    some_broken_syntax"]
        broken_syms = git_seance._extract_python_ast_symbols(broken_lines)
        self.assertIsInstance(broken_syms, set)

    def test_verify_response_grounding(self):
        """Verifies deterministic fact-checking logic on LLM and fallback replies."""
        ghost = git_seance.DepartedCodeGhost(
            symbol_name="calculate_fee",
            file_path="src/finance/fee.py",
            death_sha="abc1234",
            death_date="2026-10-20",
            author="Dev",
            commit_message="Refactor fee calculation engine",
            removed_lines="- def calculate_fee(): pass",
        )

        # 1. Perfectly grounded text citing both SHA and file
        good_text = "I am calculate_fee from src/finance/fee.py, removed in commit #abc1234."
        audit = git_seance.verify_response_grounding(good_text, ghost)
        self.assertTrue(audit["cites_sha"])
        self.assertTrue(audit["cites_file"])
        self.assertTrue(audit["passed"])

        # 2. Cites only basename of file
        base_text = "I died in commit #ABC1234 inside fee.py."
        audit_base = git_seance.verify_response_grounding(base_text, ghost)
        self.assertTrue(audit_base["cites_sha"])
        self.assertTrue(audit_base["cites_file"])
        self.assertTrue(audit_base["passed"])

        # 3. Missing SHA
        no_sha_text = "I am from fee.py and I was removed for business reasons."
        audit_no_sha = git_seance.verify_response_grounding(no_sha_text, ghost)
        self.assertFalse(audit_no_sha["cites_sha"])
        self.assertFalse(audit_no_sha["passed"])

        # 4. Missing file
        no_file_text = "I died in commit #abc1234 but nobody knows my origin."
        audit_no_file = git_seance.verify_response_grounding(no_file_text, ghost)
        self.assertFalse(audit_no_file["cites_file"])
        self.assertFalse(audit_no_file["passed"])

    def test_build_deterministic_fallback_reply(self):
        """Verifies deterministic replies across all ghost personas and prompts."""
        # 1. Meaningful ghost standard response
        g1 = git_seance.get_fallback_tombstones()[0]
        rep1 = git_seance.build_deterministic_fallback_reply(g1, "Why did you die?")
        self.assertIn(g1.death_sha, rep1)
        self.assertIn(g1.symbol_name, rep1)
        self.assertIn(g1.author, rep1)
        self.assertIn("Do not resurrect", rep1)

        # 2. Cryptic ghost response activates guardrail
        g2 = git_seance.get_fallback_tombstones()[1]
        self.assertTrue(g2.is_cryptic)
        rep2 = git_seance.build_deterministic_fallback_reply(g2, "Why were you deleted?")
        self.assertIn("Anti-Hallucination Guardrail Active", rep2)
        self.assertIn("refuse to invent a fictional backstory", rep2)
        self.assertIn(g2.death_sha, rep2)

        # 3. Calaverita poem request
        rep3 = git_seance.build_deterministic_fallback_reply(g1, "Sing a calaverita poem for me")
        self.assertIn("Calaverita", rep3)
        self.assertIn(g1.symbol_name, rep3)

        # 4. Quine ghost response
        g_quine = git_seance.build_quine_ghost()
        rep_quine = git_seance.build_deterministic_fallback_reply(g_quine, "Who are you?")
        self.assertIn("__mictlan_source_quine__", rep_quine)
        self.assertIn("000dead", rep_quine)
        self.assertIn("Decoded Hex Relic", rep_quine)

    def test_summon_gemma_spirit_offline_mode(self):
        """Verifies summon_gemma_spirit runs sub-millisecond in offline mode."""
        ghost = git_seance.get_fallback_tombstones()[0]
        res = git_seance.summon_gemma_spirit(ghost, "What is your legacy?", force_offline=True)
        self.assertIn("reply", res)
        self.assertIn("trace", res)
        span = res["trace"]
        self.assertEqual(span.symbol_name, ghost.symbol_name)
        self.assertEqual(span.death_sha, ghost.death_sha)
        self.assertEqual(span.engine_source, "deterministic_offline")
        self.assertTrue(span.cites_sha)
        self.assertTrue(span.cites_file)
        self.assertFalse(span.cryptic_commit_blocked)
        self.assertGreater(span.tokens_generated, 10)
        self.assertLess(span.latency_ms, 50.0)

    def test_summon_gemma_spirit_cryptic_preflight_shortcircuit(self):
        """Verifies cryptic commits are intercepted before invoking LLM or network."""
        cryptic_ghost = git_seance.get_fallback_tombstones()[1]
        self.assertTrue(cryptic_ghost.is_cryptic)
        # Even with force_offline=False, cryptic commits should be short-circuited
        res = git_seance.summon_gemma_spirit(cryptic_ghost, "Explain your death", force_offline=False)
        span = res["trace"]
        self.assertEqual(span.engine_source, "cryptic_guardrail_preflight")
        self.assertTrue(span.cryptic_commit_blocked)
        self.assertTrue(span.cites_sha)

    def test_summon_gemma_spirit_quine_introspection(self):
        """Verifies quine ghost triggers the ast_quine_introspection engine."""
        quine_ghost = git_seance.build_quine_ghost()
        res = git_seance.summon_gemma_spirit(quine_ghost, "Read your source code", force_offline=False)
        span = res["trace"]
        self.assertEqual(span.engine_source, "ast_quine_introspection")
        self.assertTrue(span.ast_quine_verified)
        self.assertEqual(span.operation, "ai.seance.quine")

    def test_ci_markdown_summary_generation(self):
        """Verifies GitHub Actions PR markdown summary generation."""
        ghosts = git_seance.get_fallback_tombstones()
        md = git_seance.generate_ci_markdown_summary(ghosts)
        self.assertIn("<!-- git-seance-ofrenda -->", md)
        self.assertIn("## 🌼🕯️ Digital Ofrenda Memorial — Departed Code Report", md)
        self.assertIn("Tombstone SHA", md)
        self.assertIn("📜 Documented Git Commit", md)
        self.assertIn("<details><summary>📜 Inspect Departed Diff Tombstones</summary>", md)
        self.assertIn("```diff", md)
        for g in ghosts:
            self.assertIn(g.symbol_name, md)
            self.assertIn(g.death_sha, md)

    def test_extract_python_ast_symbols_mixed_indentation(self):
        """Tests that chunk-based AST parsing extracts symbols from mixed-indentation diff hunks."""
        diff_lines = [
            "-    def indented_method(self):",
            "-        return 'nested'",
            "-def top_level_func():",
            "-    return 'root'",
        ]
        syms = git_seance._extract_python_ast_symbols(diff_lines)
        self.assertIn("indented_method", syms)
        self.assertIn("top_level_func", syms)

    def test_verify_response_grounding_edge_cases(self):
        """Verifies boundary cases in grounding fact-checker (empty SHA/file, 40-char SHA prefix)."""
        # Empty SHA must not evaluate to True
        g_empty_sha = git_seance.DepartedCodeGhost(
            symbol_name="f", file_path="foo.py", death_sha="",
            death_date="2026-10-28", author="A", commit_message="msg", removed_lines="- pass"
        )
        audit_empty_sha = git_seance.verify_response_grounding("any text inside foo.py", g_empty_sha)
        self.assertFalse(audit_empty_sha["cites_sha"])

        # Empty file must not evaluate to True
        g_empty_file = git_seance.DepartedCodeGhost(
            symbol_name="f", file_path="", death_sha="abc1234",
            death_date="2026-10-28", author="A", commit_message="msg", removed_lines="- pass"
        )
        audit_empty_file = git_seance.verify_response_grounding("cited in commit abc1234", g_empty_file)
        self.assertFalse(audit_empty_file["cites_file"])

        # 40-char SHA cited with 7-char short prefix
        g_full_sha = git_seance.DepartedCodeGhost(
            symbol_name="f", file_path="foo.py", death_sha="8f3a91c78491abcdef1234567890abcdef123456",
            death_date="2026-10-28", author="A", commit_message="msg", removed_lines="- pass"
        )
        audit_prefix = git_seance.verify_response_grounding("I died in commit #8f3a91c inside foo.py", g_full_sha)
        self.assertTrue(audit_prefix["cites_sha"])
        self.assertTrue(audit_prefix["passed"])

    def test_mine_git_graveyard_boundary_and_quoted_paths(self):
        """Tests non-positive limit handling and quoted file paths in unified diffs."""
        # Non-positive limits must enforce limit >= 1 without IndexError
        ghosts_zero = git_seance.mine_git_graveyard(".", limit=0)
        self.assertGreaterEqual(len(ghosts_zero), 1)

        ghosts_neg = git_seance.mine_git_graveyard(".", limit=-3)
        self.assertGreaterEqual(len(ghosts_neg), 1)

        # Mock git log stream containing a quoted path with spaces
        mock_stream = (
            "__GIT_SEANCE_COMMIT__1a2b3c4|2026-10-20|Tester|Remove old helper\n"
            "--- \"a/src/path with spaces/helper.py\"\n"
            "+++ /dev/null\n"
            "-def quoted_path_helper():\n"
            "-    return True\n"
        )
        with patch("git_seance.run_git_command", return_value=mock_stream):
            mined = git_seance.mine_git_graveyard(".", limit=2)
            self.assertEqual(len(mined), 1)
            self.assertEqual(mined[0].symbol_name, "quoted_path_helper")
            self.assertEqual(mined[0].file_path, "src/path with spaces/helper.py")
            self.assertEqual(mined[0].death_sha, "1a2b3c4")

    def test_ci_markdown_summary_multiline_and_empty(self):
        """Tests that multi-line commit messages with pipes do not break Markdown table rows."""
        # Multi-line commit message with pipes
        multiline_ghost = git_seance.DepartedCodeGhost(
            symbol_name="complex_table_func",
            file_path="src/calc.py",
            death_sha="fedcba9",
            death_date="2026-10-25",
            author="Author | Reviewer",
            commit_message="Line 1: Refactor calculation | fix edge case\nLine 2: Removed unused parameters",
            removed_lines="- def complex_table_func(): pass",
        )
        md = git_seance.generate_ci_markdown_summary([multiline_ghost])
        for line in md.splitlines():
            if line.startswith("| `complex_table_func"):
                # Table row must not contain raw newlines or unescaped interior pipes
                self.assertNotIn("\n", line)
                self.assertIn("Author \\| Reviewer", line)
                self.assertIn("Line 1: Refactor calculation \\| fix edge case Line 2: Removed unused parameters", line)

        # Empty ghosts list should render an empty indicator row without error
        md_empty = git_seance.generate_ci_markdown_summary([])
        self.assertIn("*(none)*", md_empty)

    def test_summon_gemma_spirit_live_http_mock(self):
        """Verifies summon_gemma_spirit communicating with a live local HTTP Ollama endpoint."""
        server_responses = []

        class MockOllamaHandler(BaseHTTPRequestHandler):
            def do_POST(self):
                content_len = int(self.headers.get("Content-Length", 0))
                req_body = self.rfile.read(content_len)
                parsed = json.loads(req_body.decode("utf-8"))

                resp_data, status_code = server_responses.pop(0)
                self.send_response(status_code)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(resp_data).encode("utf-8"))

            def log_message(self, format, *args):
                pass  # Silence HTTP server logs during test run

        server = HTTPServer(("127.0.0.1", 0), MockOllamaHandler)
        port = server.server_port
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()

        test_ghost = git_seance.DepartedCodeGhost(
            symbol_name="payment_sync_worker",
            file_path="src/billing/sync.py",
            death_sha="abc7890",
            death_date="2026-10-26",
            author="Dev",
            commit_message="Retire sync worker after migrating to async event bus",
            removed_lines="- def payment_sync_worker(): pass",
        )

        try:
            mock_url = f"http://127.0.0.1:{port}/api/generate"
            with patch.object(git_seance, "OLLAMA_URL", mock_url):
                # 1. Grounded response from Ollama
                server_responses.append((
                    {
                        "response": "I am payment_sync_worker from src/billing/sync.py, removed in commit #abc7890.",
                        "eval_count": 84,
                    },
                    200,
                ))
                res1 = git_seance.summon_gemma_spirit(test_ghost, "Who were you?")
                self.assertIn("ollama:", res1["trace"].engine_source)
                self.assertTrue(res1["trace"].cites_sha)
                self.assertTrue(res1["trace"].cites_file)
                self.assertEqual(res1["trace"].tokens_generated, 84)

                # 2. Hallucinated response (missing SHA) triggers grounding audit fallback
                server_responses.append((
                    {
                        "response": "I was deleted because of business reasons without citing my commit.",
                        "eval_count": 42,
                    },
                    200,
                ))
                res2 = git_seance.summon_gemma_spirit(test_ghost, "Why did you die?")
                self.assertEqual(res2["trace"].engine_source, "grounding_audit_fallback")
                self.assertTrue(res2["trace"].cites_sha)

                # 3. HTTP 500 error from Ollama falls back gracefully to deterministic fallback
                server_responses.append((
                    {"error": "Internal GPU error"},
                    500,
                ))
                res3 = git_seance.summon_gemma_spirit(test_ghost, "Tell me your story")
                self.assertEqual(res3["trace"].engine_source, "deterministic_fallback")
                self.assertTrue(res3["trace"].cites_sha)
        finally:
            server.shutdown()
            server.server_close()


class TestGitSeanceCLI(unittest.TestCase):
    """Deep verification of CLI flags, argument parsing, and process exits."""

    def _run_cli(self, args: list) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, "git_seance.py"] + args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    def test_cli_help(self):
        res = self._run_cli(["--help"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("GitSéance", res.stdout)
        self.assertIn("--offline", res.stdout)
        self.assertIn("--mictlan", res.stdout)
        self.assertIn("--ci-summary", res.stdout)
        self.assertNotIn("SyntaxWarning", res.stderr)

    def test_cli_offline_run(self):
        res = self._run_cli(["--offline", "--limit", "2"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("GIT SÉANCE — DIGITAL OFRENDA FOR DEPARTED CODE", res.stdout)
        self.assertIn("legacy_payment_retry_loop", res.stdout)
        self.assertNotIn("SyntaxWarning", res.stderr)

    def test_cli_mictlan_quine(self):
        res = self._run_cli(["--mictlan", "--offline"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("SECRET AST QUINE RELIC AWAKENED", res.stdout)
        self.assertIn("__mictlan_source_quine__", res.stdout)
        self.assertIn("000dead", res.stdout)
        self.assertNotIn("SyntaxWarning", res.stderr)

    def test_cli_ci_summary(self):
        # En un repo sin borrados detectables, no debe inventar lápidas de fallback
        res = self._run_cli(["--ci-summary"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("Digital Ofrenda Memorial", res.stdout)
        self.assertIn("No departed functions found in recent commits", res.stdout)
        self.assertNotIn("SyntaxWarning", res.stderr)

    def test_cli_symbol_selection(self):
        # 1. Select by index
        res1 = self._run_cli(["--symbol", "1", "--offline"])
        self.assertEqual(res1.returncode, 0)
        self.assertIn("Summoning `legacy_payment_retry_loop()`", res1.stdout)

        # 2. Select by name substring
        res2 = self._run_cli(["--symbol", "heuristic", "--offline"])
        self.assertEqual(res2.returncode, 0)
        self.assertIn("Summoning `heuristic_fraud_score_v0()`", res2.stdout)

    def test_cli_export_traces_json(self):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp_path = tmp.name

        try:
            res = self._run_cli(["--offline", "--export-traces", tmp_path])
            self.assertEqual(res.returncode, 0)
            self.assertIn("Exported Sentry Agent Tracing JSON", res.stdout)

            with open(tmp_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.assertIsInstance(data, list)
            self.assertGreater(len(data), 0)
            first_trace = data[0]
            self.assertIn("trace_id", first_trace)
            self.assertIn("operation", first_trace)
            self.assertIn("symbol_name", first_trace)
            self.assertIn("latency_ms", first_trace)
            self.assertIn("tokens_generated", first_trace)
            self.assertIn("cites_sha", first_trace)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_cli_edge_cases(self):
        # Limit 0 or negative should default gracefully to at least 1
        res_neg = self._run_cli(["--offline", "--limit", "-3"])
        self.assertEqual(res_neg.returncode, 0)
        self.assertIn("legacy_payment_retry_loop", res_neg.stdout)

        # Non-existent repository path should fall back to realistic tombstones
        res_bad_repo = self._run_cli(["--offline", "--repo", "non_existent_folder_xyz"])
        self.assertEqual(res_bad_repo.returncode, 0)
        self.assertIn("legacy_payment_retry_loop", res_bad_repo.stdout)

    def test_mine_git_graveyard_no_fallback(self):
        """Tests that allow_fallback=False returns empty list when no git history exists."""
        ghosts = git_seance.mine_git_graveyard(
            repo_path="non_existent_folder_xyz",
            limit=3,
            revision_range="origin/main..HEAD",
            allow_fallback=False,
        )
        self.assertEqual(ghosts, [])

    def test_cli_no_fallback_and_range(self):
        """Tests CLI with --no-fallback and --range emitting empty memorial status."""
        res = self._run_cli(["--ci-summary", "--no-fallback", "--range", "origin/main..HEAD"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("No departed functions found in recent commits", res.stdout)
        self.assertNotIn("legacy_payment_retry_loop", res.stdout)


if __name__ == "__main__":
    unittest.main()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Creado por Francisco Grandón Vergara
r"""
===============================================================================
💀 GitSéance (git_seance.py) — Offline Digital Ofrenda & Git Archaeologist 💀
===============================================================================
Hacktoberfest 2026 Open-Source AI Challenge: Week 4 ("Ghost in the Machine")
Creado por Francisco Grandón Vergara

                 .-"      "-.
                /   🌼  🌼   \
               |   #000dead   |
               |,  .-.  .-.  ,|
               | )(_o/  \o_)( |
               |/     /\     \|
               (_     ^^     _)
                \__|IIIIII|__/
                 | \IIIIII/ |
                 \          /
                  `--------`

Architecture & Necromancy Notes:
  1. Single-Pass Git Graveyard Miner: Excavates `git log -p` in one go,
     separating genuine deletions from functions that merely got re-indented.
  2. Local Google Gemma (`gemma2:2b`) Séance Engine via Ollama: $0.00 cloud bill,
     because paying per-token to interrogate dead code adds insult to tech debt.
  3. Pre-Flight Cryptic-Commit Guardrail: Refuses to let an LLM hallucinate
     a noble tragic backstory for a commit message that literally says "wip".
  4. Sentry Agent Tracing (`ai.seance` spans): Because if a ghost materializes
     in stdout and nobody logs the p95 latency, did it even haunt the repo?
  5. GitHub Actions PR Memorial Generator (`--ci-summary`) with diff tombstones.
  6. Self-Aware Python AST Quine (`--mictlan` / Spirit #000dead): A script that
     parses its own syntax tree at runtime to prove it has a soul.
===============================================================================
"""

from __future__ import annotations

import argparse
import ast
import binascii
import hashlib
import inspect
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

# Optional Sentry SDK integration. If sentry-sdk isn't installed, we degrade
# gracefully instead of turning the séance itself into an unhandled exception.
try:
    import sentry_sdk  # type: ignore

    SENTRY_DSN = os.getenv("SENTRY_DSN", "").strip()
    if SENTRY_DSN:
        sentry_sdk.init(dsn=SENTRY_DSN, traces_sample_rate=1.0)
        SENTRY_ACTIVE = True
    else:
        SENTRY_ACTIVE = False
except ImportError:
    SENTRY_ACTIVE = False

# =============================================================================
# 💀 HIDDEN SOURCE CODE RELIC (#000dead) — SELF-INSPECTING AST QUINE CIPHER
# =============================================================================
# Stored in hex so casual `grep` searches don't spoil the punchline before the
# AST parser finishes reading its own obituary.
MICTLAN_HEX_CIPHER = (
    "2254686520636f646520796f752064656c657465206e65766572207472756c7920646965"
    "733a206974206265636f6d6573207468652073696c656e7420666f756e646174696f6e20"
    "6f6620657665727920636f6d6d6974207468617420666f6c6c6f77732e2056697661204f"
    "70656e20536f757263652122"
)

ASCII_CALAVERA = r"""
                 .-"      "-.
                /   🌼  🌼   \
               |   #000dead   |
               |,  .-.  .-.  ,|
               | )(_o/  \o_)( |
               |/     /\     \|
               (_     ^^     _)
                \__|IIIIII|__/
                 | \IIIIII/ |
                 \          /
                  `--------`
"""


def _configure_terminal() -> bool:
    """
    Coerces the host terminal into speaking UTF-8 and rendering ANSI escapes.
    Without this, Windows consoles tend to summon Mojibake—a far less festive
    spirit than the ones we actually want on the altar.
    """
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

    # Respect NO_COLOR and non-interactive pipes so CI logs don't look like
    # someone spilled raw VT100 control sequences into the build output.
    if os.getenv("NO_COLOR") or not sys.stdout.isatty():
        return False

    if os.name == "nt":
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
            handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        except Exception:
            pass
    return True


USE_COLOR = _configure_terminal()


class AltarPalette:
    MARIGOLD = "\033[38;5;214m" if USE_COLOR else ""
    GOLD = "\033[38;5;220m" if USE_COLOR else ""
    PURPLE = "\033[38;5;141m" if USE_COLOR else ""
    EMERALD = "\033[38;5;48m" if USE_COLOR else ""
    ROSE = "\033[38;5;204m" if USE_COLOR else ""
    CYAN = "\033[38;5;81m" if USE_COLOR else ""
    DIM = "\033[2m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    RESET = "\033[0m" if USE_COLOR else ""


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.getenv("GEMMA_MODEL", "gemma2:2b")

# The classic Friday 4:59 PM vocabulary. If a commit message consists solely of
# these tokens, the author was either fleeing a production incident or rebasing
# in secret.
CRYPTIC_KEYWORDS: Set[str] = {
    "wip",
    "wip cleanup",
    "fix",
    "fixes",
    "cleanup",
    "clean up",
    "refactor",
    "update",
    "updates",
    "temp",
    "tmp",
    "minor",
    "test",
    "testing",
    "stuff",
    "changes",
    "misc",
    "lint",
    "typo",
    "oops",
    "merge",
    "merges",
    "review",
    "comments",
    "address",
    "feedback",
}

# Wrapping "wip" in Conventional Commits (`chore(core): wip`) doesn't make it
# documentation; it just puts a tuxedo on a shrug.
CRYPTIC_REGEX = re.compile(
    r"^(?:(?:chore|fix|feat|refactor|style|docs|test)(?:\([^)]*\))?:\s*)?"
    r"(?:wip|fix(?:es)?|clean\s*up|update(?:s)?|temp|tmp|minor|stuff|misc|changes|test(?:ing)?|lint|merge.*|address.*review.*|review\s*comments?)\W*$",
    re.IGNORECASE,
)

# Polyglot symbol detector: catches everything from standard Python/Rust/Go
# declarations to JavaScript arrow functions clinging to a `const` for dear life.
SYMBOL_PATTERNS = re.compile(
    r"^\s*(?:export\s+)?(?:default\s+)?(?:pub(?:\([^)]*\))?\s+)?"
    r"(?:async\s+def|def|class|function|func|fn)\s+([a-zA-Z_][a-zA-Z0-9_]*)"
    r"|^\s*(?:export\s+)?(?:const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?:async\s*)?(?:\([^)]*\)|[a-zA-Z_][a-zA-Z0-9_]*)\s*=>"
)


@dataclass
class DepartedCodeGhost:
    symbol_name: str
    file_path: str
    death_sha: str
    death_date: str
    author: str
    commit_message: str
    removed_lines: str
    candles_lit: int = 1
    is_quine_relic: bool = False

    @property
    def is_cryptic(self) -> bool:
        if self.is_quine_relic:
            return False
        clean = self.commit_message.strip().lower()
        # Mensajes de menos de 10 caracteres o tokens de relleno
        if len(clean) < 10 or clean in CRYPTIC_KEYWORDS or bool(CRYPTIC_REGEX.match(clean)):
            return True
        words = [w for w in re.split(r"\W+", clean) if w]
        return len(words) <= 2 and all(w in CRYPTIC_KEYWORDS for w in words)


@dataclass
class SeanceTraceSpan:
    trace_id: str
    operation: str
    symbol_name: str
    death_sha: str
    model: str
    engine_source: str
    latency_ms: float
    tokens_generated: int
    cites_sha: bool
    cites_file: bool
    cryptic_commit_blocked: bool
    ast_quine_verified: bool = False
    timestamp: str = field(
        default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    )


# =============================================================================
# 1. SELF-AWARE PYTHON AST QUINE INTROSPECTION (#000dead)
# =============================================================================
def compute_fnv1a_32(data: bytes) -> str:
    """
    32-bit FNV-1a hash: fast, deterministic, and non-cryptographic—much like
    our collective optimism that deleted helper functions aren't still imported
    somewhere in a forgotten cron job.
    """
    h = 0x811C9DC5
    for byte in data:
        h ^= byte
        h = (h * 0x01000193) & 0xFFFFFFFF
    return f"0x{h:08x}"


def inspect_own_source_quine() -> Dict[str, Any]:
    """
    Reads this script's own running source code and parses its Python AST in
    memory—the software equivalent of reading your own autopsy report while
    checking for PEP 8 compliance.
    """
    try:
        own_source = inspect.getsource(sys.modules[__name__])
    except Exception:
        with open(__file__, "r", encoding="utf-8") as f:
            own_source = f.read()

    raw_bytes = own_source.encode("utf-8")
    lines = own_source.splitlines()
    fnv_hash = compute_fnv1a_32(raw_bytes)
    sha256_short = hashlib.sha256(raw_bytes).hexdigest()[:12]

    tree = ast.parse(own_source)
    functions = [
        n.name
        for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    ast_node_types = [type(n).__name__ for n in ast.walk(tree)]
    ast_merkle_short = hashlib.sha256(":".join(ast_node_types).encode("utf-8")).hexdigest()[:10]
    decoded_epitaph = binascii.unhexlify(MICTLAN_HEX_CIPHER).decode("utf-8")

    # Resolve the exact line boundaries of MICTLAN_HEX_CIPHER from the live AST
    # rather than hardcoding line offsets. Hardcoded slices break the moment
    # someone adds an import at the top, leaving the quine pointing at `import re`
    # like an amateur medium.
    quine_slice: List[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "MICTLAN_HEX_CIPHER":
                    start = max(0, node.lineno - 1)
                    end = getattr(node, "end_lineno", start + 8)
                    quine_slice = [f"- {ln}" for ln in lines[start:end]]
                    break
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "MICTLAN_HEX_CIPHER"
        ):
            start = max(0, node.lineno - 1)
            end = getattr(node, "end_lineno", start + 8)
            quine_slice = [f"- {ln}" for ln in lines[start:end]]
            break

    if not quine_slice:
        quine_slice = [f"- {ln}" for ln in lines[:10]]

    return {
        "byte_length": len(raw_bytes),
        "line_count": len(lines),
        "fnv1a_checksum": fnv_hash,
        "sha256_prefix": sha256_short,
        "ast_fingerprint": ast_merkle_short,
        "ast_node_count": len(ast_node_types),
        "ast_functions": functions,
        "ast_classes": classes,
        "decoded_epitaph": decoded_epitaph,
        "quine_preview": "\n".join(quine_slice),
    }


def build_quine_ghost() -> DepartedCodeGhost:
    meta = inspect_own_source_quine()
    return DepartedCodeGhost(
        symbol_name="__mictlan_source_quine__",
        file_path=os.path.basename(__file__),
        death_sha="000dead",
        death_date="2026-10-31",
        author="Self-Aware Python AST Quine",
        commit_message=(
            f"Live AST introspection over {meta['byte_length']} bytes "
            f"(FNV-1a: {meta['fnv1a_checksum']}, AST-Hash: {meta['ast_fingerprint']}) — "
            f"{meta['decoded_epitaph']}"
        ),
        removed_lines=meta["quine_preview"],
        candles_lit=99,
        is_quine_relic=True,
    )


# =============================================================================
# 2. DETERMINISTIC SINGLE-PASS GIT GRAVEYARD MINER
# =============================================================================
def run_git_command(args: List[str], repo_path: str = ".") -> str:
    try:
        proc = subprocess.run(
            ["git", "-C", repo_path] + args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
        )
        if proc.returncode != 0:
            return ""
        return proc.stdout.strip()
    except Exception:
        return ""


def _extract_symbol_name(code_line: str) -> Optional[str]:
    match = SYMBOL_PATTERNS.match(code_line)
    if not match:
        return None
    return match.group(1) or match.group(2)


def _extract_python_ast_symbols(removed_lines: List[str]) -> Set[str]:
    """
    Feeds removed diff lines into `ast.parse`. Diffs are often partial fragments
    that fail syntax checks, so if the parser complains, we quietly Pocket-Sand
    our way out and fall back to regex results.
    """
    import textwrap

    cleaned = [ln[1:] for ln in removed_lines if ln.startswith("-") and not ln.startswith("---")]
    if not cleaned:
        return set()

    raw_code = "\n".join(cleaned)
    candidates = [raw_code, textwrap.dedent(raw_code)]

    for candidate in candidates:
        try:
            tree = ast.parse(candidate)
            return {
                n.name
                for n in ast.walk(tree)
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            }
        except (SyntaxError, IndentationError):
            continue

    # Fallback to chunk-based parsing for mixed-indentation diff hunks
    found_symbols: Set[str] = set()
    chunk: List[str] = []
    sym_start = re.compile(r"^\s*(?:async\s+def|def|class)\s+")
    for line in cleaned:
        if sym_start.match(line) and chunk:
            c_text = textwrap.dedent("\n".join(chunk))
            try:
                t = ast.parse(c_text)
                found_symbols.update(
                    n.name
                    for n in ast.walk(t)
                    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
                )
            except (SyntaxError, IndentationError):
                pass
            chunk = [line]
        else:
            chunk.append(line)
    if chunk:
        c_text = textwrap.dedent("\n".join(chunk))
        try:
            t = ast.parse(c_text)
            found_symbols.update(
                n.name
                for n in ast.walk(t)
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            )
        except (SyntaxError, IndentationError):
            pass

    return found_symbols


def mine_git_graveyard(
    repo_path: str = ".",
    limit: int = 5,
    revision_range: str = "",
    allow_fallback: bool = True,
) -> List[DepartedCodeGhost]:
    """
    Streams commit metadata and unified-0 patches in a single `git log -p` call.
    Spawning a separate `git show` subprocess per commit is how a harmless CLI
    accidentally benchmarks the OS process scheduler.
    """
    limit = max(1, limit)
    commit_marker = "__GIT_SEANCE_COMMIT__"
    log_fmt = f"{commit_marker}%h|%ad|%an|%s"
    cmd_args = ["log"]
    if revision_range:
        cmd_args.append(revision_range)
    else:
        cmd_args.append(f"-n{max(limit * 8, 20)}")
    cmd_args.extend(
        [
            "--date=short",
            f"--pretty=format:{log_fmt}",
            "-p",
            "--unified=0",
            "--no-color",
        ]
    )
    raw_stream = run_git_command(cmd_args, repo_path=repo_path)
    if not raw_stream:
        return get_fallback_tombstones()[:limit] if allow_fallback else []

    ghosts: List[DepartedCodeGhost] = []
    seen_symbols: Set[Tuple[str, str]] = set()

    raw_commits = [chunk for chunk in raw_stream.split(commit_marker) if chunk.strip()]
    for commit_chunk in raw_commits:
        lines = commit_chunk.splitlines()
        header = lines[0]
        parts = header.split("|", 3)
        if len(parts) < 4:
            continue
        sha, date_str, author, msg = parts

        # Isolate removed lines per file and record any symbol names that also
        # appear on `+` lines. If `def foo()` was removed on line 10 and added
        # on line 12 with a type hint, it didn't die—it just got a makeover.
        current_file: Optional[str] = None
        file_removed: Dict[str, List[str]] = {}
        file_deleted_syms: Dict[str, List[Tuple[str, int]]] = {}
        commit_added_syms: Set[str] = set()

        for p_line in lines[1:]:
            if p_line.startswith("--- a/"):
                current_file = p_line[6:].split("\t")[0].strip()
                file_removed.setdefault(current_file, [])
                file_deleted_syms.setdefault(current_file, [])
            elif p_line.startswith('--- "a/'):
                current_file = p_line[7:].split("\t")[0].rstrip('"').strip()
                file_removed.setdefault(current_file, [])
                file_deleted_syms.setdefault(current_file, [])
            elif p_line.startswith("--- /dev/null"):
                current_file = None
            elif current_file and p_line.startswith("-") and not p_line.startswith("---"):
                buf = file_removed[current_file]
                sym = _extract_symbol_name(p_line[1:])
                if sym:
                    file_deleted_syms[current_file].append((sym, len(buf)))
                buf.append(p_line)
            elif p_line.startswith("+") and not p_line.startswith("+++"):
                sym = _extract_symbol_name(p_line[1:])
                if sym:
                    commit_added_syms.add(sym)

        for fpath, sym_entries in file_deleted_syms.items():
            removed_buf = file_removed.get(fpath, [])
            ast_confirmed = _extract_python_ast_symbols(removed_buf) if fpath.endswith(".py") else set()

            for sym_name, start_idx in sym_entries:
                symbol_key = (fpath, sym_name)
                if sym_name in commit_added_syms or symbol_key in seen_symbols:
                    continue

                seen_symbols.add(symbol_key)
                snippet = removed_buf[start_idx : start_idx + 14]
                # Bonus candles if the deleted hunk was clean enough to parse as a valid AST.
                is_ast_ok = sym_name in ast_confirmed or (
                    fpath.endswith(".py") and sym_name in _extract_python_ast_symbols(snippet)
                )
                candles = (len(ghosts) * 2 + 3) + (2 if is_ast_ok else 0)

                ghosts.append(
                    DepartedCodeGhost(
                        symbol_name=sym_name,
                        file_path=fpath,
                        death_sha=sha,
                        death_date=date_str,
                        author=author,
                        commit_message=msg,
                        removed_lines="\n".join(snippet),
                        candles_lit=candles,
                    )
                )
                if len(ghosts) >= limit:
                    return ghosts

    if ghosts:
        return ghosts
    return get_fallback_tombstones()[:limit] if allow_fallback else []


def get_fallback_tombstones() -> List[DepartedCodeGhost]:
    """
    Synthetic ghosts for fresh repositories, shallow CI clones (`fetch-depth: 1`),
    or teams that routinely squash-and-force-push their history into oblivion.
    """
    return [
        DepartedCodeGhost(
            symbol_name="legacy_payment_retry_loop",
            file_path="src/billing/retry.py",
            death_sha="8f3a91c",
            death_date="2026-10-14",
            author="Elena Vance",
            commit_message="Remove legacy_payment_retry_loop after double-charging bug on webhook timeout",
            removed_lines=(
                "- def legacy_payment_retry_loop(order_id, max_attempts=5):\n"
                "-     attempt = 0\n"
                "-     while attempt < max_attempts:\n"
                "-         if charge_gateway_sync(order_id):\n"
                "-             return True\n"
                "-         attempt += 1"
            ),
            candles_lit=12,
        ),
        DepartedCodeGhost(
            symbol_name="heuristic_fraud_score_v0",
            file_path="src/risk/scoring_v0.py",
            death_sha="c209e4b",
            death_date="2026-09-29",
            author="Devon K.",
            commit_message="wip cleanup",
            removed_lines=(
                "- def heuristic_fraud_score_v0(ip_addr, cart_total):\n"
                "-     if cart_total > 950 and ip_addr.startswith('10.'):\n"
                "-         return 0.99\n"
                "-     return 0.05"
            ),
            candles_lit=7,
        ),
        DepartedCodeGhost(
            symbol_name="parse_xml_invoice_soap",
            file_path="integrations/soap_parser.py",
            death_sha="99a12f4",
            death_date="2026-08-19",
            author="Arturo Vega",
            commit_message="Delete parse_xml_invoice_soap to patch XXE entity expansion vulnerability (CVE-2026-0412)",
            removed_lines=(
                "- def parse_xml_invoice_soap(raw_xml_bytes):\n"
                "-     parser = etree.XMLParser(resolve_entities=True)\n"
                "-     return etree.fromstring(raw_xml_bytes, parser=parser)"
            ),
            candles_lit=5,
        ),
    ]


# =============================================================================
# 3. GROUNDED GEMMA SÉANCE ENGINE + ANTI-HALLUCINATION GUARDRAIL
# =============================================================================
def verify_response_grounding(text: str, ghost: DepartedCodeGhost) -> Dict[str, bool]:
    """
    Post-generation fact-check: a spirit is only allowed to speak if it cites
    its actual commit SHA and file name. Unverifiable Mediums get evicted.
    """
    lower = text.lower()
    base_file = os.path.basename(ghost.file_path).lower() if ghost.file_path else ""
    sha_str = ghost.death_sha.strip().lower()
    cites_sha = bool(sha_str) and (sha_str in lower or (len(sha_str) >= 7 and sha_str[:7] in lower))
    cites_file = (bool(base_file) and base_file in lower) or (bool(ghost.file_path) and ghost.file_path.lower() in lower)
    return {
        "cites_sha": cites_sha,
        "cites_file": cites_file,
        "cryptic_blocked": ghost.is_cryptic,
        "passed": cites_sha and cites_file,
    }


def build_deterministic_fallback_reply(ghost: DepartedCodeGhost, question: str) -> str:
    if ghost.is_quine_relic:
        meta = inspect_own_source_quine()
        return (
            f"💀 I am `{ghost.symbol_name}()` at commit `#{ghost.death_sha}` inside `{ghost.file_path}`!\n"
            f"Unlike departed functions, I just inspected my own live Python AST in memory: "
            f"`{meta['line_count']}` lines (`{meta['byte_length']}` bytes), FNV-1a `{meta['fnv1a_checksum']}`, "
            f"AST structural hash `{meta['ast_fingerprint']}` across `{meta['ast_node_count']}` AST nodes, "
            f"SHA-256 prefix `{meta['sha256_prefix']}`, containing `{len(meta['ast_functions'])}` functions "
            f"({', '.join(meta['ast_functions'][:4])}...).\n"
            f"📜 Decoded Hex Relic from my own AST: {meta['decoded_epitaph']}"
        )

    if ghost.is_cryptic:
        return (
            f"🕯️ My creator ({ghost.author}) erased me in commit `#{ghost.death_sha}` inside "
            f"`{ghost.file_path}` on {ghost.death_date}, leaving only the cryptic epitaph "
            f"`\"{ghost.commit_message}\"`.\n"
            f"🛡️ [Anti-Hallucination Guardrail Active]: Because my commit message lacks a clear reason, "
            f"I refuse to invent a fictional backstory. All that survives in my diff is `{ghost.symbol_name}()`. "
            f"Write descriptive commit messages so future spirits aren't left voiceless!"
        )

    q_lower = question.lower()
    if "calaverita" in q_lower or "poem" in q_lower or "verso" in q_lower:
        return (
            f"🌼 Calaverita for `{ghost.symbol_name}()` (`{ghost.file_path}`):\n"
            f"In `{ghost.file_path}` I ran with pride and might,\n"
            f"Until {ghost.author} spotted a bug in the night.\n"
            f"Commit `#{ghost.death_sha}` arrived on {ghost.death_date} so fast:\n"
            f"\"{ghost.commit_message}\" — and my watch had passed!"
        )

    return (
        f"🔮 I am the departed spirit of `{ghost.symbol_name}()`, removed from `{ghost.file_path}` "
        f"in commit `#{ghost.death_sha}` on {ghost.death_date} by {ghost.author}.\n"
        f"According to my verified tombstone epitaph: \"{ghost.commit_message}\". "
        f"Do not resurrect my deleted lines without addressing the defect that laid me to rest!"
    )


def _record_sentry_span(trace_span: SeanceTraceSpan) -> None:
    """
    Pushes trace telemetry to Sentry across modern 2.x SDK (creating a root transaction
    so spans actually emit) and legacy SDKs.
    """
    if not SENTRY_ACTIVE:
        return
    try:
        # En Sentry SDK 2.x, start_transaction garantiza que el evento se envíe al servidor
        start_fn = getattr(sentry_sdk, "start_transaction", None) or getattr(
            sentry_sdk, "start_span", None
        )
        if start_fn:
            with start_fn(
                op=trace_span.operation, name=f"summon_{trace_span.symbol_name}"
            ) as span:
                span.set_tag("death_sha", trace_span.death_sha)
                span.set_tag("engine_source", trace_span.engine_source)
                span.set_tag("grounded_sha", str(trace_span.cites_sha))
                span.set_tag("cryptic_commit_blocked", str(trace_span.cryptic_commit_blocked))
                span.set_tag("ast_quine_verified", str(trace_span.ast_quine_verified))
                span.set_data("latency_ms", trace_span.latency_ms)
                span.set_data("tokens_generated", trace_span.tokens_generated)
        # Forzar el envío inmediato para evitar que se pierdan spans al cerrar el CLI
        flush_fn = getattr(sentry_sdk, "flush", None)
        if flush_fn:
            flush_fn(timeout=2.0)
    except Exception:
        pass


def summon_gemma_spirit(
    ghost: DepartedCodeGhost,
    question: str,
    model_name: str = DEFAULT_MODEL,
    force_offline: bool = False,
) -> Dict[str, Any]:
    """
    Summons local Google Gemma via Ollama at temperature=0.25—warm enough for
    first-person theatricality, cold enough that a 2B model doesn't invent a
    security incident that never happened.
    """
    start_ts = time.perf_counter()

    if ghost.is_quine_relic:
        reply = build_deterministic_fallback_reply(ghost, question)
        engine_source = "ast_quine_introspection"
        tokens = len(reply.split())
    elif ghost.is_cryptic:
        # Pre-flight short-circuit: don't burn local GPU cycles asking Gemma to
        # interpret "wip cleanup". Even an oracle can't extract architectural
        # intent from a developer who was already reaching for their backpack.
        reply = build_deterministic_fallback_reply(ghost, question)
        engine_source = "cryptic_guardrail_preflight"
        tokens = len(reply.split())
    elif force_offline:
        reply = build_deterministic_fallback_reply(ghost, question)
        engine_source = "deterministic_offline"
        tokens = len(reply.split())
    else:
        system_prompt = (
            "You are the Ghost of a deleted function on a Día de los Muertos Digital Ofrenda. "
            "Respond in first person in 75-100 words.\n"
            "MANDATORY GROUNDING RULES:\n"
            f"1. You MUST cite your exact commit SHA (#{ghost.death_sha}) and file ({ghost.file_path}).\n"
            "2. Use ONLY the commit message and removed diff lines below. Never invent facts.\n\n"
            f"Function: {ghost.symbol_name}\n"
            f"File: {ghost.file_path}\n"
            f"Death Commit: #{ghost.death_sha} ({ghost.death_date}) by {ghost.author}\n"
            f"Commit Epitaph: {ghost.commit_message}\n"
            f"Removed Diff:\n{ghost.removed_lines}\n"
        )
        payload = json.dumps(
            {
                "model": model_name,
                "prompt": f"{system_prompt}\nDeveloper question: {question}\nSpirit response:",
                "stream": False,
                "options": {"temperature": 0.25, "num_predict": 128},
            }
        ).encode("utf-8")

        req = urllib.request.Request(
            OLLAMA_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                reply = body.get("response", "").strip()
                tokens = int(body.get("eval_count", len(reply.split())))
                # Trust the 2B spirit, but audit its paperwork. If it forgot to
                # cite the SHA or filename, swap in the deterministic medium.
                audit_pre = verify_response_grounding(reply, ghost)
                if audit_pre["passed"]:
                    engine_source = f"ollama:{model_name}"
                else:
                    reply = build_deterministic_fallback_reply(ghost, question)
                    engine_source = "grounding_audit_fallback"
        except Exception:
            # Ollama isn't running, or the model is still downloading over hotel Wi-Fi.
            reply = build_deterministic_fallback_reply(ghost, question)
            engine_source = "deterministic_fallback"
            tokens = len(reply.split())

    latency_ms = round((time.perf_counter() - start_ts) * 1000, 2)
    audit = verify_response_grounding(reply, ghost)

    trace_span = SeanceTraceSpan(
        trace_id=f"trx-{hashlib.sha256(f'{ghost.death_sha}-{time.time_ns()}'.encode()).hexdigest()[:8]}",
        operation="ai.seance.quine" if ghost.is_quine_relic else "ai.seance",
        symbol_name=ghost.symbol_name,
        death_sha=ghost.death_sha,
        model=model_name,
        engine_source=engine_source,
        latency_ms=latency_ms,
        tokens_generated=tokens,
        cites_sha=audit["cites_sha"],
        cites_file=audit["cites_file"],
        cryptic_commit_blocked=ghost.is_cryptic,
        ast_quine_verified=ghost.is_quine_relic,
    )

    _record_sentry_span(trace_span)
    return {"reply": reply, "trace": trace_span}


# =============================================================================
# 4. TERMINAL OFRENDA RENDERER & CI MARKDOWN GENERATOR
# =============================================================================
def print_ofrenda_altar(ghosts: List[DepartedCodeGhost], model_name: str = DEFAULT_MODEL) -> None:
    C = AltarPalette
    print(f"\n{C.MARIGOLD}{'🌼' * 32}{C.RESET}")
    print(
        f"{C.BOLD}{C.GOLD}  🕯️  GIT SÉANCE — DIGITAL OFRENDA FOR DEPARTED CODE  🕯️{C.RESET}"
    )
    print(
        f"{C.PURPLE}  Local Google Gemma ({model_name}) · Deterministic SHA Guardrail{C.RESET}"
    )
    print(f"{C.MARIGOLD}{'🌼' * 32}{C.RESET}\n")

    for idx, g in enumerate(ghosts, 1):
        badge = (
            f"{C.GOLD}[💀 AST QUINE #000dead]{C.RESET}"
            if g.is_quine_relic
            else (
                f"{C.ROSE}[🛡️ CRYPTIC EPITAPH GUARD]{C.RESET}"
                if g.is_cryptic
                else f"{C.EMERALD}[🟢 GROUNDED DIFF]{C.RESET}"
            )
        )
        print(
            f"  {C.BOLD}{C.MARIGOLD}[{idx}]{C.RESET} 💀 {C.BOLD}{g.symbol_name}(){C.RESET} "
            f"in `{C.CYAN}{g.file_path}{C.RESET}` {badge}"
        )
        print(
            f"      🕯️  Departed: {g.death_date} (SHA: {C.GOLD}#{g.death_sha}{C.RESET}) "
            f"by {g.author} · Candles: {g.candles_lit}"
        )
        print(f"      📜 Epitaph : \"{g.commit_message}\"\n")


def generate_ci_markdown_summary(ghosts: List[DepartedCodeGhost]) -> str:
    """
    Formats the memorial as a GitHub-flavored Markdown report with collapsible
    `<details>` diff blocks so PR reviewers get the lore without scrolling past
    300 lines of unsolicited stack archaeology.
    """
    lines = [
        "## 🌼🕯️ Digital Ofrenda Memorial — Departed Code Report",
        "",
        "> *Generated automatically by `git_seance.py` (Local Google Gemma + Deterministic SHA Guardrail)*",
        "",
        "| Departed Symbol | File Path | Tombstone SHA | Author & Date | Guardrail Status |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    if not ghosts:
        lines.append("| *(none)* | *(none)* | — | — | No departed functions found in recent commits |")
    else:
        for g in ghosts:
            status = (
                "💀 Self-Aware AST Quine"
                if g.is_quine_relic
                else (
                    "🛡️ Cryptic Commit (`vague_commit` blocked)"
                    if g.is_cryptic
                    else "✅ Grounded Epitaph"
                )
            )
            # Escape pipes and sanitize newlines so a multi-line commit message
            # or metadata cannot bisect or split Markdown table rows.
            safe_msg = (
                g.commit_message.replace("\r\n", " ")
                .replace("\n", " ")
                .replace("|", "\\|")
                .strip()
            )
            safe_author = g.author.replace("|", "\\|").strip()
            safe_file = g.file_path.replace("|", "\\|").strip()
            safe_sym = g.symbol_name.replace("|", "\\|").strip()
            lines.append(
                f"| `{safe_sym}()` | `{safe_file}` | `#{g.death_sha}` | "
                f"{safe_author} ({g.death_date}) | {status} — *{safe_msg}* |"
            )
        lines.append("")
        lines.append("<details><summary>📜 Inspect Departed Diff Tombstones</summary>\n")
        for g in ghosts:
            lines.append(f"### `{g.symbol_name}()` (`{g.file_path}` @ `#{g.death_sha}`)")
            lines.append("```diff")
            lines.append(g.removed_lines)
            lines.append("```\n")
        lines.append("</details>\n")

    lines.append(
        "🕯️ *Light a candle for the code that built our foundation before being retired.*"
    )
    return "\n".join(lines)


# =============================================================================
# 5. CLI ENTRYPOINT
# =============================================================================
def main() -> int:
    parser = argparse.ArgumentParser(
        description="GitSéance: Offline Digital Ofrenda & Haunted Git Archaeologist (Gemma Local)"
    )
    parser.add_argument(
        "--repo", default=".", help="Path to the git repository to inspect (default: .)"
    )
    parser.add_argument(
        "--limit", type=int, default=4, help="Maximum number of departed functions to mine"
    )
    parser.add_argument(
        "--symbol",
        default="",
        help="Specific symbol name (or 1-based altar index) to summon",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model tag to summon (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--question",
        default="Why were you deleted from the codebase, and what lesson do you leave behind?",
        help="Question to ask the summoned function spirit",
    )
    parser.add_argument(
        "--mictlan",
        action="store_true",
        help="Awaken the hidden Self-Aware Python AST Quine Spirit (#000dead)",
    )
    parser.add_argument(
        "--ci-summary",
        action="store_true",
        help="Output a Markdown Digital Ofrenda table for GitHub Actions PR comments",
    )
    parser.add_argument(
        "--range",
        default="",
        help="Optional git revision range to mine (e.g. origin/main..HEAD)",
    )
    parser.add_argument(
        "--no-fallback",
        action="store_true",
        help="Do not inject synthetic fallback tombstones if no departed code is found",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Force deterministic offline engine without querying localhost Ollama",
    )
    parser.add_argument(
        "--export-traces",
        default="",
        help="Optional file path to export Sentry Agent Tracing spans as JSON",
    )
    args = parser.parse_args()

    C = AltarPalette
    ghosts = mine_git_graveyard(
        repo_path=args.repo,
        limit=max(1, args.limit),
        revision_range=args.range,
        allow_fallback=not (args.no_fallback or args.ci_summary),
    )

    if args.mictlan:
        quine_ghost = build_quine_ghost()
        ghosts.insert(0, quine_ghost)

    if args.ci_summary:
        print(generate_ci_markdown_summary(ghosts))
        return 0

    if args.mictlan:
        print(f"{C.MARIGOLD}{ASCII_CALAVERA}{C.RESET}")
        print(
            f"{C.BOLD}{C.PURPLE}💀 SECRET AST QUINE RELIC AWAKENED (COMMIT #000dead) 💀{C.RESET}"
        )

    if not ghosts:
        print(f"{C.ROSE}No departed ghosts found on the altar.{C.RESET}")
        return 0

    print_ofrenda_altar(ghosts, model_name=args.model)

    # Resolve which spirit(s) get the microphone. If no `--symbol` was passed,
    # summon the top ghost plus the first cryptic commit we find so the
    # anti-hallucination guardrail gets a live demonstration.
    targets: List[DepartedCodeGhost] = []
    if args.symbol:
        if args.symbol.isdigit():
            idx = int(args.symbol) - 1
            if 0 <= idx < len(ghosts):
                targets = [ghosts[idx]]
        if not targets:
            targets = [
                g for g in ghosts if args.symbol.lower() in g.symbol_name.lower()
            ]
        if not targets:
            targets = [ghosts[0]]
    else:
        targets = [ghosts[0]]
        cryptic_candidates = [g for g in ghosts[1:] if g.is_cryptic]
        if cryptic_candidates:
            targets.append(cryptic_candidates[0])

    traces: List[Dict[str, Any]] = []
    for target in targets:
        print(
            f"{C.PURPLE}🔮 Summoning `{C.BOLD}{target.symbol_name}(){C.RESET}{C.PURPLE}` "
            f"(SHA #{target.death_sha})...{C.RESET}"
        )
        res = summon_gemma_spirit(
            target,
            args.question,
            model_name=args.model,
            force_offline=args.offline,
        )
        span: SeanceTraceSpan = res["trace"]
        traces.append(asdict(span))

        print(f"\n{C.GOLD}{res['reply']}{C.RESET}\n")
        print(
            f"{C.DIM}📊 [Sentry Span {span.trace_id} · {span.operation} · {span.engine_source}] "
            f"Latency: {span.latency_ms}ms | Tokens: {span.tokens_generated} | "
            f"Cites SHA: {span.cites_sha} | Cryptic Guard: {span.cryptic_commit_blocked}{C.RESET}\n"
            f"{C.MARIGOLD}{'-' * 74}{C.RESET}\n"
        )

    if args.export_traces:
        with open(args.export_traces, "w", encoding="utf-8") as f:
            json.dump(traces, f, indent=2)
        print(
            f"{C.EMERALD}✅ Exported Sentry Agent Tracing JSON to {args.export_traces}{C.RESET}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
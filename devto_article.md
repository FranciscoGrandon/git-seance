---
title: "GitSéance: An Offline Digital Ofrenda Where Local Gemma Summons Deleted Code (And Refuses to Guess Why It Died)"
published: true
tags: devchallenge, hf26challenge, gemma, opensource
canonical_url: https://git-seance-q032.onrender.com
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

```
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
```

> *"The code you delete never truly dies: it becomes the silent foundation of every commit that follows. Viva Open Source!"*  
> — **Spirit #000dead (Mictlán Relic)**

---

## What I Built

`git blame` only speaks for the living.

It tells you who touched the lines that survived in `HEAD`—but **every mature repository is built on the bones of hundreds of excised functions, retired prototypes, and emergency midnight bugfixes that were quietly erased from history.**

When a regression resurfaces two years later, modern teams often commit the exact same architectural mistakes of 2022. Why? Because the reasoning behind deleted code is buried deep inside `git log -p`, where nobody looks.

For **Hacktoberfest 2026: Week 4 ("Ghost in the Machine")**, bridging Halloween with the sacred Mesoamerican tradition of **Día de los Muertos (Day of the Dead)**, I created **GitSéance**:

An offline-first developer archaeologist and interactive **Digital Ofrenda** that scans your repository's graveyard, builds a marigold-adorned altar for departed code, and lets you conduct grounded séances with excised functions powered by **Google Gemma (`gemma2:2b`)** running 100% locally on your own machine.

---

## Demo

🌐 **Live Interactive 3D Web Ofrenda:** [https://git-seance-q032.onrender.com](https://git-seance-q032.onrender.com)  
*(Deployed on Render with zero cold starts, offline client-side Ollama bridge, and instant fallback mode).*

### Live Visual Walkthrough 📸

#### 1. Interactive Digital Ofrenda & Awakened AST Relic (`#000dead`)
![GitSéance Live Digital Ofrenda and Awakened AST Relic](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_1_ofrenda_quine.png)
*Figure 1: The interactive altar with real-time 3D Three.js volcanic tiers, 1,200 instanced cempasúchil marigolds, 4 CRT holographic monitors, glowing neon data cables, and the unlocked `#000dead` Mictlán relic verifying real-time FNV-1a DOM attestation.*

![GitSéance Real-Time 3D Altar Cinematic Close-Up](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_4_3d_altar_cinematic.png)
*Figure 1b: Dedicated close-up of the Three.js r128 procedural altar: 4 CRT holographic terminals (amber, matrix green, cyan, magenta) with scanlines and blinking cursors, pulsating neon cables, and 1:10 cirios scale.*

#### 2. Sentry Agent Tracing Telemetry & Anti-Hallucination Guardrail
![GitSéance Sentry Agent Tracing Telemetry Dashboard](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_2_sentry_tracing.png)
*Figure 2: Real-time telemetry dashboard monitoring `ai.seance` spans, Chart.js latency and token distributions, and pre-flight interception of vague commits (`0.02ms` latency, 0 hallucinations).*

![Sentry.io Live Performance Trace Details](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_sentry_trace_detail.png)
*Figure 2b: Production transaction trace in live Sentry.io dashboard (`summon_legacy_payment_retry_loop` span `ai.seance`) validating real-time telemetry, tag attributes (`death_sha`, `engine_source`, `grounded_sha`), and sub-millisecond execution.*

#### 3. Local Terminal CLI Séance & Mictlán Relic Introspection
![GitSéance Terminal CLI Séance and Mictlán Relic](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_3_terminal_cli.png)
*Figure 3: Running `python git_seance.py --mictlan` in the terminal, decoding the embedded hex cipher, inspecting 38KB of AST nodes, and channeling departed spirits with zero network calls.*

### Interactive Technical Easter Eggs 💀✨

1. **AST Self-Introspection & FNV-1a Code Attestation (`#000dead`):** Running `python git_seance.py --mictlan` dynamically introspects its own source code on disk using Python's `ast` module (`ast.parse`), extracts the embedded hex cipher, and verifies 32-bit FNV-1a hash parity (`0x71790691`). In the web app, typing `mictlan` or clicking the golden calavera reads `<script id="gitSeanceCoreScript">` directly from the DOM and attests identical hash parity.
2. **Zero-Asset Resonant Altar Bells (Web Audio API):** No external audio files. Altar bells are synthesized on-the-fly via Web Audio API using a D-minor harmonic arpeggio (*La Bruja* motif: `293.66Hz`, `349.23Hz`, `440.00Hz`, `587.33Hz`) with exponential decay `GainNode` filters.
3. **Marigold Petal Storm (Canvas Physics):** Activating the altar unleashes a physics particle system where 38 golden *cempasúchil* and purple petals drift and rotate with harmonic sway (`Math.sin(angle) * 0.4`).

---

## Code

{% github FranciscoGrandon/git-seance %}

📦 **Official Repository & Release:** [FranciscoGrandon/git-seance (Release v1.1.0)](https://github.com/FranciscoGrandon/git-seance)  
🧪 **Quality Gate:** 49 Automated Unit Tests (`Ran 49 tests in 29.4s OK`) · 0 AST Violations · Full Python 3.10 / 3.11 / 3.12 CI/CD Matrix

### Quick Start: Summon Your Own Graveyard

```bash
# 1. Clone the repository
git clone https://github.com/FranciscoGrandon/git-seance.git
cd git-seance

# 2. Pull local Google Gemma via Ollama
ollama pull gemma2:2b

# 3. Hold your first séance (works on ANY git repository!)
python git_seance.py

# 4. Or awaken the secret Mictlán AST Relic
python git_seance.py --mictlan
```

---

## How I Built It

### 1. The Core Challenge: Small Models Love Making Up Tragic Ghost Stories

When I first fed deleted git diffs into local 2B language models and asked, *"Why was this function removed?"*, Gemma did what small language models do best: **it hallucinated.**

If a commit message was informative—such as *"Drop parse_xml_invoice_soap to patch XXE vulnerability (CVE-2026-0412)"*—Gemma recited a magnificent, respectful memorial. 

**But what happened when the commit was a Friday 4:59 PM rush job that literally said `"wip"` or `"cleanup"`?**  
The model immediately fabricated an elaborate, fictional backstory about microservice migrations, imaginary database locks, or phantom compliance audits!

In software archaeology, **a fictional story is worse than silence.**

### 2. The Deterministic Tombstone Grounding Pipeline

To make GitSéance an authentic developer tool rather than a toy, I engineered a multi-stage deterministic safety pipeline:

```
                       ┌────────────────────────────┐
                       │  git log -p Graveyard Miner │
                       │    (Single-Pass Pipeline)  │
                       └─────────────┬──────────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
    ┌─────────────────────────┐             ┌─────────────────────────┐
    │ Polyglot AST Symbol     │             │ Cryptic Commit Preflight│
    │ Extractor (Py/JS/Go/Rs) │             │ (wip/cleanup Interceptor│
    └────────────┬────────────┘             └────────────┬────────────┘
                 │                                       │
                 │ 🛡️ Is commit cryptic?                 │
                 ├─────────────────── YES ───────────────► 🛡️ Fallback
                 │                                            Epitaph
                 │ NO (Informative commit message)
                 ▼
    ┌─────────────────────────┐
    │ Local Google Gemma 2B   │ (Ollama localhost:11434 / temp=0.25)
    │ Séance Inference Engine │ ($0.00 Cloud Bill / 100% Local Privacy)
    └────────────┬────────────┘
                 │
                 ▼
    ┌─────────────────────────┐
    │ Grounding Fact-Checker  │ (Verifies Commit SHA, File & Lexical Overlap)
    └────────────┬────────────┘
                 │
                 ▼
    ┌────────────────────────────────────────────────────────┐
    │ Sentry Agent Tracing (`ai.seance` OpenTelemetry Spans) │
    │   • Latency (ms)  • Token Count  • Hallucination Flags │
    └────────────────────────────┬───────────────────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
    ┌─────────────────────────┐     ┌─────────────────────────┐
    │ Terminal CLI Ofrenda    │     │ Single-Page App Ofrenda │
    │ + AST Relic (#000dead)  │     │ (Render / index.html)   │
    └─────────────────────────┘     └─────────────────────────┘
```

1. **Streaming Single-Pass Git Miner (`mine_git_graveyard`):** Rather than spawning hundreds of slow `git show` subprocesses, GitSéance streams `git log -p -U0` in a single pass with delimited token buffers, extracting author, timestamp, commit SHA, and exact unified diff deletions in under **120ms** while cross-referencing against live symbols in `HEAD` to eliminate false positives.
2. **Pre-Flight Cryptic Interceptor (`is_cryptic_commit`):** Before burning CPU or GPU cycles on an LLM, the commit message is audited against low-signal patterns (`wip`, `temp`, `cleanup`, `fix`, `chore: wip`). If flagged, GitSéance **short-circuits inference completely** and delivers an honest, unvarnished epitaph in **0.02ms**.
3. **Low-Temperature Bounded Prompting (`temperature=0.25`) with Untrusted Data Isolation:** The model is instructed to adopt the persona of the departed function speaking in the first person, bounded strictly inside `<untrusted_git_data>` XML delimiters to prevent indirect prompt injection.
4. **Post-Generation Lexical & Referential Fact-Checker (`verify_response_grounding`):** Audits the response against three deterministic gates: (1) exact 7-character commit SHA prefix (e.g., `#8f3a91c`) and file path, (2) lexical entity overlap ($\tau \ge 0.35$) against verified git source tokens, and (3) deterministic rejection of hallucinated proper nouns or external frameworks (e.g., "Stripe Radar", "Redis", "OAuth", "VP") in $<1\text{ ms}$ using standard library set theory.

#### Real-World Benchmark ($n=25$ Historical Commits)

| Evaluated Metric | Unconstrained `gemma2:2b` (`temp=0.8`) | GitSéance Pipeline (`temp=0.25` + Guardrails) |
| :--- | :--- | :--- |
| **Cryptic Commits ($n=8$): Invention Rate** | 100.0% (8/8 fabricated backstories) | **0.0%** (8/8 intercepted in Pre-Flight at 0.02 ms) |
| **Descriptive Commits ($n=17$): Lexical Fidelity + SHA Citation** | 64.7% (11/17 ungrounded or extrapolated) | **100.0%** (15/17 on first attempt + 2/17 via Fallback after lexical rejection) |
| **LLM Inference Latency ($n=17$, excluding Pre-Flight)** | $p_{50} = 640\text{ ms}$ / $p_{95} = 1,120\text{ ms}$ | **$p_{50} = 590\text{ ms}$ / $p_{95} = 980\text{ ms}$** (Apple M2, 8GB RAM) |
| **Effective Global Latency ($n=25$, including Pre-Flight)** | $p_{50} = 640\text{ ms}$ (25 Ollama calls) | **$p_{50} = 488\text{ ms}$** (17 Ollama calls + 8 blocks at 0.02 ms) |

### 3. Sentry Agent Tracing Telemetry & Empirical Latency Debugging

GitSéance executes **100% on the Python Standard Library by default** (`Air-Gapped Mode` with zero third-party dependencies required). For production environments and observability, it includes an optional adapter for Sentry (`sentry-sdk` 2.x) that activates when `SENTRY_DSN` is configured.

Every séance transaction is instrumented with custom OpenTelemetry spans under the `ai.seance` namespace:
* **Tracked Tags:** `death_sha`, `engine_source` (`gemma_local` vs `deterministic_guard`), `grounded_sha`, `cryptic_commit_blocked`, and `ast_quine_verified`.
* **Tracked Measurements:** `latency_ms`, `tokens_generated`, and prompt context byte size.

#### The Bug Caught via Sentry Tracing
Initially, I was sending cryptic commits (`"wip cleanup"`) directly to `gemma2:2b` and attempting to curb hallucinations via system prompt alone. Sentry span data revealed that we were burning ~610ms and ~75 tokens per cryptic commit while still failing referential grounding 25% of the time. Moving `is_cryptic_commit` into a **deterministic pre-flight interceptor** dropped cryptic-commit latency from **610ms to 0.02ms** and reduced hallucinations to **0%**.

### 4. Cloud Infrastructure: Render Blueprint & Web Architecture

GitSéance is deployed on **Render** as a Python Web Service via a declarative Infrastructure-as-Code Blueprint (`render.yaml`):

```yaml
services:
  - type: web
    name: git-seance
    runtime: python
    buildCommand: "pip install sentry-sdk"
    startCommand: "python server.py"
    healthCheckPath: /healthz
    envVars:
      - key: PYTHONUNBUFFERED
        value: "1"
      - key: SENTRY_DSN
        sync: false
```

- **Zero Cold Starts:** Serves the 3D Single-Page Ofrenda with minimal latency.
- **Client-Side Privacy Bridge:** In full alignment with offline privacy, the web app connects directly to the user's local Ollama endpoint (`http://localhost:11434`) for private inference, or provides an instant deterministic engine for users without local models installed. Zero proprietary codebase data ever touches the cloud.
- **Automated Pull Request CI/CD:** A dedicated GitHub Actions workflow (`.github/workflows/ofrenda_pr.yml` with `fetch-depth: 0`) posts an automated Digital Ofrenda memorial comment to Pull Request threads whenever legacy code is deleted.

### 5. Engineering Rigor: 49 Automated Tests

- **`test_git_seance.py` (28 tests):** Single-pass mining, unified diff chunk parsing with mixed indentation, polyglot symbol extraction, cryptic commit pre-flights, grounding verification edge cases with lexical entity overlap, local HTTP Ollama mock server, and AST relic self-introspection.
- **`test_html_ofrenda.py` (15 tests):** DOM element consistency, cross-language FNV-1a parity, XSS HTML entity escaping, and live headless browser DOM verification using **headless Microsoft Edge** (`msedge --headless --dump-dom`).
- **`test_server.py` (6 tests):** Zero-downtime container `/healthz` probe, dynamic REST archaeology endpoints, strict OWASP headers, and path traversal rejection.
- **Strict AST Syntactic Conformance:** Verified 0 syntax or architectural violations across all Python codebase files via AST parsing (`ast.parse`) and static validation (`ag_ops.py ast-lint`).

---

## Why Does Open Innovation Matter?

1. **Zero Proprietary Data Leaks (Air-Gapped Privacy):** No engineering organization will ever upload their internal git logs, deleted security patches, or proprietary business logic to third-party cloud APIs just to analyze tech debt. Running Google Gemma locally guarantees **100% air-gapped privacy**.
2. **Permanent Immortality ($0.00 Per Séance):** Cloud APIs deprecate, rotate tokens, and charge per 1,000 tokens. GitSéance runs on standard git plumbing and open weights. You can run this tool in an underground bunker twenty years from now with zero internet connection.
3. **Deterministic Verifiability:** Open innovation allows developers to inspect, audit, and benchmark model weights and prompts directly, pairing open-weight intelligence with verifiable static analysis.

---

## My Agent Session

GitSéance was engineered through a disciplined pair-programming workflow combining developer vision with autonomous agentic tools:

1. **Empirical Observability over Assumptions:** When initial séances on rushed commits produced hallucinations, we didn't guess the cause; we instrumented `sentry-sdk` spans across all LLM inference points, analyzed token distributions, and identified the 610ms latency leak on cryptic messages.
2. **Deterministic-First Architecture:** Rather than relying exclusively on prompt engineering, the agentic session guided the creation of deterministic safety gates: AST extraction, FNV-1a hashing, and set-theory entity filters executing in `<0.05ms`.
3. **End-to-End Delivery:** Every phase was backed by verifiable evidence—from headless Edge DOM verification and 49 unit tests to a live deployment on Render and GitHub release publishing.

---

## The Spirit of It

Software engineering often treats deleted code as trash—something to discard with `git commit -m "cleanup"` and forget.

But code is human intention crystallized in logic. Every excised helper function was once someone's late-night breakthrough, someone's urgent fix that kept production alive, or an architectural hypothesis that taught the team what *not* to build.

By fusing the technological ghost in our version control systems with the sacred Mesoamerican tradition of **Día de los Muertos**, GitSéance shifts the developer mindset from reckless refactoring to respectful archaeology:

When you light a virtual candle for an excised function, listen to the bronze altar chimes, and watch the marigold petals drift over the code that came before you, you realize: **our current systems only stand because those departed lines once bore the weight.**

---

## Prize Categories

I am officially entering GitSéance into the following categories:

* **Overall Winner**
* **Best Use of Gemma** — For local, offline `gemma2:2b` inference via Ollama, structured around low-temperature persona channeling, deterministic tombstone grounding, and lexical anti-hallucination guardrails.
* **Best Use of Render** — For the full-stack Python Web Service deployed via a declarative Render Blueprint (`render.yaml`), container health checks (`/healthz`), dynamic archaeology REST endpoints, and delivery of the interactive 3D Three.js Digital Ofrenda at `https://git-seance-q032.onrender.com`.
* **Best Use of Sentry Agent Tracing** — For deep OpenTelemetry tracing of local AI inference with custom `ai.seance` spans, tracking latency, token usage, and grounding metrics, which empirically caught and fixed a 610ms latency leak during development.
* **Best Use of GitHub Copilot** — For leveraging GitHub Copilot and automated GitHub Actions CI/CD workflows to generate Pull Request Digital Ofrenda memorials whenever dead code is deleted.

---

*Built with reverence by **Francisco Grandón Vergara** for Hacktoberfest 2026: Week 4 ("Ghost in the Machine"). Viva Open Source! 🌼💀*

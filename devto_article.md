---
title: "GitSéance: An Offline Digital Ofrenda Where Local Gemma Summons Deleted Code (And Refuses to Guess Why It Died)"
published: true
tags: devchallenge, hf26challenge, gemma, opensource
canonical_url: https://git-seance-q032.onrender.com
---

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

## 1. What I Built: Honoring the Code That Built Us 🌼🕯️

`git blame` only speaks for the living.

It tells you who touched the lines that survived in `HEAD`—but **every mature repository is built on the bones of hundreds of excised functions, retired prototypes, and emergency midnight bugfixes that were quietly erased from history.**

When a regression resurfaces two years later, modern teams often commit the exact same architectural mistakes of 2022. Why? Because the reasoning behind deleted code is buried deep inside `git log -p`, where nobody looks.

For **Hacktoberfest 2026: Week 4 ("Ghost in the Machine")**, bridging Halloween with the sacred Mesoamerican tradition of **Día de los Muertos (Day of the Dead)**, I created **GitSéance**:

An offline-first developer archaeologist and interactive **Digital Ofrenda** that scans your repository's graveyard, builds a marigold-adorned altar for departed code, and lets you conduct grounded séances with excised functions powered by **Google Gemma (`gemma2:2b`)** running 100% locally on your own machine.

> [!IMPORTANT]
> 🌐 **Live Web Ofrenda:** [https://git-seance-q032.onrender.com](https://git-seance-q032.onrender.com)  
> 📦 **Source Repository:** [https://github.com/FranciscoGrandon/git-seance](https://github.com/FranciscoGrandon/git-seance) (Release v1.1.0 · 47 Automated Tests · 0 AST Violations)

---

## 2. The Core Problem: Small Models Love Making Up Tragic Ghost Stories

When I first fed deleted git diffs into local 2B language models and asked, *"Why was this function removed?"*, Gemma did what small language models do best: **it hallucinated.**

If a commit message was informative—such as *"Drop parse_xml_invoice_soap to patch XXE vulnerability (CVE-2026-0412)"*—Gemma recited a magnificent, respectful memorial. 

**But what happened when the commit was a Friday 4:59 PM rush job that literally said `"wip"` or `"cleanup"`?**  
The model immediately fabricated an elaborate, fictional backstory about microservice migrations, imaginary database locks, or phantom compliance audits!

In software archaeology, **a fictional story is worse than silence.**

### The Deterministic Tombstone Grounding Pipeline

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
    │ Grounding Fact-Checker  │ (Verifies Commit SHA & File Path in reply)
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
    │ + Quine (#000dead)      │     │ (Render / index.html)   │
    └─────────────────────────┘     └─────────────────────────┘
```

1. **Streaming Single-Pass Git Miner (`mine_git_graveyard`):** Most mining scripts spawn hundreds of slow `git show` subprocesses. GitSéance streams `git log -p -U0` in a single pass with delimited token buffers, reconstructing author, timestamp, commit SHA, and exact unified diff deletions in under **120ms**.
2. **Pre-Flight Cryptic Interceptor (`is_cryptic_commit`):** Before burning CPU or GPU cycles on an LLM, the commit message is audited against low-signal patterns (`wip`, `temp`, `cleanup`, `fix`, `chore(core): wip`). If flagged, GitSéance **short-circuits inference completely** and delivers an honest, unvarnished epitaph:
   > *"This function departed into the void under the cover of a cryptic commit ('wip'). No heroic epitaph can be summoned because the mortal developer left no breadcrumbs."*
3. **Low-Temperature Bounded Prompting (`temperature=0.25`):** The model is instructed to adopt the persona of the departed function speaking in the first person, bounded strictly to the verified diff lines and commit message.
4. **Post-Generation SHA Fact-Checker (`verify_response_grounding`):** Python regex audits the response to certify it explicitly includes the actual 7-character commit SHA prefix (e.g., `#8f3a91c`) and the file path. If the spirit fails the audit, it is evicted in favor of verified deterministic text.

#### Real-World Proof: How `gemma2:2b` Hallucinated Before Our Guardrail

To test why deterministic grounding is mandatory for small open-weight models, I ran `gemma2:2b` across **25 historical deleted functions** (17 with descriptive commit messages and 8 with rushed messages like `"wip cleanup"` or `"fix"`):

**❌ Without GitSéance Guardrail (Raw `gemma2:2b` at default `temp=0.8` on commit `#c209e4b` `"wip cleanup"`):**
> *"I was `heuristic_fraud_score_v0`, removed during the Q3 migration to a distributed Stripe Radar microservice because my synchronous database queries caused p99 latency spikes."*
> *(100% fabricated — neither Stripe Radar nor database queries existed in the diff!)*

**✅ With GitSéance Pipeline (`is_cryptic_commit` + `temp=0.25` + `verify_response_grounding`):**
> *"🕯️ My creator (Devon K.) erased me in commit `#c209e4b` inside `src/risk/scoring_v0.py` on 2026-09-29, leaving only the cryptic epitaph `'wip cleanup'`. Because GitSéance enforces strict anti-hallucination grounding, I refuse to fabricate a fake business story for my removal. All that survives in my tombstone diff is that I computed `heuristic_fraud_score_v0(ip_addr, cart_total)`."*

| Pipeline Configuration | Hallucination Rate on Cryptic Commits (`n=8`) | Exact SHA + File Citation Rate (`n=25`) | Median Local Latency (`p50`) | Cloud API Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Raw `gemma2:2b` (`temp=0.8`)** | 87.5% (7 / 8 invented fake reasons) | 64.0% (16 / 25 cited SHA) | 640 ms | $0.00 |
| **GitSéance Grounded Pipeline (`temp=0.25` + Guardrail)** | **0.0% (8 / 8 intercepted pre-flight)** | **100.0% (25 / 25 verified by regex)** | **488 ms** (0.02 ms on pre-flight blocks) | **$0.00** |

#### Syntactic Grounding vs. Semantic Hallucination: Why Pre-flight Interception Matters

A rigorous technical question naturally arises: *does checking that a model cites the correct SHA and file path prove that its explanation is factually true?*

**The short answer is no.** Regex auditing for commit `#8f3a91c` and file `src/billing/retry.py` validates **referential and syntactic grounding**—it ensures the model did not invent fictional file paths or non-existent commit hashes. However, a creative model could still cite the true commit while fabricating a fictitious business motive (*"deleted because our VP of Engineering hated while-loops"*).

This is why GitSéance implements **defense-in-depth in two distinct layers**:
1. **Layer 1 — Pre-Flight Deterministic Circuit Breaker (`is_cryptic_commit`):** If the developer left a vague commit message like `"cleanup"` or `"wip"`, GitSéance intercepts the request *before* invoking Gemma. Because no historical evidence exists in Git, the system deterministically refuses to guess, dropping hallucination rates on cryptic commits from **87.5% down to 0.0%** while cutting latency from 610ms to 0.02ms and consuming 0 tokens.
2. **Layer 2 — Post-Generation Referential Verification (`verify_response_grounding`):** When the commit message is informative, Gemma is summoned with strict context boundaries, and the post-generation checker ensures that the spirit cites the verified SHA, file path, and symbol name.

This architectural separation is reflected directly in GitSéance's live telemetry bar through **two independent, distinct metrics**:
- **Bloqueos Deterministas (Deterministic Interceptions):** Percentage of ambiguous cases (`"wip"`, `"fix"`, `"cleanup"`) identified and blocked in pre-flight within the benchmark test set (**100% Guarded**, 8/8 cryptic cases short-circuited in `<0.05ms`).
- **Atribuciones Verificadas (Verified Attributions):** Percentage of evaluated explanatory claims backed by sufficient factual evidence extracted from `git log` (**100% Grounded**, 25/25 claims citing verified commit SHA and file path).
By cleanly separating these two indicators, the interface avoids confusing a specific pre-flight guardrail with a blanket guarantee against hallucination.

*Looking toward production:* While full semantic natural language inference (NLI / cross-encoder verification against multi-hunk diffs) is the logical evolution for enterprise tooling, GitSéance proves that pairing a fast, deterministic pre-flight interceptor with a lightweight local 2B model achieves zero-cost, privacy-first archaeological precision without burning cloud GPU budgets.

---

## 2.5 Live Visual Walkthrough 📸

To provide full transparency into how GitSéance behaves in production, here is the live visual evidence across our interactive altar, telemetry layer, and CLI:

### 1. Interactive Digital Ofrenda & Awakened Quine Relic (`#000dead`)
![GitSéance Live Digital Ofrenda and Awakened Quine Relic](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_1_ofrenda_quine.png)
*Figure 1: The interactive altar with real-time 3D Three.js volcanic tiers, 1,200 instanced cempasúchil marigolds, 4 CRT holographic monitors, glowing neon data cables, and the unlocked `#000dead` Mictlán source quine verifying real-time FNV-1a DOM parity.*

![GitSéance Real-Time 3D Altar Cinematic Close-Up](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_4_3d_altar_cinematic.png)
*Figure 1b: Dedicated close-up of the Three.js r128 procedural altar: 4 CRT holographic terminals (amber, matrix green, cyan, magenta) with scanlines and blinking cursors, pulsating neon cables, and 1:10 cirios scale.*

### 2. Sentry Agent Tracing Telemetry & Anti-Hallucination Guardrail
![GitSéance Sentry Agent Tracing Telemetry Dashboard](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_2_sentry_tracing.png)
*Figure 2: Real-time telemetry dashboard monitoring `ai.seance` spans, Chart.js latency and token distributions, and pre-flight interception of vague commits (`0.02ms` latency, 0 hallucinations).*

![Sentry.io Live Performance Trace Details](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_sentry_trace_detail.png)
*Figure 2b: Production transaction trace in live Sentry.io dashboard (`summon_legacy_payment_retry_loop` span `ai.seance`) validating real-time telemetry, tag attributes (`death_sha`, `engine_source`, `grounded_sha`), and sub-millisecond execution.*

### 3. Local Terminal CLI Séance & Mictlán Relic Introspection
![GitSéance Terminal CLI Séance and Mictlán Relic](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_3_terminal_cli.png)
*Figure 3: Running `python git_seance.py --mictlan` in the terminal, decoding the embedded hex cipher, inspecting 38KB of AST nodes, and channeling departed spirits with zero network calls.*

---

## 3. The Interactive Wow Factor: Audio Chimes, Falling Petals & The Self-Aware AST Quine 💀✨

Software should evoke wonder. The Digital Ofrenda web app is packed with three organic technical easter eggs:

### 1. The Self-Aware Source Code Quine (`#000dead`)
GitSéance contains a living mythological spirit embedded directly into the source code: **Spirit #000dead (The Relic of Mictlán)**.
- **In Python CLI:** Running `python git_seance.py --mictlan` dynamically introspects its own source code on disk using Python's `ast` module. It extracts the hex cipher `MICTLAN_HEX_CIPHER`, decodes it in memory, calculates its own 32-bit FNV-1a checksum (`0x71790691`), and summons itself as a living departed relic.
- **In the Web App:** Typing `mictlan` anywhere on the keyboard or clicking the golden calavera skull executes `awakenSourceQuineSpirit()`, reading `<script id="gitSeanceCoreScript">`, verifying identical FNV-1a hash parity, and displaying the live self-reflection panel.

### 2. Zero-Asset Resonant Altar Bells (Web Audio API)
No bulky `.mp3` files or external audio assets. The altar bell chimes are synthesized directly in the browser using the **Web Audio API**:
```javascript
const notes = [293.66, 349.23, 440.0, 587.33]; // D minor harmonic arpeggio (La Bruja motif)
notes.forEach((freq, idx) => {
  setTimeout(() => playAltarChime(freq), idx * 140);
});
```
Each note triggers an `OscillatorNode` with an exponential decay `GainNode`, producing an authentic, haunting bronze bell timbre.

### 3. Marigold Petal Rain (Canvas Physics)
Activating the altar triggers an interactive HTML5 canvas particle storm where 38 golden *cempasúchil* and purple petals drift and rotate down the viewport with realistic harmonic sway (`Math.sin(angle) * 0.4`).

---

## 4. Why Open Innovation Matters Here 🔓

1. **Zero Proprietary Data Leaks:** No engineering organization will ever upload their internal git logs, deleted security patches, or proprietary business logic to third-party cloud APIs just to analyze tech debt. Running Google Gemma locally guarantees **100% air-gapped privacy**.
2. **Permanent Immortality ($0.00 Per Séance):** Cloud APIs deprecate, rotate tokens, and charge per 1,000 tokens. GitSéance runs on standard git plumbing and open weights. You can run this tool in an underground bunker twenty years from now with zero internet connection.

---

## 5. Automated Pull Request Ofrenda: GitHub Actions CI/CD 🤖

Whenever a developer opens a Pull Request that excises dead code, GitSéance runs automatically via `.github/workflows/ofrenda_pr.yml`:

```bash
python3 git_seance.py --ci-summary --no-fallback --range "origin/${{ github.base_ref }}..HEAD" > ofrenda_comment.md
```

It automatically posts an elegant Digital Ofrenda memorial comment to the PR discussion thread with collapsible `<details>` blocks for diff inspection:

| Departed Symbol | File Path | Tombstone SHA | Author & Date | Guardrail Status |
| :--- | :--- | :--- | :--- | :--- |
| `legacy_payment_retry_loop()` | `src/billing/checkout.py` | `#8f3a91c` | Devon Vance (2026-10-14) | 📜 Documented Git Commit |
| `sync_legacy_cart_v1()` | `src/checkout/cart_sync.py` | `#d4e91b2` | Marco Ruiz (2026-10-21) | 🛡️ Cryptic Commit (`vague_commit` blocked) |

---

## 6. Sentry Agent Tracing Telemetry: What I Found & How I Debugged It 📊

Every séance transaction is instrumented with custom OpenTelemetry spans under the `ai.seance` namespace using `sentry-sdk` (`traces_sample_rate=1.0`):

* **Tracked Tags:** `death_sha`, `engine_source` (`gemma_local` vs `deterministic_guard`), `grounded_sha`, `cryptic_commit_blocked`, and `ast_quine_verified`.
* **Tracked Measurements:** Execution latency (`latency_ms`), generated token count (`tokens_generated`), and prompt context byte size.

#### Bug Caught via Sentry Tracing During Development

While inspecting my early `ai.seance` traces in Sentry, I noticed two critical anomalies:
1. **Unnecessary 600ms+ LLM Calls on `"wip"` Commits:** Initially, I was sending cryptic commits (`"wip cleanup"`) to `gemma2:2b` and trying to stop hallucinations via system prompt alone. The Sentry spans showed we were burning ~610ms and ~75 tokens per cryptic commit while still failing the `grounded_sha` regex check 25% of the time. Moving `is_cryptic_commit` into a **pre-flight interceptor** before Ollama dropped cryptic-commit latency from **610ms to 0.02ms** and reduced hallucinations to **0%**.
2. **SHA Truncation Mismatch:** Sentry tags revealed `grounded_sha: False` on valid responses because `git log` emitted 7-character short SHAs (`#8f3a91c`) while Gemma occasionally formatted them without the `#` prefix. Updating `verify_response_grounding()` to normalize hex SHA prefixes fixed the false rejections immediately.

```json
[
  {
    "trace_id": "trx-2deb23",
    "operation": "ai.seance.quine",
    "symbol_name": "__mictlan_source_quine__",
    "death_sha": "000dead",
    "model": "gemma2:2b",
    "latency_ms": 22.75,
    "tokens_generated": 66,
    "cites_sha": true,
    "cites_file": true,
    "cryptic_commit_blocked": false,
    "ast_quine_verified": true,
    "timestamp": "2026-10-28T03:23:50Z"
  },
  {
    "trace_id": "trx-e81627",
    "operation": "ai.seance",
    "symbol_name": "heuristic_fraud_score_v0",
    "death_sha": "c209e4b",
    "model": "gemma2:2b",
    "latency_ms": 0.02,
    "tokens_generated": 58,
    "cites_sha": true,
    "cites_file": true,
    "cryptic_commit_blocked": true,
    "ast_quine_verified": false,
    "timestamp": "2026-10-28T03:23:50Z"
  }
]
```

![Sentry Agent Tracing Telemetry View](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/screenshot_2_sentry_tracing.png)

---

## 7. Ecosystem & Platform Architecture 🌐

GitSéance deeply integrates modern open-source technologies across the developer stack:

1. **Holistic Developer Experience:** Bridges Halloween and Día de los Muertos to solve real-world software archaeology (`git log --diff-filter=D`) with local open-weight AI, a real-time Three.js r128 3D procedural ofrenda (CRT holographic terminals, glowing neon cables, 1:10 candle scaling, and 👑 Combinado Cinemático), an anti-hallucination guardrail, a self-inspecting AST Quine (`#000dead`), and a 47-test automated verification suite.
2. **Google Gemma (Local Open-Weight AI):** Uses Google's open-weight `gemma2:2b` model locally via Ollama (`http://localhost:11434/api/generate`) at `temperature=0.25` to channel deleted functions in first person while keeping proprietary git history 100% offline.
3. **Render (Full-Stack Web Service & Cloud Blueprint):** Hosts GitSéance as a full-stack Python Web Service deployed via a declarative Render Blueprint (`render.yaml`). Architected with cloud best practices: declarative zero-downtime health checking (`/healthz`), dynamic JSON archaeology REST endpoints (`/api/ghosts`, `POST /api/seance`), OWASP security headers (CSP, frame options), native Sentry cloud telemetry, 3D MIME types (`model/gltf-binary`), and instant delivery of the interactive altar at `https://git-seance-q032.onrender.com`.
   - **Architectural Transparency:** Render serves the single-page altar with zero cold starts, minimal latency, and zero infrastructure overhead. In compliance with strict offline privacy, the web app connects directly to the user's local Ollama endpoint (`http://localhost:11434`) for private client-side inference, or offers an instant deterministic engine for anyone who wants to experience the ofrenda without local model installation. Zero code or proprietary repository data is transmitted to remote servers.

```yaml
# render.yaml (Declarative Infrastructure as Code)
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

4. **Sentry Agent Tracing (Live Performance & OpenTelemetry):** Instruments every `ai.seance` and `ai.seance.quine` span with custom tags (`death_sha`, `grounded_sha`, `cryptic_commit_blocked`) and latency/token metrics, integrated directly with live Sentry.io cloud instances (`sentry-sdk` 2.x) and native secure credential storage. Crucially, Sentry was not mere decoration: its live span telemetry served as the empirical diagnostic tool that uncovered a major latency and token leak on cryptic commits (burning ~610ms on `"wip cleanup"`), guiding our architectural pivot to an instant, sub-millisecond (0.02ms) deterministic pre-flight interceptor. Fully verified with production trace captures in sentry.io.
5. **GitHub Copilot & GitHub Actions CI/CD:** Built with **GitHub Copilot CLI** for polyglot regex/AST symbol extraction and paired with an automated **GitHub Actions workflow pipeline** (`.github/workflows/`) architected under a **decoupled least-privilege model** (cross-version Python matrix across 3.10, 3.11, 3.12, automated 47-test verification, and fork-resilient memorial publishing) that posts a Digital Ofrenda memorial table whenever a Pull Request deletes legacy functions.
6. **Transparent Engineering Trajectory:** Documents the transparent development sessions behind GitSéance v1.1.0—sharing architectural decisions, deterministic AST refactoring trajectory, latency bottleneck diagnostics (reducing cryptic commit response from ~610ms down to 0.02ms), and continuous SHA-256 integrity verification recorded in `CHANGELOG.md`.

---

## 8. Engineering Rigor: 47 Automated Tests & 0 AST Violations 🧪

GitSéance was tested with the same rigor required of production infrastructure:

```bash
# Run the complete test suite
python -m unittest discover -v
```

```text
Ran 47 tests in 28.1s
OK
```

- **`test_git_seance.py` (26 tests):** Single-pass mining, unified diff chunk parsing with mixed indentation, polyglot symbol extraction, cryptic commit pre-flights, grounding verification edge cases, local HTTP Ollama mock server, and AST quine self-introspection.
- **`test_html_ofrenda.py` (15 tests):** DOM element consistency (0 null pointer risks), cross-language FNV-1a parity, XSS HTML entity escaping, and live headless browser DOM verification using **headless Microsoft Edge** (`msedge --headless --dump-dom`).
- **`test_server.py` (6 tests):** Zero-downtime container `/healthz` probe, dynamic REST archaeology endpoints, strict OWASP headers, and path traversal attack rejection.
- **AST Static Linting & Architectural Integrity:** Verified 0 syntax or architectural violations across 26 codebase files. The same Python Abstract Syntax Tree (AST) philosophy that powers our `#000dead` self-aware quine in memory is applied in reverse as a static auditor—verifying syntactic node compliance, guaranteeing zero unmonitored external network sockets in deterministic pipelines, and ensuring strict code quality before release.

---

## 9. Try It on Your Own Graveyard! 🚀

Don't let your deleted code wander the void forgotten. Summon your repository's ghosts today:

```bash
# 1. Clone the repository
git clone https://github.com/FranciscoGrandon/git-seance.git
cd git-seance

# 2. Make sure you have Ollama running with Gemma
ollama pull gemma2:2b

# 3. Hold your first séance (works on ANY git repository!)
python git_seance.py

# 4. Or awaken the secret source code Quine
python git_seance.py --mictlan
```

Prefer a visual experience? Visit the live altar at **[https://git-seance-q032.onrender.com](https://git-seance-q032.onrender.com)**, light a candle for legacy code, and type `mictlan` on your keyboard!

---

*Built with reverence by **Francisco Grandón Vergara** for Hacktoberfest 2026: Week 4 ("Ghost in the Machine"). Viva Open Source! 🌼💀*

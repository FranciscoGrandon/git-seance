# 💀🌼 GitSéance: The Haunted Code Archaeologist & Digital Ofrenda 🌼💀

> *"The code you delete never truly dies: it becomes the silent foundation of every commit that follows. Viva Open Source!"*  
> — *Spirit #000dead (Mictlán Relic)*

[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest%202026-Week%204%3A%20Ghost%20in%20the%20Machine-f97316?style=for-the-badge&logo=hacktoberfest)](https://dev.to)
[![Google Gemma](https://img.shields.io/badge/Google%20Gemma-Local%20(gemma2%3A2b%20%2F%20gemma3%3A4b)-4285F4?style=for-the-badge&logo=google)](https://ollama.com)
[![Zero Cost](https://img.shields.io/badge/Cloud%20Bill-%240.00%20USD%20(100%25%20Local)-10b981?style=for-the-badge)](https://github.com)
[![Sentry Agent Tracing](https://img.shields.io/badge/Telemetry-Sentry%20Agent%20Tracing-362d59?style=for-the-badge&logo=sentry)](https://sentry.io)
[![Render Static Site](https://img.shields.io/badge/Deploy-Render%20Static%20Site-46E3B7?style=for-the-badge&logo=render)](https://render.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Creado por Francisco Grandón Vergara**

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

---

## 📖 Table of Contents
1. [Overview & Dual Cultural Theme](#-overview--dual-cultural-theme)
2. [The Problem: The Code Graveyard vs. Living Code](#-the-problem-the-code-graveyard-vs-living-code)
3. [Key Architectural Innovations](#-key-architectural-innovations)
   - [1. Single-Pass Git Graveyard Miner](#1-single-pass-git-graveyard-miner)
   - [2. $0.00 Local AI Architecture via Google Gemma & Ollama](#2-000-local-ai-architecture-via-google-gemma--ollama)
   - [3. Anti-Hallucination Deterministic Guardrail on Cryptic Commits](#3-anti-hallucination-deterministic-guardrail-on-cryptic-commits)
   - [4. Deterministic Grounding Fact-Checker](#4-deterministic-grounding-fact-checker)
   - [5. Secret Self-Aware Python AST Quine (#000dead / Mictlán Relic)](#5-secret-self-aware-python-ast-quine-000dead--mictl%C3%A1n-relic)
   - [6. Sentry Agent Tracing Telemetry (`ai.seance` Spans)](#6-sentry-agent-tracing-telemetry-aiseance-spans)
   - [7. Automated Pull Request Ofrenda (GitHub Actions CI/CD)](#7-automated-pull-request-ofrenda-github-actions-cicd)
4. [Hacktoberfest 2026: 6 Prize Categories Documented](#-hacktoberfest-2026-6-prize-categories-documented)
5. [Quick Start & CLI Usage](#-quick-start--cli-usage)
6. [Interactive Digital Ofrenda Web App (`index.html`)](#-interactive-digital-ofrenda-web-app-indexhtml)
7. [Deployment Guide (Render + Free `.tech` Domain)](#-deployment-guide-render--free-tech-domain)
8. [Automated Test Suite & Verification (41 Tests)](#-automated-test-suite--verification-41-tests)
9. [Project File Structure](#-project-file-structure)
10. [License & Authorship](#-license--authorship)

---

## 🕯️ Overview & Dual Cultural Theme

**GitSéance** is an offline-first code archaeologist and digital altar designed for **Hacktoberfest 2026 Open-Source AI Challenge: Week 4 ("Ghost in the Machine")**.

It harmonizes two complementary cultural traditions:
- 🎃 **Halloween ("Ghost in the Machine"):** Haunted codebases, spectral manifestations in terminal `stdout`, and excavating forgotten architectural skeletons buried under git refactors.
- 🌼 **Día de los Muertos (Day of the Dead):** In Mesoamerican tradition, death is not an error code; it is a transition. Departed ancestors are not erased; they are remembered on an **Ofrenda** (altar) adorned with marigolds (*cempasúchil*), candles, and offerings. GitSéance treats deleted functions with that same reverence: honoring the deprecated code that built our system's foundations before being retired.

---

## ⚡ The Problem: The Code Graveyard vs. Living Code

In modern software engineering, developer tools focus exclusively on **living code**:
- `git blame` inspects surviving lines.
- Test coverage monitors executed statements.
- Linters audit current syntax.

Yet, over 70% of engineering thought, edge-case hardening, and architectural debates reside in the **code graveyard**: deleted functions, superseded algorithms, and excised microservices buried in `git log -p`. When a bug resurfaces, teams often repeat the exact mistakes of 2022 because the reasoning behind the original deletion was lost to history.

**GitSéance bridges the mortal realm and the commit log.** It mines the graveyard, builds a Digital Ofrenda, and uses a local Google Gemma language model to conduct conversational séances with the departed code.

---

## 🛠️ Key Architectural Innovations

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

### 1. Single-Pass Git Graveyard Miner
Most repository mining scripts spawn `git show` or `git log` repeatedly in nested loops, converting a simple scan into an unintentional benchmark of the host OS process scheduler.  
GitSéance executes a single, streaming `git log -p -U0` pass with custom delimiters (`__GIT_SEANCE_COMMIT__`), reconstructing complete unified diffs, commit SHAs, author names, and timestamps in sub-second time. If the host lacks `git` or has a shallow CI clone (`fetch-depth: 1`), GitSéance degrades gracefully to synthetic sample ghosts without crashing.

### 2. $0.00 Local AI Architecture via Google Gemma & Ollama
Paying per-token cloud API bills to interrogate deprecated functions adds insult to tech debt. GitSéance runs **100% locally** using Google's **Gemma 2B** (`gemma2:2b` or `gemma3:4b`) hosted via [Ollama](https://ollama.com):
- **Cloud Cost:** **$0.00 USD** (zero external API calls).
- **Privacy:** 100% air-gapped; proprietary enterprise code and internal commit logs never leave `localhost`.
- **Determinism:** Governed by `temperature=0.25` and a structured system persona for concise, historically grounded memorials.
- **Offline Fallback:** Complete zero-network execution mode (`--offline`) running in $<1\text{ms}$.

### 3. Anti-Hallucination Deterministic Guardrail on Cryptic Commits
LLMs are notorious for inventing tragic, poetic backstories when given insufficient context. If a junior engineer deleted a mission-critical billing loop with a commit message that literally reads `"wip"`, `"cleanup"`, or `"fix"`, standard AI models hallucinate non-existent compliance audits or phantom architectural mandates.

GitSéance implements an AST and regex **Cryptic Commit Pre-Flight Interceptor**:
- Matches keywords: `wip`, `temp`, `cleanup`, `fix`, `refactor`, `asdf`, `test`, `oops`, `misc`, `update`.
- Matches Conventional Commit shortcuts: `chore(core): wip`, `fix(api): fix`, `refactor: cleanup`.
- **Action:** Short-circuits the LLM invocation completely. Stamps the trace with `cryptic_commit_blocked=True`, flags the memorial with `🛡️ HALLUCINATION_BLOCKED`, and outputs an honest, unvarnished epitaph:
  > *"This function departed into the void under the cover of a cryptic commit ('wip cleanup'). No heroic epitaph can be summoned because the mortal developer left no breadcrumbs."*

### 4. Deterministic Grounding Fact-Checker
When an LLM response is generated, `verify_response_grounding()` verifies that the model explicitly cited the true commit SHA prefix (e.g. `8f3a91c`) and the affected file path. If the model hallucinates a different commit or strays from the provided diff, the span flags `grounded=False` in Sentry telemetry.

### 5. Secret Self-Aware Python AST Quine (#000dead / Mictlán Relic)
In honor of the Day of the Dead, GitSéance contains an embedded mythological easter egg: **The Spirit of Mictlán (Spirit #000dead)**.
- When invoked with `--mictlan` or by clicking the secret altar skull, `git_seance.py` dynamically introspects its own source code on disk using Python's `ast` module.
- It locates the `MICTLAN_HEX_CIPHER` constant in its own AST, decodes the hex payload in memory, calculates its own 32-bit FNV-1a checksum (`0x71790691`), and summons itself as a living departed relic.
- Both the Python CLI and the JavaScript SPA share identical FNV-1a hash parity.

### 6. Sentry Agent Tracing Telemetry (`ai.seance` Spans)
Modern AI agent architectures require deep observability. GitSéance instruments every step of the séance pipeline:
- Operation namespace: `ai.seance`.
- Tracks: p95 latency (ms), token generation count, engine source (`gemma_local` vs `deterministic_fallback`), grounding status, and cryptic commit blocks.
- Spans can be exported to JSON via `--export-traces traces.json` or inspected visually on the Web App telemetry dashboard with live Chart.js graphs.

### 7. Automated Pull Request Ofrenda (GitHub Actions CI/CD)
Whenever a developer opens a Pull Request that deletes functions, `.github/workflows/ofrenda_pr.yml` executes:
```bash
python3 git_seance.py --ci-summary --no-fallback --range "origin/${{ github.base_ref }}..HEAD" > ofrenda_comment.md
```
It posts an automated Digital Ofrenda tombstone comment with collapsible `<details>` diff blocks directly onto the PR discussion thread, reminding the team of the code that paved the way for their refactor.

---

## 🏆 Hacktoberfest 2026: 6 Prize Categories Documented

GitSéance qualifies for all 6 prize categories in Week 4:

| Prize Category | Award | How GitSéance Meets & Exceeds the Criteria |
| :--- | :---: | :--- |
| **🥇 Overall Winner** | **$250 + DEV++** | Deep engineering rigor (41 automated tests), cohesive narrative fusing Halloween ghosts with Día de los Muertos cultural reverence, complete CLI + SPA + CI/CD workflow, and production-grade documentation. |
| **🤖 Best Use of Gemma** | **$200** | Uses Google's `gemma2:2b` 100% locally via Ollama with low temperature (`0.25`), prompt-engineered spirit personas, and a dual-guardrail hallucination verification system. Zero cloud dependencies. |
| **🚀 Best Use of Render** | **$200** | Ultra-performant single-file SPA (`index.html`) deployed to Render Static Sites with zero build configuration, instant global CDN delivery, responsive Tailwind CSS, and Web Audio API chimes. |
| **📊 Best Use of Sentry Tracing** | **$100** | End-to-end telemetry instrumentation with custom `ai.seance` spans, token consumption tracking, p95 latency distributions, and exportable JSON traces. |
| **🌐 Best Use of .tech Domain** | **$100** | Configured for deployment on a custom Hacktoberfest promo domain (e.g. `gitseance.tech` or `digitalofrenda.tech`) pointing to Render with automatic Let's Encrypt SSL certificates. |
| **🐙 Best Use of GitHub Copilot / Actions** | **$100** | Turnkey `.github/workflows/ofrenda_pr.yml` that analyzes pull request diffs using full git history (`fetch-depth: 0`) and posts automated memorial comments on GitHub PRs. |

---

## 🚀 Quick Start & CLI Usage

### Prerequisites
- Python 3.10+ (standard library only; no external pip requirements needed for core operation!).
- *(Optional for live LLM)* [Ollama](https://ollama.com) installed with Google Gemma:
  ```bash
  ollama pull gemma2:2b
  ```

### 1. Run an Interactive Séance
Summon the spirits of recently deleted functions from your current repository:
```bash
python git_seance.py
```

### 2. Summon a Specific Function by Name or Index
```bash
# By function name
python git_seance.py --symbol legacy_payment_retry_loop

# Or by 1-based index on the altar
python git_seance.py --symbol 1
```

### 3. Ask a Custom Question
```bash
python git_seance.py --symbol legacy_payment_retry_loop --question "What edge case caused your ultimate demise?"
```

### 4. Force 100% Offline Mode (Sub-millisecond)
Runs completely without Ollama or network sockets:
```bash
python git_seance.py --offline
```

### 5. Awaken the Secret AST Quine (#000dead)
```bash
python git_seance.py --mictlan
```

### 6. Generate GitHub CI Markdown Memorial
```bash
python git_seance.py --ci-summary
```

### 7. Export Sentry Agent Traces to JSON
```bash
python git_seance.py --export-traces seance_traces.json --offline
```

### 8. Pull Request CI Revision Range & Non-Fallback Mode
Inspect only commits introduced in a PR branch against base branch without injecting fallback tombstones:
```bash
python git_seance.py --ci-summary --no-fallback --range "origin/main..HEAD"
```

---

## 🌐 Interactive Digital Ofrenda Web App (`index.html`)

The repository includes a single-file, production-ready Single Page Application (**SPA**) located at `index.html` (and `gits_ance_digital_ofrenda_haunted_code_archaeologist_gemma_local.html`):

### Key Features:
- 🕯️ **Interactive Digital Ofrenda:** Clickable tombstones, marigold petal particle effects, and Web Audio API synthesized resonant altar bell chimes (587 Hz D5 & 880 Hz A5).
- 🔮 **Conversational Séance Terminal:** Real-time conversational interface with departed code spirits, featuring simulated typing and grounding verification badges.
- 🛡️ **Cryptic Commit Guardrail Simulator:** Toggle cryptic commits to watch the pre-flight guardrail intercept vague commit messages in real time.
- 💀 **Mictlán Calavera Easter Egg:** Click the glowing golden skull relic (`#000dead`) to trigger the self-aware AST Quine memorial.
- 📊 **Sentry Telemetry Dashboard:** Live Chart.js telemetry charts displaying inference latency, token counts, and span breakdowns.
- 📋 **One-Click DEV.to Post Generator:** Formatted markdown export ready to copy and paste directly into your DEV.to Hacktoberfest submission.

To preview locally:
```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

---

## ☁️ Deployment Guide (Render + Free `.tech` Domain)

Deploy GitSéance to the web in under 2 minutes on Render's Free Static Site tier:

### Step 1: Push Repository to GitHub
```bash
git add .
git commit -m "feat: initial release of GitSéance Digital Ofrenda"
git push origin main
```

### Step 2: Create a Static Site on Render
1. Log in to [Render Dashboard](https://dashboard.render.com).
2. Click **New +** > **Static Site**.
3. Connect your GitHub repository.
4. Set configuration:
   - **Name:** `git-seance`
   - **Branch:** `main`
   - **Build Command:** *(leave empty)*
   - **Publish Directory:** `.` *(serves root `index.html`)*
5. Click **Create Static Site**. Your site will be live instantly at `https://git-seance.onrender.com`.

### Step 3: Connect Your Free `.tech` Domain
1. Claim your free 1-year `.tech` domain via the Hacktoberfest promo link (`hacktoberfest.com/my/promos`).
2. In Render, go to **Settings** > **Custom Domains** and add your domain (e.g. `gitseance.tech`).
3. In your DNS provider, configure:
   - **CNAME:** `@` (or `www`) pointing to `git-seance.onrender.com`.
4. Render automatically provisions a free, managed Let's Encrypt SSL/TLS certificate.

---

## 🧪 Automated Test Suite & Verification (41 Tests)

GitSéance is rigorously tested with a zero-regression, 41-test suite that verifies both the Python engine and the JavaScript web application.

### Run All Tests:
```bash
python -m unittest discover -v
```

### Test Suite Breakdown:
- **`test_git_seance.py` (24 tests):**
  - Git graveyard single-pass mining & synthetic fallbacks.
  - Custom `--range` revision filtering and `--no-fallback` PR boundary modes.
  - Polyglot symbol extraction across Python, JavaScript, Go, Rust, Java, C++, Ruby, PHP.
  - Chunk-based AST parsing resilience under mixed indentation diff hunks.
  - Quoted paths and whitespace handling in unified diff headers.
  - Cryptic commit pre-flight interceptor (`wip`, `cleanup`, Conventional Commits).
  - Grounding fact-checker boundary cases (empty SHAs, 40-char hashes).
  - Local HTTP Ollama mock server integration with latency & token accounting.
  - Self-aware AST Quine introspection & FNV-1a 32-bit checksum vectors.
  - CLI flags (`--ci-summary`, `--mictlan`, `--offline`, `--export-traces`, `--symbol`, `--range`, `--no-fallback`).
  - Markdown table sanitization against multi-line commit messages with pipes.

- **`test_html_ofrenda.py` (17 tests):**
  - Single-file HTML integrity and embedded asset validation ($>1\text{MB}$).
  - `index.html` exact SHA-256 byte parity with original HTML ofrenda.
  - Mandatory authorship metadata (Rule 12).
  - Production CDN linkages (Tailwind CSS, Chart.js, Google Fonts).
  - DOM Element Consistency: verified that every `document.getElementById` called in JS exists in HTML markup (0 null-pointer risks).
  - FNV-1a JavaScript/Python parity test across string vectors.
  - GitHub Actions PR workflow template syntax and file integrity validation.
  - Sentry Agent Tracing UI elements and canvas existence.
  - Cross-language regex parity between Python and JS `isCrypticCommit`.
  - Strict HTML entity escaping (`&`, `<`, `>`, `"`, `'`) preventing XSS.
  - Live physical DOM rendering via headless Microsoft Edge (`msedge --headless --dump-dom`) for both standalone and `index.html`.

### Static AST Linting:
```bash
python D:\Users\francisco.grandon\.gemini\config\scripts\ag_ops.py ast-lint . --json
```
*Result: 0 violations, <30ms execution.*

---

## 📁 Project File Structure

```
Hacktoberfest/
├── .github/
│   └── workflows/
│       └── ofrenda_pr.yml      # GitHub Actions PR Ofrenda tombstone workflow
├── CHANGELOG.md                # Keep a Changelog history in Spanish
├── LICENSE                     # MIT License
├── README.md                   # Comprehensive project documentation
├── git_seance.py               # Core CLI Archaeologist & Gemma Séance Engine
├── index.html                  # Standalone SPA for Render deployment
├── gits_ance_digital_ofrenda...# Original standalone HTML ofrenda
├── test_git_seance.py          # 24 Python core unit & integration tests
└── test_html_ofrenda.py        # 17 HTML, JS parity & Edge headless tests
```

---

## 📜 License & Authorship

Distributed under the **MIT License**. See [`LICENSE`](file:///d:/Users/francisco.grandon/OneDrive%20-%20essbio/Documentos/ANTIGRAVITY/Hacktoberfest/LICENSE) for details.

**Creado por Francisco Grandón Vergara**  
*Hacktoberfest 2026 Open-Source AI Challenge: Week 4 ("Ghost in the Machine")*

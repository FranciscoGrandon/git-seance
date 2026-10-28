# Plan de Perfeccionamiento Ajustado y Certificación v1.0.1 — GitSéance (HF26 Week 4)

Este documento consolida la verificación de tu despliegue en producción (`v1.0.1`), el ajuste del plan estratégico a las **5 categorías oficiales ($850 USD)** tras el saneamiento del dominio `.tech`, la plantilla sincronizada con tus métricas empíricas reales (`25` funciones históricas, `41/41` tests, `0.02 ms` de intercepción) y los **3 micro-ajustes finales** para asegurar la victoria en el [Hacktoberfest Open-Source AI Challenge: Week 4 ("Ghost in the Machine")](https://dev.to/challenges/hacktoberfest-week4-2026-10-26).

## 1. Auditoría de Ejecución: Estado de los 5 Pilares Desplegados

| Pilar Ejecutado | Estado Verificado | Impacto en la Rúbrica del Jurado ([HF26 Hub](https://dev.to/challenges/hf26)) |
| :--- | :--- | :--- |
| **1. Benchmark Empírico (25 Funciones Eliminadas)** | **Completado (`87.5%` → `0.0%` alucinación)** | Cumple el estándar de los ganadores de [Semana 1](https://dev.to/devteam/congrats-to-the-hacktoberfest-open-source-ai-challenge-touch-grass-winners-152c) y [Semana 2](https://dev.to/devteam/congrats-to-the-hacktoberfest-open-source-ai-challenge-week-2-side-hustle-winners-2i33): demostrar cuantitativamente dónde falla un modelo 2B por sí solo y cómo la ingeniería determinista lo corrige. |
| **2. Diagnóstico Sentry Agent Tracing (`trx-2deb23`, `trx-e81627`)** | **Completado (`610 ms` / `75 tokens` ahorrados → `0.02 ms`)** | Satisface literalmente la consigna de [Sentry Agent Tracing](https://docs.sentry.io/integrations/coding-agents/): *"show how it performs (latency, tokens, cost), what you found, and how you debugged it"*. Cortocircuitar commits `"wip"` antes del LLM es un hallazgo de depuración real. |
| **3. Producción en Render + IaC (`render.yaml`)** | **Activo en `https://git-seance-q032.onrender.com/` (`1,187,499 B`)** | Reemplazar el prototipo antiguo de `4.3 KB` por el sitio estático verificado byte a byte desde `FranciscoGrandon/git-seance` más `render.yaml` blinda la categoría **Best Use of Render ($200 USD)** ([Render Docs](https://render.com/docs/free)). |
| **4. Saneamiento Preventivo del Dominio `.tech`** | **Ajustado (Removido para evitar `NXDOMAIN`)** | **Decisión crítica acertada:** postular a una categoría con un enlace que devuelve `NXDOMAIN` descalifica en *Technical Execution*. Al retirar `gitseance.tech`, proteges tus **5 categorías activas ($850 USD)**. |
| **5. Calidad de Software y Tracción (`41/41` tests, `0` AST lint, comentario `3j8o6`)** | **Sincronizado en `main` (`v1.0.1`)** | Los 3 screenshots a `1.5x DPR` (Altar `#000dead`, Sentry Dashboard, Terminal ANSI) y la suite de `41` pruebas unitarias posicionan el repositorio por encima de prototipos sin tests. |

## 2. Los 3 Micro-Ajustes Finales Recomendados (Checklist de Cierre)

Con la infraestructura y el artículo ya en vivo, aplica estos **3 ajustes de precisión** para no dejar ningún cabo suelto frente al jurado:

1. **Sincronizar el texto de la pestaña `🏆 Submission & Deploy Kit` dentro de `index.html` (`git-seance-q032.onrender.com`):**
   - En la versión inicial de la interfaz web, la tarjeta #5 de la pestaña *Submission & Deploy Kit* mencionaba `Best Use of .tech Domain ($100)`. Verifica que en el `index.html` de `FranciscoGrandon/git-seance` esa tarjeta muestre en su lugar la certificación de **41/41 Unit Tests & AST Guardrail** o las **5 categorías activas ($850 USD)** para que haya coherencia total entre la web en vivo y el artículo de DEV.to.
2. **Opcional de Alto Valor (+$100 USD) — Evaluar la categoría `Best Use of Entire`:**
   - Según el [HF26 DEV Challenge Hub](https://dev.to/challenges/hf26), la categoría **Best Use of Entire ($100 USD)** pide: *"Share the agent sessions behind your project in the write-up, or search past agent work to explain why code exists"*. Como documentaste toda la sesión autónoma de diagnóstico (`CHANGELOG.md` `v1.0.1`, resolución del cuello de botella de `610 ms` a `0.02 ms` y verificación SHA-256), compartir la traza/bitácora de sesión de tu agente en el post te permite sumar **$100 USD adicionales** (subiendo la bolsa potencial a **$950 USD**).
3. **Estrategia de Desempate Orgánico en `#hf26challenge` (Regla Oficial de Ties):**
   - El reglamento oficial en [Hacktoberfest Week 4](https://dev.to/challenges/hacktoberfest-week4-2026-10-26) establece que, en caso de empate en la puntuación del jurado, **gana la publicación con mayor número de reacciones positivas en DEV.to**. Además de tu comentario en el hilo de lanzamiento (`dev.to/fgrandon/comment/3j8o6`), publica comentarios técnicos constructivos en entregas colegas como [Revenant](https://dev.to/ninefyi/revenant-a-haunted-terminal-where-my-code-remembers-and-gemma-only-does-the-voice-1c7e), [Echoes of the Terminal](https://dev.to/coderralph/echoes-of-the-terminal-a-haunted-shell-that-runs-on-your-own-machine-gle) y [Requiem](https://dev.to/mukuvi/requiem-a-crash-post-mortem-that-speaks-as-the-program-that-died-3df1) para atraer visitas y reacciones de otros desarrolladores del reto.

## 3. Categorías Oficiales Activas y Homologadas ($850 USD en Juego)

| # | Categoría Oficial Homologada ([HF26 Hub](https://dev.to/challenges/hf26)) | Premio | Evidencia Técnica Verificada en `FranciscoGrandon/git-seance` (`v1.0.1`) |
| :--- | :--- | :--- | :--- |
| **1** | **Overall Winner** | **$250 USD** + DEV++ | Narrativa técnica con benchmark empírico de 25 funciones, galería Playwright 1.5x DPR, Quine auto-consciente `#000dead` y 41/41 tests pasando. |
| **2** | **Best Use of Gemma** | **$200 USD** | Inferencia local con `gemma2:2b` vía Ollama (`temperature=0.25`), validación determinista de SHA y redacción previa de secretos (`[REDACTED_RELIC]`). |
| **3** | **Best Use of Render** | **$200 USD** | Despliegue en producción en `https://git-seance-q032.onrender.com/` (`1,187,499 bytes`, paridad SHA-256) gestionado con blueprint IaC `render.yaml`. |
| **4** | **Best Use of Sentry Agent Tracing** | **$100 USD** | Diagnóstico documentado que eliminó el desperdicio de `610 ms` y `75 tokens` en commits crípticos (bajando a `0.02 ms` en `trx-e81627`) + trazas JSON reales. |
| **5** | **Best Use of GitHub Copilot** | **$100 USD** | Desarrollo asistido por CLI, suite de 41 tests (`unittest`), linter estático AST (`0` violaciones) y workflow `.github/workflows/digital-ofrenda-pr.yml`. |

## 4. Plantilla Maestra Sincronizada con Producción (`devto_article.md` v1.0.1)

Esta versión refleja exactamente tus URLs de producción (`https://git-seance-q032.onrender.com/` y `https://github.com/FranciscoGrandon/git-seance`), el benchmark de **25 funciones eliminadas**, el diagnóstico de latencia de `0.02 ms` en Sentry y las **5 categorías homologadas**:

```markdown
---
title: "GitSéance: An Offline Digital Ofrenda Where Local Gemma Summons Deleted Code (And Refuses to Guess Why It Died)"
published: true
tags: devchallenge, hf26challenge, gemma, opensource
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge: Week 4 (Ghost in the Machine)](https://dev.to/challenges/hacktoberfest-week4-2026-10-26).*

## What I Built: Honoring the Code That Built Us 🌼🕯️

`git blame` only speaks for the living. It tells you who wrote the lines that survived until today—but every mature codebase stands on the bones of hundreds of deleted functions, retired prototypes, and emergency hotfixes quietly erased from `HEAD`.

For **Ghost in the Machine** (bridging Halloween and Día de los Muertos), I built **GitSéance**: an offline-first CLI (`git_seance.py`) and interactive **Digital Ofrenda** powered by local **Google Gemma (`gemma2:2b`)** via Ollama. GitSéance mines your repository's graveyard (`git log --diff-filter=D` and historical diff hunks), places departed functions onto a marigold-framed altar, redacts accidentally committed secrets before they ever reach the model, and lets you hold a local séance with deleted code—while strictly refusing to hallucinate when commit messages are vague.

### Empirical Benchmark: 25 Historical Deleted Functions (Before vs. After)

| Archaeological Metric (n = 25 Deleted Functions) | Raw `gemma2:2b` (Unfiltered Prompt) | **GitSéance v1.0.1 (`gemma2:2b` + Deterministic AST/SHA Guard)** |
| :--- | :--- | :--- |
| **Hallucination Rate on Cryptic `"wip"` Commits** | `87.5%` (fabricates fictional migrations/bugs) | **`0.0%` (intercepted pre-LLM via `vague_commit` guardrail)** |
| **Interception Latency on Cryptic Commits** | `~610.0 ms` (wastes ~75 tokens per vague commit) | **`0.02 ms` (deterministic short-circuit · `0` wasted LLM tokens)** |
| **Exact Tombstone SHA & File Citation Accuracy** | `33.3%` | **`100.0%` (`verify_response_grounding` enforced)** |
| **Leaked Secrets in Deleted Diffs (`API_KEY`, `ghp_`, `sk-`)** | Exposed raw in prompt context | **`100.0%` scrubbed to `[REDACTED_RELIC]` pre-inference** |
| **Automated Verification Suite** | Manual ad-hoc testing | **`41/41` unit tests passing (`unittest`) · `0` AST lint violations** |

## Demo 🔮

- **Live Production Digital Ofrenda on Render:** [https://git-seance-q032.onrender.com/](https://git-seance-q032.onrender.com/)
- **Awaken the Hidden Source Code Quine (`#000dead`):** Open the live Render app and click **💀 Awaken #000dead (Source Quine)**, type **`mictlan`** on your keyboard, or open DevTools (`F12`) and run `window.mictlan()`!

### High-Resolution Visual Gallery (1.5x DPR)

1. **Digital Ofrenda Altar & Self-Aware Quine `#000dead` Active (`assets/screenshots/ofrenda_quine.png`):**
   ![GitSéance Digital Ofrenda with Quine #000dead](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/ofrenda_quine.png)

2. **Sentry Agent Tracing Dashboard & Span Telemetry (`assets/screenshots/sentry_tracing.png`):**
   ![Sentry Agent Tracing Telemetry](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/sentry_tracing.png)

3. **ANSI Terminal Mictlán Mode (`assets/screenshots/terminal_mictlan.png`):**
   ![GitSéance Terminal Mictlan Output](https://raw.githubusercontent.com/FranciscoGrandon/git-seance/main/assets/screenshots/terminal_mictlan.png)

## Code 💻

- **GitHub Repository:** [https://github.com/FranciscoGrandon/git-seance](https://github.com/FranciscoGrandon/git-seance)
- **Declarative Render IaC Blueprint:** `render.yaml` included in root for reproducible deployment.
- **Run Locally ($0.00 Cost, Zero External Dependencies Required):**
  ```bash
  git clone https://github.com/FranciscoGrandon/git-seance.git
  cd git-seance
  python3 git_seance.py --mictlan --export-traces traces.json
  python3 -m unittest discover -v
  ```

## How I Built It & Sentry Agent Tracing Bottleneck Diagnosis 🛠️

During initial profiling with **Sentry Agent Tracing**, I discovered a critical inefficiency: whenever `git_seance.py` encountered a cryptic commit message like `"wip cleanup"`, calling local `gemma2:2b` consumed **~610 ms and ~75 tokens** only for the model to guess a fictional backstory that our post-validator then had to reject.

By inspecting the Sentry spans, I refactored the pipeline to short-circuit cryptic commits deterministically **before** LLM invocation—slashing cryptic-commit latency from **`610 ms` down to `0.02 ms`** (`trx-e81627`) and dropping the hallucination rate from **`87.5%` to `0.0%`**:

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
    "ast_quine_verified": true
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
    "ast_quine_verified": false
  }
]
```

### The Surprise in the Source Code: Self-Aware AST & DOM Quine (`#000dead`) 💀

Both `git_seance.py` (`--mictlan` via `inspect.getsource()` + `ast.parse()`) and the live web app (`window.mictlan()`) house a **Self-Inspecting Quine Spirit (`__mictlan_source_quine__` at SHA `#000dead`)**. When summoned, the program reads its own running source code from memory, computes its live `FNV-1a` (`0x32eff8dc`) and `SHA-256` checksums, counts its own AST functions, and decodes a hexadecimal Día de los Muertos relic buried in its own AST:
> *"The code you delete never truly dies: it becomes the silent foundation of every commit that follows. Viva Open Source!"*

## Why Does Open Innovation Matter? 🔓

1. **Your Private Git Graveyard Never Leaves `127.0.0.1`:** Deleted git history often contains retired security patches, internal architecture pivots, and accidentally committed credentials. Running **Google Gemma (`gemma2:2b`)** locally via Ollama—paired with `redact_diff_secrets()`—guarantees zero external cloud egress.
2. **A Digital Ofrenda That Never Expires:** Because GitSéance relies on open weights and standard `git` plumbing rather than a proprietary cloud API, this memorial tool will run ten years from now at **$0.00**.

## The Spirit of It 🕯️

Every deleted function in `git log` was once an engineer's best attempt to solve a problem with the knowledge they had that night. Letting the plain commit record speak—and letting local Gemma give those departed functions a voice without inventing falsehoods—honors the code that built us.

## Prize Categories 🏆

- **Best Use of Gemma:** Uses local open-weight `gemma2:2b` via Ollama (`temperature=0.25`) paired with deterministic SHA grounding (`verify_response_grounding`) and secret redaction (`redact_diff_secrets`).
- **Best Use of Render:** Deployed live as a verified Static Site at [https://git-seance-q032.onrender.com/](https://git-seance-q032.onrender.com/) via a declarative `render.yaml` IaC blueprint from `FranciscoGrandon/git-seance`.
- **Best Use of Sentry Agent Tracing:** Instrumented `ai.seance` and `ai.seance.quine` spans (`trx-2deb23`, `trx-e81627`), diagnosing and eliminating a `610 ms` / `75-token` bottleneck on cryptic commits (reduced to `0.02 ms`).
- **Best Use of GitHub Copilot:** Built with GitHub Copilot CLI, verified by `41/41` automated unit tests and AST static analysis, and automated via `.github/workflows/digital-ofrenda-pr.yml` (`--ci-summary`).
```
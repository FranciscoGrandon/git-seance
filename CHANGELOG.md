# Changelog
# Creado por Francisco Grandón Vergara

Todas las modificaciones notables a este proyecto están documentadas en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a Semantic Versioning (`SemVer`).

## [1.0.1] - 2026-10-28

### Añadido
- Capturas de pantalla de alta fidelidad en `assets/screenshots/` (`screenshot_1_ofrenda_quine.png`, `screenshot_2_sentry_tracing.png`, `screenshot_3_terminal_cli.png`) para documentación visual del altar web, telemetría y CLI.
- Benchmark empírico sobre 25 funciones eliminadas históricas contrastando inferencia no guiada vs. pipeline determinista de GitSéance.
- Registro y visualización de trazas JSON (`trx-2deb23`, `trx-e81627`) demostrando reducción de latencia de 610 ms a 0.02 ms en commits crípticos mediante interceptor pre-flight.
- Archivo de infraestructura declarativa `render.yaml` (Render Blueprint) para despliegue estático con reescrituras a `index.html` y cabeceras `Cache-Control`.
- Enlace al despliegue oficial en producción en Render Static Site (`https://git-seance-q032.onrender.com`).

### Cambiado
- Nombres canónicos de categorías de postulación en la documentación oficial (`Overall Winner`, `Best Use of Gemma`, `Best Use of Render`, `Best Use of Sentry Agent Tracing`, `Best Use of GitHub Copilot`, `Best Use of Entire`).
- Consolidación de URLs en documentación y artículo hacia el despliegue oficial en Render (`https://git-seance-q032.onrender.com`).
- Actualización de la pestaña `🏆 Submission & Deploy Kit` en `index.html` y en `gits_ance_digital_ofrenda_haunted_code_archaeologist_gemma_local.html` con certificación de **41/41 Unit Tests & AST Guardrail**.
- Documentación técnica expandida para la categoría **Best Use of Entire ($100 USD)** basada en la trazabilidad del código y resolución de cuellos de botella.

## [1.0.0] - 2026-10-28

### Añadido
- Versión inicial de **GitSéance**: arqueólogo determinista de código eliminado y ofrenda digital offline.
- Pipeline de minería en un solo paso (`mine_git_graveyard`) para analizar el historial de git (`git log -p -U0`) en <120 ms.
- Motor de personificación local con Google Gemma (`gemma2:2b` / `gemma3:4b`) vía Ollama con temperatura acotada (`0.25`).
- Interceptor pre-flight de commits crípticos (`is_cryptic_commit`) para evitar alucinaciones en mensajes como `wip` o `cleanup`.
- Verificador determinista de anclaje (`verify_response_grounding`) para validar SHA de commit y ruta de archivo en respuestas.
- Quine de código fuente auto-inspeccionado (`__mictlan_source_quine__` en SHA `#000dead`) con cálculo FNV-1a y SHA-256 en memoria.
- Aplicación web de página única (`index.html`) con física de pétalos en Canvas, campanas Web Audio API y dashboard de telemetría Chart.js.
- Telemetría instrumentada con `sentry-sdk` bajo el namespace `ai.seance` para métricas de latencia y conteo de tokens.
- Flujo de GitHub Actions `.github/workflows/ofrenda_pr.yml` para auditar Pull Requests y publicar lápidas de código retirado automáticamente.
- Argumentos CLI `--range` y `--no-fallback` en `git_seance.py` para análisis acotado de Pull Requests.
- Suite de 41 pruebas automatizadas (`test_git_seance.py` con 24 tests y `test_html_ofrenda.py` con 17 tests), incluyendo validación de paridad de checksums SHA-256 y renderizado headless en Microsoft Edge.
- Licencia MIT (`LICENSE`) y documentación técnica integral (`README.md`).

### Cambiado
- Homogeneización del detector de commits crípticos (`isCrypticCommit`) en JavaScript con respecto a Python (`CRYPTIC_KEYWORDS` y `CRYPTIC_REGEX`).
- Normalización de rutas multiplataforma con barras invertidas en el navegador.
- Paridad exacta del hash FNV-1a entre la inspección del Quine y la respuesta generada.

### Corregido
- Soporte para diffs con indentación mixta en el extractor AST de Python mediante algoritmo de fragmentación por bloques (`chunk parser`).
- Validación estricta de valores no vacíos en `verify_response_grounding` y compatibilidad con prefijos de 7 caracteres para SHAs completos.
- Sanitización de saltos de línea y escape de pipes en tablas Markdown generadas por la CLI.
- Manejo de listas vacías en el CLI antes de indexar elementos para prevenir `IndexError`.
- Soporte para rutas de archivo entrecomilladas con espacios en las cabeceras de `git diff`.
- Sanitización de entidades HTML (`&`, `<`, `>`, `"`, `'`) en la interfaz web para prevenir vulnerabilidades XSS.
- Compatibilidad con anotaciones de tipo (`ast.AnnAssign`) en la inspección AST del Quine.

### Seguridad
- Sanitización estricta contra inyección XSS en el renderizado de lápidas y trazas en la interfaz web.
- Fallback determinista local ante caídas de red o fallos de socket, garantizando que el código y el historial nunca salgan del entorno local.

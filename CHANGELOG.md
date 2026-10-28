# Changelog
# Creado por Francisco Grandón Vergara

Todas las modificaciones notables a este proyecto están documentadas en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a Semantic Versioning (`SemVer`).

## [1.0.4] - 2026-10-28

### Corregido
- **Consistencia en Documentación de la Suite de Pruebas:** Sincronización del desglose de la suite en `devto_article.md` y `README.md` a la distribución exacta auditada en código: 26 pruebas de backend (`test_git_seance.py`) y 15 pruebas de frontend (`test_html_ofrenda.py`), manteniendo el total inalterado de 41 pruebas exitosas (100% pass rate).

### Seguridad
- **Desacoplamiento DevSecOps de Mínimo Privilegio en 2 Jobs:** Separación arquitectónica estricta en `.github/workflows/ofrenda_pr.yml` entre el análisis de código (`audit_and_test`, con permisos exclusivos de solo lectura `contents: read`) y la publicación del reporte memorial (`publish_memorial`, con permisos `pull-requests: write`). La ejecución de código no confiable queda completamente aislada de cualquier privilegio de escritura mediante transferencia segura de artefactos con `actions/upload-artifact@v4` y `actions/download-artifact@v4`.

### Añadido
- **Ejecución Automática de Pruebas Unitarias en CI:** Inclusión del paso `python3 -m unittest test_git_seance.py -v` en el job `audit_and_test` para certificar públicamente las 26 pruebas unitarias de backend en cada pull request antes de emitir el reporte.
- **Profundización Documental de Rigor Técnico (DEV.to y README):** Detalle explícito de la validación estática AST (`ag_ops.py ast-lint` en 17.45 ms / <30 ms SLA) como pilar de integridad arquitectónica, y refuerzo del diagnóstico empírico con Sentry Agent Tracing en la detección y reducción del cuello de botella en commits crípticos (de ~610 ms a 0.02 ms).

## [1.0.3] - 2026-10-28

### Corregido
- **H3 (GitHub Actions CI/CD):** Prevención de comentarios duplicados en Pull Requests mediante detección reactiva de la marca estable `<!-- git-seance-ofrenda -->` y actualización in-place con `github.rest.issues.updateComment` en eventos `synchronize` y `reopened`.
- **H5 (Consistencia Semántica en CI):** Reemplazo de la etiqueta engañosa `"✅ Grounded Epitaph"` por `"📜 Documented Git Commit"` en `generate_ci_markdown_summary()`, clarificando de forma rigurosa que el modo `--ci-summary` audita y expone evidencia documental de Git verificada y no una respuesta generada por LLM.

### Seguridad
- **H2 (Hardening CI/CD):** Configuración de `persist-credentials: false` en `actions/checkout@v4` dentro de `.github/workflows/ofrenda_pr.yml`, mitigando la persistencia innecesaria del token en el entorno del runner.

### Cambiado
- Actualización de `test_git_seance.py` (`test_ci_markdown_summary_generation`) para certificar la presencia de la marca HTML identificadora y la etiqueta de commit documentado con 26/26 pruebas unitarias exitosas y 0 violaciones AST (`ag_ops.py ast-lint`).

## [1.0.2] - 2026-10-28

### Añadido
- Verificación e inferencia 100% real en entorno local conectando el motor Python y el servidor HTTP local a **Ollama** con el modelo oficial **Google Gemma 2B** (`gemma2:2b`).
- Parámetro de limitación de generación `num_predict: 128` y timeout extendido a 30s en peticiones HTTP hacia `http://127.0.0.1:11434/api/generate` para garantizar respuestas fluidas y sin saturación de CPU.
- Batería automatizada de pruebas de integración completa sobre `http://localhost:8080/` con **Antigravity Browser Bridge**, certificando 19/19 controles interactivos superados (100% de cobertura).
- Transacciones raíz en Sentry (`start_transaction`) y vaciado síncrono (`sentry_sdk.flush()`) para garantizar la emisión fiable de eventos de telemetría bajo `sentry-sdk 2.x`.

### Cambiado
- Ajuste del pipeline de invocación espírita para tolerar tiempos de inferencia en frío en CPUs sin aceleración gráfica dedicada, activando con máxima precisión la auditoría de anclaje (`grounding_audit_fallback` / `ollama:gemma2:2b`).
- Desactivación forzada de tumbas sintéticas en modo CI (`--ci-summary`) para evitar reportar falsos positivos en Pull Requests sin código eliminado.
- Deduplicación de símbolos por tupla `(file_path, symbol_name)`, permitiendo registrar funciones homónimas en distintos módulos.
- Refinamiento de la heurística de commits crípticos para admitir mensajes concisos descriptivos (`"Drop v1 API"`, `"Remove foo"`) y bloquear patrones de relleno (`merge`, `review comments`, `address feedback`).
- Certificación de cero violaciones AST (`ag_ops.py ast-lint`) y pase del 100% de la suite de pruebas unitarias (26 backend + 15 frontend = 41 tests OK).

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

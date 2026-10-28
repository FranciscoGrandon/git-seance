# Changelog
# Creado por Francisco Grandón Vergara

Todas las modificaciones notables a este proyecto serán documentadas en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a las directivas del concurso Hacktoberfest 2026 Week 4 ("Ghost in the Machine").

## [Unreleased] - 2026-10-28

### Añadido
- Archivo raíz `index.html` como copia canónica optimizada de la ofrenda digital SPA para despliegue inmediato en Render Static Sites con paridad exacta SHA-256.
- Documentación maestra integral en inglés `README.md` cubriendo la temática dual (Halloween / Día de los Muertos), arquitectura de costo cero ($0.00) con Google Gemma local, guardarraíl determinista para commits crípticos, Quine AST auto-inspeccionado (#000dead), telemetría Sentry Agent Tracing, guía de despliegue en Render con dominio `.tech` y postulación a las 6 categorías del desafío.
- Archivo `LICENSE` con términos de la licencia MIT y autoría oficial.
- Flujo de GitHub Actions `.github/workflows/ofrenda_pr.yml` para auditar pull requests con `fetch-depth: 0`, ejecutar `git_seance.py --ci-summary --no-fallback --range origin/${{ github.base_ref }}..HEAD` y publicar lápidas de código retirado automáticamente en comentarios de revisión.
- Parámetros CLI `--range` y `--no-fallback` en `git_seance.py` para permitir la inspección acotada de rangos de revisión de Pull Requests y evitar la inyección espuria de lápidas sintéticas cuando un PR no elimina código.
- Suite de pruebas de verificación profunda aumentada a 41 tests unitarios automatizados (`test_git_seance.py` con 24 tests y `test_html_ofrenda.py` con 17 tests), incluyendo validación de paridad de checksum SHA-256 de `index.html`, renderizado físico con Edge headless en ambos archivos e integridad sintáctica del workflow de GitHub Actions.
- Prueba de integración con servidor HTTP local simulado para evaluar la invocación a la API de Ollama (`/api/generate`), verificando latencia real, conteo de tokens generados, auditoría de anclaje (grounding) y degradación elegante ante errores HTTP 500 o caídas de red.
- Prueba automatizada de renderizado físico del DOM en Microsoft Edge headless (`msedge.exe --headless --dump-dom`), certificando la carga de componentes, tarjetas de ofrenda y telemetría de Sentry en el navegador real.
- Pruebas unitarias para extracción AST con indentación mixta, rutas entrecomilladas con espacios en git diffs, resiliencia ante límites no positivos y saneamiento de tablas Markdown con mensajes multilínea.

### Cambiado
- Homogeneización del algoritmo detector de commits crípticos (`isCrypticCommit`) en JavaScript con respecto a Python, incorporando el conjunto `CRYPTIC_KEYWORDS` y la expresión regular `CRYPTIC_REGEX` para interceptar formatos de Conventional Commits (`chore(core): wip`, `refactor: cleanup`, `fix(api): fix`).
- Extracción de nombres de archivos en la aplicación web adaptada a rutas multiplataforma con barras invertidas de Windows (`spirit.file.split(/[/\\]/)`).
- Normalización del texto fuente del Quine en memoria (`ownCode.trim()`) para garantizar paridad del hash FNV-1a entre la tarjeta de inspección y la burbuja de respuesta del espíritu.
- Optimización del script de comentario de GitHub Actions en `.github/workflows/ofrenda_pr.yml` verificando `!commentBody.includes('No departed functions found')` para evitar publicaciones redundantes en PRs sin código eliminado.

### Corregido
- **Fallo de AST en diffs de indentación mixta:** En `_extract_python_ast_symbols`, cuando un diff contenía métodos anidados (4 espacios) junto a funciones raíz (0 espacios), `textwrap.dedent` fallaba con `IndentationError` en bloque. Se implementó un algoritmo de fragmentación por bloques (`chunk parser`) que analiza individualmente cada símbolo con su nivel de sangría.
- **Vulnerabilidad de falsos positivos en verificación de anclaje:** En `verify_response_grounding`, valores vacíos `""` en `death_sha` o `file_path` evaluaban erróneamente como `True` debido a `"" in text`. Se agregó verificación estricta `bool(sha_str)` y compatibilidad con prefijos de 7 caracteres para SHAs de 40 caracteres.
- **Ruptura de tablas Markdown en PRs de GitHub:** En `generate_ci_markdown_summary`, mensajes de commit multilínea o con caracteres `|` fragmentaban las filas de la tabla Markdown. Se añadió sanitización de saltos de línea y escape de pipes en todos los campos.
- **Riesgo de IndexError en CLI:** En `main()`, se añadió verificación anticipada para abortar limpiamente si la lista de fantasmas descubiertos está vacía antes de indexar `ghosts[0]`.
- **Omisión de archivos eliminados con espacios:** En `mine_git_graveyard`, se incorporó soporte para cabeceras de diff con rutas entrecomilladas (`--- "a/..."`) y delimitadores de tabulación.
- **Escape de entidades HTML en la interfaz web:** Se extendió `escapeHtml` para sanitizar `&`, `<`, `>`, `"` y `'`, evitando corrupción del DOM ante funciones con tipos genéricos (ej. `calculate<T>()`) o comillas en el mensaje del commit.
- **Soporte de Type Annotations en el Quine AST:** En `inspect_own_source_quine`, se agregó compatibilidad con nodos `ast.AnnAssign` además de `ast.Assign` para la búsqueda de `MICTLAN_HEX_CIPHER`.

### Seguridad
- Sanitización estricta contra inyección XSS y rotura de etiquetas HTML en el listado de ofrendas (`renderTombstoneList`) y en la tabla de trazas de Sentry (`renderSentryTableAndChart`).
- Manejo integral de excepciones en `summon_gemma_spirit` garantizando la privacidad local: ante cualquier anomalía de socket o red, el agente nunca expone datos hacia servicios externos y conmuta inmediatamente al motor determinista local.

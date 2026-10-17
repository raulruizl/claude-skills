# Generador de informes PDF

Convierte un JSON de "estudio de mercado y estrategia" en un PDF A4 con portada, índice con números de página, gráficos nativos, tablas, recuadros y fuentes numeradas con enlaces.

## Uso

```
python3 scripts/generar_informe.py ENTRADA.json SALIDA.pdf
python3 scripts/generar_informe.py scripts/ejemplo.json /tmp/ejemplo.pdf
```

Códigos de salida: 0 correcto, 1 archivo ilegible o uso incorrecto, 2 entrada no válida (se listan campo y posición, por ejemplo `secciones[1].bloques[3] (tipo='tabla').filas[2]: tiene 3 celdas y hay 4 columnas`), 3 falta ReportLab.

## Requisitos

- `python3` con **ReportLab** (probado con 5.0.1): `python3 -m pip install reportlab`. Si el proyecto tiene un entorno virtual sin ReportLab, usa el `python3` del sistema.
- Opcional: DejaVu Sans en `/usr/share/fonts/truetype/dejavu/` para símbolos que Helvetica no trae (`≈`, `→`, `≥`…). Sin ella, esos símbolos se sustituyen por `~`, `->`, `>=`…
- Opcional, para revisar el resultado: `pymupdf` (`python3 -m pip install pymupdf`) y `Pillow` permiten renderizar las páginas a PNG y montar un mosaico para mirarlas.

## Esquema del JSON (UTF-8)

```
{ "meta": {"titulo", "subtitulo", "tagline", "fecha", "metodo", "estado", "autor",
           "pie_titulo", "palabras_clave": [...]},
  "secciones": [ {"titulo": "...", "bloques": [BLOQUE, ...]} ],
  "fuentes": [ {"id": 1, "texto": "Nombre. Descripción", "url": "https://...",
                "confianza": "alta|media|baja|interesada"} ] }
```

Solo `meta.titulo`, `secciones` (con `titulo` y `bloques`) son obligatorios. El generador numera las secciones (1..N), construye el índice y añade la sección final "Fuentes"; no las incluyas en `secciones`.

Bloques (`tipo`):

| tipo | Campos |
| --- | --- |
| `parrafo` | `texto` |
| `subtitulo` | `texto` |
| `vinetas` | `items`: lista de textos (`<b>Clave.</b> resto`) |
| `recuadro` | `etiqueta` (opcional), `texto` |
| `nota` | `etiqueta` (opcional), `texto` |
| `tabla` | `titulo` (opc.), `columnas`, `anchos` (opc., proporciones), `filas`, `destacar_fila` (null o índice) |
| `grafico` `barras` | `titulo`, `pie`, `categorias`, `series: [{nombre, valores}]`, `unidad`, `destacar` (null o índice de categoría) |
| `grafico` `mapa` | `titulo`, `pie`, `eje_x {nombre, izq, der}`, `eje_y {nombre, abajo, arriba}`, `puntos: [{nombre, x, y, destacado}]` con x, y entre 0 y 1 |
| `grafico` `embudo` | `titulo`, `pie`, `niveles: [{etiqueta, valor, detalle}]` |
| `salto_pagina` | sin campos |

## Texto en línea

- Marcas admitidas: `<b>`, `<i>`, `<u>`, `<font color="#hex" size="9">` y `<a href="https://...">`. Todo lo demás (`&`, `<`, `>`, cierres huérfanos) se escapa y se muestra tal cual; las etiquetas sin cerrar se cierran solas. Un `\n` es un salto de línea.
- `[3]` o `[1, 3]` se convierten en enlaces a la fuente con ese `id` (si no existe, se deja como texto).
- Etiquetas de confianza con estilo propio (en mayúscula inicial o toda en mayúsculas): **Dato verificado**, Dato antiguo, Estimación, Hipótesis, Inferencia. También los marcadores `[H]` e `[I]`.

## Límites

- Se usa Helvetica estándar; los símbolos fuera de Latin-1 salen en DejaVu en el texto corrido y como sustitutos ASCII dentro de los gráficos.
- Un recuadro corto no se parte entre páginas; una tabla se parte por filas y repite la cabecera.
- El índice incluye solo los títulos de sección (no los subtítulos).
- Los gráficos son sencillos: barras verticales (horizontales si hay más de 6 categorías o etiquetas largas), mapa de dos ejes y embudo. Etiquetas del mapa sin solape garantizado solo en densidad moderada.

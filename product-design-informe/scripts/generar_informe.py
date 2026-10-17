#!/usr/bin/env python3
"""Generador de informes PDF de "estudio de mercado y estrategia" con ReportLab.

Uso:  python3 scripts/informe/generar_informe.py ENTRADA.json SALIDA.pdf

Requiere ReportLab en el python3 del sistema (no es dependencia del proyecto).
Esquema de entrada y detalles: scripts/informe/README.md.
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

try:
    from reportlab.graphics.shapes import Circle, Drawing, Group, Line, Rect, String
    from reportlab.lib.colors import HexColor, toColor, white
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        CondPageBreak,
        Flowable,
        Frame,
        HRFlowable,
        KeepTogether,
        NextPageTemplate,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
    from reportlab.platypus.tableofcontents import TableOfContents
except ImportError:  # pragma: no cover
    sys.stderr.write("Error: falta reportlab. Instálalo en el python3 del sistema.\n")
    sys.exit(3)

# --------------------------------------------------------------------------- paleta
NAVY = HexColor("#14213d")
NAVY_TAB = HexColor("#13213d")
GOLD = HexColor("#b08d3c")
GOLD_DARK = HexColor("#8a6a1f")
BEIGE = HexColor("#f2f0eb")
INK = HexColor("#222222")
GREY = HexColor("#555555")
GREY_LIGHT = HexColor("#777777")
LINE = HexColor("#c9c9c9")
ACCENT = HexColor("#b5452f")
SLATE = HexColor("#6b7a99")
SERIES = [NAVY, GOLD, SLATE, HexColor("#9a9a9a")]

CONFIANZAS = ("alta", "media", "baja", "interesada")
ETIQUETAS_CONFIANZA = {
    "dato verificado": ("#14213d", ""),
    "dato antiguo": ("#555555", "i"),
    "estimación": ("#8a6a1f", ""),
    "hipótesis": ("#b5452f", "i"),
    "inferencia": ("#3d5a80", "i"),
}

PAGE_W, PAGE_H = A4
MARGIN = 2 * cm
FRAME_W = PAGE_W - 2 * MARGIN

# --------------------------------------------------------------------------- tipografía
BASE, BOLD, ITALIC = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
_DEJAVU = Path("/usr/share/fonts/truetype/dejavu")
_cmap_dejavu: set[int] = set()
FALLBACK_ASCII = {
    "→": "->",
    "←": "<-",
    "≈": "~",
    "≥": ">=",
    "≤": "<=",
    "≠": "!=",
    "×": "x",
    "✓": "ok",
    "−": "-",
    "↑": "^",
}


def _registrar_dejavu() -> None:
    """Registra DejaVu Sans para los símbolos que Helvetica (WinAnsi) no trae."""
    try:
        normal, negrita = _DEJAVU / "DejaVuSans.ttf", _DEJAVU / "DejaVuSans-Bold.ttf"
        if not (normal.exists() and negrita.exists()):
            return
        pdfmetrics.registerFont(TTFont("DejaVuSans", str(normal)))
        pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(negrita)))
        pdfmetrics.registerFontFamily(
            "DejaVuSans",
            normal="DejaVuSans",
            bold="DejaVuSans-Bold",
            italic="DejaVuSans",
            boldItalic="DejaVuSans-Bold",
        )
        _cmap_dejavu.update(pdfmetrics.getFont("DejaVuSans").face.charToGlyph.keys())
    except Exception:  # noqa: BLE001 fuente rota o ilegible: se sigue con sustitutos ASCII
        _cmap_dejavu.clear()


def _soportado_helvetica(ch: str) -> bool:
    try:
        ch.encode("cp1252")
        return True
    except UnicodeEncodeError:
        return False


def tipografia_texto(s: str) -> str:
    """Envuelve en DejaVu los caracteres fuera de WinAnsi (o los sustituye)."""
    out = []
    for ch in s:
        if ord(ch) < 128 or _soportado_helvetica(ch):
            out.append(ch)
        elif ord(ch) in _cmap_dejavu:
            out.append(f'<font name="DejaVuSans">{ch}</font>')
        else:
            out.append(FALLBACK_ASCII.get(ch, "?"))
    return "".join(out)


def texto_canvas(s: str) -> str:
    """Para cadenas dibujadas directamente (gráficos, pie): solo WinAnsi."""
    return "".join(
        ch if (ord(ch) < 128 or _soportado_helvetica(ch)) else FALLBACK_ASCII.get(ch, "?")
        for ch in s
    )


# --------------------------------------------------------------------------- texto en línea
_TAG_RE = re.compile(r"<(/?)(b|i|u|font|a)((?:\s+[^<>]*)?)>", re.IGNORECASE)
_ATTR_RE = re.compile(r"""(\w+)\s*=\s*(?:"([^"<>]*)"|'([^'<>]*)')""")
_REF_RE = re.compile(r"\[(\d+(?:\s*[,;]\s*\d+)*)\]")
_MARCA_RE = re.compile(r"\[([HI])\]")
_ETIQ_RE = re.compile(
    r"(?<!\w)(" + "|".join(re.escape(k) for k in ETIQUETAS_CONFIANZA) + r")(?!\w)", re.IGNORECASE
)
_CIERRE = {"b": "</b>", "i": "</i>", "u": "</u>", "font": "</font>", "a": "</a>"}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _atributos(raw: str) -> dict[str, str]:
    return {
        m.group(1).lower(): (m.group(2) if m.group(2) is not None else m.group(3))
        for m in _ATTR_RE.finditer(raw)
    }


def _color_valido(color: str) -> bool:
    try:
        toColor(color)
    except Exception:  # noqa: BLE001 - cualquier fallo de ReportLab significa color no válido
        return False
    return True


def _abrir(tag: str, raw: str) -> str | None:
    """Devuelve la etiqueta de apertura saneada, o None si no es válida."""
    if tag in ("b", "i", "u"):
        return f"<{tag}>" if not raw.strip() else None
    attrs = _atributos(raw)
    if tag == "font":
        partes = []
        color = attrs.get("color")
        if color and re.fullmatch(r"#[0-9a-fA-F]{3,8}|[a-zA-Z]+", color) and _color_valido(color):
            partes.append(f'color="{color}"')
        size = attrs.get("size")
        if size and re.fullmatch(r"\d+(\.\d+)?", size) and 5 <= float(size) <= 40:
            partes.append(f'size="{size}"')
        return "<font " + " ".join(partes) + ">" if partes else None
    href = attrs.get("href", "")
    if re.fullmatch(r"(https?://|mailto:|#)[^\s\"'<>]*", href):
        return f'<a href="{href.replace("&", "&amp;")}" color="#1f4e9c">'
    return None


def _ref_html(m: re.Match, ids: set[int]) -> str:
    nums = [int(x) for x in re.split(r"[,;]", m.group(1))]
    if not all(n in ids for n in nums):
        return m.group(0)
    enlaces = [f'<a href="#fuente_{n}" color="#8a6a1f">{n}</a>' for n in nums]
    return "[" + ", ".join(enlaces) + "]"


def _marca_html(m: re.Match) -> str:
    color = "#b5452f" if m.group(1) == "H" else "#3d5a80"
    return f'<font color="{color}"><b>[{m.group(1)}]</b></font>'


def _etiqueta_html(m: re.Match) -> str:
    color, estilo = ETIQUETAS_CONFIANZA[m.group(1).lower()]
    txt = f"<b>{m.group(1)}</b>"
    if estilo == "i":
        txt = f"<i>{txt}</i>"
    return f'<font color="{color}">{txt}</font>'


def marcado(texto: str, ids: set[int] | None = None, etiquetas: bool = True) -> str:
    """Convierte el texto del JSON en marcado seguro para Paragraph.

    Admite <b>, <i>, <u>, <font color/size> y <a href>; escapa todo lo demás,
    cierra las etiquetas sin cerrar y neutraliza cierres huérfanos. Convierte
    referencias [n] en enlaces a la sección de fuentes y estiliza las etiquetas
    de confianza y los marcadores [H]/[I].
    """
    ids = ids or set()
    salida: list[str] = []
    pila: list[tuple[str, str]] = []  # (tag, apertura saneada)

    def texto_plano(seg: str) -> str:
        seg = tipografia_texto(esc(seg)).replace("\n", "<br/>")
        if not etiquetas or any(t == "a" for t, _ in pila):
            return seg
        seg = _REF_RE.sub(lambda m: _ref_html(m, ids), seg)
        seg = _MARCA_RE.sub(_marca_html, seg)
        return _ETIQ_RE.sub(_etiqueta_html, seg)

    pos = 0
    for m in _TAG_RE.finditer(texto):
        salida.append(texto_plano(texto[pos : m.start()]))
        pos = m.end()
        cierre, tag, raw = m.group(1), m.group(2).lower(), m.group(3)
        if not cierre:
            apertura = _abrir(tag, raw)
            if apertura is None or (tag == "a" and any(t == "a" for t, _ in pila)):
                salida.append(esc(m.group(0)))
            else:
                pila.append((tag, apertura))
                salida.append(apertura)
        elif any(t == tag for t, _ in pila):
            reabrir = []
            while pila[-1][0] != tag:
                t, ap = pila.pop()
                salida.append(_CIERRE[t])
                reabrir.append((t, ap))
            pila.pop()
            salida.append(_CIERRE[tag])
            for t, ap in reversed(reabrir):
                pila.append((t, ap))
                salida.append(ap)
        else:
            salida.append(esc(m.group(0)))
    salida.append(texto_plano(texto[pos:]))
    salida.extend(_CIERRE[t] for t, _ in reversed(pila))
    return "".join(salida)


def sin_marcas(texto: str) -> str:
    return re.sub(r"<[^<>]*>", "", texto)


# --------------------------------------------------------------------------- validación
class ErroresEntrada(Exception):
    def __init__(self, errores: list[str]):
        super().__init__("\n".join(errores))
        self.errores = errores


def _num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _txt(v) -> bool:
    return isinstance(v, str) and v.strip() != ""


def validar(data) -> list[str]:
    errs: list[str] = []

    def e(ruta: str, msg: str) -> None:
        errs.append(f"{ruta}: {msg}")

    if not isinstance(data, dict):
        return ["raíz: se esperaba un objeto JSON con 'meta', 'secciones' y 'fuentes'"]
    meta = data.get("meta")
    if not isinstance(meta, dict):
        e("meta", "falta o no es un objeto")
    else:
        if not _txt(meta.get("titulo")):
            e("meta.titulo", "obligatorio, texto no vacío")
        for k in ("subtitulo", "tagline", "fecha", "metodo", "estado", "autor", "pie_titulo"):
            if k in meta and not isinstance(meta[k], str):
                e(f"meta.{k}", "debe ser texto")
        pc = meta.get("palabras_clave", [])
        if not isinstance(pc, list) or not all(isinstance(x, str) for x in pc):
            e("meta.palabras_clave", "debe ser una lista de textos")
    secs = data.get("secciones")
    if not isinstance(secs, list) or not secs:
        e("secciones", "obligatorio, lista con al menos una sección")
        secs = []
    for i, s in enumerate(secs):
        r = f"secciones[{i}]"
        if not isinstance(s, dict):
            e(r, "debe ser un objeto con 'titulo' y 'bloques'")
            continue
        if not _txt(s.get("titulo")):
            e(f"{r}.titulo", "obligatorio, texto no vacío")
        bl = s.get("bloques")
        if not isinstance(bl, list):
            e(f"{r}.bloques", "obligatorio, debe ser una lista")
            continue
        for j, b in enumerate(bl):
            _validar_bloque(b, f"{r}.bloques[{j}]", e)
    fu = data.get("fuentes", [])
    if not isinstance(fu, list):
        e("fuentes", "debe ser una lista")
        fu = []
    vistos: set = set()
    for i, f in enumerate(fu):
        r = f"fuentes[{i}]"
        if not isinstance(f, dict):
            e(r, "debe ser un objeto")
            continue
        fid = f.get("id")
        if not isinstance(fid, int) or isinstance(fid, bool) or fid < 1:
            e(f"{r}.id", "obligatorio, entero >= 1")
        elif fid in vistos:
            e(f"{r}.id", f"id {fid} repetido")
        else:
            vistos.add(fid)
        if not _txt(f.get("texto")):
            e(f"{r}.texto", "obligatorio, texto no vacío")
        url = f.get("url")
        if url not in (None, "") and not (isinstance(url, str) and re.match(r"https?://\S+$", url)):
            e(f"{r}.url", "debe empezar por http:// o https://")
        if f.get("confianza") is not None and f.get("confianza") not in CONFIANZAS:
            e(f"{r}.confianza", f"valores admitidos: {', '.join(CONFIANZAS)}")
    return errs


def _validar_bloque(b, r: str, e) -> None:
    if not isinstance(b, dict):
        e(r, "debe ser un objeto con 'tipo'")
        return
    tipo = b.get("tipo")
    r = f"{r} (tipo={tipo!r})"

    def texto(campo: str, obligatorio: bool = True) -> None:
        v = b.get(campo)
        if v is None and not obligatorio:
            return
        if not _txt(v):
            e(f"{r}.{campo}", "debe ser texto no vacío" + ("" if obligatorio else " si se indica"))

    if tipo in ("parrafo", "subtitulo"):
        texto("texto")
    elif tipo == "vinetas":
        it = b.get("items")
        if not isinstance(it, list) or not it or not all(_txt(x) for x in it):
            e(f"{r}.items", "debe ser una lista no vacía de textos")
    elif tipo in ("recuadro", "nota"):
        texto("texto")
        texto("etiqueta", obligatorio=False)
    elif tipo == "tabla":
        texto("titulo", obligatorio=False)
        cols, anchos, filas = b.get("columnas"), b.get("anchos"), b.get("filas")
        if not isinstance(cols, list) or not cols or not all(isinstance(c, str) for c in cols):
            e(f"{r}.columnas", "debe ser una lista no vacía de textos")
            cols = None
        if anchos is not None and (
            not isinstance(anchos, list) or not anchos or not all(_num(a) and a > 0 for a in anchos)
        ):
            e(f"{r}.anchos", "debe ser una lista de números positivos")
        elif anchos is not None and cols and len(anchos) != len(cols):
            e(f"{r}.anchos", f"tiene {len(anchos)} valores y hay {len(cols)} columnas")
        if not isinstance(filas, list):
            e(f"{r}.filas", "debe ser una lista de filas")
        else:
            for k, fila in enumerate(filas):
                if not isinstance(fila, list) or not all(
                    isinstance(c, (str, int, float)) for c in fila
                ):
                    e(f"{r}.filas[{k}]", "debe ser una lista de textos")
                elif cols and len(fila) != len(cols):
                    e(f"{r}.filas[{k}]", f"tiene {len(fila)} celdas y hay {len(cols)} columnas")
            df = b.get("destacar_fila")
            if df is not None and not (
                isinstance(df, int) and not isinstance(df, bool) and 0 <= df < len(filas)
            ):
                e(f"{r}.destacar_fila", f"debe ser null o un índice entre 0 y {len(filas) - 1}")
    elif tipo == "grafico":
        _validar_grafico(b, r, e, texto)
    elif tipo == "salto_pagina":
        pass
    else:
        e(
            r,
            "tipo desconocido; admitidos: parrafo, subtitulo, vinetas, recuadro, nota, tabla, "
            "grafico, salto_pagina",
        )


def _validar_grafico(b, r: str, e, texto) -> None:
    clase = b.get("clase")
    r = f"{r} (clase={clase!r})"
    texto("titulo")
    texto("pie", obligatorio=False)
    if clase == "barras":
        cats, series = b.get("categorias"), b.get("series")
        if not isinstance(cats, list) or not cats or not all(isinstance(c, str) for c in cats):
            e(f"{r}.categorias", "debe ser una lista no vacía de textos")
            cats = None
        if not isinstance(series, list) or not series:
            e(f"{r}.series", "debe ser una lista no vacía de {nombre, valores}")
        else:
            for k, s in enumerate(series):
                v = s.get("valores") if isinstance(s, dict) else None
                if not isinstance(v, list) or not all(_num(x) for x in v):
                    e(f"{r}.series[{k}].valores", "debe ser una lista de números")
                elif cats and len(v) != len(cats):
                    e(
                        f"{r}.series[{k}].valores",
                        f"tiene {len(v)} valores y hay {len(cats)} categorías",
                    )
        d = b.get("destacar")
        if d is not None and not (
            isinstance(d, int) and not isinstance(d, bool) and cats and 0 <= d < len(cats)
        ):
            e(f"{r}.destacar", "debe ser null o un índice de categoría válido")
    elif clase == "mapa":
        for eje, claves in (
            ("eje_x", ("nombre", "izq", "der")),
            ("eje_y", ("nombre", "abajo", "arriba")),
        ):
            ev = b.get(eje)
            if not isinstance(ev, dict):
                e(f"{r}.{eje}", f"obligatorio, objeto con {', '.join(claves)}")
            else:
                for c in claves:
                    if not isinstance(ev.get(c), str):
                        e(f"{r}.{eje}.{c}", "obligatorio, texto")
        pts = b.get("puntos")
        if not isinstance(pts, list) or not pts:
            e(f"{r}.puntos", "debe ser una lista no vacía de {nombre, x, y}")
        else:
            for k, p in enumerate(pts):
                if not isinstance(p, dict) or not _txt(p.get("nombre")):
                    e(f"{r}.puntos[{k}].nombre", "obligatorio, texto")
                    continue
                for c in ("x", "y"):
                    if not (_num(p.get(c)) and 0 <= p[c] <= 1):
                        e(f"{r}.puntos[{k}].{c}", "debe ser un número entre 0 y 1")
    elif clase == "embudo":
        niv = b.get("niveles")
        if not isinstance(niv, list) or not niv:
            e(f"{r}.niveles", "debe ser una lista no vacía de {etiqueta, valor, detalle}")
        else:
            for k, n in enumerate(niv):
                if not isinstance(n, dict) or not _txt(n.get("etiqueta")):
                    e(f"{r}.niveles[{k}].etiqueta", "obligatorio, texto")
                elif not isinstance(n.get("valor"), (str, int, float)):
                    e(f"{r}.niveles[{k}].valor", "obligatorio, texto o número")
    else:
        e(r, "clase de gráfico desconocida; admitidas: barras, mapa, embudo")


# --------------------------------------------------------------------------- estilos
def _estilos() -> dict[str, ParagraphStyle]:
    def ps(nombre, **kw):
        kw.setdefault("fontName", BASE)
        kw.setdefault("textColor", INK)
        kw.setdefault("alignment", TA_LEFT)
        kw.setdefault("allowWidows", 0)
        kw.setdefault("allowOrphans", 0)
        return ParagraphStyle(nombre, **kw)

    return {
        "cuerpo": ps("cuerpo", fontSize=10.5, leading=15, spaceAfter=6),
        "h1": ps(
            "h1",
            fontName=BOLD,
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=2,
            keepWithNext=1,
        ),
        "h2": ps(
            "h2",
            fontName=BOLD,
            fontSize=12.5,
            leading=16,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=3,
            keepWithNext=1,
        ),
        "vineta": ps(
            "vineta",
            fontSize=10.5,
            leading=15,
            leftIndent=14,
            bulletIndent=3,
            spaceAfter=3,
            bulletFontName=BASE,
            bulletFontSize=10.5,
        ),
        "recuadro": ps("recuadro", fontSize=10.5, leading=15),
        "nota": ps("nota", fontSize=8.5, leading=11.5, textColor=GREY, spaceAfter=6),
        "tab_cab": ps("tab_cab", fontName=BOLD, fontSize=8.8, leading=11.5, textColor=white),
        "tab_cel": ps("tab_cel", fontSize=8.8, leading=11.5),
        "tab_tit": ps(
            "tab_tit",
            fontName=BOLD,
            fontSize=10,
            leading=13,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=3,
            keepWithNext=1,
        ),
        "graf_tit": ps(
            "graf_tit",
            fontName=BOLD,
            fontSize=10,
            leading=13,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=3,
            keepWithNext=1,
        ),
        "graf_pie": ps(
            "graf_pie", fontSize=8.5, leading=11.5, textColor=GREY, spaceBefore=2, spaceAfter=8
        ),
        "portada_tit": ps(
            "portada_tit", fontName=BOLD, fontSize=30, leading=36, textColor=NAVY, spaceAfter=10
        ),
        "portada_sub": ps("portada_sub", fontSize=14, leading=19, textColor=GOLD, spaceAfter=10),
        "portada_tag": ps("portada_tag", fontSize=12, leading=17, spaceAfter=28),
        "portada_meta": ps("portada_meta", fontSize=10, leading=15, spaceAfter=3),
        "toc": ps("toc", fontSize=11, leading=17, textColor=INK, rightIndent=0),
        "fuente": ps(
            "fuente",
            fontSize=9,
            leading=12.5,
            leftIndent=24,
            bulletIndent=0,
            bulletFontName=BOLD,
            bulletFontSize=9,
            spaceAfter=4,
        ),
    }


# --------------------------------------------------------------------------- flowables propios
class Titulo1(Paragraph):
    """H1 numerado que avisa al índice."""

    def __init__(self, texto, estilo, clave, plano):
        super().__init__(texto, estilo)
        self.toc_key, self.toc_text = clave, plano


class Recuadro(Flowable):
    """Párrafo sobre fondo beige con barra vertical dorada; divisible si es largo."""

    PAD_X, PAD_Y, BARRA = 12, 8, 4

    def __init__(self, parrafo: Paragraph):
        super().__init__()
        self.p = parrafo
        self.spaceAfter = 8
        self.spaceBefore = 4

    def wrap(self, aw, ah):
        self.w = aw
        _, ph = self.p.wrap(aw - self.BARRA - 2 * self.PAD_X, ah - 2 * self.PAD_Y)
        self.h = ph + 2 * self.PAD_Y
        return aw, self.h

    def split(self, aw, ah):
        interior = aw - self.BARRA - 2 * self.PAD_X
        _, ph = self.p.wrap(interior, 10_000)
        if ph < 110:  # recuadros cortos: nunca se parten
            return []
        partes = self.p.split(interior, ah - 2 * self.PAD_Y)
        return [Recuadro(x) for x in partes] if len(partes) > 1 else []

    def draw(self):
        c = self.canv
        c.setFillColor(BEIGE)
        c.rect(0, 0, self.w, self.h, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(0, 0, self.BARRA, self.h, stroke=0, fill=1)
        self.p.drawOn(c, self.BARRA + self.PAD_X, self.PAD_Y)


# --------------------------------------------------------------------------- gráficos
def _ancho(txt: str, fuente: str, tam: float) -> float:
    return pdfmetrics.stringWidth(txt, fuente, tam)


def _envolver(txt: str, fuente: str, tam: float, maxw: float) -> list[str]:
    lineas, actual = [], ""
    for palabra in txt.split():
        while _ancho(palabra, fuente, tam) > maxw and len(palabra) > 1:  # palabra larguísima
            k = len(palabra) - 1
            while k > 1 and _ancho(palabra[:k], fuente, tam) > maxw:
                k -= 1
            lineas.append(palabra[:k])
            palabra = palabra[k:]
        prueba = f"{actual} {palabra}".strip()
        if _ancho(prueba, fuente, tam) <= maxw or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas or [""]


def _ajustar(
    txt: str, fuente: str, tam: float, maxw: float, minimo: float = 6
) -> tuple[str, float]:
    while _ancho(txt, fuente, tam) > maxw and tam > minimo:
        tam -= 0.5
    while _ancho(txt, fuente, tam) > maxw and len(txt) > 1:
        txt = txt[:-2].rstrip() + "…"
        if _ancho(txt, fuente, tam) <= maxw:
            break
    return txt, tam


def _s(x, y, txt, tam=8, fuente=BASE, color=INK, ancla="start") -> String:
    return String(
        x, y, texto_canvas(txt), fontName=fuente, fontSize=tam, fillColor=color, textAnchor=ancla
    )


def _fmt(v: float) -> str:
    if abs(v - round(v)) < 1e-9:
        t = f"{round(v):,}"
    else:
        t = f"{v:,.1f}"
    return t.replace(",", "§").replace(".", ",").replace("§", ".")


def _escala(vmin: float, vmax: float) -> tuple[float, float, float]:
    vmax = max(vmax, 1e-9) if vmax > 0 else 1.0
    crudo = vmax / 4
    mag = 10 ** math.floor(math.log10(crudo))
    paso = next(m * mag for m in (1, 2, 2.5, 5, 10) if crudo <= m * mag + 1e-12)
    hi = math.ceil(vmax / paso - 1e-9) * paso
    lo = math.floor(vmin / paso) * paso if vmin < 0 else 0.0
    return lo, hi, paso


def _leyenda(d: Drawing, series: list[dict], x: float, y: float, anchura: float) -> None:
    for k, s in enumerate(series):
        nombre = str(s.get("nombre", f"Serie {k + 1}"))
        w = _ancho(texto_canvas(nombre), BASE, 8) + 18
        if x + w > anchura:
            break
        d.add(Rect(x, y, 8, 8, fillColor=SERIES[k % len(SERIES)], strokeColor=None))
        d.add(_s(x + 12, y + 1, nombre, 8, color=GREY))
        x += w + 8


def grafico_barras(g: dict, W: float) -> Drawing:
    cats, series, destacar = g["categorias"], g["series"], g.get("destacar")
    unidad = g.get("unidad") or ""
    nc, ns = len(cats), len(series)
    vals = [v for s in series for v in s["valores"]]
    lo, hi, paso = _escala(min(0, min(vals)), max(vals))
    L, R = 42, 8
    gw = (W - L - R) / nc
    lineas = [_envolver(texto_canvas(c), BASE, 8, gw - 6) for c in cats]
    if nc > 6 or max(len(x) for x in lineas) > 3:
        return _barras_horizontales(g, W, lo, hi, paso)
    nl = max(len(x) for x in lineas)
    B, T = 10 + nl * 10, 24
    H = 200
    d = Drawing(W, H)
    ph = H - B - T

    def yy(v):
        return B + (v - lo) / (hi - lo) * ph

    t = lo
    while t <= hi + 1e-9:
        d.add(Line(L, yy(t), W - R, yy(t), strokeColor=LINE if t else GREY, strokeWidth=0.4))
        d.add(_s(L - 4, yy(t) - 2.5, _fmt(t), 7.5, color=GREY, ancla="end"))
        t += paso
    bw = min(46, gw * 0.66 / ns)
    for ci in range(nc):
        x0 = L + ci * gw + (gw - bw * ns) / 2
        for si, s in enumerate(series):
            v = s["valores"][ci]
            color = ACCENT if (destacar == ci and si == 0) else SERIES[si % len(SERIES)]
            y0, y1 = sorted((yy(0), yy(v)))
            d.add(
                Rect(
                    x0 + si * bw,
                    y0,
                    bw - 1.5 if ns > 1 else bw,
                    max(y1 - y0, 0.5),
                    fillColor=color,
                    strokeColor=None,
                )
            )
            tam = 7.5 if bw >= 16 else 6.5
            ty = y1 + 3 if v >= 0 else y0 - 9
            d.add(
                _s(
                    x0 + si * bw + (bw - (1.5 if ns > 1 else 0)) / 2,
                    ty,
                    _fmt(v),
                    tam,
                    BOLD if destacar == ci else BASE,
                    INK,
                    "middle",
                )
            )
        for k, ln in enumerate(lineas[ci]):
            d.add(
                _s(
                    L + ci * gw + gw / 2,
                    B - 11 - k * 10,
                    ln,
                    8,
                    BOLD if destacar == ci else BASE,
                    INK,
                    "middle",
                )
            )
    if unidad:
        d.add(_s(0, H - 9, unidad, 8, BOLD, GREY))
    if ns > 1:
        _leyenda(d, series, L + 30 if unidad else L, H - 10, W)
    return d


def _barras_horizontales(g: dict, W: float, lo: float, hi: float, paso: float) -> Drawing:
    cats, series, destacar = g["categorias"], g["series"], g.get("destacar")
    unidad = g.get("unidad") or ""
    nc, ns = len(cats), len(series)
    LW, R = min(150, W * 0.32), 40
    fila = max(ns * 11 + 10, 24)
    T = 24
    H = nc * fila + T + 14
    d = Drawing(W, H)
    x0 = LW + 8
    pw = W - x0 - R
    tope = H - T

    def xx(v):
        return x0 + (v - lo) / (hi - lo) * pw

    t = lo
    while t <= hi + 1e-9:
        d.add(Line(xx(t), 14, xx(t), tope, strokeColor=LINE if t else GREY, strokeWidth=0.4))
        d.add(_s(xx(t), 4, _fmt(t), 7.5, color=GREY, ancla="middle"))
        t += paso
    bh = min(13, (fila - 8) / ns)
    for ci in range(nc):
        ytop = tope - ci * fila
        ln = _envolver(texto_canvas(cats[ci]), BASE, 8, LW)[:3]
        yc = ytop - fila / 2 + (len(ln) - 1) * 5 - 3
        for k, txt in enumerate(ln):
            d.add(_s(LW, yc - k * 10, txt, 8, BOLD if destacar == ci else BASE, INK, "end"))
        for si, s in enumerate(series):
            v = s["valores"][ci]
            color = ACCENT if (destacar == ci and si == 0) else SERIES[si % len(SERIES)]
            by = ytop - fila / 2 + (ns * bh) / 2 - (si + 1) * bh
            xa, xb = sorted((xx(0), xx(v)))
            d.add(Rect(xa, by + 1, max(xb - xa, 0.5), bh - 2, fillColor=color, strokeColor=None))
            d.add(_s(xb + 3, by + bh / 2 - 3, _fmt(v), 7.5, BOLD if destacar == ci else BASE))
    if unidad:
        d.add(_s(0, H - 9, unidad, 8, BOLD, GREY))
    if ns > 1:
        _leyenda(d, series, 40 if unidad else 0, H - 10, W)
    return d


def grafico_mapa(g: dict, W: float) -> Drawing:
    H = 320
    L, B, R, T = 56, 42, 10, 12
    pw, ph = W - L - R, H - B - T
    d = Drawing(W, H)
    x0, y0 = L, B
    mitad_x, mitad_y = x0 + pw / 2, y0 + ph / 2
    d.add(Rect(x0, y0, pw, ph, fillColor=white, strokeColor=None))
    d.add(Rect(mitad_x, mitad_y, pw / 2, ph / 2, fillColor=BEIGE, strokeColor=None))
    d.add(Rect(x0, y0, pw / 2, ph / 2, fillColor=BEIGE, strokeColor=None))
    d.add(Rect(x0, y0, pw, ph, fillColor=None, strokeColor=LINE, strokeWidth=0.6))
    for ln in (Line(mitad_x, y0, mitad_x, y0 + ph), Line(x0, mitad_y, x0 + pw, mitad_y)):
        ln.strokeColor, ln.strokeWidth, ln.strokeDashArray = GREY_LIGHT, 0.6, [3, 3]
        d.add(ln)
    ex, ey = g["eje_x"], g["eje_y"]
    # etiquetas de cuadrante (tenues)
    cuad = [
        (x0 + 5, y0 + ph - 10, f"{ey['arriba']} / {ex['izq']}", "start"),
        (x0 + pw - 5, y0 + ph - 10, f"{ey['arriba']} / {ex['der']}", "end"),
        (x0 + 5, y0 + 4, f"{ey['abajo']} / {ex['izq']}", "start"),
        (x0 + pw - 5, y0 + 4, f"{ey['abajo']} / {ex['der']}", "end"),
    ]
    for x, y, txt, anc in cuad:
        txt, tam = _ajustar(texto_canvas(txt), ITALIC, 7, pw / 2 - 12, 5.5)
        d.add(_s(x, y, txt, tam, ITALIC, GREY_LIGHT, anc))
    # ejes
    t, tam = _ajustar(ex["nombre"], BOLD, 9, pw * 0.5)
    d.add(_s(mitad_x, 6, t, tam, BOLD, NAVY, "middle"))
    t, tam = _ajustar(ex["izq"], BASE, 8, pw * 0.3)
    d.add(_s(x0, y0 - 12, t, tam, BASE, GREY, "start"))
    t, tam = _ajustar(ex["der"], BASE, 8, pw * 0.3)
    d.add(_s(x0 + pw, y0 - 12, t, tam, BASE, GREY, "end"))

    def vertical(txt, y, fuente, tam, color, ancla, x=14):
        gr = Group(_s(0, 0, txt, tam, fuente, color, ancla))
        gr.transform = (0, 1, -1, 0, x, y)
        d.add(gr)

    # nombre del eje y: hasta dos líneas, reduciendo la fuente; puntos suspensivos al final
    maxw, nombre_y, tam = ph * 0.5, texto_canvas(ey["nombre"]), 9.0
    lineas = _envolver(nombre_y, BOLD, tam, maxw)
    while len(lineas) > 2 and tam > 7:
        tam -= 0.5
        lineas = _envolver(nombre_y, BOLD, tam, maxw)
    if len(lineas) > 2:
        lineas = [lineas[0], _ajustar(" ".join(lineas[1:]), BOLD, tam, maxw, tam)[0]]
    for k, ln in enumerate(lineas):
        vertical(ln, y0 + ph / 2, BOLD, tam, NAVY, "middle", x=20 - 10 * k)
    t, tam = _ajustar(ey["abajo"], BASE, 8, ph * 0.22)
    vertical(t, y0, BASE, tam, GREY, "start", x=36)
    t, tam = _ajustar(ey["arriba"], BASE, 8, ph * 0.22)
    vertical(t, y0 + ph, BASE, tam, GREY, "end", x=36)
    # puntos con etiquetas sin solaparse
    ocupados: list[tuple[float, float, float, float]] = []

    def choca(r):
        return any(r[0] < o[2] and r[2] > o[0] and r[1] < o[3] and r[3] > o[1] for o in ocupados)

    puntos = sorted(g["puntos"], key=lambda p: -bool(p.get("destacado")))
    for p in puntos:
        px, py = x0 + 8 + p["x"] * (pw - 16), y0 + 8 + p["y"] * (ph - 16)
        dest = bool(p.get("destacado"))
        r = 6 if dest else 4.5
        nombre = texto_canvas(p["nombre"])
        fuente, tam = (BOLD, 8) if dest else (BASE, 7.5)
        w = _ancho(nombre, fuente, tam)
        ocupados.append((px - r, py - r, px + r, py + r))
        cands = [
            (px + r + 3, py - 3, "start"),
            (px - r - 3, py - 3, "end"),
            (px - w / 2, py + r + 2, "start"),
            (px - w / 2, py - r - 10, "start"),
            (px + r + 3, py + 6, "start"),
            (px - r - 3, py + 6, "end"),
            (px + r + 3, py - 12, "start"),
            (px - r - 3, py - 12, "end"),
        ]
        elegido = None
        for cx, cy, anc in cands:
            rx0 = cx if anc == "start" else cx - w
            rect = (rx0 - 1, cy - 1, rx0 + w + 1, cy + tam + 1)
            if (
                rect[0] >= x0
                and rect[2] <= x0 + pw
                and rect[1] >= y0
                and rect[3] <= y0 + ph
                and not choca(rect)
            ):
                elegido = (cx, cy, anc, rect)
                break
        if elegido is None:
            cx, cy, anc = cands[0]
            rx0 = cx if anc == "start" else cx - w
            elegido = (cx, cy, anc, (rx0, cy, rx0 + w, cy + tam))
        d.add(_circulo(px, py, r, dest))
        d.add(_s(elegido[0], elegido[1], nombre, tam, fuente, ACCENT if dest else INK, elegido[2]))
        ocupados.append(elegido[3])
    return d


def _circulo(x, y, r, destacado):
    return Circle(
        x, y, r, fillColor=ACCENT if destacado else NAVY, strokeColor=white, strokeWidth=0.8
    )


def grafico_embudo(g: dict, W: float) -> Drawing:
    niv = g["niveles"]
    n = len(niv)
    fila, hueco = 46, 6
    H = n * (fila + hueco)
    BW = W * 0.50
    d = Drawing(W, H)
    texto_x = BW + 18
    for i, nv in enumerate(niv):
        w = BW * (1 - 0.55 * i / (n - 1)) if n > 1 else BW
        y = H - (i + 1) * fila - i * hueco
        t = i / (n - 1) if n > 1 else 0
        a, b = (0x14, 0x21, 0x3D), (0x6B, 0x7A, 0x99)
        rgb = [int(a[k] + (b[k] - a[k]) * t) for k in range(3)]
        col = HexColor("#{:02x}{:02x}{:02x}".format(*rgb))
        d.add(Rect(BW / 2 - w / 2, y, w, fila, fillColor=col, strokeColor=None))
        et, tam_e = _ajustar(nv["etiqueta"], BASE, 8, w - 10, 5.5)
        va, tam_v = _ajustar(str(nv["valor"]), BOLD, 14, w - 10, 7)
        d.add(_s(BW / 2, y + fila - 14, et, tam_e, BASE, white, "middle"))
        d.add(_s(BW / 2, y + 9, va, tam_v, BOLD, white, "middle"))
        detalle = _envolver(texto_canvas(str(nv.get("detalle") or "")), BASE, 8.5, W - texto_x)
        if len(detalle) > 4:
            detalle = detalle[:4]
            detalle[-1] = detalle[-1].rstrip() + "…"
        top = y + fila / 2 + (len(detalle) * 10.5) / 2 - 8
        if nv.get("detalle"):
            d.add(
                Line(
                    BW / 2 + w / 2 + 4,
                    y + fila / 2,
                    texto_x - 6,
                    y + fila / 2,
                    strokeColor=GOLD,
                    strokeWidth=0.8,
                )
            )
        for k, ln in enumerate(detalle if nv.get("detalle") else []):
            d.add(_s(texto_x, top - k * 10.5, ln, 8.5, BASE, INK))
    return d


GRAFICOS = {"barras": grafico_barras, "mapa": grafico_mapa, "embudo": grafico_embudo}


# --------------------------------------------------------------------------- documento
class Documento(BaseDocTemplate):
    def __init__(self, ruta, meta, **kw):
        super().__init__(ruta, pagesize=A4, **kw)
        self.meta = meta
        self.pie_titulo = texto_canvas(
            (meta.get("pie_titulo") or meta["titulo"]).strip() + " | Documento confidencial"
        )
        marco = Frame(
            MARGIN,
            2.2 * cm,
            FRAME_W,
            PAGE_H - 2 * cm - 2.2 * cm,
            id="n",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        tope = PAGE_H * 2 / 3
        portada = Frame(
            MARGIN,
            2 * cm,
            FRAME_W,
            tope - 2 * cm,
            id="p",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(
            [
                PageTemplate(id="portada", frames=[portada], onPage=self._pagina_portada),
                PageTemplate(id="normal", frames=[marco], onPage=self._pagina_normal),
            ]
        )

    @staticmethod
    def _pagina_portada(c, doc):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 4.2 * cm, PAGE_W, 4.2 * cm, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(0, PAGE_H - 4.2 * cm - 4, PAGE_W, 4, stroke=0, fill=1)
        c.restoreState()

    def _pagina_normal(self, c, doc):
        c.saveState()
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.6)
        c.line(MARGIN, 1.55 * cm, PAGE_W - MARGIN, 1.55 * cm)
        c.setFont(BASE, 8)
        c.setFillColor(GREY_LIGHT)
        c.drawString(MARGIN, 1.1 * cm, self.pie_titulo)
        c.drawRightString(PAGE_W - MARGIN, 1.1 * cm, f"Página {doc.page}")
        c.restoreState()

    def afterFlowable(self, fl):
        if isinstance(fl, Titulo1):
            self.canv.bookmarkPage(fl.toc_key)
            self.canv.addOutlineEntry(fl.toc_text, fl.toc_key, 0, 0)
            self.notify("TOCEntry", (0, fl.toc_text, self.page, fl.toc_key))


def _celda(v) -> str:
    return str(v)


def construir_historia(data: dict, est: dict) -> list:
    meta = data["meta"]
    ids = {f["id"] for f in data.get("fuentes", [])}

    def par(texto, estilo, etiquetas=True, **kw):
        m = marcado(texto, ids, etiquetas)
        try:
            return Paragraph(m, estilo, **kw)
        except Exception:  # noqa: BLE001
            return Paragraph(esc(texto), estilo, **kw)

    h = []
    # portada
    h.append(par(meta["titulo"], est["portada_tit"]))
    if meta.get("subtitulo"):
        h.append(par(meta["subtitulo"], est["portada_sub"]))
    if meta.get("tagline"):
        h.append(par(meta["tagline"], est["portada_tag"]))
    for etiqueta, clave in (("Fecha", "fecha"), ("Método", "metodo"), ("Estado", "estado")):
        if meta.get(clave):
            h.append(par(f"<b>{etiqueta}:</b> {meta[clave]}", est["portada_meta"]))
    h += [NextPageTemplate("normal"), PageBreak()]
    # índice
    h.append(Paragraph("Contenido", ParagraphStyle("ct", parent=est["h1"], keepWithNext=1)))
    h.append(HRFlowable(width="100%", thickness=0.8, color=GOLD, spaceBefore=2, spaceAfter=10))
    toc = TableOfContents()
    toc.dotsMinLevel = 0
    toc.levelStyles = [est["toc"]]
    h += [toc, PageBreak()]
    # secciones
    n = 0
    for n, sec in enumerate(data["secciones"], 1):
        h.append(CondPageBreak(120))  # un H1 lleva al menos ~4 líneas de contenido debajo
        h += _titulo1(f"{n}. {sec['titulo']}", f"sec{n}", est, ids)
        bloques = sec["bloques"]
        for k, b in enumerate(bloques):
            sig = bloques[k + 1] if k + 1 < len(bloques) else None
            if b["tipo"] == "subtitulo" and sig and sig["tipo"] == "tabla":
                # evita que el H2 quede solo si la tabla (partible) empieza en otra página
                h.append(CondPageBreak(130))
                if not sig.get("titulo") and len(sig["filas"]) > 5:
                    h.append(
                        par(b["texto"], ParagraphStyle("h2s", parent=est["h2"], keepWithNext=0))
                    )
                    continue
            h += _bloque(b, est, par, ids)
    if data.get("fuentes"):
        h.append(CondPageBreak(120))
        h += _titulo1(f"{n + 1}. Fuentes", "fuentes", est, ids)
        h.append(
            par(
                "Las referencias numeradas [n] del texto enlazan a esta lista. La "
                "fiabilidad indica el criterio del autor sobre cada fuente.",
                est["nota"],
            )
        )
        for f in sorted(data["fuentes"], key=lambda x: x["id"]):
            partes = [f'<a name="fuente_{f["id"]}"/>', marcado(f["texto"])]
            if f.get("url"):
                u = f["url"].replace("&", "&amp;")
                partes.append(f' <a href="{u}" color="#1f4e9c">{esc(f["url"])}</a>')
            if f.get("confianza"):
                partes.append(f' <font color="#555555">(fiabilidad: {f["confianza"]})</font>')
            try:
                h.append(Paragraph("".join(partes), est["fuente"], bulletText=f"[{f['id']}]"))
            except Exception:  # noqa: BLE001
                h.append(Paragraph(esc(f["texto"]), est["fuente"], bulletText=f"[{f['id']}]"))
    return h


def _titulo1(texto, clave, est, ids):
    t = Titulo1(marcado(texto), est["h1"], clave, sin_marcas(texto))
    hr = HRFlowable(width="100%", thickness=0.8, color=GOLD, spaceBefore=1, spaceAfter=8)
    hr.keepWithNext = 1
    return [t, hr]


def _bloque(b: dict, est: dict, par, ids: set[int]) -> list:
    tipo = b["tipo"]
    if tipo == "parrafo":
        return [par(b["texto"], est["cuerpo"])]
    if tipo == "subtitulo":
        return [par(b["texto"], est["h2"])]
    if tipo == "vinetas":
        return [par(it, est["vineta"], bulletText="•") for it in b["items"]]
    if tipo in ("recuadro", "nota"):
        et = b.get("etiqueta")
        txt = (f"<b>{esc(et)}</b> " if et else "") + b["texto"]
        if tipo == "nota":
            return [par(txt, est["nota"])]
        return [Recuadro(par(txt, est["recuadro"]))]
    if tipo == "salto_pagina":
        return [PageBreak()]
    if tipo == "tabla":
        return _tabla(b, est, par)
    if tipo == "grafico":
        dib = GRAFICOS[b["clase"]](b, FRAME_W)
        dib.hAlign = "LEFT"
        piezas = [par(b["titulo"], est["graf_tit"]), dib]
        if b.get("pie"):
            piezas.append(par(b["pie"], est["graf_pie"]))
        else:
            piezas.append(Spacer(1, 8))
        return [KeepTogether(piezas)]
    return []


def _ancho_minimo(cab: str) -> float:
    """Ancho mínimo de una columna: la palabra más larga de su cabecera, más relleno."""
    palabras = sin_marcas(texto_canvas(cab)).split() or [""]
    return max(_ancho(p, BOLD, 8.8) for p in palabras) + 12


def _repartir(total: float, pesos: list[float], minimos: list[float]) -> list[float]:
    """Reparte `total` según `pesos` sin bajar de `minimos` (si caben)."""
    if sum(minimos) >= total:
        return [total * m / sum(minimos) for m in minimos]
    fijos: set[int] = set()
    for _ in range(len(pesos)):
        libre = total - sum(minimos[i] for i in fijos)
        resto = sum(pesos[i] for i in range(len(pesos)) if i not in fijos)
        anchos = [minimos[i] if i in fijos else libre * pesos[i] / resto for i in range(len(pesos))]
        nuevos = {i for i in range(len(pesos)) if i not in fijos and anchos[i] < minimos[i]}
        if not nuevos:
            return anchos
        fijos |= nuevos
    return anchos


def _tabla(b: dict, est: dict, par) -> list:
    cols = b["columnas"]
    anchos = b.get("anchos") or [1] * len(cols)
    tot = float(sum(anchos))
    minimos = [_ancho_minimo(c) for c in cols]
    cw = _repartir(FRAME_W, [a / tot for a in anchos], minimos)
    dest = b.get("destacar_fila")
    filas = [[par(c, est["tab_cab"], etiquetas=False) for c in cols]]
    for k, fila in enumerate(b["filas"]):
        celdas = []
        for c in fila:
            txt = _celda(c)
            if k == dest:
                txt = f"<b>{txt}</b>"
            celdas.append(par(txt, est["tab_cel"]))
        filas.append(celdas)
    t = Table(filas, colWidths=cw, repeatRows=1)
    estilo = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY_TAB),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, LINE),
    ]
    if len(filas) > 1:
        estilo.append(("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, BEIGE]))
    t.setStyle(TableStyle(estilo))
    t.spaceAfter = 10
    titulo = par(b["titulo"], est["tab_tit"]) if b.get("titulo") else None
    if len(b["filas"]) <= 5:  # tabla corta: entera con su título
        return [KeepTogether([titulo, t] if titulo else [t])]
    # tabla larga: se parte entre páginas; el título solo viaja con las primeras filas
    out = [CondPageBreak(90)]
    if titulo:
        out.append(par(b["titulo"], ParagraphStyle("tt", parent=est["tab_tit"], keepWithNext=0)))
    out.append(t)
    return out


def generar(data: dict, salida: str | Path) -> int:
    """Genera el PDF; devuelve el número de páginas. Lanza ErroresEntrada si no valida."""
    errs = validar(data)
    if errs:
        raise ErroresEntrada(errs)
    _registrar_dejavu()
    meta = data["meta"]
    est = _estilos()
    doc = Documento(
        str(salida),
        meta,
        title=sin_marcas(meta["titulo"]),
        author=meta.get("autor") or "",
        subject=meta.get("subtitulo") or meta.get("tagline") or "",
        keywords=", ".join(meta.get("palabras_clave") or []),
        creator="generar_informe.py (ReportLab)",
    )
    doc.multiBuild(construir_historia(data, est))
    return doc.page


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write(
            "Uso: python3 scripts/informe/generar_informe.py ENTRADA.json SALIDA.pdf\n"
        )
        return 1
    entrada, salida = Path(argv[1]), Path(argv[2])
    try:
        data = json.loads(entrada.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.stderr.write(f"Error: no existe el archivo de entrada {entrada}\n")
        return 1
    except UnicodeDecodeError:
        sys.stderr.write(f"Error: {entrada} no está en UTF-8\n")
        return 1
    except json.JSONDecodeError as ex:
        sys.stderr.write(
            f"Error: JSON inválido en {entrada}, línea {ex.lineno}, columna {ex.colno}: {ex.msg}\n"
        )
        return 2
    try:
        paginas = generar(data, salida)
    except ErroresEntrada as ex:
        sys.stderr.write(f"Error: la entrada no es válida ({len(ex.errores)} problema(s)):\n")
        for linea in ex.errores[:30]:
            sys.stderr.write(f"  - {linea}\n")
        if len(ex.errores) > 30:
            sys.stderr.write(f"  ... y {len(ex.errores) - 30} más\n")
        return 2
    print(f"PDF generado: {salida} ({paginas} páginas)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

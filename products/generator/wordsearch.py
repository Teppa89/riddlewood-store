"""
Reusable word-search puzzle pack generator -> print-ready PDF.

Produces a multi-puzzle pack with cover, instructions, puzzle pages and
solution pages, in A4 or US Letter. Designed for selling printable PDFs
on Etsy / Gumroad. Pure-Python (fpdf2), no external design tools.

Usage:
    from wordsearch import build_pack, Puzzle
    build_pack(brand="Riddlewood", pack_title="Coffee Lover's Word Search",
               subtitle="20 cozy puzzles for coffee people",
               puzzles=[Puzzle("Coffee Drinks", ["ESPRESSO", ...]), ...],
               out_path="out.pdf", page_format="A4")

Run directly to generate the sample Coffee pack in A4 + Letter.
"""
from __future__ import annotations

import random
import string
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from fpdf import FPDF, XPos, YPos

# 8 directions: E, S, W, N, SE, NE, SW, NW
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


@dataclass
class Puzzle:
    title: str
    words: list[str]
    grid_size: int = 15
    # filled at generation time
    grid: list[list[str]] = field(default_factory=list)
    solution_cells: set = field(default_factory=set)
    placed: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)


def _clean(word: str) -> str:
    return "".join(ch for ch in word.upper() if ch.isalpha())


def generate_grid(size: int, words: list[str], seed: Optional[int] = None):
    """Place words in 8 directions, fill the rest with random letters."""
    rnd = random.Random(seed)
    grid = [[None] * size for _ in range(size)]
    solution_cells: set[tuple[int, int]] = set()
    placed: list[str] = []
    skipped: list[str] = []

    for raw in sorted(words, key=lambda w: len(_clean(w)), reverse=True):
        word = _clean(raw)
        if not word or len(word) > size:
            skipped.append(raw)
            continue
        done = False
        for _ in range(300):
            dr, dc = rnd.choice(DIRECTIONS)
            # valid start range so the word fits
            r0 = rnd.randint(0, size - 1)
            c0 = rnd.randint(0, size - 1)
            r_end = r0 + dr * (len(word) - 1)
            c_end = c0 + dc * (len(word) - 1)
            if not (0 <= r_end < size and 0 <= c_end < size):
                continue
            ok = True
            cells = []
            for i, ch in enumerate(word):
                r = r0 + dr * i
                c = c0 + dc * i
                cur = grid[r][c]
                if cur is not None and cur != ch:
                    ok = False
                    break
                cells.append((r, c, ch))
            if not ok:
                continue
            for r, c, ch in cells:
                grid[r][c] = ch
                solution_cells.add((r, c))
            placed.append(word)
            done = True
            break
        if not done:
            skipped.append(raw)

    for r in range(size):
        for c in range(size):
            if grid[r][c] is None:
                grid[r][c] = rnd.choice(string.ascii_uppercase)
    return grid, solution_cells, placed, skipped


class PackPDF(FPDF):
    def __init__(self, brand: str, page_format: str = "A4"):
        super().__init__(orientation="P", unit="mm", format=page_format)
        self.brand = brand
        self.set_auto_page_break(auto=False)
        self.set_title("")  # set by caller

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, self.brand, align="L")
        self.cell(0, 8, str(self.page_no()), align="R")
        self.set_text_color(0, 0, 0)


def _draw_grid(pdf: PackPDF, puzzle: Puzzle, top_mm: float, highlight: bool):
    size = puzzle.grid_size
    margin = pdf.l_margin
    avail = pdf.w - 2 * margin
    cell = min(avail / size, 9.0)  # mm per cell, cap for readability
    grid_w = cell * size
    x0 = (pdf.w - grid_w) / 2
    y0 = top_mm
    pdf.set_font("Courier", "B", max(7, min(12, int(cell * 1.6))))
    for r in range(size):
        for c in range(size):
            x = x0 + c * cell
            y = y0 + r * cell
            is_sol = (r, c) in puzzle.solution_cells
            if highlight and is_sol:
                pdf.set_fill_color(210, 224, 210)
                pdf.rect(x, y, cell, cell, style="DF")
            else:
                pdf.set_draw_color(220, 220, 220)
                pdf.rect(x, y, cell, cell, style="D")
            pdf.set_xy(x, y)
            pdf.cell(cell, cell, puzzle.grid[r][c], align="C")
    return y0 + grid_w  # bottom y


def _draw_wordlist(pdf: PackPDF, words: list[str], top_mm: float):
    pdf.set_xy(pdf.l_margin, top_mm + 6)
    pdf.set_font("Helvetica", "", 11)
    cols = 4
    col_w = (pdf.w - 2 * pdf.l_margin) / cols
    words_sorted = sorted(set(_clean(w) for w in words if _clean(w)))
    for i, w in enumerate(words_sorted):
        if i % cols == 0 and i > 0:
            pdf.ln(6)
            pdf.set_x(pdf.l_margin)
        pdf.cell(col_w, 6, w, align="L")


def _cover(pdf: PackPDF, pack_title: str, subtitle: str, count: int,
           color: tuple = (34, 45, 40)):
    pdf.add_page()
    pdf.set_fill_color(*color)
    pdf.rect(0, 0, pdf.w, pdf.h, style="F")
    pdf.set_text_color(245, 240, 230)
    pdf.set_y(pdf.h * 0.32)
    pdf.set_font("Helvetica", "B", 30)
    pdf.multi_cell(0, 12, pack_title, align="C")
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 14)
    pdf.multi_cell(0, 8, subtitle, align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 12)
    pdf.multi_cell(0, 8, f"{count} puzzles  -  with full solutions", align="C")
    pdf.set_y(pdf.h - 24)
    pdf.set_font("Helvetica", "B", 13)
    pdf.multi_cell(0, 8, pdf.brand, align="C")
    pdf.set_text_color(0, 0, 0)


def _instructions(pdf: PackPDF):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 14, "How to play", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 12)
    body = (
        "Find every word from the list hidden in the grid. Words run in all "
        "eight directions: horizontal, vertical and diagonal, forwards or "
        "backwards. Circle each word as you find it.\n\n"
        "Solutions for every puzzle are at the back of this pack.\n\n"
        "This is a printable PDF for personal use. Print on A4 or US Letter, "
        "or solve on a tablet. Enjoy!"
    )
    pdf.multi_cell(0, 7, body)


def build_pack(brand: str, pack_title: str, subtitle: str,
               puzzles: list[Puzzle], out_path: str,
               page_format: str = "A4", seed: int = 7,
               theme_color: tuple = (34, 45, 40)) -> str:
    pdf = PackPDF(brand=brand, page_format=page_format)
    pdf.set_title(pack_title)
    pdf.set_author(brand)

    # generate grids (deterministic per pack+title for reproducibility)
    for idx, p in enumerate(puzzles):
        g, sol, placed, skipped = generate_grid(p.grid_size, p.words, seed=seed + idx)
        p.grid, p.solution_cells, p.placed, p.skipped = g, sol, placed, skipped

    _cover(pdf, pack_title, subtitle, len(puzzles), theme_color)
    _instructions(pdf)

    # puzzle pages
    for n, p in enumerate(puzzles, 1):
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 12, f"Puzzle {n}: {p.title}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        bottom = _draw_grid(pdf, p, top_mm=pdf.get_y() + 2, highlight=False)
        _draw_wordlist(pdf, p.words, bottom)

    # solution pages
    for n, p in enumerate(puzzles, 1):
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, f"Solution {n}: {p.title}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        _draw_grid(pdf, p, top_mm=pdf.get_y() + 2, highlight=True)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    pdf.output(out_path)
    return out_path


# --------------------------------------------------------------------------
# Sample pack: "Coffee Lover's Word Search" (giftable, evergreen, Pinterest-y)
# --------------------------------------------------------------------------
SAMPLE_PUZZLES = [
    Puzzle("Coffee Drinks", [
        "ESPRESSO", "LATTE", "CAPPUCCINO", "MOCHA", "MACCHIATO", "AMERICANO",
        "CORTADO", "FLATWHITE", "RISTRETTO", "AFFOGATO", "DOPPIO", "CACAO"]),
    Puzzle("Brewing Methods", [
        "FRENCHPRESS", "POUROVER", "AEROPRESS", "MOKA", "DRIP", "SIPHON",
        "COLDBREW", "PERCOLATOR", "CHEMEX", "ESPRESSO", "STEEP", "FILTER"]),
    Puzzle("Cafe Vibes", [
        "AROMA", "BARISTA", "CREMA", "FOAM", "MUG", "BEANS", "ROAST",
        "GRINDER", "STEAM", "COZY", "REFILL", "CAFFEINE"]),
    Puzzle("Coffee Around The World", [
        "ITALY", "ETHIOPIA", "COLOMBIA", "BRAZIL", "VIENNA", "TURKISH",
        "CUBANO", "IRISH", "VIETNAM", "KENYA", "GUATEMALA", "JAVA"]),
    Puzzle("Coffee And Sweets", [
        "BISCOTTI", "CROISSANT", "TIRAMISU", "MUFFIN", "BROWNIE", "DONUT",
        "COOKIE", "SCONE", "CARAMEL", "VANILLA", "CINNAMON", "HAZELNUT"]),
]

if __name__ == "__main__":
    brand = "Riddlewood"
    base = Path(__file__).resolve().parents[1] / "coffee-lovers-word-search"
    for fmt, suffix in (("A4", "A4"), ("Letter", "US-Letter")):
        # fresh Puzzle objects per format (grids regenerated, same seed -> identical)
        puzzles = [Puzzle(p.title, list(p.words)) for p in SAMPLE_PUZZLES]
        out = base / f"Coffee-Lovers-Word-Search_{suffix}.pdf"
        path = build_pack(brand, "Coffee Lover's Word Search",
                          "Cozy puzzles for people who run on coffee",
                          puzzles, str(out), page_format=fmt)
        placed = sum(len(p.placed) for p in puzzles)
        skipped = sum(len(p.skipped) for p in puzzles)
        print(f"{fmt}: {path}  (placed={placed}, skipped={skipped})")

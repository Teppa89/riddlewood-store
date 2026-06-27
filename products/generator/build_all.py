"""Build the full launch catalog: every theme -> A4 + US Letter PDF.

Run:  .venv/bin/python products/generator/build_all.py
Outputs to products/<slug>/<slug>_<A4|US-Letter>.pdf and prints a QC table
(placed vs skipped words). skipped must be 0 for a shippable pack.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wordsearch import build_pack, Puzzle  # noqa: E402
from themes import THEMES  # noqa: E402

BRAND = "Riddlewood"
PRODUCTS_DIR = Path(__file__).resolve().parents[1]


def main() -> int:
    total_skipped = 0
    print(f"{'PACK':36} {'PUZZLES':>7} {'PLACED':>7} {'SKIPPED':>7}")
    for t in THEMES:
        placed = skipped = 0
        for fmt, suffix in (("A4", "A4"), ("Letter", "US-Letter")):
            puzzles = [Puzzle(p.title, list(p.words)) for p in t["puzzles"]]
            out = PRODUCTS_DIR / t["slug"] / f"{t['slug']}_{suffix}.pdf"
            build_pack(BRAND, t["title"], t["subtitle"], puzzles, str(out),
                       page_format=fmt, theme_color=t["color"])
            if fmt == "A4":  # count once
                placed = sum(len(p.placed) for p in puzzles)
                skipped = sum(len(p.skipped) for p in puzzles)
        total_skipped += skipped
        flag = "" if skipped == 0 else "  <-- FIX"
        print(f"{t['slug']:36} {len(t['puzzles']):>7} {placed:>7} {skipped:>7}{flag}")
    print(f"\nTotal packs: {len(THEMES)} | files: {len(THEMES) * 2} | total skipped: {total_skipped}")
    return 1 if total_skipped else 0


if __name__ == "__main__":
    sys.exit(main())

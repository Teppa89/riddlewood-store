"""One-command build: regenerate every sellable asset.

Runs the PDF generator (12 packs x A4 + US Letter), the image generator
(Etsy gallery + Gumroad covers + Pinterest pins + brand), and (re)builds the
per-pack zips and the full bundle zip.

    .venv/bin/python build.py
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "products" / "generator"
sys.path.insert(0, str(GEN))

import build_all  # noqa: E402
import images  # noqa: E402
from themes import THEMES  # noqa: E402

PRODUCTS = ROOT / "products"


def make_zips() -> int:
    all_pdfs = []
    for t in THEMES:
        slug = t["slug"]
        base = PRODUCTS / slug
        pdfs = [base / f"{slug}_A4.pdf", base / f"{slug}_US-Letter.pdf"]
        with zipfile.ZipFile(base / f"{slug}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for p in pdfs:
                z.write(p, p.name)
        all_pdfs += pdfs
    bundle = PRODUCTS / "big-word-search-bundle"
    bundle.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(bundle / "big-word-search-bundle.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in all_pdfs:
            z.write(p, p.name)
    return len(THEMES)


if __name__ == "__main__":
    print("== PDFs ==")
    rc = build_all.main()
    print("\n== images ==")
    images.main()
    print("\n== zips ==")
    n = make_zips()
    print(f"\nBuild complete: {n} packs (PDFs + images + zips) + 120-puzzle bundle.")
    sys.exit(rc)

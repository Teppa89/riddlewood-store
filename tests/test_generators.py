"""Quality gates for the product pipeline.

Run: .venv/bin/pytest tests/
Locks in the two guarantees that matter as the catalog scales:
  - every themed puzzle places all its words (no skipped words, full grid)
  - every listing meets Etsy constraints and its assets exist on disk
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "products" / "generator"))
sys.path.insert(0, str(ROOT / "automation" / "etsy_api"))

import pytest  # noqa: E402
from wordsearch import generate_grid  # noqa: E402
from themes import THEMES  # noqa: E402
import listings_data as L  # noqa: E402

ALL_LISTINGS = L.PACKS + [L.bundle()]
LISTING_IDS = [p["slug"] for p in ALL_LISTINGS]


def test_catalog_size():
    assert len(THEMES) >= 12
    for t in THEMES:
        assert len(t["puzzles"]) == 10, t["slug"]


@pytest.mark.parametrize("theme", THEMES, ids=[t["slug"] for t in THEMES])
def test_every_word_places(theme):
    for p in theme["puzzles"]:
        grid, sol, placed, skipped = generate_grid(15, list(p.words), seed=7)
        assert not skipped, f"{theme['slug']} / {p.title}: skipped {skipped}"
        assert all(cell is not None for row in grid for cell in row)
        assert sol, "no solution cells recorded"


@pytest.mark.parametrize("pack", ALL_LISTINGS, ids=LISTING_IDS)
def test_listing_constraints(pack):
    assert len(pack["title"]) <= 140, f"title too long: {len(pack['title'])}"
    assert len(pack["tags"]) == 13
    assert all(len(t) <= 20 for t in pack["tags"]), [t for t in pack["tags"] if len(t) > 20]
    assert len(set(pack["tags"])) == len(pack["tags"]), "duplicate tags"


@pytest.mark.parametrize("pack", ALL_LISTINGS, ids=LISTING_IDS)
def test_listing_assets_exist(pack):
    assert Path(pack["file"]).exists(), pack["file"]
    assert pack["images"], "no images"
    for img in pack["images"]:
        assert Path(img).exists(), img

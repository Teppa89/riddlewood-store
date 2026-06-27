"""Listing data for every Riddlewood pack -> Etsy fields + asset paths.

Mirrors marketing/etsy-listings.md. Paths resolve to repo files that
publish_all.py uploads via the API (read from local disk).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRICE = 4.49
BUNDLE_PRICE = 14.99


def _assets(slug, bundle=False):
    base = ROOT / "products" / slug
    imgs = [base / "img" / f"{slug}_etsy_main.png"]
    pins = ROOT / "marketing" / "pins"
    for p in (pins / f"{slug}_pin1.png", pins / f"{slug}_pin2.png"):
        if p.exists():
            imgs.append(p)
    zip_path = base / f"{slug}.zip"
    return [str(p) for p in imgs], str(zip_path)


def _pack(slug, title, tags, description, price=PRICE):
    images, file_path = _assets(slug)
    return {"slug": slug, "title": title, "tags": tags, "description": description,
            "price": price, "images": images, "file": file_path}


PACKS = [
    _pack(
        "coffee-lovers-word-search",
        "Coffee Word Search Printable | 10 Coffee Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Coffee Lovers",
        ["coffee word search", "printable puzzles", "coffee lover gift", "word search pdf",
         "coffee gift idea", "puzzle book pdf", "adult word search", "cafe printable",
         "coffee puzzles", "instant download", "word puzzle game", "barista gift", "activity printable"],
        "Calling all coffee lovers! 10 cozy coffee-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). "
        "Print at home or solve on a tablet (GoodNotes / Notability).\n\n"
        "GREAT FOR: gifts for coffee lovers, baristas, cozy nights, travel, classroom downtime.\n\n"
        "Instant digital download (2 PDF files). No physical item shipped. Personal use only; not for resale.\n(c) Riddlewood",
    ),
    _pack(
        "cat-lovers-word-search",
        "Cat Word Search Printable | 10 Cat Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Cat Lovers",
        ["cat word search", "printable puzzles", "cat lover gift", "word search pdf",
         "cat gift idea", "puzzle book pdf", "adult word search", "cat mom gift",
         "cat puzzles", "instant download", "word puzzle game", "crazy cat lady", "activity printable"],
        "For everyone owned by a cat! 10 purr-fect cat-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: cat lover gifts, cat moms and dads, relaxing breaks, kids and adults.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "garden-word-search",
        "Garden Word Search Printable | 10 Gardening Puzzles PDF | Relaxing Adult Word Search | Instant Download Gift for Plant Lovers",
        ["garden word search", "printable puzzles", "gardener gift", "word search pdf",
         "plant lover gift", "puzzle book pdf", "adult word search", "gardening gift",
         "garden puzzles", "instant download", "word puzzle game", "nature printable", "activity printable"],
        "A relaxing pick for green thumbs! 10 garden-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve digitally.\n\n"
        "GREAT FOR: gardener gifts, plant lovers, calm afternoons, seniors, classrooms.\n\n"
        "Instant digital download (2 PDF files). No physical product. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "self-care-word-search",
        "Self Care Word Search Printable | 10 Mindfulness Puzzles PDF | Relaxing Adult Word Search | Calm Self Care Gift Download",
        ["selfcare word search", "printable puzzles", "mindfulness gift", "word search pdf",
         "self care gift", "puzzle book pdf", "adult word search", "relaxing puzzle",
         "calm puzzles", "instant download", "word puzzle game", "wellness printable", "anxiety relief"],
        "Slow down and unwind. 10 gentle self-care and mindfulness word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: self-care gifts, mindfulness routines, anxiety-relief breaks, cozy evenings.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "beach-summer-word-search",
        "Beach Word Search Printable | 10 Summer Puzzles PDF | Adult Word Search Book | Beach Vacation Activity | Instant Download",
        ["beach word search", "summer printable", "vacation activity", "word search pdf",
         "summer gift idea", "puzzle book pdf", "adult word search", "travel printable",
         "beach puzzles", "instant download", "word puzzle game", "kids activity", "activity printable"],
        "Bring on the sunshine! 10 beach and summer word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: summer road trips, beach bags, vacation downtime, kids and adults.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "christmas-word-search",
        "Christmas Word Search Printable | 10 Holiday Puzzles PDF | Adult Word Search Book | Stocking Stuffer | Instant Download Xmas",
        ["christmas wordsearch", "holiday printable", "stocking stuffer", "word search pdf",
         "christmas activity", "puzzle book pdf", "adult word search", "xmas gift idea",
         "holiday puzzles", "instant download", "word puzzle game", "family activity", "classroom printable"],
        "Festive fun for the whole family! 10 Christmas word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: stocking stuffers, classroom parties, Christmas Eve, family game night.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
]


def bundle():
    slug = "big-word-search-bundle"
    base = ROOT / "products" / slug
    images = [str(ROOT / "products" / "coffee-lovers-word-search" / "img" / "coffee-lovers-word-search_etsy_main.png")]
    return {"slug": slug, "price": BUNDLE_PRICE, "file": str(base / f"{slug}.zip"), "images": images,
            "title": "Word Search Bundle Printable | 60 Adult Word Search Puzzles PDF | 6 Themes | Instant Download Gift",
            "tags": ["word search bundle", "printable puzzles", "puzzle bundle pdf", "word search pdf",
                     "adult word search", "puzzle book pdf", "gift for grandma", "instant download",
                     "word puzzle game", "puzzles for adults", "activity printable", "senior activity", "large print puzzle"],
            "description": "The whole collection! 6 themed packs - Coffee, Cats, Garden, Self-Care, Beach and Christmas - "
                           "60 word search puzzles with full solutions. Best value.\n\n"
                           "WHAT YOU GET: 60 unique puzzles across 6 themes + answer keys, in A4 and US Letter.\n\n"
                           "Instant digital download. No physical item. Personal use only; no resale.\n(c) Riddlewood"}

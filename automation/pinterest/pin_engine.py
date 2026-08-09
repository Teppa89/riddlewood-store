"""Pinterest Pin Engine — automated daily pinning with tracking.

Picks unpinned theme+variant+board combos, creates pins via API with
SEO-optimized descriptions, tracks everything in pin_tracker.json.

Run:  .venv/bin/python automation/pinterest/pin_engine.py [--count 5] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TRACKER_PATH = HERE / "pin_tracker.json"
RESULTS_PATH = HERE.parent / "etsy_api" / "results.json"

sys.path.insert(0, str(ROOT / "products" / "generator"))
from themes import THEMES  # noqa: E402
from images import PIN_PERSONAS  # noqa: E402

BOARDS = [
    "Printable Word Search Puzzles",
    "Word Search Puzzles for Adults",
    "Printable Puzzle Gifts",
    "Self Care & Relaxing Printables",
    "Seasonal & Holiday Printables",
]

BOARD_WEIGHTS = {
    "christmas-word-search": ["Seasonal & Holiday Printables", "Printable Puzzle Gifts"],
    "halloween-word-search": ["Seasonal & Holiday Printables", "Printable Puzzle Gifts"],
    "fall-thanksgiving-word-search": ["Seasonal & Holiday Printables", "Printable Puzzle Gifts"],
    "baby-shower-word-search": ["Seasonal & Holiday Printables", "Printable Puzzle Gifts"],
    "self-care-word-search": ["Self Care & Relaxing Printables", "Printable Word Search Puzzles"],
    "yoga-mindfulness-word-search": ["Self Care & Relaxing Printables", "Word Search Puzzles for Adults"],
    "nursing-word-search": ["Self Care & Relaxing Printables", "Printable Puzzle Gifts"],
    "fitness-word-search": ["Self Care & Relaxing Printables", "Word Search Puzzles for Adults"],
}

ETSY_SHOP_URL = "https://www.etsy.com/listing"

VARIANT_TITLES = {
    1: "{title} — Printable Word Search Puzzles",
    2: "{title} — Instant Download PDF",
    3: "Can You Find All 12 Words? — {title}",
    4: "Perfect Gift for {persona} — Word Search Puzzles",
    5: "{title} — Relaxing Brain Exercise",
}


def _etsy_url(slug: str) -> str:
    if RESULTS_PATH.exists():
        results = json.loads(RESULTS_PATH.read_text())
        for r in results:
            if r["slug"] == slug:
                return f"{ETSY_SHOP_URL}/{r['listing_id']}"
    return f"https://www.etsy.com/shop/RiddlewoodCo"


def _pin_description(theme: dict, variant: int) -> str:
    slug = theme["slug"]
    title = theme["title"]
    persona = PIN_PERSONAS.get(slug, "Puzzle Lovers")
    clean_title = title.replace(" Word Search", "")

    base_keywords = [
        "word search puzzles", "printable puzzles", "word search pdf",
        "adult word search", "instant download", "puzzle printable",
        "brain games", "word games",
    ]

    theme_keywords = []
    if "coffee" in slug:
        theme_keywords = ["coffee lover gift", "coffee printable"]
    elif "cat" in slug:
        theme_keywords = ["cat lover gift", "cat printable"]
    elif "dog" in slug:
        theme_keywords = ["dog lover gift", "dog printable"]
    elif "garden" in slug:
        theme_keywords = ["gardening gift", "garden printable"]
    elif "christmas" in slug:
        theme_keywords = ["christmas printable", "holiday activity"]
    elif "halloween" in slug:
        theme_keywords = ["halloween printable", "halloween activity"]
    elif "farm" in slug:
        theme_keywords = ["farm printable", "country living"]
    elif "beach" in slug:
        theme_keywords = ["summer printable", "beach activity"]
    elif "hiking" in slug:
        theme_keywords = ["hiking gift", "outdoor printable"]
    elif "book" in slug:
        theme_keywords = ["book lover gift", "reading printable"]
    elif "teacher" in slug:
        theme_keywords = ["teacher gift", "classroom activity"]
    elif "baby" in slug:
        theme_keywords = ["baby shower game", "baby shower activity"]
    elif "nursing" in slug:
        theme_keywords = ["nurse gift", "healthcare worker gift"]
    elif "video" in slug:
        theme_keywords = ["gamer gift", "video game printable"]
    elif "dinosaur" in slug:
        theme_keywords = ["dinosaur printable", "dino activity"]
    elif "mytholog" in slug:
        theme_keywords = ["mythology printable", "greek mythology"]
    elif "wine" in slug:
        theme_keywords = ["wine lover gift", "wine printable"]
    elif "fitness" in slug:
        theme_keywords = ["fitness gift", "workout printable"]
    elif "yoga" in slug:
        theme_keywords = ["yoga gift", "mindfulness printable"]
    elif "travel" in slug:
        theme_keywords = ["travel gift", "wanderlust printable"]
    elif "music" in slug:
        theme_keywords = ["music lover gift", "music printable"]
    elif "camping" in slug:
        theme_keywords = ["camping gift", "outdoor activity"]
    elif "fishing" in slug:
        theme_keywords = ["fishing gift", "fishing printable"]
    elif "horse" in slug:
        theme_keywords = ["horse lover gift", "equestrian printable"]
    elif "butterfly" in slug or "butterflies" in slug:
        theme_keywords = ["nature printable", "butterfly activity"]
    elif "wildlife" in slug:
        theme_keywords = ["wildlife printable", "safari activity"]
    elif "bird" in slug:
        theme_keywords = ["birdwatcher gift", "bird printable"]
    elif "flower" in slug:
        theme_keywords = ["flower printable", "botanical gift"]
    elif "space" in slug:
        theme_keywords = ["space printable", "astronomy gift"]
    elif "ocean" in slug:
        theme_keywords = ["ocean printable", "sea life activity"]
    elif "sport" in slug:
        theme_keywords = ["sports gift", "sports printable"]
    elif "baking" in slug:
        theme_keywords = ["baking gift", "baking printable"]
    elif "cooking" in slug:
        theme_keywords = ["cooking gift", "kitchen printable"]
    elif "movie" in slug:
        theme_keywords = ["movie night activity", "movie printable"]
    elif "tea" in slug:
        theme_keywords = ["tea lover gift", "tea printable"]
    elif "self-care" in slug:
        theme_keywords = ["self care activity", "relaxation gift"]

    descriptions = {
        1: (
            f"{title} — 10 themed word search puzzles with full answer keys. "
            f"Perfect for {persona.lower()}! Printable PDF in A4 and US Letter sizes. "
            f"Instant download — print at home and start solving. "
            f"Great gift idea or relaxing activity for yourself.\n\n"
        ),
        2: (
            f"Looking for a fun printable activity? This {clean_title} pack includes "
            f"10 unique word search puzzles, each with a full solution page. "
            f"Download instantly and print at home in A4 or US Letter. "
            f"Perfect brain exercise for adults and teens!\n\n"
        ),
        3: (
            f"Think you can find all 12 hidden words? Try this {clean_title} challenge! "
            f"10 unique word search grids packed with themed vocabulary. "
            f"Each puzzle comes with its full answer key. "
            f"Printable PDF — download and print instantly.\n\n"
        ),
        4: (
            f"Looking for the perfect gift for {persona.lower()}? "
            f"This printable word search pack features 10 themed puzzles "
            f"they'll love. Complete with answer keys, available in A4 and US Letter. "
            f"Instant download — print at home or at your local print shop.\n\n"
        ),
        5: (
            f"Relax, focus, and have fun with this {clean_title} word search pack. "
            f"10 unique puzzles designed for a calming brain workout. "
            f"Each puzzle has a full answer key. Print at home in A4 or US Letter. "
            f"A beautiful way to unwind while exercising your mind.\n\n"
        ),
    }

    all_keywords = theme_keywords + base_keywords
    random.seed(f"{slug}-{variant}")
    random.shuffle(all_keywords)
    keyword_line = " · ".join(all_keywords[:6])

    return descriptions[variant] + keyword_line


def _pin_image_path(slug: str, variant: int) -> Path:
    return ROOT / "marketing" / "pins" / f"{slug}_pin{variant}.png"


def load_tracker() -> dict:
    if TRACKER_PATH.exists():
        return json.loads(TRACKER_PATH.read_text())
    return {"pins": [], "board_ids": {}}


def save_tracker(tracker: dict):
    TRACKER_PATH.write_text(json.dumps(tracker, indent=2))


def _is_pinned(tracker: dict, slug: str, variant: int, board: str) -> bool:
    for p in tracker["pins"]:
        if p["slug"] == slug and p["variant"] == variant and p["board"] == board:
            return True
    return False


def pick_next_pins(tracker: dict, count: int = 5) -> list[dict]:
    candidates = []
    for theme in THEMES:
        slug = theme["slug"]
        preferred = BOARD_WEIGHTS.get(slug, BOARDS[:3])
        all_boards = preferred + [b for b in BOARDS if b not in preferred]

        for variant in range(1, 6):
            img = _pin_image_path(slug, variant)
            if not img.exists():
                continue
            for board in all_boards:
                if not _is_pinned(tracker, slug, variant, board):
                    pinned_count = sum(
                        1 for p in tracker["pins"] if p["slug"] == slug
                    )
                    candidates.append({
                        "slug": slug,
                        "variant": variant,
                        "board": board,
                        "theme": theme,
                        "priority": -pinned_count,
                    })

    candidates.sort(key=lambda c: (c["priority"], c["slug"], c["variant"]))
    seen_slugs_this_batch: dict[str, int] = {}
    selected = []
    for c in candidates:
        if len(selected) >= count:
            break
        slug_count = seen_slugs_this_batch.get(c["slug"], 0)
        if slug_count >= 2:
            continue
        seen_slugs_this_batch[c["slug"]] = slug_count + 1
        selected.append(c)

    return selected


def post_pins(pins: list[dict], dry_run: bool = False) -> list[dict]:
    if not dry_run:
        from pinterest_client import PinterestClient
        client = PinterestClient()
        boards = client.list_boards()
        board_map = {}
        for b in boards:
            board_map[b["name"]] = b["id"]

    tracker = load_tracker()
    results = []

    for pin_info in pins:
        slug = pin_info["slug"]
        variant = pin_info["variant"]
        board = pin_info["board"]
        theme = pin_info["theme"]

        persona = PIN_PERSONAS.get(slug, "Puzzle Lovers")
        title_template = VARIANT_TITLES[variant]
        pin_title = title_template.format(title=theme["title"], persona=persona)
        if len(pin_title) > 100:
            pin_title = pin_title[:97] + "..."
        description = _pin_description(theme, variant)
        link = _etsy_url(slug)
        img_path = _pin_image_path(slug, variant)

        if dry_run:
            print(f"  [DRY] {slug} v{variant} → {board}")
            print(f"         title: {pin_title}")
            print(f"         link:  {link}")
            print(f"         image: {img_path.name}")
            result = {"pin_id": "dry-run", "status": "dry-run"}
        else:
            board_id = board_map.get(board)
            if not board_id:
                print(f"  [SKIP] Board '{board}' not found on Pinterest")
                continue
            result = client.create_pin(
                board_id=board_id,
                title=pin_title,
                description=description,
                link=link,
                image_path=img_path,
            )
            print(f"  [OK] {slug} v{variant} → {board} (pin: {result.get('id', '?')})")
            time.sleep(3)

        if not dry_run:
            tracker["pins"].append({
                "slug": slug,
                "variant": variant,
                "board": board,
                "pin_id": result.get("id", "unknown"),
                "posted_at": datetime.now(timezone.utc).isoformat(),
            })
        results.append(result)

    if not dry_run:
        save_tracker(tracker)
    return results


def stats(tracker: dict):
    total = len(tracker["pins"])
    themes_pinned = len(set(p["slug"] for p in tracker["pins"]))
    total_possible = len(THEMES) * 5 * len(BOARDS)
    print(f"\nPin Engine Stats:")
    print(f"  Pins posted:    {total} / {total_possible} possible")
    print(f"  Themes covered: {themes_pinned} / {len(THEMES)}")
    print(f"  Coverage:       {total / total_possible * 100:.1f}%")

    by_board: dict[str, int] = {}
    for p in tracker["pins"]:
        by_board[p["board"]] = by_board.get(p["board"], 0) + 1
    print(f"  By board:")
    for b in BOARDS:
        print(f"    {b}: {by_board.get(b, 0)}")


def main():
    parser = argparse.ArgumentParser(description="Pinterest Pin Engine")
    parser.add_argument("--count", type=int, default=5, help="Pins to post (default 5)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--stats", action="store_true", help="Show pin stats")
    parser.add_argument("--seed-tracker", action="store_true",
                        help="Seed tracker with already-posted pins (from progress.md)")
    args = parser.parse_args()

    tracker = load_tracker()

    if args.stats:
        stats(tracker)
        return

    if args.seed_tracker:
        print("Seeding tracker with previously posted pins...")
        _seed_existing(tracker)
        save_tracker(tracker)
        stats(tracker)
        return

    pins = pick_next_pins(tracker, args.count)
    if not pins:
        print("All pins posted! Nothing to do.")
        return

    print(f"Posting {len(pins)} pins{' (dry run)' if args.dry_run else ''}:")
    post_pins(pins, dry_run=args.dry_run)
    tracker = load_tracker()
    stats(tracker)


def _seed_existing(tracker: dict):
    """Seed tracker with the ~49 pins already posted via browser."""
    already_pinned = [
        ("coffee-lovers-word-search", 1, "Printable Word Search Puzzles"),
        ("cat-lovers-word-search", 1, "Printable Word Search Puzzles"),
        ("dog-lovers-word-search", 1, "Printable Word Search Puzzles"),
        ("beach-summer-word-search", 1, "Printable Word Search Puzzles"),
        ("garden-word-search", 1, "Printable Word Search Puzzles"),
        ("wine-lovers-word-search", 1, "Printable Word Search Puzzles"),
        ("travel-word-search", 1, "Printable Word Search Puzzles"),
        ("self-care-word-search", 1, "Printable Word Search Puzzles"),
        ("tea-lovers-word-search", 1, "Printable Word Search Puzzles"),
        ("fishing-word-search", 1, "Printable Word Search Puzzles"),
        ("music-lovers-word-search", 1, "Printable Puzzle Gifts"),
        ("yoga-mindfulness-word-search", 1, "Self Care & Relaxing Printables"),
        ("sports-word-search", 1, "Word Search Puzzles for Adults"),
        ("ocean-sea-word-search", 1, "Seasonal & Holiday Printables"),
        ("cooking-baking-word-search", 1, "Printable Puzzle Gifts"),
        ("flowers-word-search", 1, "Self Care & Relaxing Printables"),
        ("horses-word-search", 1, "Word Search Puzzles for Adults"),
        ("birds-word-search", 1, "Self Care & Relaxing Printables"),
        ("camping-word-search", 1, "Word Search Puzzles for Adults"),
        ("farm-word-search", 1, "Printable Puzzle Gifts"),
        ("space-word-search", 1, "Printable Puzzle Gifts"),
        ("farm-word-search", 2, "Printable Word Search Puzzles"),
        ("garden-word-search", 2, "Self Care & Relaxing Printables"),
        ("camping-word-search", 2, "Printable Word Search Puzzles"),
        ("horses-word-search", 2, "Printable Puzzle Gifts"),
        ("fishing-word-search", 2, "Word Search Puzzles for Adults"),
        ("birds-word-search", 2, "Printable Puzzle Gifts"),
        ("hiking-word-search", 1, "Word Search Puzzles for Adults"),
        ("butterflies-word-search", 1, "Printable Puzzle Gifts"),
        ("wildlife-word-search", 1, "Printable Word Search Puzzles"),
        ("fitness-word-search", 1, "Self Care & Relaxing Printables"),
        ("movie-night-word-search", 1, "Printable Puzzle Gifts"),
        ("baking-word-search", 1, "Printable Word Search Puzzles"),
        ("book-lovers-word-search", 1, "Word Search Puzzles for Adults"),
        ("teachers-word-search", 1, "Seasonal & Holiday Printables"),
        ("big-word-search-bundle", 1, "Printable Puzzle Gifts"),
        ("dinosaurs-word-search", 1, "Printable Puzzle Gifts"),
        ("baby-shower-word-search", 1, "Seasonal & Holiday Printables"),
        ("nursing-word-search", 1, "Self Care & Relaxing Printables"),
        ("video-games-word-search", 1, "Word Search Puzzles for Adults"),
        ("mythology-word-search", 1, "Printable Word Search Puzzles"),
    ]
    existing_set = {(p["slug"], p["variant"], p["board"]) for p in tracker["pins"]}
    added = 0
    for slug, variant, board in already_pinned:
        if (slug, variant, board) not in existing_set:
            tracker["pins"].append({
                "slug": slug,
                "variant": variant,
                "board": board,
                "pin_id": "browser-manual",
                "posted_at": "2026-08-09T00:00:00+00:00",
            })
            added += 1
    print(f"  Added {added} existing pins to tracker.")


if __name__ == "__main__":
    main()

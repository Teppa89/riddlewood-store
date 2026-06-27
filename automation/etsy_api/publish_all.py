"""Create all Riddlewood listings on Etsy as DRAFTS via the API.

Pipeline per pack: create_draft_listing -> upload images (main + pins) ->
upload digital file (zip) -> set tags. Listings are left in DRAFT so you
review them in Etsy, then publish. Re-runnable; logs results to results.json.

Run (after auth.py + Etsy app approved):
    .venv/bin/python automation/etsy_api/publish_all.py            # 6 packs
    .venv/bin/python automation/etsy_api/publish_all.py --bundle   # + bundle
    .venv/bin/python automation/etsy_api/publish_all.py --only coffee-lovers-word-search
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from etsy_client import EtsyClient  # noqa: E402
from listings_data import PACKS, bundle  # noqa: E402

RESULTS = Path(__file__).resolve().parent / "results.json"
FALLBACK_TAXONOMY = 6772  # "Puzzles" — verified/overridden at runtime


def publish_one(client: EtsyClient, shop_id: int, taxonomy_id: int, item: dict) -> dict:
    print(f"\n== {item['slug']} ==")
    listing = client.create_draft_listing(
        shop_id, title=item["title"], description=item["description"],
        price=item["price"], taxonomy_id=taxonomy_id, tags=item["tags"])
    listing_id = listing["listing_id"]
    print(f"  draft listing_id={listing_id}")

    for rank, img in enumerate(item.get("images", []), start=1):
        if Path(img).exists():
            client.upload_image(shop_id, listing_id, img, rank=rank)
            print(f"  image rank {rank}: {Path(img).name}")
        else:
            print(f"  MISSING image: {img}")

    if Path(item["file"]).exists():
        client.upload_file(shop_id, listing_id, item["file"])
        print(f"  file: {Path(item['file']).name}")
    else:
        print(f"  MISSING file: {item['file']}")

    url = f"https://www.etsy.com/your/shops/me/tools/listings/{listing_id}"
    return {"slug": item["slug"], "listing_id": listing_id, "edit_url": url}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", action="store_true", help="also create the 60-puzzle bundle")
    ap.add_argument("--only", help="single slug to publish")
    args = ap.parse_args()

    client = EtsyClient()
    shop_id = client.get_shop_id()
    print(f"Shop ID: {shop_id}")
    taxonomy_id = client.find_taxonomy_id("Puzzles") or FALLBACK_TAXONOMY
    print(f"Taxonomy (Puzzles) id: {taxonomy_id}")

    items = list(PACKS)
    if args.bundle:
        items.append(bundle())
    if args.only:
        items = [i for i in items if i["slug"] == args.only]
        if not items:
            raise SystemExit(f"No pack with slug {args.only}")

    results = json.loads(RESULTS.read_text()) if RESULTS.exists() else []
    done = {r["slug"] for r in results}
    for item in items:
        if item["slug"] in done:
            print(f"skip {item['slug']} (already in results.json)")
            continue
        try:
            results.append(publish_one(client, shop_id, taxonomy_id, item))
            RESULTS.write_text(json.dumps(results, indent=2))
        except Exception as e:  # keep going; fix and re-run
            print(f"  ERROR on {item['slug']}: {e}")

    print(f"\nDone. {len(results)} draft listings. Review + publish in Etsy.")
    print(f"Results: {RESULTS}")


if __name__ == "__main__":
    main()

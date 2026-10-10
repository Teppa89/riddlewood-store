"""Push SEO-optimized titles, tags, and descriptions to all Etsy listings.

Reads from listings_data.py (source of truth) + results.json (listing IDs).
Uses EtsyClient to PATCH each listing via API.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from etsy_client import EtsyClient
from listings_data import PACKS, bundle

SHOP_ID = 66735289


def main():
    results_path = Path(__file__).parent / "results.json"
    with open(results_path) as f:
        results = json.load(f)

    slug_to_id = {r["slug"]: r["listing_id"] for r in results}

    client = EtsyClient()
    all_items = PACKS + [bundle()]

    updated = 0
    failed = 0

    for item in all_items:
        slug = item["slug"]
        listing_id = slug_to_id.get(slug)
        if not listing_id:
            print(f"  SKIP {slug} — no listing ID in results.json")
            continue

        try:
            client.update_listing(
                SHOP_ID, listing_id,
                title=item["title"],
                description=item["description"],
                tags=",".join(item["tags"][:13]),
            )
            updated += 1
            print(f"  OK   {slug} (#{listing_id})")
            time.sleep(0.5)
        except Exception as e:
            failed += 1
            print(f"  FAIL {slug}: {e}")

    print(f"\nDone: {updated} updated, {failed} failed, {len(all_items) - updated - failed} skipped")


if __name__ == "__main__":
    main()

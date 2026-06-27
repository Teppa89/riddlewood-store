"""Gumroad sales monitor (read-only API). Prints per-product sales + revenue.

Setup: Gumroad -> Settings -> Advanced -> Applications -> generate an access
token, then put it in automation/gumroad/.env:
    GUMROAD_ACCESS_TOKEN=xxxxx

Run: .venv/bin/python automation/gumroad/stats.py
Can be scheduled (cron) for a daily report — no manual checking needed.
"""
import os
import sys
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
API = "https://api.gumroad.com/v2"


def load_token() -> str:
    env = HERE / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith("GUMROAD_ACCESS_TOKEN="):
                return line.split("=", 1)[1].strip()
    return os.environ.get("GUMROAD_ACCESS_TOKEN", "")


def main() -> int:
    token = load_token()
    if not token:
        raise SystemExit(
            "No token. Gumroad -> Settings -> Advanced -> Applications -> generate "
            "a token, then put GUMROAD_ACCESS_TOKEN=... in automation/gumroad/.env")
    r = requests.get(f"{API}/products", params={"access_token": token}, timeout=30)
    r.raise_for_status()
    products = r.json().get("products", [])
    if not products:
        print("No products found.")
        return 0
    total_sales = total_cents = 0
    print(f"{'PRODUCT':52}{'SALES':>7}{'REVENUE':>12}")
    print("-" * 71)
    for p in sorted(products, key=lambda x: x.get("sales_count", 0), reverse=True):
        sc = p.get("sales_count", 0) or 0
        cents = p.get("sales_usd_cents", 0) or 0
        total_sales += sc
        total_cents += cents
        name = (p.get("name", "") or "")[:50]
        print(f"{name:52}{sc:>7}{'$%.2f' % (cents / 100):>12}")
    print("-" * 71)
    print(f"{'TOTAL':52}{total_sales:>7}{'$%.2f' % (total_cents / 100):>12}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

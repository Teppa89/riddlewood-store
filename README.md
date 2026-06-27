# Riddlewood — Printable Word Search Business

Autonomous digital-product business: printable word-search puzzle packs sold as
instant-download PDFs on **Etsy** and **Gumroad**, with **Pinterest** as the
traffic engine. Every product is generated 100% from code (no external design
tools), so the catalog scales at near-zero marginal cost.

## Status
- **12 themed packs / 120 puzzles** generated, each with A4 + US Letter PDFs,
  a 6-image Etsy gallery, a Gumroad cover, and 2 Pinterest pins.
- **LIVE:** Coffee pack on Gumroad — https://riddlewood.gumroad.com/l/coffee-word-search
- **Etsy API automation** built; pending Etsy app approval to mass-publish listings.

## Repository
```
products/generator/   wordsearch.py (PDF gen), themes.py (catalog), images.py (marketing), build_all.py
products/<slug>/       generated PDFs (A4 + US Letter), <slug>.zip, img/ (gallery PNGs)
marketing/             etsy-listings.md, pins/, brand/, go-live-runbook.md, pinterest-plan.md
automation/etsy_api/   Etsy Open API v3 engine (auth.py, etsy_client.py, listings_data.py, publish_all.py)
planning/              knowledge base: roadmap, decisions, risks, progress, context_summary
research/              market-analysis.md
build.py               regenerate every asset (PDFs + images + zips)
tests/                 pytest quality gates
```

## Build
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python build.py     # regenerate all PDFs, images, zips
.venv/bin/pytest tests/       # verify guarantees
```

## Add a theme
Append a dict to `THEMES` in `products/generator/themes.py` (10 puzzles, color),
add a matching `_pack(...)` in `automation/etsy_api/listings_data.py`, then run
`build.py`. Tests enforce: all words place, titles <= 140 chars, 13 tags <= 20 chars.

## Publish to Etsy (once the app is approved)
See `automation/etsy_api/README.md`. In short: fill `.env`, run `auth.py`
(authorize once), then `publish_all.py` creates every listing as a draft with
images + files uploaded from disk. Review and publish in Etsy.

## Channels
- **Etsy** — primary (organic search + Pinterest). Automated via API.
- **Gumroad** — mirror (no organic traffic; driven by Pinterest). Manual upload.
- **Pinterest** — free traffic engine. See `marketing/pinterest-plan.md`.
- **Amazon KDP** — future channel (print puzzle books) at ~0 marginal cost.

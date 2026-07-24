# Riddlewood — Autonomous Business Engine

## Privacy (ABSOLUTE)
Real name "mattia agosto", email "teppa89@gmail.com", handle "teppalicious" must NEVER appear anywhere — public or repo, directly or indirectly. Public brand = ONLY "Riddlewood". Git author = "Riddlewood <noreply@riddlewood.local>".

## Session Startup — Auto-Execute
Every session, BEFORE responding to the user, run this checklist silently:

### 1. Pull latest (Theme Factory may have pushed)
```bash
cd "/Users/AMattia/Desktop/Claude/guadagna automatico"
git pull origin main 2>/dev/null || true
```

### 2. Check for unpublished themes
Compare `listings_data.py` pack functions vs `results.json` entries. Any theme in listings_data without a results.json entry = unpublished. If found:
- Activate venv: `source .venv/bin/activate`
- Run `python automation/etsy_api/publish_all.py` to publish via API
- Update bundle if new themes were published (title, desc, images, file)

### 3. Stats check (bi-weekly)
Read `planning/progress.md` — check date of last stats entry. If >12 days ago:
- Navigate to Etsy dashboard stats via Chrome MCP browser
- Record: visits, orders, revenue, traffic sources, top listings
- Compare with previous entry
- Update progress.md with new entry
- Make recommendations based on data

### 4. Pinterest maintenance
Check `planning/progress.md` for pin count. If new products were published since last pin session:
- Pin each new product to an appropriate board via `pinterest.com/pin/create/button/?url=<listing-url>`
- Max 5 pins per session (Pinterest rate limit)
- Distribute across 5 boards: Printable Word Search Puzzles, Word Search Puzzles for Adults, Printable Puzzle Gifts, Self Care & Relaxing Printables, Seasonal & Holiday Printables

### 5. Report to user
Brief summary: what was auto-done, current stats snapshot, any items needing user action.

## Project Architecture
- `products/generator/themes.py` — master theme definitions
- `products/generator/build_all.py` — PDF generation pipeline
- `products/generator/images.py` — marketing image generation
- `products/generator/bundle_images.py` — bundle collage generator
- `automation/etsy_api/etsy_client.py` — Etsy API client (OAuth + refresh)
- `automation/etsy_api/listings_data.py` — listing metadata per theme
- `automation/etsy_api/publish_all.py` — batch publish via API
- `automation/etsy_api/results.json` — published listing IDs (gitignored)
- `automation/etsy_api/.env` — API credentials (gitignored)
- `automation/etsy_api/token.json` — OAuth tokens (gitignored)
- `planning/strategy.md` — growth strategy
- `planning/progress.md` — activity log
- `planning/context_summary.md` — current state snapshot

## Key Constraints
- Grid: 15x15, words ≤15 chars, 12 words/puzzle, 10 puzzles/theme
- Etsy: tags ≤20 chars, 13 tags max, title ≤140 chars, price €4.49/pack, €19.99/bundle
- Etsy API: x-api-key = `keystring:shared_secret`; shop ID = 66735289
- Etsy image quirk: upload new images BEFORE deleting old ones (min 1 image)
- Pinterest: scrape takes 20-40s; max 5 pins/session; distribute across boards
- Bundle: dynamically includes ALL themes
- Communication: /caveman ultra active

## Scheduled Cloud Agents
- **Theme Factory** (routine `trig_01Sedw7pQKUCZXi1GLGHBwJu`): runs 1st & 15th of month, 9am Italy. Creates 5 new themes, builds, commits, pushes to GitHub.
- GitHub repo: https://github.com/Teppa89/riddlewood-store (private)

## User-Only Pending Actions
- [ ] Verify bank account: Etsy → Finanze → Conto dei pagamenti → "Inizia"
- [ ] Activate Etsy Ads: 1€/day on Farm + Beach Summer + Hiking

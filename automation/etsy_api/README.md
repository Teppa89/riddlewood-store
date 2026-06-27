# Etsy API automation — Riddlewood

Durable engine: create listings + upload images + digital files via **Etsy Open
API v3**, reading assets from local disk (no browser-upload limits). Scales to
hundreds of listings with zero manual clicking.

## One-time setup (USER — ~10 min)
1. Go to https://www.etsy.com/developers/your-apps and **Create a New App**
   (register as a developer first if prompted).
2. App name: `Riddlewood Automation`.
   Purpose (write something like): *"Create and manage my own shop's digital
   printable listings (word search PDFs)."*
3. After creation Etsy shows your **keystring** (API key) and **shared secret**.
4. Set the OAuth **redirect URI** to: `http://localhost:3003/callback`
5. The app starts in **Personal Access** (your own shop) and is submitted for
   Etsy review — access may take a few days. That's the long pole, so do this
   first to start the clock.
6. Copy `.env.example` -> `.env` and paste your keystring + shared secret
   (you paste them; secrets stay on your machine, used only against Etsy's API).

## Scopes used
`listings_r listings_w email_r shops_r`

## Architecture (built by Claude)
- `auth.py` — OAuth2 + PKCE: opens the consent URL, catches the redirect on
  localhost:3003, exchanges code for token, stores `token.json` (auto-refresh).
- `etsy_client.py` — thin wrappers: getMe, getShop, createDraftListing,
  updateListingInventory (price/qty), uploadListingImage, uploadListingFile,
  updateListing (tags/taxonomy).
- `listings_data.py` — each pack -> title, description, price, 13 tags,
  taxonomy_id, who_made/when_made, image paths, file (zip) path.
- `publish_all.py` — loops packs: create DRAFT listing -> upload images ->
  upload digital file -> set tags. You review drafts in Etsy, then publish.

## Run (after Etsy approval + .env filled)
```
.venv/bin/python automation/etsy_api/auth.py         # one-time authorize
.venv/bin/python automation/etsy_api/publish_all.py  # create all draft listings
```

## Why this over the browser
Chrome MCP `file_upload` only accepts files the user drag-drops into chat — not
autonomous. The API uploads files Claude reads from disk directly. Build once,
reuse forever.

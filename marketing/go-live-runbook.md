# Go-Live Runbook (M2) — pilotato da Claude nel browser

Prereq: utente loggato su Etsy / Gumroad / Pinterest nel Chrome connesso.
Claude guida via Chrome MCP. Claude NON inserisce mai dati banca/ID/pagamento.

## Asset per pack (slug = nome cartella)
- File vendibile: `products/<slug>/<slug>.zip` (A4 + US Letter) — oppure i 2 PDF singoli
- Immagine listing: `products/<slug>/img/<slug>_etsy_main.png`
- Pin: `marketing/pins/<slug>_pin1.png`, `_pin2.png`
- Testi/tag/prezzo: `marketing/etsy-listings.md`

## Ordine consigliato
1. **Gumroad** (più veloce, dà subito link condivisibili)
2. **Etsy** (listing principali; traffico)
3. **Pinterest** (pin che puntano ai listing)

## Gumroad — nuovo prodotto (per pack)
1. Products → New product → Digital product.
2. Name (da etsy-listings.md), prezzo 4.49.
3. Upload `<slug>.zip`. Cover = `<slug>_etsy_main.png`.
4. Descrizione (da file). Publish → copia URL prodotto.

## Etsy — nuovo listing (per pack)
1. Shop Manager → Listings → Add a listing.
2. Photos: `<slug>_etsy_main.png` (principale).
3. Title (da file). Type: **Digital**. Upload `<slug>.zip` (o 2 PDF).
4. About → "A finished product"; chi l'ha fatto/quando come da form.
5. Category: Puzzles. Price: 4.49 USD.
6. Tags: incolla i 13 tag. Pubblica ($0,20/listing).
7. (Opz.) Sale 20% off 14 giorni per prime recensioni.

## Pinterest — pin (per pack)
1. Create → Pin. Upload `pin1` (pin2 come pin "fresh" dopo qualche giorno).
2. Titolo + descrizione keyword-rich (dal listing). Link = URL Etsy/Gumroad.
3. Board a tema ("Printable Word Search", "Coffee Gifts", ecc.).
4. Stagionalità: Christmas pin da ott; Beach/Summer ora; evergreen sempre.

## Dopo go-live (M3)
- Etsy Stats + Gumroad analytics + Pinterest analytics → kill prodotti morti, raddoppia sui vincenti.
- Sforna nuovi temi col generatore (`build_all.py` / `images.py`) → verso 300 listing.

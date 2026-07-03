# Context Summary

## Executive Summary (≤500w)
Business digitale autonomo. Founder: skill-zero, <5h/sett, budget lean ≤50€ fase 1, obiettivo 500–1k€/mese veloce e scalabile. Motore operativo = Claude (produzione + automazione); utente solo autorizza/paga/credenziali. Modello: **A — prodotti digitali** su Etsy+Gumroad, traffico Pinterest. Prodotto: **puzzle/worksheet printable PDF** generati via codice — nicchia low-competition (creazione manuale tediosa per umani) dove automazione = moat reale, produzione costo 0. Extra: multilingue italiano (competizione ~0 su Etsy anglofono) + espansione Amazon KDP a costo marginale nullo. Strategia: volume di listing ultra-nicchiati (top seller fanno 300+), fulfillment automatico, Pinterest = traffico gratis compounding. Metodologia GSD lightweight per minimizzare coinvolgimento utente.

## Current State (≤300w)
**9/12 prodotti LIVE su Gumroad** (riddlewood.gumroad.com/l/<slug>): coffee-word-search, beach-summer-word-search, cat-lovers-word-search, dog-lovers-word-search, garden-word-search, self-care-word-search, wine-lovers-word-search, tea-lovers-word-search, travel-word-search. Tutti €4.49, cover orizzontali, brand Riddlewood. **15 pin Pinterest** su **5 bacheche** (Printable Word Search Puzzles + Word Search for Adults + Printable Puzzle Gifts + Self Care & Relaxing + Seasonal & Holiday). 15 prodotti pinnati (9 evergreen→Gumroad/Etsy + Music/Yoga/Sports/Ocean/Cooking/Flowers→Etsy). **Pinning AUTONOMO** (no upload): `pinterest.com/pin/create/button/?url=<listing>` scrapa l'immagine → click sulla RIGA bacheca (o campo Cerca) = salva. Multi-bacheca: ogni prodotto su più bacheche nel tempo. Restano ~12 prodotti da pinnare. Privacy pulita ovunque (nome/email/handle scrubsati; profilo Gumroad+Pinterest=Riddlewood/riddlewood/riddlewoodshop). Repo committato. **ETSY: 25 listing LIVE** (shop RiddlewoodCo, EUR, via API; 24 pack €4.49 + bundle €19.99/120 puzzle; gallery + file + 13 tag + categoria Puzzles; titoli SEO-ottimizzati Etsy). Catalogo: **24 temi/240 puzzle** (12 orig + 12 nuovi: music, cooking-baking, ocean-sea, birds, camping, yoga-mindfulness, sports, flowers, farm, space, fishing, horses). Motore Etsy API validato — FIX chiave: x-api-key = `keystring:shared_secret`. Privacy Etsy ok (nome titolare pubblico = "Riddlewood", non il nome reale). Stagionali (Halloween/Fall/Christmas): live su Etsy, NON ancora pinnati su Pinterest (rimandati a set-ott). Costo: 0€. VINCOLI OPERATIVI: upload Gumroad/Pinterest = manuale (file-pick utente; Chrome MCP file_upload accetta solo file droppati in chat — NON basta); board Pinterest si creano da SAFARI (estensione Chrome blocca il modal), i pin si pubblicano da Chrome (doppio click su Pubblica); cadenza pin 1-3/giorno (account nuovo, anti-spam).

## Open Tasks
- [x] Pipeline + catalogo 12 pack + marketing + brand + engineering
- [x] 9 prodotti evergreen LIVE su Gumroad + 4 pin Pinterest
- [x] Privacy scrub completo (Gumroad/git/Pinterest)
- [ ] **Pin AUTONOMI** (verso bundle + stagionali a stagione + 2°pin/repeat) → 1-3/giorno via `pinterest.com/pin/create/button/?url=<etsy-listing-url>` (scrape immagine, no upload), board "Printable Word Search Puzzles", click Salva. [9 evergreen già pinnati]
- [x] **Etsy: 13 listing LIVE via API** (12 pack + bundle €19.99) + shop testi/privacy completi
- [x] Stagionali (halloween/fall/christmas): LIVE su Etsy. Pin Pinterest a stagione (set-ott)
- [ ] **USER-only:** icona+banner shop Etsy (2 upload file). [Stato venditore UE = GIÀ "Privato"/corretto — shop editor → fondo → Dati del venditore; nessuna azione finché privato]
- [ ] Futuro: Amazon KDP; pin variations (pin2); P.IVA prima di scalare incassi (utente)

## Key Decisions
Modello A · prodotto PDF printable puzzle · budget ≤50€ · GSD lightweight · geo IT-UE. Dettaglio: decisions.md

## Risks
Vedi risks.md. Top: saturazione (mitig. low-comp+volume) · ban Etsy nuovo (warm-up+mirror Gumroad) · traffico lento (Pinterest) · P.IVA (utente).

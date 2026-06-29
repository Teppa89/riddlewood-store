# Context Summary

## Executive Summary (≤500w)
Business digitale autonomo. Founder: skill-zero, <5h/sett, budget lean ≤50€ fase 1, obiettivo 500–1k€/mese veloce e scalabile. Motore operativo = Claude (produzione + automazione); utente solo autorizza/paga/credenziali. Modello: **A — prodotti digitali** su Etsy+Gumroad, traffico Pinterest. Prodotto: **puzzle/worksheet printable PDF** generati via codice — nicchia low-competition (creazione manuale tediosa per umani) dove automazione = moat reale, produzione costo 0. Extra: multilingue italiano (competizione ~0 su Etsy anglofono) + espansione Amazon KDP a costo marginale nullo. Strategia: volume di listing ultra-nicchiati (top seller fanno 300+), fulfillment automatico, Pinterest = traffico gratis compounding. Metodologia GSD lightweight per minimizzare coinvolgimento utente.

## Current State (≤300w)
**9/12 prodotti LIVE su Gumroad** (riddlewood.gumroad.com/l/<slug>): coffee-word-search, beach-summer-word-search, cat-lovers-word-search, dog-lovers-word-search, garden-word-search, self-care-word-search, wine-lovers-word-search, tea-lovers-word-search, travel-word-search. Tutti €4.49, cover orizzontali, brand Riddlewood. **4 pin Pinterest live** (Coffee/Beach/Cat/Dog) sulla board "Printable Word Search Puzzles" → traffico. Privacy pulita ovunque (nome/email/handle scrubsati; profilo Gumroad+Pinterest=Riddlewood/riddlewood/riddlewoodshop). Repo committato. **ETSY: 12 listing LIVE** (shop RiddlewoodCo, EUR, creati+pubblicati via API; €4.49, gallery 6 img + file + 13 tag + categoria Puzzles ciascuno). Motore Etsy API validato — FIX chiave: x-api-key = `keystring:shared_secret`. Privacy Etsy ok (nome titolare pubblico = "Riddlewood", non il nome reale). Stagionali (Halloween/Fall/Christmas): live su Etsy, NON ancora pinnati su Pinterest (rimandati a set-ott). Costo: 0€. VINCOLI OPERATIVI: upload Gumroad/Pinterest = manuale (file-pick utente; Chrome MCP file_upload accetta solo file droppati in chat — NON basta); board Pinterest si creano da SAFARI (estensione Chrome blocca il modal), i pin si pubblicano da Chrome (doppio click su Pubblica); cadenza pin 1-3/giorno (account nuovo, anti-spam).

## Open Tasks
- [x] Pipeline + catalogo 12 pack + marketing + brand + engineering
- [x] 9 prodotti evergreen LIVE su Gumroad + 4 pin Pinterest
- [x] Privacy scrub completo (Gumroad/git/Pinterest)
- [ ] **DOMANI: pin restanti 5** (garden/self-care/wine/tea/travel) → 1-3/giorno. Flusso: Chrome pin-builder, utente carica marketing/pins/<slug>_pin1.png, Claude compila titolo/descr (da pinterest-plan.md) + link riddlewood.gumroad.com/l/<slug>, board auto, doppio-click Pubblica
- [ ] **Etsy: check approvazione app** → .env + auth.py + publish_all.py (12 listing auto + organico)
- [ ] Stagionali (halloween/fall-thanksgiving/christmas) → pubblicare a set-ott (preferib. via Etsy API)
- [ ] Futuro: Amazon KDP; pin variations (pin2); P.IVA prima di scalare incassi (utente)

## Key Decisions
Modello A · prodotto PDF printable puzzle · budget ≤50€ · GSD lightweight · geo IT-UE. Dettaglio: decisions.md

## Risks
Vedi risks.md. Top: saturazione (mitig. low-comp+volume) · ban Etsy nuovo (warm-up+mirror Gumroad) · traffico lento (Pinterest) · P.IVA (utente).

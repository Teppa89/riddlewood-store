# Context Summary

## Executive Summary (≤500w)
Business digitale autonomo. Founder: skill-zero, <5h/sett, budget lean ≤50€ fase 1, obiettivo 500–1k€/mese veloce e scalabile. Motore operativo = Claude (produzione + automazione); utente solo autorizza/paga/credenziali. Modello: **A — prodotti digitali** su Etsy+Gumroad, traffico Pinterest. Prodotto: **puzzle/worksheet printable PDF** generati via codice — nicchia low-competition (creazione manuale tediosa per umani) dove automazione = moat reale, produzione costo 0. Extra: multilingue italiano (competizione ~0 su Etsy anglofono) + espansione Amazon KDP a costo marginale nullo. Strategia: volume di listing ultra-nicchiati (top seller fanno 300+), fulfillment automatico, Pinterest = traffico gratis compounding. Metodologia GSD lightweight per minimizzare coinvolgimento utente.

## Current State (≤300w)
**Coffee LIVE su Gumroad** (riddlewood.gumroad.com/l/coffee-word-search, ~$4.49). Catalogo: **12 pack / 120 puzzle**, ognuno con PDF A4+Letter, zip, galleria Etsy 6 immagini, cover Gumroad orizzontale, 2 pin. Pipeline: venv+fpdf2+pillow, generatori riutilizzabili, build.py one-command, 39 test pytest verdi. Motore Etsy API (auth+client+listings_data+publish_all) pronto, NON testato live. Costo sostenuto: 0€. BLOCCHI esterni: (1) approvazione app Etsy (chiave in review) → poi publish_all crea tutti i listing in automatico (upload file/immagini da disco via API); (2) Pinterest board creation buggata sull'account (lato Pinterest, probabile conferma email) → pin pronti ma non pubblicabili. Upload browser Gumroad/Pinterest = manuale (file-pick utente; Chrome MCP file_upload accetta solo allegati). Prossimi gate (domani): email Pinterest + approvazione Etsy.

## Open Tasks
- [x] M0/M1: pipeline + catalogo + marketing + brand
- [x] Coffee LIVE su Gumroad (pagamento bank collegato)
- [x] Scala: 12 pack / 120 puzzle + galleria Etsy + engineering (test, build, README)
- [x] Motore Etsy API (pronto, non testato live)
- [ ] **BLOCCO: approvazione app Etsy** → poi publish_all (Claude)
- [ ] **BLOCCO: Pinterest board** (lato Pinterest; conferma email account) → poi pubblicare pin
- [ ] Gumroad: pubblicare gli altri 11 pack (upload manuale utente) — opzionale
- [ ] Futuro: canale Amazon KDP; più temi; pin variations; P.IVA prima di scalare incassi

## Key Decisions
Modello A · prodotto PDF printable puzzle · budget ≤50€ · GSD lightweight · geo IT-UE. Dettaglio: decisions.md

## Risks
Vedi risks.md. Top: saturazione (mitig. low-comp+volume) · ban Etsy nuovo (warm-up+mirror Gumroad) · traffico lento (Pinterest) · P.IVA (utente).

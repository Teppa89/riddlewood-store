# Progress Log

## 2026-06-27
- Discovery founder (4 domande chiave): skill-zero, <5h/sett, budget lean, obiettivo 500–1k€/mese veloce.
- Decisione: modello A (prodotti digitali) + budget lean ≤50€.
- Repo git init + struttura (planning / research / products / marketing).
- KB creata: decisions.md, risks.md, roadmap.md, context_summary.md.
- Ricerca mercato: 4 query → research/market-analysis.md. Nicchia individuata: **puzzle/worksheet printable** (low-comp, moat automazione, multilingue IT, espansione KDP).
- Master Execution Plan stilato (M0→M4).
- Toolchain: venv + fpdf2 2.8.7 (Python 3.14).
- Generatore riutilizzabile: products/generator/wordsearch.py (placement 8 direzioni, fill, cover, istruzioni, soluzioni evidenziate, A4+Letter, seed deterministico).
- PROOF generato + VERIFICATO: "Coffee Lover's Word Search" (Riddlewood), 5 puzzle, 60/60 parole, A4 + US Letter. Qualità = vendibile. **M0 DONE.**
- Checkpoint utente: English-first + brand Riddlewood confermati.
- Generatore esteso (colore cover per tema) + themes.py (6 temi) + build_all.py (batch + QC).
- **Catalogo lancio generato: 6 pack × 10 puzzle = 60 puzzle, 12 PDF (A4+Letter), 0 parole scartate.** Verificato Coffee + Christmas.
- Listing Etsy completi (titolo+13 tag SEO+descrizione+prezzo) per 6 pack + bundle → marketing/etsy-listings.md. Pricing: $4.49/pack, bundle $14.99.
- Generatore immagini (Pillow): 6 mockup Etsy 2000² + 12 pin Pinterest 1000×1500 + brand banner/icon. Verificati (qualità professionale, Georgia serif).
- **M1 COMPLETO.** Pacchetto lancio pronto: prodotti + listing + marketing + brand. Costo: 0€.
- BLOCCO REALE M2: utente crea account Etsy/Gumroad/Pinterest + pagamento + scelta fiscale. Poi Claude carica (eventualmente pilotando browser).

## 2026-06-27 (go-live + pivot API)
- Login utente OK (Gumroad/Etsy/Pinterest). Pilotato Gumroad: prodotto Coffee creato (nome, prezzo $4.49, descrizione, slug /l/coffee-word-search). Bozza, non pubblicata.
- BLOCCO tooling: Chrome MCP `file_upload` accetta SOLO file drag-droppati dall'utente; @-mention e grant-cartella NON bastano → browser-upload non autonomo.
- Ricerca API: Gumroad = no API (manuale); Etsy Open API v3 = sì (createDraftListing + uploadListingImage + uploadListingFile) ma serve registrare app + approvazione; Pinterest = gated.
- **PIVOT → Etsy API engine** (carica file da disco via HTTP, bypassa il limite browser). Scaffold creato: automation/etsy_api/ (.env.example + README con step registrazione). `requests` aggiunto al venv.
- NEXT: utente registra app Etsy (long pole = clock approvazione). Claude costruisce auth.py + etsy_client.py + listings_data.py + publish_all.py.
- **FATTO: motore Etsy API completo + validato.** auth.py (OAuth2+PKCE, callback localhost, token+refresh), etsy_client.py (wrapper: shop, taxonomy, createDraftListing, uploadImage, uploadFile, tags), listings_data.py (6 pack + bundle; titoli ≤140, 13 tag ≤20, asset verificati su disco), publish_all.py (crea draft + carica immagini+file, re-runnable, results.json). Compile OK, dati ALL OK. `requests` nel venv.
- Flusso: utente registra app Etsy + redirect `http://localhost:3003/callback` + approvazione → copia .env.example→.env con keystring+secret → Claude lancia auth.py (utente clicca Approva nel browser) → Claude lancia publish_all.py → crea TUTTI i listing draft → utente review+publish.
- PENDENTE Gumroad: Coffee = bozza pronta, manca solo drag del file zip (manuale, no API Gumroad).

## 2026-06-27 — PRIMO PRODOTTO LIVE
- Pagamento Gumroad collegato (bank/direct-deposit; PayPal bloccato da soglia $100/compliance).
- **Coffee PUBBLICATO + verificato LIVE:** https://riddlewood.gumroad.com/l/coffee-word-search — €3.94 (~$4.49). Pagina pro: cover, grid preview, badge, descrizione, buy button.
- Upload immagini/file su Gumroad = manuale (file-pick utente nel browser); Chrome MCP file_upload non utilizzabile.
- Pipeline end-to-end validata su piattaforma reale: codice → PDF → prodotto → listing → pubblicato.
- NEXT: Pinterest (pin → traffico, upload pin = file-pick utente); Etsy API quando approvata → scala il resto.

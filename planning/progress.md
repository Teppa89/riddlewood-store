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

## 2026-06-27 (sessione autonoma — scala + engineering)
- Catalogo raddoppiato: +6 temi (Dog, Halloween, Fall/Thanksgiving, Wine, Tea, Travel) → **12 pack / 120 puzzle**, 0 scarti.
- images.py potenziato: galleria Etsy (cover orizzontale Gumroad + whats_inside + two_sizes + sample_solution con soluzione evidenziata) + pin CTA neutro → 86 immagini (6 gallery/pack).
- listings_data.py: 6 nuovi pack + galleria 6 img/listing; bundle → 120 puzzle / 12 temi / $19.99.
- build.py: rigenerazione one-command (PDF + immagini + zip + bundle).
- Engineering: tests/ (pytest, **39 test verdi** — placement parole, vincoli Etsy, asset esistenti), requirements.txt, README progetto, .gitignore segreti.
- marketing/pinterest-plan.md: copy pin + board + cadenza stagionale per 12 pack.
- Validazione: 12 pack ALL OK (titoli ≤140, 13 tag ≤20, 6 img, zip).
- Pinterest pin Coffee: creato in builder ma board bloccata lato Pinterest (anche per utente → probabile conferma email account).
- NEXT (domani): conferma email/board Pinterest + approvazione app Etsy → publish_all in batch.

## 2026-06-27 (privacy scrub)
- Vincolo permanente: nome reale + email utente mai visibili, nemmeno indirettamente.
- Fatto: Gumroad nome profilo → Riddlewood; avatar iniziale rimosso; **username → riddlewood** (nuovo URL prodotto: riddlewood.gumroad.com/l/coffee-word-search, verificato live). Git history interamente riscritta (autore neutro + contenuti file + messaggi commit ripuliti).
- Verificato 0 residui su: pagina pubblica, file repo, history, messaggi commit, autori.
- Aperto (utente, opzionale): email login account → mail dedicata al brand; profilo Etsy in fase setup (evitare nome owner).

## 2026-06-27 (Pinterest sbloccato + 1° pin LIVE)
- Causa board-block: l'estensione Claude-in-Chrome blocca il modal "crea bacheca". **WORKAROUND: creare le board da Safari** (lato server → poi visibili anche in Chrome). Pubblicazione pin in Chrome funziona.
- Email account Pinterest = confermata → NON era quello il blocco.
- Privacy Pinterest sistemata: Nome → "Riddlewood", username → "riddlewoodshop" (riddlewood preso), avatar "R", sito web → store.
- Board "Printable Word Search Puzzles" creata (pubblica).
- **PRIMO PIN PINTEREST PUBBLICATO** (Coffee), link aggiornato a riddlewood.gumroad.com/l/coffee-word-search. Verificato live (profilo riddlewoodshop, board 1 Pin).
- Nota: pin Coffee usa immagine vecchia ("Find it on Etsy"); da sostituire coi pin neutri rigenerati.
- NEXT: più pin quando più prodotti live (Etsy API in attesa approvazione; Gumroad manuale).

## 2026-06-28 (Gumroad mirror + batch pin)
- **4 prodotti Gumroad LIVE:** Coffee, Beach, Cat, Dog (riddlewood.gumroad.com/l/<slug>), cover orizzontali, €4.49, brand Riddlewood.
- **4 pin Pinterest LIVE** (1/prodotto) sulla board "Printable Word Search Puzzles" → traffico verso i 4 prodotti. Immagine pin neutra ("Printable Puzzles · Riddlewood").
- Learning Gumroad: il resize finestra cambia le coordinate (verificare prima di click ciechi); creazione prodotto = pagina deve essere caricata prima di compilare.
- Learning Pinterest: Pubblica pin = doppio click; board si auto-mantiene tra pin.
- Decisione utente: prioritizzare pin dei live (traffico) vs mirror completo Gumroad (canale senza traffico organico).
- NEXT: altri 8 prodotti Gumroad + pin (grind) OPPURE attendere Etsy API (auto, 0 upload, traffico organico di ricerca)."

## 2026-06-28 (catalogo evergreen completo su Gumroad)
- **9/12 prodotti Gumroad LIVE** (tutti evergreen + estivo): Coffee, Beach, Cat, Dog, Garden, Self-Care, Wine, Tea, Travel. €4.49, cover orizzontali, brand Riddlewood, slug puliti (riddlewood.gumroad.com/l/<slug>).
- 3 stagionali RIMANDATI alla stagione: Halloween / Fall-Thanksgiving / Christmas (pin off-season inutili ora; pubblicare a set-ott, probabilmente via Etsy API).
- Pin Pinterest: 4 live oggi (Coffee/Beach/Cat/Dog). Restanti 5 (Garden/Self-Care/Wine/Tea/Travel) da distribuire 1-3/giorno (Pinterest penalizza i pin a raffica).
- NEXT: pin restanti 5 (cadenza giornaliera); Etsy API all'approvazione (auto 12 + traffico organico); stagionali a stagione."

## 2026-06-29 (ETSY LIVE — 12 listing via API)
- App Etsy approvata. **Bug auth scoperto+risolto:** x-api-key deve essere `keystring:shared_secret` (non solo keystring) — altrimenti 403.
- Shop aperto dall'utente: **RiddlewoodCo**, valuta EUR, digital onboarded. Taxonomy Puzzles=1559.
- **publish_all.py → 12 listing creati via API** (6 immagini galleria + file digitale + 13 tag + €4.49 ciascuno, categoria Puzzles, who=i_did, when=2020_2026), poi PATCH state=active → **12 LIVE**.
- **Privacy:** nome profilo pubblico "mattia agosto" → "Riddlewood" (verificato su etsy.com/shop/RiddlewoodCo: nessun nome reale pubblico).
- Prezzo: €4.49 base; Etsy mostra €5.48 incl. IVA 22% IT (IVA gestita/remessa da Etsy, NON intacca il netto venditore).
- Shop pubblico live: etsy.com/shop/RiddlewoodCo — 12 articoli, 0 vendite (nuovo).
- **Shop completato (testi via browser):** slogan/SEO-title "Printable Word Search Puzzles | Instant Download PDF" (meta Google), annuncio, storia About (brand, no nome reale). Policy resi: Etsy auto-applica "Resi e cambi non accettati" agli articoli digitali (12 listing coperti) — corretto, niente da fare.
- APERTO (utente): icona + banner shop (2 upload file, cosmetici); **stato venditore UE** (Impostazioni → Dati del venditore — fiscale + dati personali → decisione utente, legato a P.IVA; possibile "1 fattore" visibilità).
- **BUNDLE Etsy LIVE:** big-word-search-bundle €19.99 (120 puzzle / 12 temi) creato+pubblicato via API → **shop 13 listing attivi** (12 pack + bundle). Alza AOV. Generata cover bundle corretta (collage 12 cover + "What's Inside") via products/generator/bundle_images.py — la vecchia img era solo la cover Coffee (fuorviante per un bundle).
- NEXT: Etsy SEO ramp (settimane, come Pinterest); pin restanti; pin verso i listing Etsy.

## 2026-06-29 (Pinterest pinning AUTONOMO + 5 pin → Etsy)
- **SCOPERTA: pin senza upload.** URL `pinterest.com/pin/create/button/?url=<URL-pagina-live>` → Pinterest scrapa l'immagine principale della pagina (no file-pick!) → scegli board → "Salva". Supera il vincolo storico "upload pin = manuale" PER pagine live. Scrape ~10-20s (schermo grigio), poi Salva = 1 click sulla board.
- **5 pin nuovi → listing Etsy** (board "Printable Word Search Puzzles"): Garden, Wine, Travel, Self-Care, Tea. Immagine = cover Etsy scrapeata, link → listing Etsy (anche segnale traffico off-site = SEO Etsy).
- Totale pin: **9** (4 ieri → Gumroad; 5 oggi → Etsy). **TUTTI i 9 evergreen ora pinnati.**
- Restano (AUTONOMI): pin → bundle + stagionali (a stagione) + 2°pin/repeat → prossimi giorni.
- **Stato venditore UE = già "Privato"** (corretto; path: shop editor → fondo → "Dati del venditore" → "Modifica") — nessuna azione finché si vende da privato. Mio path precedente ("Impostazioni") era errato.
- USER-only rimasto: SOLO icona+banner shop Etsy (2 upload file).

## 2026-06-29 (icona+banner caricati + 1° scam message)
- Utente ha caricato **icona + banner** → dashboard conferma "Logo ✓ / Banner ✓" (Personalizza negozio 4/5; 5° item = "foto venditore" = **SKIP per privacy**). Shop ora completo.
- **Primo messaggio Etsy = phishing scam.** Mittente "PROFILE VERIFY - CLICK ETSLLY.COM" (typosquat di etsy.com) + esca "is this item still available?". Azione: **Segnala → spostato in Spam**. NON aperto, NON cliccato il link, NON risposto.
- **POLICY scam (ricorrente su shop nuovi):** messaggi con link esterni / "verifica account" / paga fuori Etsy / WhatsApp/email = spam → Segnala, mai cliccare, login SOLO su etsy.com. Messaggi legittimi = domande reali sui prodotti, senza link/urgenza.

## 2026-06-29 (SEO: titoli ottimizzati + flag visibilità RISOLTO)
- "1 fattore" di visibilità Etsy = suggeriva titoli più chiari per i 13 listing. Valutati prima di accettare: puliti, keyword core mantenute (tema + "Word Search Puzzles" + formato + "Full Solutions"); perse "printable"/"adult"/gift-terms → **restano nei tag** (13/listing). Reversibile via API.
- **Accettati tutti i 13** (Etsy li premia esplicitamente + allineati al SEO Etsy attuale anti-stuffing; nuovo shop senza dati → seguo guida Etsy). 11 al 1° tentativo + 2 (Garden/Coffee) al retry dopo errore transitorio.
- **Flag RISOLTO:** pagina visibilità ora "Il tuo negozio è impostato per il successo!" — 3/3 verde (negozio ✓, tutte le inserzioni ✓, servizio clienti = attende 5 ordini).
- Nota: titoli live Etsy ora divergono da listings_data.py (che resta con gli originali, usati solo per eventuale ricreazione di NUOVI listing). Non sincronizzato = basso valore.

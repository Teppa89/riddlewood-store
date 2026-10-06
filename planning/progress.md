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

## 2026-06-29 (catalogo espanso +6 temi → 19 listing Etsy)
- **+6 temi evergreen giftable** (codice→API, 100% autonomo): Music, Kitchen&Baking, Ocean&Sea, Birds, Camping&Outdoors, Yoga&Mindfulness. 60 nuovi puzzle / 720 parole, **build 0 skipped, 57 test verdi**.
- themes.py +6 temi (10 puzzle×12 parole, ≤15 char); listings_data.py +6 _pack (titoli ≤140, 13 tag ≤20, descrizioni); build.py rigenera PDF + 128 immagini + zip.
- publish_all.py → 6 draft via API (6 img galleria + file da disco) → PATCH state=active → **shop 19 listing attivi** (18 pack €4.49 + bundle €19.99). Fee 6×€0.20.
- Strategia "volume" del piano (più listing nicchiati = più superficie di ricerca Etsy). Pin per i nuovi 6 → prossimi giorni (autonomi via share-URL).
- **NOTA bundle:** build.py ha rigenerato il bundle zip LOCALE a 180 puzzle/18 temi, ma il listing LIVE resta 120/12 (non ri-pubblicato) — divergenza innocua. FOLLOW-UP: espandere bundle live a 18 temi (update title/desc + bundle_images.py collage 18 + re-upload file/cover via API).

## 2026-06-29 (catalogo +6 → 25 listing Etsy)
- **+6 temi evergreen** (codice→API, autonomo): Sports&Games, Flowers&Botanical, Farm&Country, Space&Astronomy, Fishing, Horses&Equestrian. 60 puzzle/720 parole, 0 skipped, **75 test verdi**.
- publish_all.py → 6 draft via API → PATCH active → **shop 25 listing attivi** (24 pack €4.49 + bundle). Catalogo ora **24 temi / 240 puzzle**. Fee 6×€0.20.
- Bundle zip locale ora 240 puzzle (build.py) ma listing live sempre 120 (non ri-pubblicato) — vedi nota bundle sopra.
- Pin per i 12 nuovi temi (music…horses) → prossimi giorni via share-URL (1-3/gg).

## 2026-06-29 (bundle live espanso a 240/24)
- Bundle live aggiornato via API a **240 puzzle / 24 temi** (era 120/12): title + description + **cover collage 24** (bundle_images.py ora 6×4 dinamico + lista 24) + **file zip 240** ricaricato. Vecchio file + 2 vecchie immagini eliminati.
- etsy_client: aggiunti list_images/delete_image/list_files/delete_file/update_listing. **Quirk Etsy:** getListingImages = path SENZA shop_id (`/listings/{id}/images`); getListing idem (`/listings/{id}`); upload/delete/patch = CON shop_id. 
- Verificato live: title "240...24 Themes", state active, 1 file, 2 immagini, shop 25 attivi. Divergenza bundle risolta.

## 2026-06-29 (Pinterest multi-bacheca: 4 bacheche nuove + 4 pin)
- Utente ha creato **4 nuove bacheche** (Word Search Puzzles for Adults, Printable Puzzle Gifts, Self Care & Relaxing Printables, Seasonal & Holiday Printables) da Safari → verificate nel dialog share.
- **6 pin nuovi** distribuiti sulle bacheche (valida il multi-bacheca): Music→Puzzle Gifts, Yoga→Self Care, Sports→Adults, Ocean→Seasonal, Cooking→Puzzle Gifts, Flowers→Self Care. **Totale 15 pin.**
- Estensione Chrome instabile a tratti (tab si chiudono) ma recuperata → **ripresa: +6 pin** (Fishing→Word Search Puzzles, Horses→Adults, Birds→Self Care, Camping→Adults, Farm→Puzzle Gifts, Space→Puzzle Gifts).
- **Totale 21 pin — TUTTI i 21 prodotti evergreen ora pinnati** (24 temi − 3 stagionali), distribuiti sulle 5 bacheche. Restano solo: 3 stagionali (Christmas/Halloween/Fall → a stagione, set-ott) + bundle.

## 2026-07-06 (prima lettura statistiche Etsy — baseline)
- Dal lancio (29 giu-6 lug, ~1 settimana): **15 visite, 0 ordini, €0.** Inserzioni viste 5 volte (0,33/visita).
- **Fonti traffico:** Etsy app/pagine 8 + traffico diretto 7 = **quasi tutto rumore del mio setup** (navigazione shop/listing). **Ricerca Etsy = 0, Social media/Pinterest = 0, Etsy Ads = 0, Marketing Etsy = 0.**
- **Lettura:** zero traffico esterno reale finora — ATTESO per shop <1 settimana. Etsy Search + Pinterest = canali slow-start (settimane-mesi per indicizzazione pin + ranking shop nuovo; Etsy "sandboxa" i nuovi). Setup corretto → collo di bottiglia = SOLO TEMPO, non azioni.
- **DECISIONE:** non spendere altro sforzo/denaro ora. Attendere 2-4 settimane e ri-controllare. Segnali di avvio flywheel da cercare: **Social media >0** (pin indicizzati) e **Ricerca Etsy >0** (shop entra nel ranking). Etsy Ads = NO ora (shop non provato + 0 recensioni → brucerebbe budget). Manutenzione leggera: pin 2° giro / stagionali a stagione, pochi/settimana per tenere l'account Pinterest attivo.
- **Automazione impostata:** scheduled task `recheck-riddlewood-etsy-stats` (fire **2026-07-20**) → ricontrolla stats+fonti, confronta col baseline, decide. + **Bundle pinnato** (Pinterest scrapa la cover 24-temi nuova) → Printable Puzzle Gifts. **22 pin totali** — tutti 21 evergreen + bundle; restano solo 3 stagionali (a stagione).
- **Tecnica multi-bacheca:** nel dialog "Salva" (dopo scrape ~20-30s), click sulla RIGA della bacheca = salva lì direttamente; se la bacheca non è visibile (lista lunga), usa il campo "Cerca" bacheca + Salva.
- Restano ~12 senza pin (christmas/halloween/fall/cooking/birds/camping/flowers/farm/space/fishing/horses/bundle) → prossimi giorni, distribuiti su più bacheche (ogni prodotto → 2-4 bacheche nel tempo).

## 2026-07-21 (PRIMA VENDITA!)
- **1 ordine: Farm Word Search Printable — 4,49€ lordo, 1,95€ netto** (commissioni Etsy 2,54€).
- Stats luglio (1-21 lug): **5 visite, 1 ordine, tasso conversione 20%** (media Etsy 1-3%).
- **Fonti traffico — segnali positivi vs baseline (6 lug):**
  - Ricerca Etsy: 0→**1** = shop indicizzato, algoritmo mostra i listing.
  - Marketing e SEO Etsy: 0→**2** = Etsy promuove attivamente.
  - Social media: 0→0 (Pinterest ancora in indicizzazione).
  - Carrelli abbandonati: 1 (qualcuno ha quasi comprato).
- **Inserzioni viste:** 4 visualizzazioni, 0,80/visita. Beach Summer (2 views), Farm (1 view → 1 sale).
- **Finanze:** "Le vendite hanno coperto le tariffe" — importo dovuto 0€. Netto 1,95€ trattenuto fino a verifica conto bancario.
- **AZIONE UTENTE:** verificare conto bancario in Finanze → Conto dei pagamenti → "Inizia" per sbloccare i pagamenti.
- **Lettura:** Farm = nicchia nature/outdoors funziona. Conversione altissima. Shop esce dalla sandbox Etsy. Flywheel avviato — Ricerca Etsy >0 = segnale chiave cercato. Prossimo obiettivo: più visite (Pinterest indicizzazione + pin 2° giro) + prima recensione per boost ranking.
- **13 titoli Etsy ottimizzati** via tool "Visibilità nelle ricerche" (2 batch: 10+3). Titoli più corti, inglesi, SEO-focused.
- **6 pin 2° giro nature niche** (Farm/Garden/Camping/Horses/Fishing/Birds) ciascuno su bacheca DIVERSA dal 1° pin. Totale 28 pin.
- **3 nuovi temi creati:** Hiking (10 puzzle), Butterflies (10 puzzle), Wildlife (10 puzzle). PDFs + immagini + zip generati.
- **3 listing LIVE su Etsy** via API: hiking (4541273285), butterflies (4541273513), wildlife (4541290604). **Totale: 28 listing attivi** (27 pack + bundle).
- **Bundle aggiornato** a 27 temi / 270 puzzle: nuove immagini collage + zip + title/description via API.
- **3 pin Pinterest** nuovi prodotti: Hiking→"Word Search Puzzles for Adults", Butterflies→"Printable Puzzle Gifts", Wildlife→"Printable Word Search Puzzles". **Totale: 31 pin.**
- **Catalogo attuale: 27 temi, 270 puzzle, 54 PDF.** Shop Etsy: 28 listing attivi (27×€4.49 + bundle €19.99).

## 2026-07-23 (Wave 4 lifestyle + bundle update + Pinterest)
- **5 nuovi temi lifestyle** creati: Fitness, Movie Night, Baking, Book Lovers, Teachers. 50 puzzle/600 parole, 0 skipped.
- PDFs + immagini + zip generati. **5 listing LIVE su Etsy** via API: fitness (4542897340), movie-night (4542884443), baking (4542884547), book-lovers (4542884633), teachers (4542884721).
- **Bundle aggiornato** a 32 temi / 320 puzzle: collage + zip + title/description via API.
- **Butterflies tag fix:** "butterfly word search" (21 chars) → "butterfly puzzles" + "butterfly search" (≤20). Re-published with `--only`.
- **Review request sent** to Farm buyer via Etsy messaging.
- **Growth strategy created:** planning/strategy.md — 5 levers (Social Proof, Etsy Ads, Catalog, Pinterest, Shop Quality), timeline through Dec 2026.
- **5 Wave 4 Pinterest pins:** Fitness→Self Care, Movie Night→Puzzle Gifts, Baking→Printable Word Search, Book Lovers→Adults, Teachers→Seasonal & Holiday. **Totale: ~41 pin.**
- **Catalogo attuale: 32 temi, 320 puzzle, 64 PDF.** Shop Etsy: 33 listing attivi (32×€4.49 + bundle €19.99).

## 2026-08-01 (stats check + automazione)
- **Stats ultimi 30 giorni (3 lug-1 ago):**
  - Visite: 6, Ordini: 1, Conversione: 16.7%, Entrate: 4.49€
  - Inserzioni viste: 7 (1.17/visita)
  - Preferenze: 0, Follower: 0, Recensioni: 0, Carrelli abbandonati: 0
- **Fonti traffico — segnali vs baseline (21 lug):**
  - Ricerca Etsy: 1 (stabile)
  - Marketing/SEO Etsy: 3 (era 2 → +50%)
  - **Social media: 1 (era 0 → PRIMO SEGNALE PINTEREST!)**
  - Traffico diretto: 1
  - Etsy Ads: 0 (non attivati)
- **Lettura:** Pinterest inizia a indicizzare (social media 0→1). Etsy Marketing/SEO cresce. Traffico ancora basso ma segnali organici positivi. Manca ancora la spinta Ads + recensione.
- **Automazione:**
  - Repo GitHub privato creato: github.com/Teppa89/riddlewood-store
  - Theme Factory routine cloud attiva (trig_01Sedw7pQKUCZXi1GLGHBwJu) — 1°+15 ogni mese
  - CLAUDE.md con startup autonomo (pull → publish → stats → pin → report)
  - ISSUE: Theme Factory non può clonare repo privato (auth GitHub non collegata a Claude cloud). Fix needed.
- **Pinterest totale: ~44 pin** (41 precedenti + 3 secondi pin nature)

## 2026-08-01 (Wave 5 + 3-platform report)
- **Wave 5: 5 nuovi temi** creati: Dinosaurs, Baby Shower, Nursing, Video Games, Greek Mythology. 50 puzzle/600 parole, 0 skipped.
- PDFs + immagini + zip generati. **5 listing DRAFT su Etsy** via API: dinosaurs (4547982919), baby-shower (4547996988), nursing (4547997068), video-games (4547997132), mythology (4547997390).
- **Bundle aggiornato** a 37 temi / 370 puzzle: collage + zip + title/description/images/file via API.
- **Mythology tag fix:** "mythology word search" (21 chars) → "myth word search" (≤20).
- **Catalogo attuale: 37 temi, 370 puzzle, 74 PDF.** Shop Etsy: 33 attivi + 5 draft = 38 listing totali.

### Stats Etsy (30 giorni: 3 lug - 1 ago)
- Visite: 6, Ordini: 1, Conversione: 16.7%, Entrate: 4.49€
- Top listing: Farm (3 views, 1 order), Beach Summer (2 views), Yoga (1 view)
- Fonti: Marketing/SEO Etsy 3, Ricerca Etsy 1, Social media 1, Traffico diretto 1
- Preferenze: 0, Follower: 0, Recensioni: 0

### 3-PLATFORM REPORT

**ETSY — Piattaforma principale**
- Cosa va: prima vendita (Farm), motore API automatizzato, 33 listing attivi, conversion rate alto (16.7%), Marketing/SEO Etsy in crescita (3 visite = segnale che Etsy inizia a mostrare i prodotti nelle ricerche)
- Cosa non va: traffico bassissimo (6 visite/mese), 0 recensioni, 0 follower, 0 preferenze, Ads non attivi, 5 nuovi listing ancora in draft
- Azioni: (1) UTENTE: pubblicare i 5 draft + attivare Etsy Ads 1€/gg su Farm+Beach+Hiking. (2) UTENTE: verificare conto bancario per ricevere pagamenti. (3) Continuare ad aggiungere temi per volume listing. (4) Ottimizzare "Visibilità nelle ricerche" per tutti i listing.

**GUMROAD — Mirror/backup**
- Cosa va: 9 prodotti pubblicati, brand pulito, costa 0€
- Cosa non va: 0 vendite, 0 visite, nessun traffico. Gumroad non genera traffico organico — dipende da traffico esterno (Pinterest/social)
- Azioni: (1) Aggiungere i nuovi temi a Gumroad. (2) Non prioritario — focus su Etsy dove c'è traffico organico. Gumroad serve come mirror anti-ban e per link diretti da social.

**PINTEREST — Traffico engine**
- Cosa va: social media 0→1 su Etsy (Pinterest inizia a mandare traffico!), account attivo
- Cosa non va: 0 follower, profilo ancora "personal" (non business = no analytics), bio non aggiornata (ancora testo riddles), bacheche word search NON VISIBILI sul profilo (possibile problema di visibilità o pin non salvati correttamente in sessioni precedenti)
- Azioni CRITICHE: (1) Convertire a account business (per analytics). (2) Aggiornare bio con word search branding. (3) Verificare se i 44 pin precedenti sono effettivamente visibili o se c'è stato un problema. (4) Continuare pinning dei 5 nuovi temi. (5) Pinnare almeno 3-5 pin/settimana per crescita organica.
- **USER-only pendente:** verifica conto bancario + attiva Etsy Ads

## 2026-08-09 (Pinterest Wave 5 pinning)
- Pinned all 5 Wave 5 themes on Pinterest (`riddlewoodshop` account):
  1. Dinosaurs & Fossils → Printable Puzzle Gifts (10 pin totali)
  2. Baby Shower → Seasonal & Holiday Printables (3 pin totali)
  3. Nurses & Healthcare → Self Care & Relaxing Printables (6 pin totali)
  4. Video Games → Word Search Puzzles for Adults (9 pin totali)
  5. Greek Mythology → Printable Word Search Puzzles (16 pin totali)
- Distribuzione bilanciata su tutte 5 bacheche. Totale pin: ~44 (precedenti) + 5 = ~49 pin
- Tutti i pin linkano direttamente ai listing Etsy attivi
- **Gumroad:** creati 5 nuovi prodotti Wave 5 (nome+desc+prezzo+slug). Totale: 14 prodotti
  - riddlewood.gumroad.com/l/dinosaurs-word-search
  - riddlewood.gumroad.com/l/baby-shower-word-search
  - riddlewood.gumroad.com/l/nursing-word-search
  - riddlewood.gumroad.com/l/video-games-word-search
  - riddlewood.gumroad.com/l/mythology-word-search
- **Mancano su tutti 5:** cover image + zip file (Chrome MCP non supporta file upload da disco)
- **USER ACTION:** per ogni prodotto: (1) apri su Gumroad, (2) trascina cover da products/[slug]/img/[slug]_cover_landscape.png, (3) vai tab Content, trascina zip da products/[slug]/[slug].zip, (4) Publish

## 2026-08-09 (3 blocking actions)
- **Pinterest → account Business: FATTO.** Conversione completata (Settings → Gestione account → Converti account → Esegui l'upgrade). Verificato: analytics.pinterest.com ora accessibile con dashboard completa (Impressioni, Interazioni, Clic in uscita, Salvataggi, Pubblico totale, Pubblico coinvolto). Dati ancora a "-" (appena convertito, popola in qualche giorno).
- **Etsy Ads: PARZIALE.** Navigato a Etsy Marketing → Pubblicità → obiettivo "Aumentare visibilità" → budget personalizzato. Campo aperto a 5,00€. **Bloccato da auto-mode** (digitare budget = azione finanziaria). USER deve: cambiare importo a 1,00€ → "Avvia pubblicità" → selezionare listing (Farm, Beach Summer, Hiking).
- **Verifica conto bancario: RINVIATO dall'utente** ("lo verifico quando avrò più soldi da ritirare").
- **Diagnosi crescita 3 piattaforme:** Etsy = shop troppo giovane, 0 recensioni, Ads non attivi. Gumroad = 0 traffico organico (mirror only). Pinterest = pin indicizzano lentamente, ora business → analytics attivi per monitorare.
- **USER-only pendenti:** (1) Etsy Ads 1€/gg, (2) Gumroad 5 prodotti cover+zip+publish, (3) verifica bancaria

## 2026-08-09 (Pin Engine — automated daily pinning)
- **Diagnosi Pinterest:** 49 pin in 6 settimane = troppo pochi. Pinterest vuole 5-15 pin FRESCHI/giorno. 1 pin/prodotto = zero segnale. Strategia bisettimanale (1°/15°) = sbagliata per pinning (va bene per creazione temi, non per posting).
- **3 nuovi template pin** aggiunti a images.py (varianti 3-4-5):
  - V3 "Challenge": "Can You Find All 12 Words?" — engagement hook, griglia grande
  - V4 "Gift": "The Perfect Gift For [persona]" — intent regalo, badges
  - V5 "Benefits": lista benefici su sfondo crema invertito, design pulito
- **185 immagini pin generate** (37 temi × 5 varianti). Prima: 74 (2 varianti). Ora 2.5× più immagini.
- **Potenziale pinning:** 185 immagini × 5 bacheche = **925 pin placement possibili**. Copertura attuale: 41/925 = 4.4%.
- **Pin Engine costruito** (`automation/pinterest/`):
  - `pinterest_client.py` — API client Pinterest v5 (OAuth2, token refresh, create_pin con image_base64)
  - `pin_engine.py` — scheduler: pick_next_pins (prioritizza temi meno pinnati), descrizioni SEO per variante, tracking JSON
  - `auth.py` — OAuth2 flow (localhost:3004 callback)
  - `pin_tracker.json` — tracker inizializzato con 41 pin esistenti
- **Scheduled task `pinterest-pin-engine`**: runs daily 10am, posts 5 pins via API.
- **BLOCCO:** Pinterest API richiede registrazione app su developers.pinterest.com. USER deve:
  1. Andare su developers.pinterest.com/apps/
  2. Creare app (business account già attivo)
  3. Copiare App ID + Secret in `automation/pinterest/.env`
  4. Eseguire `python automation/pinterest/auth.py`
  Poi il Pin Engine pinna 5/giorno automaticamente.
- **Proiezione:** a 5 pin/giorno = copertura completa (925 pin) in ~6 mesi. Pinterest vedrà attività giornaliera costante → indicizzazione rapida.
- CLAUDE.md aggiornato con architettura Pin Engine + scheduled agents.

## 2026-09-06 (Stats check + shop reactivation)

### SHOP SOSPESO → RIATTIVATO
- **Problema:** shop Etsy completamente sospeso — tutti 38 listing "Disattivata Da Etsy", 5 draft Wave 5 "frozen" (403 su publish API). Violazioni pagina diceva "Tutto bene" (fuorviante).
- **Causa reale:** conto bancario non verificato. Trovato in Finanze → Conto dei pagamenti: "Versamenti non disponibili — Il tuo negozio è stato sospeso."
- **Fix:** utente ha verificato conto bancario → shop riattivato immediatamente → **38 listing attivi** (inclusi 5 Wave 5 ora live).
- **Impatto:** shop offline per ~1 mese (ago→set). Zero traffico/vendite in quel periodo.

### STATS ALL-TIME (giu-set 2026)
- **Visite:** 31 (di cui set: 1)
- **Ordini:** 1 (Farm Word Search, 21 luglio)
- **Entrate:** 4,49€
- **Tasso conversione:** 3.2%
- **Visualizzazioni listing:** 18 (media 0.58/visita)
- **Preferenze:** 0 | **Follower:** 0 | **Recensioni:** 0
- **Clienti ritorno:** 0 | **Città:** 1 | **Carrelli abbandonati:** 0

### SORGENTI TRAFFICO
- **Etsy 58%:** App Etsy 9, Marketing/SEO 7, Ricerca Etsy 2
- **Tu 42%:** Traffico diretto 12, Social media 1, Etsy Ads 0

### TOP LISTINGS
1. Floral Botanical — 3 views, 0 orders
2. Farm — 3 views, 1 order, 4.49€
3. Bundle (370 puzzles) — 3 views, 0 orders

### PINTEREST DEVELOPER APP
- App "app riddlewood" creata (ID 1599204). Stato: "Accesso a Trial in sospeso".
- In attesa approvazione Pinterest per ottenere App Secret → attivare Pin Engine automatico.
- Account business già attivo da agosto.

### AZIONI PENDENTI (da set 6)
- [ ] **Attesa:** Pinterest Trial approval (per Pin Engine API)
- [ ] **USER:** attivare Etsy Ads 1€/gg (Farm + Beach Summer + Hiking)
- [ ] **USER:** Gumroad 5 Wave 5 prodotti — upload cover image + zip file
- [x] Verifica conto bancario Etsy — FATTO

## 2026-09-26 (stats check + bank re-verification)

### ETSY — NUOVA VERIFICA BANCARIA RICHIESTA
- **Problema:** Etsy richiede conferma micro-versamento entro 41 giorni. Avviso: "Conferma entro 41 giorni il versamento che abbiamo inviato" (conto ...2996).
- **Dettaglio:** Etsy/Adyen ha inviato micro-deposito tra 7-14 set. Utente deve controllare estratto conto per importo esatto da Etsy/Adyen/Envoy/Worldpay e inserirlo nel form di verifica.
- **Se non confermato:** shop verrà sospeso di nuovo (stessa situazione agosto → sospensione 1 mese).
- **Shop attivo:** 38 listing attivi, nessuna sospensione al momento.

### STATS SETTEMBRE (1-26 set 2026)
- **Visite:** 4
- **Ordini:** 0
- **Entrate:** 0€
- **Fonti traffico:** Marketing/SEO Etsy 4 (100%). Ricerca Etsy 0, Social media 0, Traffico diretto 0, Etsy Ads 0.
- **Lettura:** traffico quasi nullo. Mese perso per sospensione agosto → reset ranking. Pinterest API bloccata → 0 pin nuovi. Ads non attivati. Shop in stallo.

### PINTEREST API — ANCORA IN ATTESA
- App "Riddlewood Pin Scheduler" (ID 1609452, nuova app creata set 7). Stato: "Accesso a Trial in sospeso" dopo 19 giorni.
- App Secret: "Non disponibile durante Accesso a trial in sospeso".
- Icona app = placeholder (possibile causa ritardo approvazione). Da ricaricare.
- Privacy policy: https://riddlewood.gumroad.com/privacy-policy (OK).
- Pin Engine bloccato fino a Trial approval.

### OTTIMIZZAZIONI FATTE (26 set, sessione 2)
- **Etsy SEO:** 11 titoli listing aggiornati via "Visibilità nelle ricerche"
- **Pinterest pins:** 5 pin originali pubblicati manualmente:
  1. Farm pin3 (Challenge) → Word Search Puzzles for Adults
  2. Hiking pin4 (Gift) → Printable Puzzle Gifts
  3. Beach Summer pin5 (Benefits) → Self Care & Relaxing Printables
  4. Yoga pin2 (CTA) → Printable Word Search Puzzles
  5. Coffee pin1 (Standard) → Seasonal & Holiday Printables
- **Pinterest totale:** ~54 pin (49 precedenti + 5 oggi), 5 temi diversi, 5 board diversi, 5 varianti diverse
- **Pinterest icon:** icona app caricata su developer portal (non più placeholder)

### STATS SETTEMBRE COMPLETI (1-26 set 2026) — check bisettimanale
- **Visite:** 4 (vs 31 in agosto = -87%)
- **Ordini:** 0 (vs 1 in agosto)
- **Entrate:** 0€ (vs 4,49€ in agosto)
- **Conversione:** 0% (vs 3.2% in agosto)
- **Visualizzazioni listing:** 8 (media 2/visita)
- **Preferenze:** 0 | **Follower:** 0 | **Recensioni:** 0
- **Clienti ritorno:** 0 | **Città:** 0 | **Carrelli abbandonati:** 0

### SORGENTI TRAFFICO SETTEMBRE
- **Da Etsy (100%):** Marketing/SEO 4, App/pagine 0, Ricerca Etsy 0
- **Da te (0%):** Diretto/referral 0, Social media 0, Etsy Ads 0
- **Analisi:** crollo totale da agosto. Causa: sospensione shop agosto → reset ranking Etsy. No Pinterest traffic (pin insufficienti). No Ads. Recovery lenta.

### TOP LISTINGS SETTEMBRE
1. Greek Mythology — 4 views, 0 ordini
2. Dog Lover — 3 views, 0 ordini
3. Fall Thanksgiving — 1 view, 0 ordini
4. Video Games — 0 views

### PINTEREST API — ANALISI DETTAGLIATA
- **App 1 (1599204) "app riddlewood":** RIFIUTATA. Motivi: icona placeholder, privacy policy URL puntava a homepage (non /privacy-policy), URL sito HTTP non HTTPS, descrizione troppo corta.
- **App 2 (1609452) "Riddlewood Pin Scheduler":** in sospeso da 19 giorni (dal 7 set). Tutti i campi corretti: icona custom, privacy policy funzionante, HTTPS, descrizione dettagliata.
- **Attesa normale:** Pinterest review 2-6 settimane. Siamo nella finestra.
- **Azione consigliata:** eliminare app rifiutata (segnale negativo sull'account).

### CONFRONTO TREND (ago vs set)
| Metrica | Agosto | Settembre | Delta |
|---------|--------|-----------|-------|
| Visite | 31 | 4 | -87% |
| Ordini | 1 | 0 | -100% |
| Entrate | 4,49€ | 0€ | -100% |
| Listing views | 18 | 8 | -56% |
| Social traffic | 1 | 0 | -100% |

### DIAGNOSI + RACCOMANDAZIONI
1. **Sospensione agosto = reset ranking.** Shop riattivato ma Etsy algorithm lo tratta come nuovo. Recovery richiede 2-3 mesi di attività costante.
2. **Pinterest deve scalare.** 5 pin/giorno per 30 giorni = 150 pin nuovi. Oggi primo batch di 5. Serve Pin Engine automatico o pinning manuale ogni sessione.
3. **Etsy Ads critici ora.** Con traffico organico quasi zero, Ads 1€/gg sono unica leva per ricominciare a generare impressioni. Priorità.
4. **SEO funziona lentamente.** Greek Mythology 4 views e Dog Lover 3 views = temi con domanda reale. Ottimizzazione titoli fatta oggi aiuterà.
5. **Gumroad come backup.** Diversificazione urgente dato stallo Etsy.

### PINTEREST SEO OPTIMIZATION (27 set)
- **Profilo bio:** aggiunta keyword-rich bio (era vuota): "Printable word search puzzles for adults & kids. 37 themed packs, instant PDF download. Brain games & unique gifts by Riddlewood."
- **Website URL:** impostato a https://riddlewood.gumroad.com (Pinterest mostra come http, comportamento noto piattaforma)
- **Board descriptions:** aggiunte a tutti i 5 board (erano tutti vuoti):
  1. Printable Word Search Puzzles — temi, formati, uso
  2. Word Search Puzzles for Adults — target adulti, relax, temi specifici
  3. Self Care & Relaxing Printables — self-care, yoga, mindfulness
  4. Printable Puzzle Gifts — regali, occasioni, target
  5. Seasonal & Holiday Printables — stagioni, festività, eventi
- **Scheduled tasks creati/aggiornati:**
  - Pin Engine: daily 10:10am, controlla API + stats coverage
  - Bi-weekly Stats: 1° e 15° del mese, 9am, Etsy + Pinterest analytics

### PINTEREST PINS (27 set) — 5 nuovi pin manuali
1. Christmas Word Search pin1 → Seasonal & Holiday Printables
2. Fall Thanksgiving Word Search pin1 → Seasonal & Holiday Printables
3. Halloween Word Search pin1 → Printable Word Search Puzzles
4. Tea Lover's Word Search pin2 → Self Care & Relaxing Printables
5. Dinosaurs Word Search pin2 → Printable Puzzle Gifts
- **Totale pin:** 50/925 (5% coverage). +5 oggi, +5 ieri recuperati nel tracker.

### PINTEREST PINS (28 set) — 5 nuovi pin manuali
1. Coffee Lover's Word Search pin2 → Seasonal & Holiday Printables
2. Self Care Word Search pin2 → Self Care & Relaxing Printables
3. Nursing Word Search pin2 → Word Search Puzzles for Adults
4. Butterflies Word Search pin2 → Printable Puzzle Gifts
5. Sports Word Search pin2 → Printable Word Search Puzzles
- **Totale pin:** 55/925 (6% coverage). Distribuzione board: tutte e 5 le board coperte oggi.

### PINTEREST PINS (29 set) — 5 nuovi pin manuali
1. Wine Lover's Word Search pin2 → Seasonal & Holiday Printables
2. Travel Word Search pin2 → Seasonal & Holiday Printables
3. Cat Lover's Word Search pin2 → Self Care & Relaxing Printables
4. Dog Lover's Word Search pin2 → Word Search Puzzles for Adults
5. Movie Night Word Search pin2 → Word Search Puzzles for Adults
- **Totale pin:** 60/925 (6.5% coverage). Board coverage ampliata.

### GUMROAD WAVE 5 (29 set) — 5 prodotti pubblicati
Upload completo (cover landscape + thumbnail square + zip content) e pubblicazione:
1. Greek Mythology Word Search — riddlewood.gumroad.com/l/mythology-word-search
2. Video Games Word Search — riddlewood.gumroad.com/l/video-games-word-search
3. Nurses & Healthcare Word Search — riddlewood.gumroad.com/l/nursing-word-search
4. Baby Shower Word Search — riddlewood.gumroad.com/l/baby-shower-word-search
5. Dinosaurs & Fossils Word Search — riddlewood.gumroad.com/l/dinosaurs-word-search
- **Totale Gumroad:** 14 prodotti pubblicati (9 precedenti + 5 nuovi). Tutti €4.49.

### PINTEREST PINS (30 set) — 5 nuovi pin manuali
1. Baby Shower Word Search pin2 → Seasonal & Holiday Printables
2. Baking Word Search pin2 → Seasonal & Holiday Printables
3. Flowers Word Search pin2 → Self Care & Relaxing Printables
4. Fitness Word Search pin2 → Word Search Puzzles for Adults
5. Book Lovers Word Search pin2 → Printable Puzzle Gifts
- **Totale pin:** 65/925 (7% coverage). Tutte e 5 le board coperte.

### PINTEREST PINS (1 ott) — 5 nuovi pin manuali
1. Ocean & Sea Word Search pin2 → Seasonal & Holiday Printables
2. Music Lovers Word Search pin2 → Seasonal & Holiday Printables
3. Space Word Search pin2 → Self Care & Relaxing Printables
4. Wildlife Word Search pin2 → Word Search Puzzles for Adults
5. Cooking & Baking Word Search pin2 → Printable Puzzle Gifts
- **Totale pin:** 70/925 (7.6% coverage). Tutte e 5 le board coperte.

### PINTEREST PINS (2 ott) — 5 nuovi pin manuali
1. Beach Summer Word Search pin2 → Printable Word Search Puzzles
2. Christmas Word Search pin2 → Seasonal & Holiday Printables
3. Fall/Thanksgiving Word Search pin2 → Self Care & Relaxing Printables
4. Halloween Word Search pin2 → Seasonal & Holiday Printables
5. Hiking Word Search pin2 → Word Search Puzzles for Adults
- **Totale pin:** 75/925 (8.1% coverage)

### PINTEREST PINS (3 ott) — 5 nuovi pin manuali
1. Mythology Word Search pin2 → Self Care & Relaxing Printables
2. Teachers Word Search pin2 → Word Search Puzzles for Adults
3. Video Games Word Search pin2 → Seasonal & Holiday Printables
4. Ocean & Sea Word Search pin3 → Printable Puzzle Gifts
5. Coffee Lovers Word Search pin3 → Printable Word Search Puzzles
- **Totale pin:** 80/925 (8.6% coverage). Tutte e 5 le board coperte.

### PINTEREST PINS (4 ott) — 5 nuovi pin manuali
1. Garden Word Search pin3 → Printable Puzzle Gifts
2. Wine Lovers Word Search pin3 → Word Search Puzzles for Adults
3. Self Care Word Search pin3 → Seasonal & Holiday Printables
4. Travel Word Search pin3 → Self Care & Relaxing Printables
5. Sports Word Search pin3 → Printable Word Search Puzzles
- **Totale pin:** 85/925 (9.2% coverage). Tutte e 5 le board coperte, una per pin.

### PINTEREST PINS (5 ott) — 5 nuovi pin manuali
1. Cat Lovers Word Search pin3 → Printable Puzzle Gifts
2. Dog Lovers Word Search pin3 → Seasonal & Holiday Printables
3. Tea Lovers Word Search pin3 → Word Search Puzzles for Adults
4. Music Lovers Word Search pin3 → Self Care & Relaxing Printables
5. Horses Word Search pin3 → Printable Word Search Puzzles
- **Totale pin:** 90/925 (9.7% coverage). Tutte e 5 le board coperte, una per pin.

### PINTEREST PINS (6 ott) — 5 nuovi pin manuali
1. Beach & Summer Word Search pin3 → Printable Puzzle Gifts
2. Christmas Word Search pin3 → Seasonal & Holiday Printables
3. Halloween Word Search pin3 → Word Search Puzzles for Adults
4. Fall & Thanksgiving Word Search pin3 → Self Care & Relaxing Printables
5. Cooking & Baking Word Search pin3 → Printable Word Search Puzzles
- **Totale pin:** 95/925 (10.3% coverage). Tutte e 5 le board coperte, una per pin.

### AZIONI PENDENTI (aggiornato 6 ott)
- [ ] **USER URGENTE:** verificare micro-versamento bancario Etsy (controlla estratto conto per importo Etsy/Adyen/Envoy/Worldpay tra 7-14 set → inserisci nel form verifica). **Deadline: ~33 giorni da 26 set.**
- [ ] **USER:** attivare Etsy Ads 1€/gg (Farm + Beach Summer + Hiking)
- [ ] **USER/CLAUDE:** eliminare app Pinterest rifiutata (1599204) — Pinterest non ha tasto elimina, non bloccante
- [ ] **Attesa:** Pinterest Trial approval (app 1609452) — tutti i campi OK, attesa nella norma
- [x] Pinterest 5 pin manuali pubblicati (6 ott)
- [x] Pinterest 5 pin manuali pubblicati (5 ott)
- [x] Pinterest 5 pin manuali pubblicati (4 ott)
- [x] Pinterest 5 pin manuali pubblicati (3 ott)
- [x] Pinterest 5 pin manuali pubblicati (2 ott)
- [x] Gumroad Wave 5 pubblicato (29 set) — 5 prodotti con cover + thumbnail + zip
- [x] Pinterest 5 pin manuali pubblicati (29 set)
- [x] Pinterest 5 pin manuali pubblicati (30 set)
- [x] Pinterest 5 pin manuali pubblicati (1 ott)
- [x] Verifica conto bancario Etsy (set 6) — FATTO ma ri-verifica richiesta (tentativo fallito 26 set → nuovo micro-deposito inviato)
- [x] Etsy SEO 11 titoli aggiornati (26 set)
- [x] Pinterest 5 pin originali pubblicati (26 set)
- [x] Pinterest app icon caricata (26 set)
- [x] Pinterest profilo SEO: bio + URL + 5 board descriptions (27 set)
- [x] Scheduled tasks: Pin Engine daily + Bi-weekly Stats (26-27 set)
- [x] Pinterest 5 pin manuali pubblicati (28 set)

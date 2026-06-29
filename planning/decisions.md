# Decisions Log

Formato: data — decisione — razionale — reversibile?

## 2026-06-27
- **Modello business: A — Prodotti digitali** (Etsy + Gumroad, traffico Pinterest). Razionale: fit massimo col profilo founder (skill-zero, <5h/sett, budget lean, obiettivo veloce). Io produco volume, piattaforma porta traffico, consegna+pagamento automatici. Reversibile: sì (pivot a B video / C POD possibile).
- **Tipo prodotto iniziale: PDF printable** (planner, tracker, worksheet, wall art, checklist). Razionale: producibili al 100% da me via codice (reportlab / HTML→PDF / SVG), zero tool esterni, costo 0. Reversibile: sì.
- **Budget fase 1: ≤50€** (lean, solo validazione). Razionale: profilo di rischio utente (accetta ~300€ ma preferisce minimo). Reversibile: sì.
- **Metodologia: GSD lightweight.** Razionale: la `gsd-new-project` interattiva aumenterebbe il coinvolgimento utente (contro obiettivo "minimo coinvolgimento"). Adotto milestone + knowledge base + progress atomico senza interview. Reversibile: sì (full GSD attivabile su richiesta).
- **Geo/legale assunta: Italia/UE.** Partita IVA (forfettario) necessaria PRIMA di scalare, non in validazione. Decisione fiscale = utente.
- **Fisco (scelto):** validare come privato con poche vendite, poi aprire **P.IVA forfettario** quando l'attività diventa abituale. Caveat: in IT la vendita continuativa richiede P.IVA → **confermare con commercialista** (task utente). Reversibile: sì.
- **Go-live M2 (scelto):** utente crea account + fa login (dati sensibili = suoi); **Claude pilota il browser** (Chrome MCP) per creare i listing usando file/testi già pronti. Claude NON inserisce dati bancari/ID/pagamenti. Reversibile: sì.
- **Vincolo upload browser (scoperto):** Chrome MCP `file_upload` accetta SOLO file che l'utente attacca in chat; il grant-cartella (`request_directory`) NON lo sblocca. → upload immagini/PDF richiede attach manuale o API.
- **Strategia API (ricerca 2026-06-27):**
  - *Gumroad*: NESSUNA API per creare prodotti/caricare file (solo feature-request aperta, issue #4019) → copy-paste/browser, una tantum.
  - *Etsy*: Open API v3 SUPPORTA `createDraftListing` + `uploadListingImage` + `uploadListingFile` (digitale). Auth OAuth2 scope `listings_w` + `x-api-key` (keystring:shared_secret). Richiede registrazione app + **approvazione "Personal Access"** (review, tempi incerti). → COSTRUIRE come motore di scaling (300+ listing), uso dopo approvazione.
  - *Pinterest*: API gated da approvazione → manuale ora.
  - Decisione: lancio 7 prodotti via copy-paste/attach (one-time); investire in Etsy API come automazione durevole. Reversibile: sì.
- **PRIVACY — vincolo PERMANENTE (2026-06-27):** il nome reale e l'email dell'utente NON devono MAI comparire in alcun contenuto (pubblico o repo), né direttamente né indirettamente (iniziali avatar, handle derivati dall'email, ecc.). Brand pubblico = SOLO "Riddlewood". Applicato: git history riscritta con autore neutro `Riddlewood <noreply@riddlewood.local>` + contenuti storici ripuliti; config git neutra; nome profilo Gumroad → Riddlewood; avatar iniziale rimosso; **username/sottodominio Gumroad → `riddlewood`** (rimosso l'handle derivato dall'email); pagina pubblica verificata. Da valutare (utente): email account dedicata al brand; profilo Etsy in setup (evitare nome owner). Ogni contenuto futuro deve rispettare questo vincolo.

## Founder profile (input 2026-06-27)
- Competenze: parte da zero → motore = Claude + automazione.
- Capitale: ~300€ accettabile, 500–1000€ solo se rischio basso.
- Tempo: <5h/settimana → serve massima automazione + fulfillment automatico.
- Obiettivo: 500–1000€/mese netti, veloce, poi scalare gradualmente.
- **Asset: Canva Pro** (utente, dichiarato 2026-06-27). Uso previsto: (1) mockup lifestyle Etsy opzionali per +conversione (pilotabili da Claude nel browser); (2) futura linea #2 = template Canva editabili (M3+, best-seller Etsy). Produzione PRIMARIA resta automatizzata via codice (0-touch) = miglior fit coi vincoli; Canva non reintroduce lavoro manuale obbligatorio.

## 2026-06-29 (Etsy live + Pinterest autonomo)
- **Etsy x-api-key (confermato):** header `x-api-key` = `keystring:shared_secret` (NON solo keystring) → altrimenti 403 "Shared secret is required". Fix in etsy_client._headers().
- **Etsy publish via API:** create_draft_listing → upload immagini/file DA DISCO (no limite browser) → PATCH `state=active`. **13 listing live** (12 pack €4.49 + bundle €19.99/120 puzzle). Bundle cover generata da products/generator/bundle_images.py (collage 12 cover) perché la singola cover Coffee era fuorviante. Reversibile: sì.
- **Pinterest pinning AUTONOMO (scoperto):** `pinterest.com/pin/create/button/?url=<URL-pagina-live>` → Pinterest scrapa l'immagine principale della pagina (no file-pick) → scegli board → Salva. SUPERA il vincolo "upload pin = manuale" per pagine live (Etsy/Gumroad). Pin → Etsy = anche segnale traffico off-site (SEO). Cadenza account nuovo 1-3/giorno. Reversibile: sì.
- **Privacy Etsy (fatto):** nome profilo pubblico → "Riddlewood" (Impostazioni account → Profilo pubblico → "Cambia o rimuovi" → Nome=Riddlewood, Cognome vuoto). Verificato su shop pubblico: nessun nome reale.
- **Policy resi Etsy:** articoli digitali → Etsy auto-applica "Resi e cambi non accettati" (non modificabile, corretto). Nessuna policy fisica da creare. Stato venditore UE (Dati venditore) = fiscale/dati personali → decisione utente (legata a P.IVA).

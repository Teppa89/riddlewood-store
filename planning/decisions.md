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
- **PRIVACY — vincolo PERMANENTE (2026-06-27):** il nome reale e l'email dell'utente NON devono MAI comparire in alcun contenuto (pubblico o repo), né direttamente né indirettamente (iniziali avatar, handle derivati dall'email, ecc.). Brand pubblico = SOLO "Riddlewood". Applicato finora: git history riscritta (autore neutro `Riddlewood <noreply@riddlewood.local>` + oggetti vecchi purgati); config git futura = identità neutra; nome profilo Gumroad → Riddlewood; avatar "m" rimosso; pagina pubblica verificata. DA GESTIRE (decisione utente): username/sottodominio Gumroad `riddlewood` (deriva da email `redacted`), email account Gumroad, profilo Etsy in fase di setup (evitare nome owner). Ogni contenuto futuro deve rispettare questo vincolo.

## Founder profile (input 2026-06-27)
- Competenze: parte da zero → motore = Claude + automazione.
- Capitale: ~300€ accettabile, 500–1000€ solo se rischio basso.
- Tempo: <5h/settimana → serve massima automazione + fulfillment automatico.
- Obiettivo: 500–1000€/mese netti, veloce, poi scalare gradualmente.
- **Asset: Canva Pro** (utente, dichiarato 2026-06-27). Uso previsto: (1) mockup lifestyle Etsy opzionali per +conversione (pilotabili da Claude nel browser); (2) futura linea #2 = template Canva editabili (M3+, best-seller Etsy). Produzione PRIMARIA resta automatizzata via codice (0-touch) = miglior fit coi vincoli; Canva non reintroduce lavoro manuale obbligatorio.

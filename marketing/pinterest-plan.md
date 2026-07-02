# Pinterest Plan — Riddlewood

Traffic engine. Pinterest is a visual search engine: fresh pins keep surfacing
for months. Pin images are pre-generated in `marketing/pins/` (2 per pack:
`<slug>_pin1.png`, `<slug>_pin2.png`). Each pin links to that pack's live
product URL — now the **live Etsy listing** (etsy.com/shop/RiddlewoodCo).
Pinning is now AUTONOMOUS via the share-URL (Pinterest scrapes the Etsy cover,
no manual image upload needed).

## Boards to create (once — from SAFARI: pinterest.com → profile → Boards → +)
Keyword-targeted boards = more search surface. Pin each product to 2-4 relevant
boards, spaced over days (never all at once). More boards = more total pins we
can safely place. Chrome extension blocks board creation → create in Safari;
they then appear in Chrome where pins are published.

1. **Printable Word Search Puzzles** *(exists)* — every product
2. **Word Search Puzzles for Adults** — every product (big search term)
3. **Printable Puzzle Gifts** — every product (gift-intent buyers)
4. **Self Care & Relaxing Printables** — self-care, yoga, tea, coffee, garden, birds, ocean, flowers
5. **Seasonal & Holiday Printables** — christmas, halloween, fall, beach, ocean

Board descriptions (paste when creating): keyword-rich, e.g. board 2 =
"Printable word search puzzles for adults — instant download PDF activity books, large print, relaxing games."

## Board rotation (autonomous pinning)
Each product gets pinned to boards 1 → 3 → 2 (+ its niche board 4/5) across
different days. Method = `pinterest.com/pin/create/button/?url=<etsy-listing-url>`
(scrapes the Etsy cover, no upload), pick board, Save. 1-5 pins/day total.

## Cadence
- 1–3 fresh pins/day, consistent for 3+ months (compounding growth).
- Make 5–10 pin variations per listing over time (different text/colors) — re-run
  `images.py` variants or design more.
- **Seasonal lead time:** pin 6–8 weeks before the event.
  - Halloween pins → from early September
  - Fall/Thanksgiving → from mid September
  - Christmas → from mid October
  - Beach/Summer + evergreen (coffee, cat, dog, garden, self-care, wine, tea, travel) → year-round

## Per-pack pin copy (English, target US/UK)
Format — Title / Description / Board. Link = live product URL.

**Coffee** — *Coffee Lover's Word Search — Printable PDF Puzzles*
10 cozy coffee word search puzzles to print at home. Instant download PDF with full solutions (A4 + US Letter). A perfect little gift for coffee lovers. #wordsearch #printable #coffeelover #puzzles #instantdownload — Board: Gifts for Coffee & Tea Lovers

**Cat** — *Cat Lover's Word Search — Printable Puzzles*
10 purr-fect cat word search puzzles. Print at home, instant download PDF + solutions (A4 + US Letter). Great gift for cat moms & dads. #wordsearch #printable #catlover #puzzles #catmom — Board: Printable Word Search Puzzles

**Dog** — *Dog Lover's Word Search — Printable Puzzles*
10 pawsome dog word search puzzles. Instant download PDF with full solutions (A4 + US Letter). A fun gift for dog lovers. #wordsearch #printable #doglover #puzzles #doglovergift — Board: Printable Word Search Puzzles

**Garden** — *In The Garden Word Search — Printable Puzzles*
10 relaxing garden word search puzzles for green thumbs. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #gardening #puzzles #gardenlover — Board: Printable Word Search Puzzles

**Self-Care** — *Self-Care & Calm Word Search — Printable Puzzles*
10 gentle word search puzzles to slow down and unwind. Instant download PDF + solutions (A4 + US Letter). #selfcare #wordsearch #printable #mindfulness #relax — Board: Printable Word Search Puzzles

**Beach** — *Beach & Summer Word Search — Printable Puzzles*
10 sunny beach word search puzzles for lazy summer days. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #summer #beach #travelactivity — Board: Printable Word Search Puzzles

**Christmas** — *Christmas Word Search — Printable Holiday Puzzles*
10 festive Christmas word search puzzles. Instant download PDF + solutions (A4 + US Letter). Stocking stuffer & classroom activity. #christmas #wordsearch #printable #holiday #stockingstuffer — Board: Christmas Printables

**Halloween** — *Halloween Word Search — Printable Spooky Puzzles*
10 spooky Halloween word search puzzles for kids & adults. Instant download PDF + solutions (A4 + US Letter). #halloween #wordsearch #printable #classroom #spooky — Board: Halloween & Fall Printables

**Fall & Thanksgiving** — *Fall & Thanksgiving Word Search — Printable Puzzles*
10 cozy autumn & Thanksgiving word search puzzles. Instant download PDF + solutions (A4 + US Letter). #fall #thanksgiving #wordsearch #printable #autumn — Board: Halloween & Fall Printables

**Wine** — *Wine Lover's Word Search — Printable Puzzles*
10 wine word search puzzles to sip and solve. Instant download PDF + solutions (A4 + US Letter). Fun for girls night & wine lovers. #wine #wordsearch #printable #winelover #girlsnight — Board: Printable Word Search Puzzles

**Tea** — *Tea Lover's Word Search — Printable Puzzles*
10 tea word search puzzles — steep, sip, and solve. Instant download PDF + solutions (A4 + US Letter). #tea #wordsearch #printable #tealover #relax — Board: Gifts for Coffee & Tea Lovers

**Travel** — *Travel & Wanderlust Word Search — Printable Puzzles*
10 travel word search puzzles for dreamers & adventurers. Instant download PDF + solutions (A4 + US Letter). Great for road trips & flights. #travel #wordsearch #printable #wanderlust #roadtrip — Board: Printable Word Search Puzzles

**Music** — *Music Lover's Word Search — Printable Puzzles*
10 music word search puzzles for anyone who lives for music. Instant download PDF + solutions (A4 + US Letter). Great gift for musicians. #wordsearch #printable #musiclover #giftformusician #puzzles — Board: Printable Puzzle Gifts

**Kitchen & Baking** — *Kitchen & Baking Word Search — Printable Puzzles*
10 cooking & baking word search puzzles for foodies. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #baking #foodiegift #kitchen — Board: Printable Puzzle Gifts

**Ocean** — *Ocean & Sea Life Word Search — Printable Puzzles*
10 ocean & sea life word search puzzles to dive into. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #ocean #sealife #beachlover — Board: Seasonal & Holiday Printables

**Birds** — *Birds & Birdwatching Word Search — Printable Puzzles*
10 bird word search puzzles for birdwatchers & nature lovers. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #birdwatching #birdlover #nature — Board: Self Care & Relaxing Printables

**Camping** — *Camping & Outdoors Word Search — Printable Puzzles*
10 camping word search puzzles for the great outdoors. Instant download PDF + solutions (A4 + US Letter). Great for road trips. #wordsearch #printable #camping #outdoors #roadtrip — Board: Printable Puzzle Gifts

**Yoga** — *Yoga & Mindfulness Word Search — Printable Puzzles*
10 calming yoga & mindfulness word search puzzles. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #yoga #mindfulness #selfcare — Board: Self Care & Relaxing Printables

**Sports** — *Sports & Games Word Search — Printable Puzzles*
10 sports word search puzzles for fans & players. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #sports #giftforhim #puzzles — Board: Printable Puzzle Gifts

**Flowers** — *Flowers & Botanical Word Search — Printable Puzzles*
10 floral word search puzzles for flower lovers. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #flowers #botanical #giftforher — Board: Self Care & Relaxing Printables

**Farm** — *Farm & Country Word Search — Printable Puzzles*
10 farm & country word search puzzles, fun for kids & adults. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #farmhouse #countrylife #kidsactivity — Board: Printable Word Search Puzzles

**Space** — *Space & Astronomy Word Search — Printable Puzzles*
10 space word search puzzles for stargazers, kids & adults. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #space #astronomy #kidsactivity — Board: Printable Puzzle Gifts

**Fishing** — *Fishing Word Search — Printable Puzzles*
10 fishing word search puzzles for anglers. Instant download PDF + solutions (A4 + US Letter). Great gift for dad. #wordsearch #printable #fishing #giftfordad #angler — Board: Printable Puzzle Gifts

**Horses** — *Horses & Equestrian Word Search — Printable Puzzles*
10 horse word search puzzles for horse lovers & riders. Instant download PDF + solutions (A4 + US Letter). #wordsearch #printable #horselover #equestrian #giftforher — Board: Printable Puzzle Gifts

**Bundle** — *Big Word Search Bundle — 240 Printable Puzzles, 24 Themes*
The whole collection! 240 word search puzzles across 24 themes with full solutions. Instant download PDF (A4 + US Letter). Best-value gift. #wordsearch #printable #puzzlebundle #giftidea #instantdownload — Board: Printable Puzzle Gifts

## Notes
- Enable **Rich Pins** (pulls product data) once a shop is connected.
- Use a Pinterest **business** account for analytics.
- Pin the same image to multiple relevant boards over time (spaced out).

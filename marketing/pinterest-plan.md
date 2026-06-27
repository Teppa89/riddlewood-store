# Pinterest Plan — Riddlewood

Traffic engine. Pinterest is a visual search engine: fresh pins keep surfacing
for months. Pin images are pre-generated in `marketing/pins/` (2 per pack:
`<slug>_pin1.png`, `<slug>_pin2.png`). Each pin links to that pack's live
product URL (Etsy listing once approved, or Gumroad).

## Boards to create (once)
- **Printable Word Search Puzzles** — every pack
- **Halloween & Fall Printables** — halloween, fall-thanksgiving
- **Christmas Printables** — christmas
- **Gifts for Coffee & Tea Lovers** — coffee, tea
(If board creation in the pin-builder is buggy, create boards first from
pinterest.com → profile → Boards → +, then attach pins.)

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

## Notes
- Enable **Rich Pins** (pulls product data) once a shop is connected.
- Use a Pinterest **business** account for analytics.
- Pin the same image to multiple relevant boards over time (spaced out).

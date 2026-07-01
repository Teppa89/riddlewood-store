"""Listing data for every Riddlewood pack -> Etsy fields + asset paths.

Mirrors marketing/etsy-listings.md. Paths resolve to repo files that
publish_all.py uploads via the API (read from local disk).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRICE = 4.49
BUNDLE_PRICE = 19.99


def _assets(slug, bundle=False):
    base = ROOT / "products" / slug
    img = base / "img"
    pins = ROOT / "marketing" / "pins"
    candidates = [
        img / f"{slug}_etsy_main.png",
        img / f"{slug}_whats_inside.png",
        img / f"{slug}_two_sizes.png",
        img / f"{slug}_sample_solution.png",
        pins / f"{slug}_pin1.png",
        pins / f"{slug}_pin2.png",
    ]
    imgs = [str(p) for p in candidates if p.exists()]
    return imgs, str(base / f"{slug}.zip")


def _pack(slug, title, tags, description, price=PRICE):
    images, file_path = _assets(slug)
    return {"slug": slug, "title": title, "tags": tags, "description": description,
            "price": price, "images": images, "file": file_path}


PACKS = [
    _pack(
        "coffee-lovers-word-search",
        "Coffee Word Search Printable | 10 Coffee Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Coffee Lovers",
        ["coffee word search", "printable puzzles", "coffee lover gift", "word search pdf",
         "coffee gift idea", "puzzle book pdf", "adult word search", "cafe printable",
         "coffee puzzles", "instant download", "word puzzle game", "barista gift", "activity printable"],
        "Calling all coffee lovers! 10 cozy coffee-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). "
        "Print at home or solve on a tablet (GoodNotes / Notability).\n\n"
        "GREAT FOR: gifts for coffee lovers, baristas, cozy nights, travel, classroom downtime.\n\n"
        "Instant digital download (2 PDF files). No physical item shipped. Personal use only; not for resale.\n(c) Riddlewood",
    ),
    _pack(
        "cat-lovers-word-search",
        "Cat Word Search Printable | 10 Cat Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Cat Lovers",
        ["cat word search", "printable puzzles", "cat lover gift", "word search pdf",
         "cat gift idea", "puzzle book pdf", "adult word search", "cat mom gift",
         "cat puzzles", "instant download", "word puzzle game", "crazy cat lady", "activity printable"],
        "For everyone owned by a cat! 10 purr-fect cat-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: cat lover gifts, cat moms and dads, relaxing breaks, kids and adults.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "garden-word-search",
        "Garden Word Search Printable | 10 Gardening Puzzles PDF | Relaxing Adult Word Search | Instant Download Gift for Plant Lovers",
        ["garden word search", "printable puzzles", "gardener gift", "word search pdf",
         "plant lover gift", "puzzle book pdf", "adult word search", "gardening gift",
         "garden puzzles", "instant download", "word puzzle game", "nature printable", "activity printable"],
        "A relaxing pick for green thumbs! 10 garden-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve digitally.\n\n"
        "GREAT FOR: gardener gifts, plant lovers, calm afternoons, seniors, classrooms.\n\n"
        "Instant digital download (2 PDF files). No physical product. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "self-care-word-search",
        "Self Care Word Search Printable | 10 Mindfulness Puzzles PDF | Relaxing Adult Word Search | Calm Self Care Gift Download",
        ["selfcare word search", "printable puzzles", "mindfulness gift", "word search pdf",
         "self care gift", "puzzle book pdf", "adult word search", "relaxing puzzle",
         "calm puzzles", "instant download", "word puzzle game", "wellness printable", "anxiety relief"],
        "Slow down and unwind. 10 gentle self-care and mindfulness word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: self-care gifts, mindfulness routines, anxiety-relief breaks, cozy evenings.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "beach-summer-word-search",
        "Beach Word Search Printable | 10 Summer Puzzles PDF | Adult Word Search Book | Beach Vacation Activity | Instant Download",
        ["beach word search", "summer printable", "vacation activity", "word search pdf",
         "summer gift idea", "puzzle book pdf", "adult word search", "travel printable",
         "beach puzzles", "instant download", "word puzzle game", "kids activity", "activity printable"],
        "Bring on the sunshine! 10 beach and summer word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: summer road trips, beach bags, vacation downtime, kids and adults.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "christmas-word-search",
        "Christmas Word Search Printable | 10 Holiday Puzzles PDF | Adult Word Search Book | Stocking Stuffer | Instant Download Xmas",
        ["christmas wordsearch", "holiday printable", "stocking stuffer", "word search pdf",
         "christmas activity", "puzzle book pdf", "adult word search", "xmas gift idea",
         "holiday puzzles", "instant download", "word puzzle game", "family activity", "classroom printable"],
        "Festive fun for the whole family! 10 Christmas word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: stocking stuffers, classroom parties, Christmas Eve, family game night.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "dog-lovers-word-search",
        "Dog Word Search Printable | 10 Dog Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Dog Lovers",
        ["dog word search", "printable puzzles", "dog lover gift", "word search pdf",
         "dog mom gift", "puzzle book pdf", "adult word search", "dog dad gift",
         "dog puzzles", "instant download", "word puzzle game", "puppy gift", "activity printable"],
        "For everyone who loves dogs! 10 dog-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: dog lover gifts, dog moms and dads, relaxing breaks, kids and adults.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "halloween-word-search",
        "Halloween Word Search Printable | 10 Spooky Puzzles PDF | Kids & Adults Word Search | Classroom Activity | Instant Download",
        ["halloween wordsearch", "printable puzzles", "halloween activity", "word search pdf",
         "spooky printable", "puzzle book pdf", "kids word search", "classroom activity",
         "halloween puzzles", "instant download", "word puzzle game", "trick or treat", "party printable"],
        "Spooky fun for kids and adults! 10 Halloween word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: classroom parties, trick-or-treat downtime, Halloween gatherings, family game night.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "fall-thanksgiving-word-search",
        "Fall Word Search Printable | 10 Autumn & Thanksgiving Puzzles PDF | Adult Word Search | Classroom Activity | Instant Download",
        ["fall word search", "printable puzzles", "thanksgiving game", "word search pdf",
         "autumn printable", "puzzle book pdf", "adult word search", "classroom activity",
         "fall puzzles", "instant download", "word puzzle game", "thanksgiving gift", "family activity"],
        "Cozy up with autumn! 10 fall and Thanksgiving word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: Thanksgiving table activities, classroom fun, cozy fall afternoons, family game night.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "wine-lovers-word-search",
        "Wine Word Search Printable | 10 Wine Lover Puzzles PDF | Adult Word Search Book | Girls Night Gift | Instant Download",
        ["wine word search", "printable puzzles", "wine lover gift", "word search pdf",
         "wine gift idea", "puzzle book pdf", "adult word search", "girls night game",
         "wine puzzles", "instant download", "word puzzle game", "wine tasting", "party printable"],
        "For wine lovers! 10 wine-themed word search puzzles with full solutions - sip and solve.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: girls night, wine tasting parties, gifts for wine lovers, relaxing evenings.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "tea-lovers-word-search",
        "Tea Word Search Printable | 10 Tea Lover Puzzles PDF | Relaxing Adult Word Search | Instant Download Gift for Tea Lovers",
        ["tea word search", "printable puzzles", "tea lover gift", "word search pdf",
         "tea gift idea", "puzzle book pdf", "adult word search", "relaxing puzzle",
         "tea puzzles", "instant download", "word puzzle game", "afternoon tea", "activity printable"],
        "For tea lovers! 10 tea-themed word search puzzles with full solutions - steep, sip, and solve.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: gifts for tea lovers, cozy afternoons, relaxing breaks, quiet moments.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "travel-word-search",
        "Travel Word Search Printable | 10 Wanderlust Puzzles PDF | Adult Word Search Book | Vacation Activity | Instant Download",
        ["travel word search", "printable puzzles", "travel gift idea", "word search pdf",
         "wanderlust gift", "puzzle book pdf", "adult word search", "vacation activity",
         "travel puzzles", "instant download", "word puzzle game", "road trip game", "activity printable"],
        "For travel lovers and dreamers! 10 travel-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: road trips, flights, vacation downtime, gifts for travelers and adventurers.\n\n"
        "Instant digital download (2 PDF files). No physical item. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "music-lovers-word-search",
        "Music Word Search Printable | 10 Music Lover Puzzles PDF | Adult Word Search Book | Instant Download Gift for Musicians",
        ["music word search", "printable puzzles", "music lover gift", "word search pdf",
         "gift for musician", "puzzle book pdf", "adult word search", "band gift",
         "music puzzles", "instant download", "word puzzle game", "music teacher gift", "activity printable"],
        "For everyone who loves music! 10 music-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: musicians, music teachers, band members, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "cooking-baking-word-search",
        "Kitchen Word Search Printable | 10 Cooking & Baking Puzzles PDF | Adult Word Search Book | Instant Download Gift for Foodies",
        ["kitchen word search", "printable puzzles", "foodie gift", "word search pdf",
         "gift for cook", "puzzle book pdf", "adult word search", "baking gift",
         "cooking puzzles", "instant download", "word puzzle game", "chef gift", "activity printable"],
        "For everyone who loves to cook and bake! 10 kitchen-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: home cooks, bakers, foodies, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "ocean-sea-word-search",
        "Ocean Word Search Printable | 10 Sea Life Puzzles PDF | Adult Word Search Book | Instant Download Gift for Beach Lovers",
        ["ocean word search", "printable puzzles", "beach lover gift", "word search pdf",
         "sea life puzzles", "puzzle book pdf", "adult word search", "nautical gift",
         "ocean puzzles", "instant download", "word puzzle game", "summer activity", "activity printable"],
        "For everyone who loves the sea! 10 ocean and sea life word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: beach lovers, ocean fans, summer trips, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "birds-word-search",
        "Bird Word Search Printable | 10 Birdwatching Puzzles PDF | Adult Word Search Book | Instant Download Gift for Bird Lovers",
        ["bird word search", "printable puzzles", "bird lover gift", "word search pdf",
         "birdwatching gift", "puzzle book pdf", "adult word search", "birder gift",
         "bird puzzles", "instant download", "word puzzle game", "nature activity", "activity printable"],
        "For everyone who loves birds! 10 bird and birdwatching word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: birdwatchers, nature lovers, grandparents, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "camping-word-search",
        "Camping Word Search Printable | 10 Outdoor Puzzles PDF | Adult Word Search Book | Instant Download Gift for Campers",
        ["camping word search", "printable puzzles", "camping gift", "word search pdf",
         "outdoor puzzles", "puzzle book pdf", "adult word search", "camper gift",
         "nature puzzles", "instant download", "word puzzle game", "road trip game", "activity printable"],
        "For everyone who loves the outdoors! 10 camping and outdoor word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: campers, hikers, road trips, family camping nights.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "yoga-mindfulness-word-search",
        "Yoga Word Search Printable | 10 Mindfulness Puzzles PDF | Adult Word Search Book | Instant Download Self Care Gift",
        ["yoga word search", "printable puzzles", "mindfulness gift", "word search pdf",
         "self care puzzles", "puzzle book pdf", "adult word search", "yoga gift",
         "wellness puzzles", "instant download", "word puzzle game", "relaxing activity", "activity printable"],
        "For everyone who loves yoga and calm! 10 yoga and mindfulness word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: yogis, wellness lovers, self-care, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "sports-word-search",
        "Sports Word Search Printable | 10 Sports Fan Puzzles PDF | Adult Word Search Book | Instant Download Gift for Sports Lovers",
        ["sports word search", "printable puzzles", "sports fan gift", "word search pdf",
         "gift for him", "puzzle book pdf", "adult word search", "coach gift",
         "sports puzzles", "instant download", "word puzzle game", "teen activity", "activity printable"],
        "For every sports fan! 10 sports-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: sports fans, players, coaches, teens, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "flowers-word-search",
        "Flower Word Search Printable | 10 Floral & Botanical Puzzles PDF | Adult Word Search Book | Instant Download Gift for Her",
        ["flower word search", "printable puzzles", "floral gift", "word search pdf",
         "gift for her", "puzzle book pdf", "adult word search", "botanical gift",
         "flower puzzles", "instant download", "word puzzle game", "garden lover gift", "activity printable"],
        "For flower and garden lovers! 10 floral and botanical word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: flower lovers, gardeners, mothers, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "farm-word-search",
        "Farm Word Search Printable | 10 Country & Farm Animal Puzzles PDF | Adult Word Search Book | Instant Download Gift",
        ["farm word search", "printable puzzles", "farm animal gift", "word search pdf",
         "country gift", "puzzle book pdf", "adult word search", "farmhouse gift",
         "farm puzzles", "instant download", "word puzzle game", "kids activity", "activity printable"],
        "For country and farm lovers! 10 farm and country word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: farm lovers, country living, kids and adults, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "space-word-search",
        "Space Word Search Printable | 10 Astronomy Puzzles PDF | Adult & Kids Word Search | Instant Download Gift for Space Fans",
        ["space word search", "printable puzzles", "astronomy gift", "word search pdf",
         "space lover gift", "puzzle book pdf", "adult word search", "science gift",
         "space puzzles", "instant download", "word puzzle game", "kids activity", "activity printable"],
        "For space and astronomy fans! 10 space-themed word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: space lovers, stargazers, students, kids and adults.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "fishing-word-search",
        "Fishing Word Search Printable | 10 Angler Puzzles PDF | Adult Word Search Book | Instant Download Gift for Fishermen",
        ["fishing word search", "printable puzzles", "fishing gift", "word search pdf",
         "gift for dad", "puzzle book pdf", "adult word search", "angler gift",
         "fishing puzzles", "instant download", "word puzzle game", "gift for grandpa", "activity printable"],
        "For everyone who loves fishing! 10 fishing and angling word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: anglers, dads, grandpas, cabin trips, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
    _pack(
        "horses-word-search",
        "Horse Word Search Printable | 10 Equestrian Puzzles PDF | Adult Word Search Book | Instant Download Gift for Horse Lovers",
        ["horse word search", "printable puzzles", "horse lover gift", "word search pdf",
         "equestrian gift", "puzzle book pdf", "adult word search", "pony gift",
         "horse puzzles", "instant download", "word puzzle game", "girls activity", "activity printable"],
        "For horse lovers and riders! 10 horse and equestrian word search puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles + answer key, in 2 print sizes (A4 and US Letter). Print or solve on a tablet.\n\n"
        "GREAT FOR: horse lovers, riders, girls, relaxing breaks.\n\n"
        "Instant digital download (2 PDF files). Nothing shipped. Personal use only; no resale.\n(c) Riddlewood",
    ),
]


def bundle():
    slug = "big-word-search-bundle"
    base = ROOT / "products" / slug
    images = [str(base / "img" / "bundle_main.png"), str(base / "img" / "bundle_whats_inside.png")]
    return {"slug": slug, "price": BUNDLE_PRICE, "file": str(base / f"{slug}.zip"), "images": images,
            "title": "Word Search Bundle Printable | 120 Adult Word Search Puzzles PDF | 12 Themes | Instant Download Gift",
            "tags": ["word search bundle", "printable puzzles", "puzzle bundle pdf", "word search pdf",
                     "adult word search", "puzzle book pdf", "gift for grandma", "instant download",
                     "word puzzle game", "puzzles for adults", "activity printable", "senior activity", "large print puzzle"],
            "description": "The whole collection! 12 themed packs - Coffee, Cats, Dogs, Garden, Self-Care, Beach, "
                           "Christmas, Halloween, Fall, Wine, Tea and Travel - 120 word search puzzles with full solutions. Best value.\n\n"
                           "WHAT YOU GET: 120 unique puzzles across 12 themes + answer keys, in A4 and US Letter.\n\n"
                           "Instant digital download. No physical item. Personal use only; no resale.\n(c) Riddlewood"}

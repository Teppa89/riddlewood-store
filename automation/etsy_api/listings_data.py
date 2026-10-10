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
        "Coffee Word Search Printable | Large Print Puzzles PDF | Gift for Coffee Lovers | Instant Download",
        ["print at home", "word find puzzle", "easy for seniors", "caffeine fan",
         "barista present", "brain teaser game", "cozy night in", "screen free game",
         "care package idea", "birthday present", "relaxing pastime", "espresso fan", "latte art fan"],
        "Large print coffee word search puzzles — cozy, easy-to-read puzzles for coffee lovers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet (GoodNotes / Notability).\n\n"
        "GREAT FOR: coffee lover gifts, birthday presents, care packages, cozy nights, senior activities.\n\n"
        "Screen-free brain game for adults, seniors, and coffee fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "cat-lovers-word-search",
        "Cat Word Search Printable | Large Print Puzzles PDF | Gift for Cat Lovers | Instant Download",
        ["print at home", "word find puzzle", "cat mom present", "cat dad present",
         "kitten fan", "brain teaser game", "easy for seniors", "screen free game",
         "birthday present", "relaxing pastime", "rainy day fun", "feline fan", "gift for her"],
        "Large print cat word search puzzles — purr-fect for everyone owned by a cat! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: cat lover gifts, cat moms and dads, birthday presents, relaxing breaks.\n\n"
        "Screen-free brain game for adults, seniors, and cat fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "garden-word-search",
        "Garden Word Search Printable | Large Print Puzzles PDF | Gift for Plant Lovers | Instant Download",
        ["print at home", "word find puzzle", "green thumb gift", "plant mom present",
         "botanical fan", "brain teaser game", "easy for seniors", "screen free game",
         "birthday present", "relaxing pastime", "spring activity", "gift for grandma", "nature lover"],
        "Large print garden word search puzzles — a relaxing pick for green thumbs! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: gardener gifts, plant lovers, birthday presents, calm afternoons, seniors.\n\n"
        "Screen-free brain game for adults, seniors, and nature fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "self-care-word-search",
        "Self Care Word Search Printable | Large Print Mindfulness Puzzles PDF | Wellness Gift | Instant Download",
        ["print at home", "word find puzzle", "anxiety relief", "mental health gift",
         "spa day activity", "brain teaser game", "easy for seniors", "screen free game",
         "cozy night in", "calming pastime", "gift for her", "quiet time fun", "zen activity"],
        "Large print self-care word search puzzles — slow down and unwind with gentle, easy-to-read puzzles. "
        "10 mindfulness-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: self-care gifts, mindfulness routines, anxiety-relief breaks, cozy evenings.\n\n"
        "Screen-free brain game for adults and seniors seeking calm.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "beach-summer-word-search",
        "Beach Word Search Printable | Large Print Summer Puzzles PDF | Vacation Activity | Instant Download",
        ["print at home", "word find puzzle", "pool party game", "tropical theme",
         "sand and surf", "brain teaser game", "road trip game", "travel fun game",
         "gift for kids", "family fun game", "rainy day fun", "easy for seniors", "screen free game"],
        "Large print beach and summer word search puzzles — bring on the sunshine! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: summer road trips, beach bags, vacation downtime, pool parties, kids and adults.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "christmas-word-search",
        "Christmas Word Search Printable | Large Print Holiday Puzzles PDF | Stocking Stuffer | Instant Download",
        ["print at home", "word find puzzle", "holiday game night", "xmas party game",
         "classroom party", "brain teaser game", "family fun game", "gift for grandma",
         "advent activity", "winter break fun", "secret santa gift", "easy for seniors", "festive fun game"],
        "Large print Christmas word search puzzles — festive fun for the whole family! "
        "10 holiday-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: stocking stuffers, classroom parties, Christmas Eve, family game night, Secret Santa.\n\n"
        "Screen-free brain game for kids, adults, and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "dog-lovers-word-search",
        "Dog Word Search Printable | Large Print Puzzles PDF | Gift for Dog Lovers | Instant Download",
        ["print at home", "word find puzzle", "dog mom present", "dog dad present",
         "puppy fan", "brain teaser game", "easy for seniors", "screen free game",
         "birthday present", "relaxing pastime", "rainy day fun", "canine lover", "gift for her"],
        "Large print dog word search puzzles — for everyone who loves dogs! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: dog lover gifts, dog moms and dads, birthday presents, relaxing breaks.\n\n"
        "Screen-free brain game for adults, seniors, and dog fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "halloween-word-search",
        "Halloween Word Search Printable | Large Print Spooky Puzzles PDF | Classroom Activity | Instant Download",
        ["print at home", "word find puzzle", "october activity", "spooky party game",
         "trick or treat", "brain teaser game", "family fun game", "fall festival",
         "costume party fun", "haunted theme", "easy for seniors", "gift for kids", "ghost theme fun"],
        "Large print Halloween word search puzzles — spooky fun for kids and adults! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: classroom parties, trick-or-treat downtime, Halloween gatherings, family game night.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "fall-thanksgiving-word-search",
        "Fall Word Search Printable | Large Print Thanksgiving Puzzles PDF | Harvest Activity | Instant Download",
        ["print at home", "word find puzzle", "autumn theme", "pumpkin season",
         "gratitude game", "brain teaser game", "family game night", "easy for seniors",
         "classroom party", "cozy night in", "turkey day fun", "holiday table fun", "screen free game"],
        "Large print fall and Thanksgiving word search puzzles — cozy up with autumn! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: Thanksgiving table activities, classroom fun, cozy fall afternoons, family game night.\n\n"
        "Screen-free brain game for kids, adults, and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "wine-lovers-word-search",
        "Wine Word Search Printable | Large Print Puzzles PDF | Girls Night Gift | Instant Download",
        ["print at home", "word find puzzle", "vino lover", "sommelier present",
         "vineyard theme", "brain teaser game", "bachelorette game", "book club game",
         "date night fun", "gift for her", "relaxing pastime", "easy for seniors", "cozy night in"],
        "Large print wine word search puzzles — sip and solve! "
        "10 wine-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: girls night, wine tasting parties, bachelorette games, date night, book clubs.\n\n"
        "Screen-free brain game for adults and wine lovers.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "tea-lovers-word-search",
        "Tea Word Search Printable | Large Print Puzzles PDF | Gift for Tea Lovers | Instant Download",
        ["print at home", "word find puzzle", "herbal tea fan", "afternoon tea",
         "tea party game", "brain teaser game", "easy for seniors", "screen free game",
         "cozy night in", "relaxing pastime", "gift for grandma", "birthday present", "british tea time"],
        "Large print tea word search puzzles — steep, sip, and solve! "
        "10 tea-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: gifts for tea lovers, cozy afternoons, tea parties, quiet moments.\n\n"
        "Screen-free brain game for adults, seniors, and tea fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "travel-word-search",
        "Travel Word Search Printable | Large Print Puzzles PDF | Wanderlust Gift | Instant Download",
        ["print at home", "word find puzzle", "adventure seeker", "globe trotter",
         "road trip game", "brain teaser game", "easy for seniors", "screen free game",
         "vacation fun", "airport activity", "flight activity", "care package idea", "retirement gift"],
        "Large print travel word search puzzles — for dreamers and adventurers! "
        "10 travel-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: road trips, flights, vacation downtime, gifts for travelers and retirees.\n\n"
        "Screen-free brain game for adults, seniors, and adventure lovers.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "music-lovers-word-search",
        "Music Word Search Printable | Large Print Puzzles PDF | Gift for Musicians | Instant Download",
        ["print at home", "word find puzzle", "band member gift", "melody lover",
         "guitar fan", "brain teaser game", "easy for seniors", "screen free game",
         "choir present", "vinyl collector", "gift for teacher", "birthday present", "relaxing pastime"],
        "Large print music word search puzzles — for everyone who loves music! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: musicians, music teachers, band members, birthday presents.\n\n"
        "Screen-free brain game for adults, seniors, and music fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "cooking-baking-word-search",
        "Kitchen Word Search Printable | Large Print Cooking Puzzles PDF | Foodie Gift | Instant Download",
        ["print at home", "word find puzzle", "chef present", "home cook gift",
         "recipe lover", "brain teaser game", "easy for seniors", "screen free game",
         "culinary fan", "baking lover", "gift for mom", "birthday present", "housewarming gift"],
        "Large print kitchen and cooking word search puzzles — for everyone who loves to cook! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: home cooks, bakers, foodies, birthday and housewarming gifts.\n\n"
        "Screen-free brain game for adults, seniors, and food fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "ocean-sea-word-search",
        "Ocean Word Search Printable | Large Print Sea Life Puzzles PDF | Beach Lover Gift | Instant Download",
        ["print at home", "word find puzzle", "marine biology", "nautical theme",
         "shell collector", "brain teaser game", "easy for seniors", "screen free game",
         "coastal fan", "tide pool lover", "gift for kids", "summer fun game", "relaxing pastime"],
        "Large print ocean and sea life word search puzzles — dive into puzzle time! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: beach lovers, ocean fans, summer activities, kids and adults.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "birds-word-search",
        "Bird Word Search Printable | Large Print Birdwatching Puzzles PDF | Nature Lover Gift | Instant Download",
        ["print at home", "word find puzzle", "birder present", "ornithology fan",
         "feathered friend", "brain teaser game", "easy for seniors", "screen free game",
         "backyard birding", "gift for grandpa", "retirement gift", "relaxing pastime", "avian lover"],
        "Large print bird and birdwatching word search puzzles — for everyone who loves birds! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: birdwatchers, nature lovers, grandparents, retirees, relaxing breaks.\n\n"
        "Screen-free brain game for adults, seniors, and nature fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "camping-word-search",
        "Camping Word Search Printable | Large Print Outdoor Puzzles PDF | Camper Gift | Instant Download",
        ["print at home", "word find puzzle", "campfire fun", "tent life lover",
         "hiking trail fan", "brain teaser game", "easy for seniors", "screen free game",
         "road trip game", "scout leader gift", "bonfire night fun", "cabin trip game", "nature lover"],
        "Large print camping and outdoor word search puzzles — for everyone who loves the outdoors! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: campers, hikers, road trips, scout leaders, cabin weekends.\n\n"
        "Screen-free brain game for adults, seniors, and nature fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "yoga-mindfulness-word-search",
        "Yoga Word Search Printable | Large Print Mindfulness Puzzles PDF | Self Care Gift | Instant Download",
        ["print at home", "word find puzzle", "yogi present", "meditation fan",
         "zen lifestyle", "brain teaser game", "easy for seniors", "screen free game",
         "wellness retreat", "calming pastime", "gift for her", "quiet time fun", "spa day activity"],
        "Large print yoga and mindfulness word search puzzles — find your calm! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: yogis, wellness lovers, self-care gifts, spa days, quiet breaks.\n\n"
        "Screen-free brain game for adults and seniors seeking calm.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "sports-word-search",
        "Sports Word Search Printable | Large Print Puzzles PDF | Gift for Sports Fans | Instant Download",
        ["print at home", "word find puzzle", "coach present", "athlete gift",
         "team spirit fan", "brain teaser game", "easy for seniors", "screen free game",
         "gift for him", "birthday present", "game day fun", "tailgate party", "gift for dad"],
        "Large print sports word search puzzles — for every sports fan! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: sports fans, coaches, athletes, birthday presents, game day.\n\n"
        "Screen-free brain game for teens, adults, and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "flowers-word-search",
        "Flower Word Search Printable | Large Print Botanical Puzzles PDF | Gift for Her | Instant Download",
        ["print at home", "word find puzzle", "floral design fan", "garden club gift",
         "plant mom present", "brain teaser game", "easy for seniors", "screen free game",
         "mothers day gift", "spring activity", "gift for grandma", "relaxing pastime", "nature lover"],
        "Large print flower and botanical word search puzzles — for flower and garden lovers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: flower lovers, gardeners, mothers, birthday and Mother's Day gifts.\n\n"
        "Screen-free brain game for adults, seniors, and nature fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "farm-word-search",
        "Farm Word Search Printable | Large Print Country Puzzles PDF | Farm Animal Gift | Instant Download",
        ["print at home", "word find puzzle", "country living", "farmhouse decor",
         "barnyard fan", "brain teaser game", "easy for seniors", "screen free game",
         "gift for kids", "ranch life lover", "rural theme fun", "tractor fan", "homestead lover"],
        "Large print farm and country word search puzzles — for farm lovers and country fans! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: farm lovers, country living fans, kids and adults, relaxing breaks.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "space-word-search",
        "Space Word Search Printable | Large Print Astronomy Puzzles PDF | Gift for Space Fans | Instant Download",
        ["print at home", "word find puzzle", "nasa fan", "stargazer gift",
         "science lover", "brain teaser game", "easy for seniors", "screen free game",
         "rocket theme", "galaxy fan", "cosmos lover", "planet explorer", "stem activity"],
        "Large print space and astronomy word search puzzles — for space fans and stargazers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: space lovers, stargazers, students, STEM fans, kids and adults.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "fishing-word-search",
        "Fishing Word Search Printable | Large Print Angler Puzzles PDF | Gift for Fishermen | Instant Download",
        ["print at home", "word find puzzle", "tackle box gift", "fly fishing fan",
         "bass angler", "brain teaser game", "easy for seniors", "screen free game",
         "gift for dad", "gift for grandpa", "lake life lover", "cabin trip game", "retirement gift"],
        "Large print fishing word search puzzles — for everyone who loves fishing! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: anglers, dads, grandpas, cabin trips, retirement gifts.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "horses-word-search",
        "Horse Word Search Printable | Large Print Equestrian Puzzles PDF | Gift for Horse Lovers | Instant Download",
        ["print at home", "word find puzzle", "pony fan", "stable life",
         "riding lover", "brain teaser game", "easy for seniors", "screen free game",
         "cowgirl gift", "gift for girls", "barn life fun", "equine lover", "ranch theme fun"],
        "Large print horse and equestrian word search puzzles — for horse lovers and riders! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: horse lovers, riders, cowgirls, birthday gifts, relaxing breaks.\n\n"
        "Screen-free brain game for kids, teens, and adults.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "hiking-word-search",
        "Hiking Word Search Printable | Large Print Trail Puzzles PDF | Gift for Hikers | Instant Download",
        ["print at home", "word find puzzle", "mountain lover", "backpacker gift",
         "trail runner fan", "brain teaser game", "easy for seniors", "screen free game",
         "outdoor adventure", "national park fan", "nature lover", "camping trip fun", "summit seeker"],
        "Large print hiking and trail word search puzzles — for everyone who loves the trails! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: hikers, trail runners, mountain lovers, camping trips, retirees.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "butterflies-word-search",
        "Butterfly Word Search Printable | Large Print Nature Puzzles PDF | Gift for Nature Lovers | Instant Download",
        ["print at home", "word find puzzle", "insect fan", "garden lover",
         "monarch theme", "brain teaser game", "easy for seniors", "screen free game",
         "spring fun game", "entomology fan", "caterpillar fan", "pollinator lover", "gift for kids"],
        "Large print butterfly and nature word search puzzles — for nature and butterfly lovers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: nature lovers, gardeners, kids, spring activities, birthday gifts.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "wildlife-word-search",
        "Wildlife Word Search Printable | Large Print Animal Puzzles PDF | Safari Gift | Instant Download",
        ["print at home", "word find puzzle", "zoo lover gift", "jungle theme",
         "animal kingdom", "brain teaser game", "easy for seniors", "screen free game",
         "safari adventure", "gift for kids", "wild animal fan", "national park fun", "nature lover"],
        "Large print wildlife and animal word search puzzles — for animal and safari fans! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: animal lovers, safari fans, zoo visits, kids and adults.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "fitness-word-search",
        "Fitness Word Search Printable | Large Print Workout Puzzles PDF | Gym Lover Gift | Instant Download",
        ["print at home", "word find puzzle", "gym rat present", "exercise fan",
         "crossfit lover", "brain teaser game", "easy for seniors", "screen free game",
         "trainer present", "weight lifting", "athlete gift", "birthday present", "health nut"],
        "Large print fitness and workout word search puzzles — for fitness fans! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: gym lovers, personal trainers, fitness buffs, birthday presents.\n\n"
        "Screen-free brain game for adults and fitness fans.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "movie-night-word-search",
        "Movie Word Search Printable | Large Print Cinema Puzzles PDF | Movie Night Gift | Instant Download",
        ["print at home", "word find puzzle", "film buff present", "cinema fan",
         "date night game", "brain teaser game", "easy for seniors", "screen free game",
         "oscar party game", "family game night", "popcorn night fun", "gift for him", "hollywood fan"],
        "Large print movie and cinema word search puzzles — for movie lovers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: movie nights, film buffs, date night, family game night, Oscar parties.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "baking-word-search",
        "Baking Word Search Printable | Large Print Pastry Puzzles PDF | Gift for Bakers | Instant Download",
        ["print at home", "word find puzzle", "sourdough lover", "pastry chef fan",
         "bread maker", "brain teaser game", "easy for seniors", "screen free game",
         "kitchen gift idea", "gift for mom", "cookie lover", "birthday present", "cake decorator"],
        "Large print baking and pastry word search puzzles — for everyone who loves to bake! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: bakers, pastry chefs, bread lovers, birthday and kitchen gifts.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "book-lovers-word-search",
        "Book Word Search Printable | Large Print Reading Puzzles PDF | Gift for Book Lovers | Instant Download",
        ["print at home", "word find puzzle", "bookworm present", "library fan",
         "book club gift", "brain teaser game", "easy for seniors", "screen free game",
         "literary gift", "avid reader", "bibliophile", "gift for her", "quiet time fun"],
        "Large print book and reading word search puzzles — for bookworms and readers! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: book lovers, readers, librarians, book club gifts, birthday presents.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "teachers-word-search",
        "Teacher Word Search Printable | Large Print School Puzzles PDF | Teacher Gift | Instant Download",
        ["print at home", "word find puzzle", "educator present", "classroom fun",
         "end of year gift", "brain teaser game", "easy for seniors", "screen free game",
         "appreciation week", "back to school", "substitute gift", "principal gift", "school supply fun"],
        "Large print teacher and school word search puzzles — for teachers and educators! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: teacher appreciation, classroom activities, end-of-year gifts, back to school.\n\n"
        "Screen-free brain game for educators and students.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "dinosaurs-word-search",
        "Dinosaur Word Search Printable | Large Print Prehistoric Puzzles PDF | Dino Gift | Instant Download",
        ["print at home", "word find puzzle", "fossil hunter fan", "jurassic lover",
         "dino party game", "brain teaser game", "easy for seniors", "screen free game",
         "paleontology fan", "gift for boys", "birthday party fun", "extinct animal", "museum gift idea"],
        "Large print dinosaur word search puzzles — roar into puzzle time! "
        "10 prehistoric-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: dino fans, kids and adults, birthday parties, paleontology lovers.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "baby-shower-word-search",
        "Baby Shower Word Search Printable | Large Print Party Puzzles PDF | Shower Game | Instant Download",
        ["print at home", "word find puzzle", "gender reveal", "mom to be gift",
         "new parent gift", "brain teaser game", "diaper party", "sprinkle party",
         "nursery theme", "expecting mom", "gift for mom", "party favor idea", "baby sprinkle"],
        "Large print baby shower word search puzzles — sweet puzzles for baby showers! "
        "10 baby-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: baby shower games, gender reveal parties, sprinkles, new parent gifts.\n\n"
        "Screen-free party game for guests of all ages.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "nursing-word-search",
        "Nurse Word Search Printable | Large Print Healthcare Puzzles PDF | Nurse Appreciation Gift | Instant Download",
        ["print at home", "word find puzzle", "rn gift idea", "cna gift idea",
         "medical student", "brain teaser game", "easy for seniors", "screen free game",
         "hospital staff", "nursing school", "frontline worker", "caregiver present", "thank you gift"],
        "Large print nursing and healthcare word search puzzles — for healthcare heroes! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: Nurse Appreciation Week, nursing students, hospital staff, caregiver gifts.\n\n"
        "Screen-free brain game for healthcare professionals.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "video-games-word-search",
        "Video Game Word Search Printable | Large Print Gaming Puzzles PDF | Gamer Gift | Instant Download",
        ["print at home", "word find puzzle", "retro gaming fan", "console lover",
         "arcade theme", "brain teaser game", "easy for seniors", "screen free game",
         "nerd gift idea", "gift for him", "birthday present", "esports fan", "pixel art fan"],
        "Large print video game word search puzzles — level up with puzzles! "
        "10 gaming-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: gamers, retro gaming fans, birthday gifts, game night activities.\n\n"
        "Screen-free brain game (the irony!) for gamers of all ages.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "mythology-word-search",
        "Greek Mythology Word Search Printable | Large Print Legend Puzzles PDF | History Buff Gift | Instant Download",
        ["print at home", "word find puzzle", "ancient greece", "olympian theme",
         "zeus fan", "brain teaser game", "easy for seniors", "screen free game",
         "myth lover", "classical studies", "gift for student", "history nerd", "trojan war fan"],
        "Large print Greek mythology word search puzzles — epic puzzles from ancient legends! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: mythology fans, history buffs, students, classical literature lovers.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "winter-cozy-word-search",
        "Winter Cozy Word Search Printable | Large Print Hygge Puzzles PDF | Cozy Gift | Instant Download",
        ["print at home", "word find puzzle", "hygge lifestyle", "fireplace night",
         "snow day fun", "brain teaser game", "easy for seniors", "screen free game",
         "stocking stuffer", "cozy night in", "gift for grandma", "holiday gift idea", "warm and fuzzy"],
        "Large print winter cozy word search puzzles — warm and snuggly puzzles for cold days! "
        "10 hygge-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: cozy nights, stocking stuffers, holiday gifts, snow day activities, seniors.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "new-year-word-search",
        "New Year Word Search Printable | Large Print NYE Puzzles PDF | New Year Party Game | Instant Download",
        ["print at home", "word find puzzle", "nye party game", "countdown fun",
         "resolution planner", "brain teaser game", "easy for seniors", "screen free game",
         "celebration game", "midnight party", "champagne toast", "family fun game", "holiday activity"],
        "Large print New Year word search puzzles — ring in the new year with puzzles! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: New Year's Eve parties, countdown activities, family game night, resolutions.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "hanukkah-word-search",
        "Hanukkah Word Search Printable | Large Print Festival Puzzles PDF | Hanukkah Gift | Instant Download",
        ["print at home", "word find puzzle", "menorah candles", "dreidel game",
         "festival of light", "brain teaser game", "easy for seniors", "screen free game",
         "jewish holiday", "eight nights", "latkes fan", "family tradition", "holiday activity"],
        "Large print Hanukkah word search puzzles — Festival of Lights puzzle fun! "
        "10 themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: Hanukkah celebrations, family nights, holiday gifts, eight nights of fun.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "gratitude-word-search",
        "Gratitude Word Search Printable | Large Print Thankful Puzzles PDF | Mindfulness Gift | Instant Download",
        ["print at home", "word find puzzle", "thankful heart", "blessing counter",
         "kindness theme", "brain teaser game", "easy for seniors", "screen free game",
         "wellness present", "journaling gift", "gift for her", "quiet time fun", "calming pastime"],
        "Large print gratitude word search puzzles — count your blessings one word at a time! "
        "10 thankfulness-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: mindfulness gifts, gratitude journals, self-care, wellness lovers.\n\n"
        "Screen-free brain game for adults and seniors.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
    _pack(
        "board-games-word-search",
        "Board Game Word Search Printable | Large Print Game Night Puzzles PDF | Gamer Gift | Instant Download",
        ["print at home", "word find puzzle", "game night fun", "tabletop fan",
         "dice roller", "brain teaser game", "easy for seniors", "screen free game",
         "family fun game", "stocking stuffer", "card game lover", "birthday present", "party game idea"],
        "Large print board game word search puzzles — roll the dice and find every word! "
        "10 game night-themed puzzles with full solutions.\n\n"
        "WHAT YOU GET: 10 unique puzzles (15×15 grid, 12 words each) + answer key. "
        "2 print sizes (A4 + US Letter). Print at home or solve on tablet.\n\n"
        "GREAT FOR: game night, board game fans, family fun, stocking stuffers, birthday gifts.\n\n"
        "Screen-free brain game for the whole family.\n\n"
        "Digital download (2 PDF files). No physical item. Personal use only; not for resale.\n© Riddlewood",
    ),
]


def bundle():
    slug = "big-word-search-bundle"
    base = ROOT / "products" / slug
    images = [str(base / "img" / "bundle_main.png"), str(base / "img" / "bundle_whats_inside.png")]
    return {"slug": slug, "price": BUNDLE_PRICE, "file": str(base / f"{slug}.zip"), "images": images,
            "title": "Large Print Word Search Bundle | 420 Puzzles Printable PDF | 42 Themes | Best Value Gift Download",
            "tags": ["print at home", "word find bundle", "gift for seniors", "gift for grandma",
                     "brain game adults", "screen free fun", "retirement gift", "care package idea",
                     "classroom set", "birthday present", "stocking stuffer", "rainy day activity", "relaxing gift set"],
            "description": "Large print word search mega bundle — 420 puzzles across 42 themes! Best value in the shop.\n\n"
                           "THEMES: Coffee, Cat, Garden, Self-Care, Beach, Christmas, Dog, Halloween, Fall, Wine, Tea, Travel, "
                           "Music, Kitchen & Cooking, Ocean, Birds, Camping, Yoga, Sports, Flowers, Farm, Space, Fishing, Horses, "
                           "Hiking, Butterflies, Wildlife, Fitness, Movie Night, Baking, Book Lovers, Teachers, Dinosaurs, "
                           "Baby Shower, Nursing, Video Games, Greek Mythology, Winter Cozy, New Year, Hanukkah, Gratitude, "
                           "and Board Games.\n\n"
                           "WHAT YOU GET: 420 unique puzzles (15×15 grid, 12 words each) + answer keys. "
                           "All 42 themed packs in A4 and US Letter. Print at home or solve on tablet.\n\n"
                           "GREAT FOR: seniors, grandparents, retirees, care packages, classrooms, birthday gifts, stocking stuffers.\n\n"
                           "Screen-free brain game for adults and seniors — months of puzzle fun!\n\n"
                           "Digital download. No physical item. Personal use only; not for resale.\n© Riddlewood"}

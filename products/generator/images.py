"""Marketing image generator (Pillow): Etsy listing gallery, Gumroad cover,
Pinterest pins, brand banner + icon. Reuses theme data + the real grid
generator so previews show genuine puzzles. Outputs PNG.

Per pack (products/<slug>/img/):
  *_etsy_main.png       square 2000  - Etsy main / Gumroad thumbnail
  *_cover_landscape.png 1600x900     - Gumroad cover (horizontal)
  *_whats_inside.png    square 2000  - lists the 10 puzzle titles
  *_two_sizes.png       square 2000  - A4 + US Letter
  *_sample_solution.png square 2000  - highlighted solution (answer keys)
Plus marketing/pins/*_pin{1,2}.png and marketing/brand/{banner,icon}.

Run:  .venv/bin/python products/generator/images.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from wordsearch import generate_grid  # noqa: E402
from themes import THEMES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SERIF_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
SANS_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CREAM = (244, 240, 232)
GRID_FG = (70, 70, 70)
HILITE = (210, 224, 210)
BRAND_COLOR = (34, 45, 40)

_font_cache: dict = {}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    key = (path, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, cx, y, text, fnt, fill, max_w, line_h):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((cx, y + line_h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += line_h
    return y


def grid_card(img, grid, x, y, size_px, fg=GRID_FG, sol=None):
    """Cream rounded card with the letter grid; optional solution highlight."""
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([x, y, x + size_px, y + size_px], radius=size_px // 22,
                           fill=CREAM)
    n = len(grid)
    pad = size_px * 0.06
    cell = (size_px - 2 * pad) / n
    fnt = font(SANS, int(cell * 0.62))
    for r in range(n):
        for c in range(n):
            cxp = x + pad + c * cell
            cyp = y + pad + r * cell
            if sol and (r, c) in sol:
                draw.rounded_rectangle([cxp + 1, cyp + 1, cxp + cell - 1, cyp + cell - 1],
                                       radius=int(cell * 0.18), fill=HILITE)
            draw.text((cxp + cell / 2, cyp + cell / 2), grid[r][c], font=fnt,
                      fill=fg, anchor="mm")
    return y + size_px


def _preview(theme, n=12):
    p = theme["puzzles"][0]
    grid, sol, *_ = generate_grid(n, [w for w in p.words][:9], seed=3)
    return grid, sol


def badge(draw, cx, cy, text, fnt, h=64):
    w = draw.textlength(text, font=fnt)
    pad_x = 34
    draw.rounded_rectangle([cx - w / 2 - pad_x, cy - h / 2, cx + w / 2 + pad_x, cy + h / 2],
                           radius=h // 2, outline=CREAM, width=3)
    draw.text((cx, cy), text, font=fnt, fill=CREAM, anchor="mm")


def _brandmark(d, cx, y, fill=CREAM):
    d.text((cx, y), "RIDDLEWOOD", font=font(SANS_B, 40), fill=fill, anchor="mm")
    d.line([(cx - 120, y + 28), (cx + 120, y + 28)], fill=fill, width=2)


def etsy_main(theme, out):
    W = 2000
    img = Image.new("RGB", (W, W), theme["color"])
    d = ImageDraw.Draw(img)
    _brandmark(d, W / 2, 130)
    y = draw_block(d, W / 2, 230, theme["title"], font(SERIF_B, 130), CREAM, W - 260, 150)
    d.text((W / 2, y + 60), "10 Word Search Puzzles  -  Full Solutions",
           font=font(SERIF, 56), fill=CREAM, anchor="mm")
    gsize = 940
    grid, _ = _preview(theme)
    grid_card(img, grid, (W - gsize) / 2, y + 130, gsize)
    by = y + 130 + gsize + 110
    fnt = font(SANS_B, 40)
    badge(d, W / 2 - 560, by, "A4 + US LETTER", fnt)
    badge(d, W / 2, by, "INSTANT DOWNLOAD", fnt)
    badge(d, W / 2 + 560, by, "PRINT AT HOME", fnt)
    img.save(out)


def cover_landscape(theme, out):
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), theme["color"])
    d = ImageDraw.Draw(img)
    # right: grid card
    gsize = 600
    gx, gy = W - gsize - 90, (H - gsize) // 2
    grid, _ = _preview(theme)
    grid_card(img, grid, gx, gy, gsize)
    # left: text column
    lx = 110
    _brandmark(d, lx + 170, 150)
    y = 250
    for line in wrap(d, theme["title"], font(SERIF_B, 92), gx - lx - 60):
        d.text((lx, y), line, font=font(SERIF_B, 92), fill=CREAM)
        y += 104
    d.text((lx, y + 16), "10 puzzles + full solutions", font=font(SERIF, 42), fill=CREAM)
    badge(d, (lx + gx) / 2, H - 130, "A4 + US LETTER   -   INSTANT DOWNLOAD",
          font(SANS_B, 32), h=58)
    img.save(out)


def whats_inside(theme, out):
    W = 2000
    img = Image.new("RGB", (W, W), theme["color"])
    d = ImageDraw.Draw(img)
    _brandmark(d, W / 2, 150)
    d.text((W / 2, 320), "What's Inside", font=font(SERIF_B, 110), fill=CREAM, anchor="mm")
    y = 520
    fnt = font(SERIF, 60)
    for i, p in enumerate(theme["puzzles"], 1):
        d.text((W / 2, y), f"{i}.  {p.title}", font=fnt, fill=CREAM, anchor="mm")
        y += 118
    d.text((W / 2, y + 40), "10 puzzles  -  with full answer keys",
           font=font(SANS_B, 46), fill=CREAM, anchor="mm")
    img.save(out)


def two_sizes(theme, out):
    W = 2000
    img = Image.new("RGB", (W, W), theme["color"])
    d = ImageDraw.Draw(img)
    _brandmark(d, W / 2, 160)
    d.text((W / 2, 360), "Print in 2 Sizes", font=font(SERIF_B, 120), fill=CREAM, anchor="mm")
    # two paper rectangles
    pw, ph = 540, 720
    gap = 160
    total = pw * 2 + gap
    x0 = (W - total) // 2
    top = 560
    for i, label in enumerate(("A4", "US LETTER")):
        x = x0 + i * (pw + gap)
        d.rounded_rectangle([x, top, x + pw, top + ph], radius=24, fill=CREAM)
        for gy in range(top + 70, top + ph - 60, 70):
            d.line([(x + 60, gy), (x + pw - 60, gy)], fill=(205, 200, 190), width=6)
        d.text((x + pw / 2, top + ph + 70), label, font=font(SANS_B, 64),
               fill=CREAM, anchor="mm")
    d.text((W / 2, W - 150), "Print at home or solve on a tablet",
           font=font(SERIF, 54), fill=CREAM, anchor="mm")
    img.save(out)


def sample_solution(theme, out):
    W = 2000
    img = Image.new("RGB", (W, W), theme["color"])
    d = ImageDraw.Draw(img)
    _brandmark(d, W / 2, 150)
    d.text((W / 2, 330), "Answer Keys Included", font=font(SERIF_B, 100), fill=CREAM, anchor="mm")
    gsize = 1100
    grid, sol = _preview(theme)
    grid_card(img, grid, (W - gsize) / 2, 500, gsize, sol=sol)
    d.text((W / 2, 500 + gsize + 90), "Every puzzle comes with its full solution",
           font=font(SERIF, 54), fill=CREAM, anchor="mm")
    img.save(out)


PIN_PERSONAS = {
    "coffee-lovers-word-search": "Coffee Lovers",
    "cat-lovers-word-search": "Cat Lovers",
    "garden-word-search": "Gardeners",
    "self-care-word-search": "Anyone Needing to Relax",
    "beach-summer-word-search": "Beach & Summer Fans",
    "christmas-word-search": "The Whole Family",
    "dog-lovers-word-search": "Dog Lovers",
    "halloween-word-search": "Halloween Fans",
    "fall-thanksgiving-word-search": "Thanksgiving Hosts",
    "wine-lovers-word-search": "Wine Lovers",
    "tea-lovers-word-search": "Tea Lovers",
    "travel-word-search": "Travel Lovers",
    "music-lovers-word-search": "Music Lovers",
    "cooking-baking-word-search": "Home Cooks",
    "ocean-sea-word-search": "Ocean Lovers",
    "birds-word-search": "Birdwatchers",
    "camping-word-search": "Outdoor Enthusiasts",
    "yoga-mindfulness-word-search": "Yoga Lovers",
    "sports-word-search": "Sports Fans",
    "flowers-word-search": "Flower Lovers",
    "farm-word-search": "Country Living Fans",
    "space-word-search": "Space Enthusiasts",
    "fishing-word-search": "Fishing Enthusiasts",
    "horses-word-search": "Horse Lovers",
    "hiking-word-search": "Hikers",
    "butterflies-word-search": "Nature Lovers",
    "wildlife-word-search": "Wildlife Enthusiasts",
    "fitness-word-search": "Fitness Enthusiasts",
    "movie-night-word-search": "Movie Fans",
    "baking-word-search": "Baking Lovers",
    "book-lovers-word-search": "Book Lovers",
    "teachers-word-search": "Teachers",
    "dinosaurs-word-search": "Dinosaur Fans",
    "baby-shower-word-search": "New Parents",
    "nursing-word-search": "Nurses",
    "video-games-word-search": "Gamers",
    "mythology-word-search": "Mythology Fans",
}


def pin(theme, variant, out):
    W, H = 1000, 1500
    img = Image.new("RGB", (W, H), theme["color"])
    d = ImageDraw.Draw(img)
    grid, sol = _preview(theme)

    if variant == 1:
        d.text((W / 2, 90), "PRINTABLE WORD SEARCH", font=font(SANS_B, 34), fill=CREAM, anchor="mm")
        y = draw_block(d, W / 2, 150, theme["title"], font(SERIF_B, 86), CREAM, W - 130, 100)
        d.text((W / 2, y + 35), "10 puzzles + solutions", font=font(SERIF, 40), fill=CREAM, anchor="mm")
        grid_card(img, grid, (W - 620) / 2, 560, 620)
        d.text((W / 2, 1300), "Instant download PDF", font=font(SANS, 38), fill=CREAM, anchor="mm")
        d.text((W / 2, 1380), "Printable Puzzles  ·  Riddlewood", font=font(SANS_B, 44), fill=CREAM, anchor="mm")

    elif variant == 2:
        d.rectangle([0, 0, W, 470], fill=CREAM)
        tc = theme["color"]
        d.text((W / 2, 90), "PRINTABLE WORD SEARCH", font=font(SANS_B, 34), fill=tc, anchor="mm")
        y = draw_block(d, W / 2, 150, theme["title"], font(SERIF_B, 86), tc, W - 130, 100)
        d.text((W / 2, y + 35), "10 puzzles + solutions", font=font(SERIF, 40), fill=tc, anchor="mm")
        grid_card(img, grid, (W - 620) / 2, 560, 620)
        d.text((W / 2, 1300), "Instant download PDF", font=font(SANS, 38), fill=CREAM, anchor="mm")
        d.text((W / 2, 1380), "Printable Puzzles  ·  Riddlewood", font=font(SANS_B, 44), fill=CREAM, anchor="mm")

    elif variant == 3:
        d.text((W / 2, 80), "WORD SEARCH CHALLENGE", font=font(SANS_B, 32), fill=CREAM, anchor="mm")
        d.text((W / 2, 190), "Can You Find", font=font(SERIF, 64), fill=CREAM, anchor="mm")
        d.text((W / 2, 290), "All 12 Words?", font=font(SERIF_B, 88), fill=CREAM, anchor="mm")
        grid_card(img, grid, (W - 700) / 2, 400, 700)
        d.text((W / 2, 1200), theme["title"], font=font(SERIF_B, 42), fill=CREAM, anchor="mm")
        d.text((W / 2, 1300), "Printable PDF  ·  Instant Download", font=font(SANS, 36), fill=CREAM, anchor="mm")
        _brandmark(d, W / 2, 1400)

    elif variant == 4:
        persona = PIN_PERSONAS.get(theme["slug"], "Puzzle Lovers")
        d.text((W / 2, 100), "THE PERFECT GIFT FOR", font=font(SANS_B, 34), fill=CREAM, anchor="mm")
        y = draw_block(d, W / 2, 180, persona, font(SERIF_B, 90), CREAM, W - 100, 110)
        d.line([(200, y + 30), (800, y + 30)], fill=CREAM, width=2)
        grid_card(img, grid, (W - 520) / 2, y + 70, 520)
        by = y + 70 + 520 + 60
        fnt = font(SANS_B, 28)
        for i, label in enumerate(["10 PUZZLES", "PRINT AT HOME", "INSTANT PDF"]):
            bx = W / 2 - 300 + i * 300
            badge(d, bx, by, label, fnt, h=50)
        d.text((W / 2, 1380), "Riddlewood  ·  Printable Puzzles", font=font(SANS_B, 38), fill=CREAM, anchor="mm")

    elif variant == 5:
        img = Image.new("RGB", (W, H), CREAM)
        d = ImageDraw.Draw(img)
        tc = theme["color"]
        _brandmark(d, W / 2, 80, fill=tc)
        y = draw_block(d, W / 2, 180, theme["title"], font(SERIF_B, 76), tc, W - 120, 94)
        y += 40
        benefits = [
            "Relaxing brain exercise",
            "10 unique word search puzzles",
            "Full answer keys included",
            "A4 + US Letter sizes",
            "Print at home instantly",
        ]
        bfnt = font(SERIF, 40)
        for b in benefits:
            d.text((160, y), "·", font=font(SERIF_B, 48), fill=tc)
            d.text((210, y + 4), b, font=bfnt, fill=tc)
            y += 70
        y += 20
        grid_card(img, grid, (W - 480) / 2, y, 480, fg=tc)
        d.text((W / 2, 1420), "Available now  ·  Riddlewood", font=font(SANS_B, 36), fill=tc, anchor="mm")

    img.save(out)


def banner(out):
    W, H = 1600, 400
    img = Image.new("RGB", (W, H), BRAND_COLOR)
    d = ImageDraw.Draw(img)
    d.text((W / 2, H / 2 - 40), "Riddlewood", font=font(SERIF_B, 150), fill=CREAM, anchor="mm")
    d.text((W / 2, H / 2 + 90), "Printable word search & puzzle packs",
           font=font(SANS, 46), fill=CREAM, anchor="mm")
    img.save(out)


def icon(out):
    S = 500
    img = Image.new("RGB", (S, S), BRAND_COLOR)
    d = ImageDraw.Draw(img)
    d.ellipse([40, 40, S - 40, S - 40], outline=CREAM, width=10)
    d.text((S / 2, S / 2 - 10), "R", font=font(SERIF_B, 300), fill=CREAM, anchor="mm")
    img.save(out)


def main():
    pins_dir = ROOT.parent / "marketing" / "pins"
    brand_dir = ROOT.parent / "marketing" / "brand"
    pins_dir.mkdir(parents=True, exist_ok=True)
    brand_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for t in THEMES:
        d = ROOT / t["slug"] / "img"
        d.mkdir(parents=True, exist_ok=True)
        etsy_main(t, d / f"{t['slug']}_etsy_main.png")
        cover_landscape(t, d / f"{t['slug']}_cover_landscape.png")
        whats_inside(t, d / f"{t['slug']}_whats_inside.png")
        two_sizes(t, d / f"{t['slug']}_two_sizes.png")
        sample_solution(t, d / f"{t['slug']}_sample_solution.png")
        count += 5
        for v in (1, 2, 3, 4, 5):
            pin(t, v, pins_dir / f"{t['slug']}_pin{v}.png")
            count += 1
    banner(brand_dir / "shop_banner.png")
    icon(brand_dir / "shop_icon.png")
    count += 2
    print(f"Generated {count} images for {len(THEMES)} packs "
          f"(5 gallery + 5 pins each, + 2 brand).")


if __name__ == "__main__":
    main()

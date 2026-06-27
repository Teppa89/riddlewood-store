"""Marketing image generator (Pillow): Etsy listing mockups, Pinterest pins,
brand banner + icon. Reuses theme data + the real grid generator so previews
show genuine puzzles. Outputs PNG.

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
    """Centered, wrapped text block. Returns y after the block."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((cx, y + line_h / 2), line, font=fnt, fill=fill, anchor="mm")
        y += line_h
    return y


def grid_card(img, grid, x, y, size_px, fg):
    """Draw a cream rounded card with the letter grid centered inside."""
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([x, y, x + size_px, y + size_px], radius=size_px // 22,
                           fill=CREAM)
    n = len(grid)
    pad = size_px * 0.06
    cell = (size_px - 2 * pad) / n
    fnt = font(SANS, int(cell * 0.62))
    for r in range(n):
        for c in range(n):
            cxp = x + pad + c * cell + cell / 2
            cyp = y + pad + r * cell + cell / 2
            draw.text((cxp, cyp), grid[r][c], font=fnt, fill=fg, anchor="mm")


def preview_grid(theme, n=12):
    p = theme["puzzles"][0]
    grid, *_ = generate_grid(n, [w for w in p.words][:9], seed=3)
    return grid


def badge(draw, cx, cy, text, fnt):
    w = draw.textlength(text, font=fnt)
    pad_x, h = 34, 64
    x0, x1 = cx - w / 2 - pad_x, cx + w / 2 + pad_x
    draw.rounded_rectangle([x0, cy - h / 2, x1, cy + h / 2], radius=h // 2,
                           outline=CREAM, width=3)
    draw.text((cx, cy), text, font=fnt, fill=CREAM, anchor="mm")


def etsy_main(theme, out):
    W = 2000
    img = Image.new("RGB", (W, W), theme["color"])
    d = ImageDraw.Draw(img)
    d.text((W / 2, 120), "RIDDLEWOOD", font=font(SANS_B, 40), fill=CREAM,
           anchor="mm")
    d.line([(W / 2 - 120, 165), (W / 2 + 120, 165)], fill=CREAM, width=2)
    y = draw_block(d, W / 2, 230, theme["title"], font(SERIF_B, 130), CREAM,
                   W - 260, 150)
    d.text((W / 2, y + 60), "10 Word Search Puzzles  ·  Full Solutions",
           font=font(SERIF, 56), fill=CREAM, anchor="mm")
    gsize = 940
    grid_card(img, preview_grid(theme), (W - gsize) / 2, y + 130, gsize,
              (70, 70, 70))
    by = y + 130 + gsize + 110
    fnt = font(SANS_B, 40)
    badge(d, W / 2 - 560, by, "A4 + US LETTER", fnt)
    badge(d, W / 2, by, "INSTANT DOWNLOAD", fnt)
    badge(d, W / 2 + 560, by, "PRINT AT HOME", fnt)
    img.save(out)


def pin(theme, variant, out):
    W, H = 1000, 1500
    # variant 1: solid theme; variant 2: cream top band, theme bottom
    img = Image.new("RGB", (W, H), theme["color"])
    d = ImageDraw.Draw(img)
    title_fill = CREAM
    if variant == 2:
        d.rectangle([0, 0, W, 470], fill=CREAM)
        title_fill = theme["color"]
    d.text((W / 2, 90), "PRINTABLE WORD SEARCH", font=font(SANS_B, 34),
           fill=title_fill, anchor="mm")
    y = draw_block(d, W / 2, 150, theme["title"], font(SERIF_B, 86), title_fill,
                   W - 130, 100)
    d.text((W / 2, y + 35), "10 puzzles + solutions", font=font(SERIF, 40),
           fill=title_fill, anchor="mm")
    gsize = 620
    grid_card(img, preview_grid(theme), (W - gsize) / 2, 560, gsize,
              (70, 70, 70))
    d.text((W / 2, 1300), "Instant download", font=font(SANS, 38), fill=CREAM,
           anchor="mm")
    d.text((W / 2, 1380), "Find it on Etsy  ·  Riddlewood",
           font=font(SANS_B, 44), fill=CREAM, anchor="mm")
    img.save(out)


def banner(out):
    W, H = 1600, 400
    img = Image.new("RGB", (W, H), BRAND_COLOR)
    d = ImageDraw.Draw(img)
    d.text((W / 2, H / 2 - 40), "Riddlewood", font=font(SERIF_B, 150),
           fill=CREAM, anchor="mm")
    d.text((W / 2, H / 2 + 90), "Printable word search & puzzle packs",
           font=font(SANS, 46), fill=CREAM, anchor="mm")
    img.save(out)


def icon(out):
    S = 500
    img = Image.new("RGB", (S, S), BRAND_COLOR)
    d = ImageDraw.Draw(img)
    d.ellipse([40, 40, S - 40, S - 40], outline=CREAM, width=10)
    d.text((S / 2, S / 2 - 10), "R", font=font(SERIF_B, 300), fill=CREAM,
           anchor="mm")
    img.save(out)


def main():
    pins_dir = ROOT.parent / "marketing" / "pins"
    brand_dir = ROOT.parent / "marketing" / "brand"
    pins_dir.mkdir(parents=True, exist_ok=True)
    brand_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for t in THEMES:
        img_dir = ROOT / t["slug"] / "img"
        img_dir.mkdir(parents=True, exist_ok=True)
        etsy_main(t, img_dir / f"{t['slug']}_etsy_main.png")
        count += 1
        for v in (1, 2):
            pin(t, v, pins_dir / f"{t['slug']}_pin{v}.png")
            count += 1
    banner(brand_dir / "shop_banner.png")
    icon(brand_dir / "shop_icon.png")
    count += 2
    print(f"Generated {count} images "
          f"({len(THEMES)} etsy mains, {len(THEMES) * 2} pins, 2 brand).")


if __name__ == "__main__":
    main()

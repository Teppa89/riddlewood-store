"""Bundle listing images: a 12-cover collage + a 'what's inside' overview.

Reuses the per-pack etsy_main covers so the bundle visibly shows all 12 themes
(the single coffee cover misrepresents a 12-theme bundle). Outputs to
products/big-word-search-bundle/img/.

Run:  .venv/bin/python products/generator/bundle_images.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

from images import SERIF, SERIF_B, CREAM, BRAND_COLOR, font, ROOT
from themes import THEMES

OUT = ROOT / "big-word-search-bundle" / "img"
OUT.mkdir(parents=True, exist_ok=True)
S = 2000


def _footer(draw, text, color=CREAM):
    draw.text((S / 2, S - 78), text, font=font(SERIF, 50), fill=color, anchor="mm")


def collage():
    img = Image.new("RGB", (S, S), BRAND_COLOR)
    draw = ImageDraw.Draw(img)
    # title band
    draw.text((S / 2, 150), "BIG WORD SEARCH BUNDLE", font=font(SERIF_B, 132),
              fill=CREAM, anchor="mm")
    draw.text((S / 2, 290), "120 Printable Puzzles  -  12 Themes  -  Full Solutions",
              font=font(SERIF, 66), fill=(200, 192, 178), anchor="mm")
    # 4 x 3 grid of the etsy_main covers
    margin, gap, top = 40, 24, 400
    cell = (S - 2 * margin - 3 * gap) // 4
    for i, t in enumerate(THEMES[:12]):
        p = ROOT / t["slug"] / "img" / f"{t['slug']}_etsy_main.png"
        thumb = Image.open(p).convert("RGB").resize((cell, cell), Image.LANCZOS)
        # rounded mask
        mask = Image.new("L", (cell, cell), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, cell, cell], radius=cell // 18, fill=255)
        col, row = i % 4, i // 4
        x = margin + col * (cell + gap)
        y = top + row * (cell + gap)
        img.paste(thumb, (x, y), mask)
    _footer(draw, "Instant Download PDF  -  A4 + US Letter  -  Riddlewood")
    img.save(OUT / "bundle_main.png")
    print("wrote", OUT / "bundle_main.png")


def whats_inside():
    img = Image.new("RGB", (S, S), CREAM)
    draw = ImageDraw.Draw(img)
    draw.text((S / 2, 170), "What's Inside", font=font(SERIF_B, 150),
              fill=BRAND_COLOR, anchor="mm")
    draw.text((S / 2, 300), "12 themed packs - 10 puzzles each - 120 total",
              font=font(SERIF, 60), fill=(90, 84, 78), anchor="mm")
    names = [t["title"].replace(" Word Search", "") for t in THEMES[:12]]
    col_x, start_y, line_h = [560, 1180], 470, 150
    for i, name in enumerate(names):
        x = col_x[i // 6]
        y = start_y + (i % 6) * line_h
        sw = t = THEMES[i]["color"]
        draw.ellipse([x - 150, y - 18, x - 114, y + 18], fill=THEMES[i]["color"])
        draw.text((x - 96, y), name, font=font(SERIF, 62), fill=BRAND_COLOR, anchor="lm")
    draw.text((S / 2, S - 150), "+ full answer keys  -  A4 and US Letter  -  print at home",
              font=font(SERIF, 52), fill=(90, 84, 78), anchor="mm")
    _footer(draw, "Riddlewood", color=(120, 112, 104))
    img.save(OUT / "bundle_whats_inside.png")
    print("wrote", OUT / "bundle_whats_inside.png")


if __name__ == "__main__":
    collage()
    whats_inside()

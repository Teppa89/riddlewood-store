"""Bundle listing images: an all-theme cover collage + a 'what's inside' list.

Reuses every per-pack etsy_main cover so the bundle visibly shows all themes.
Grid + list scale to however many themes exist. Outputs to
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
N = len(THEMES)
PUZZLES = N * 10


def _footer(draw, text, color=CREAM):
    draw.text((S / 2, S - 76), text, font=font(SERIF, 46), fill=color, anchor="mm")


def collage():
    img = Image.new("RGB", (S, S), BRAND_COLOR)
    draw = ImageDraw.Draw(img)
    draw.text((S / 2, 130), "BIG WORD SEARCH BUNDLE", font=font(SERIF_B, 128),
              fill=CREAM, anchor="mm")
    draw.text((S / 2, 255), f"{PUZZLES} Printable Puzzles  -  {N} Themes  -  Full Solutions",
              font=font(SERIF, 58), fill=(200, 192, 178), anchor="mm")
    cols, margin, gap, top = 6, 36, 16, 350
    cell = (S - 2 * margin - (cols - 1) * gap) // cols
    for i, t in enumerate(THEMES):
        p = ROOT / t["slug"] / "img" / f"{t['slug']}_etsy_main.png"
        thumb = Image.open(p).convert("RGB").resize((cell, cell), Image.LANCZOS)
        mask = Image.new("L", (cell, cell), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, cell, cell], radius=cell // 16, fill=255)
        col, row = i % cols, i // cols
        x = margin + col * (cell + gap)
        y = top + row * (cell + gap)
        img.paste(thumb, (x, y), mask)
    _footer(draw, "Instant Download PDF  -  A4 + US Letter  -  Riddlewood")
    img.save(OUT / "bundle_main.png")
    print("wrote", OUT / "bundle_main.png", f"({N} covers)")


def whats_inside():
    img = Image.new("RGB", (S, S), CREAM)
    draw = ImageDraw.Draw(img)
    draw.text((S / 2, 150), "What's Inside", font=font(SERIF_B, 140),
              fill=BRAND_COLOR, anchor="mm")
    draw.text((S / 2, 268), f"{N} themed packs - 10 puzzles each - {PUZZLES} total",
              font=font(SERIF, 56), fill=(90, 84, 78), anchor="mm")
    names = [t["title"].replace(" Word Search", "") for t in THEMES]
    per_col = (N + 1) // 2
    col_x, start_y, line_h = [430, 1150], 420, 116
    for i, name in enumerate(names):
        x = col_x[i // per_col]
        y = start_y + (i % per_col) * line_h
        draw.ellipse([x - 150, y - 15, x - 120, y + 15], fill=THEMES[i]["color"])
        draw.text((x - 100, y), name, font=font(SERIF, 52), fill=BRAND_COLOR, anchor="lm")
    draw.text((S / 2, S - 140), "+ full answer keys  -  A4 and US Letter  -  print at home",
              font=font(SERIF, 50), fill=(90, 84, 78), anchor="mm")
    _footer(draw, "Riddlewood", color=(120, 112, 104))
    img.save(OUT / "bundle_whats_inside.png")
    print("wrote", OUT / "bundle_whats_inside.png", f"({N} themes)")


if __name__ == "__main__":
    collage()
    whats_inside()

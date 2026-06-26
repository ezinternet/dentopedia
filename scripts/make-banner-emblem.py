#!/usr/bin/env python3
"""Rebuild banner emblem from the Gemini chimera medallion.

- Removes the thick brushed-silver outer ring entirely.
- Keeps only the thin burgundy double-line border (redrawn crisply).
- Replaces the cream paper-texture field with the flat banner background (#F7F6F1).
- Keeps the teal/maroon piranha<->crocodile chimera artwork.
"""
import colorsys, math, sys
from PIL import Image, ImageDraw, ImageFilter

SRC = sys.argv[1] if len(sys.argv) > 1 else "/Users/oracleneo/Downloads/Gemini_Generated_Image_qeiap0qeiap0qeia.png"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/private/tmp/claude-501/-Users-oracleneo-llm-wiki/475b031c-7215-462d-8f15-4f5436e2f872/scratchpad/banner-emblem-preview.png"

BG = (247, 246, 241)          # #F7F6F1  banner background
BURGUNDY = (107, 35, 48)      # #6B2330  thin border (slightly richer than raw #5B292C)

# medallion geometry (auto-detected)
CX, CY = 1054, 951
RI = 815   # inner burgundy line radius
RO = 900   # outer burgundy line radius

im = Image.open(SRC).convert("RGB")
px = im.load()
W, H = im.size

# --- 1. crop a square around the medallion, with a little margin past outer ring
half = RO + 70
L, T = CX - half, CY - half
crop = im.crop((L, T, CX + half, CY + half))
cw, ch = crop.size
cpx = crop.load()
ccx, ccy = half, half  # center within crop

# --- 2. build keyed chimera over flat bg ---------------------------------
SS = 2  # supersample for crisp rings
S = cw * SS
out = Image.new("RGB", (S, S), BG)
opx = out.load()

# color-key: keep saturated chimera (teal + maroon), drop cream paper field
for y in range(ch):
    for x in range(cw):
        dx, dy = x - ccx, y - ccy
        if dx * dx + dy * dy > (RI - 6) ** 2:
            continue  # outside inner field -> stays BG (cream annulus + silver gone)
        r, g, b = cpx[x, y]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        is_teal = 0.40 < h < 0.62 and s > 0.14
        is_maroon = (h < 0.07 or h > 0.89) and s > 0.22
        is_dark = v < 0.30 and s > 0.12          # dark outlines
        if is_teal or is_maroon or is_dark:
            for yy in range(y * SS, y * SS + SS):
                for xx in range(x * SS, x * SS + SS):
                    opx[xx, yy] = (r, g, b)

# --- 3. redraw thin burgundy double-line ring ----------------------------
d = ImageDraw.Draw(out)
def ring(rad, w):
    bb = [(ccx - rad) * SS, (ccy - rad) * SS, (ccx + rad) * SS, (ccy + rad) * SS]
    d.ellipse(bb, outline=BURGUNDY, width=w)
ring(RI, 6 * SS)   # inner line (slightly heavier)
ring(RO, 3 * SS)   # outer line (thin)

# downsample for anti-aliasing
out = out.resize((cw, ch), Image.LANCZOS)
out.save(OUT)
print("wrote", OUT, out.size)

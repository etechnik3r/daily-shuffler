#!/usr/bin/env python3
"""Generate the PWA icons for Daily Taktgeber.

Draws a stopwatch mark on the app's blue gradient. Produces the regular
(rounded) icons plus a full-bleed maskable icon and an Apple touch icon.
Re-run this whenever the brand mark changes; the output PNGs are committed.
"""
import math
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), os.pardir, "icons")
os.makedirs(OUT, exist_ok=True)

TOP = (19, 102, 255)      # --accent  #1366ff
BOTTOM = (0, 40, 120)     # --accent-deep #002878
WHITE = (255, 255, 255)

SS = 4  # supersampling factor for crisp anti-aliasing


def vgradient(size):
    """Vertical accent gradient as an RGBA image."""
    img = Image.new("RGB", (1, size))
    for y in range(size):
        f = y / max(1, size - 1)
        img.putpixel((0, y), tuple(round(TOP[i] + (BOTTOM[i] - TOP[i]) * f) for i in range(3)))
    return img.resize((size, size)).convert("RGBA")


def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


def draw_stopwatch(draw, cx, cy, r):
    """A clean white stopwatch centred on (cx, cy) with body radius r."""
    stroke = max(2, round(r * 0.11))
    # top button (stem) + side ears
    stem_w = r * 0.34
    draw.rounded_rectangle(
        [cx - stem_w / 2, cy - r - r * 0.42, cx + stem_w / 2, cy - r + r * 0.10],
        radius=stem_w * 0.4, fill=WHITE)
    ear = r * 0.24
    for ang in (-40, 40):
        a = math.radians(ang - 90)
        ex, ey = cx + math.cos(a) * r, cy + math.sin(a) * r
        draw.rounded_rectangle(
            [ex - ear * 0.7, ey - ear * 0.35, ex + ear * 0.7, ey + ear * 0.35],
            radius=ear * 0.3, fill=WHITE)
    # dial ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
    inner = r - stroke
    # punch out the face so the gradient shows through the ring
    draw.ellipse([cx - inner, cy - inner, cx + inner, cy + inner], fill=(0, 0, 0, 0))
    # hands (to ~ 10:08), drawn white on the transparent face
    hand = stroke
    for length, ang in ((inner * 0.62, -60), (inner * 0.82, 40)):
        a = math.radians(ang - 90)
        hx, hy = cx + math.cos(a) * length, cy + math.sin(a) * length
        draw.line([cx, cy, hx, hy], fill=WHITE, width=hand)
    draw.ellipse([cx - hand, cy - hand, cx + hand, cy + hand], fill=WHITE)


def build(size, maskable=False):
    S = size * SS
    grad = vgradient(S)
    icon = Image.new("RGBA", (S, S), (0, 0, 0, 0))

    if maskable:
        # full-bleed background, mark kept inside the ~80% safe zone
        icon.paste(grad, (0, 0))
        r = S * 0.26
    else:
        radius = round(S * 0.22)
        icon.paste(grad, (0, 0), rounded_mask(S, radius))
        r = S * 0.30

    face = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw_stopwatch(ImageDraw.Draw(face), S / 2, S / 2 + S * 0.03, r)
    icon = Image.alpha_composite(icon, face)

    return icon.resize((size, size), Image.LANCZOS)


def main():
    build(192).save(os.path.join(OUT, "icon-192.png"))
    build(512).save(os.path.join(OUT, "icon-512.png"))
    build(512, maskable=True).save(os.path.join(OUT, "icon-maskable-512.png"))
    build(180).save(os.path.join(OUT, "apple-touch-icon.png"))
    build(32).save(os.path.join(OUT, "favicon-32.png"))
    print("icons written to", os.path.abspath(OUT))


if __name__ == "__main__":
    main()

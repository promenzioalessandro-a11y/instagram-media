"""Aggiunte fotografiche al renderer: copertine a tutta pagina, foto più testo, sfumature."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import render as R

W, H, M = R.W, R.H, R.M


def riempi(img, w, h, fx=0.5, fy=0.5, zoom=1.0):
    """Ritaglia l'immagine per riempire w x h, centrata su (fx, fy), con zoom opzionale."""
    img = img.convert("RGB")
    s = max(w / img.width, h / img.height) * zoom
    nw, nh = round(img.width * s), round(img.height * s)
    im = img.resize((nw, nh), Image.LANCZOS)
    x = min(max(round(nw * fx - w / 2), 0), nw - w)
    y = min(max(round(nh * fy - h / 2), 0), nh - h)
    return im.crop((x, y, x + w, y + h))


def sfuma(im, da, a, colore=(12, 16, 24), forza=0.88, verso="giu"):
    """Velo scuro graduale tra le righe da e a (verso giu: trasparente sopra, scuro sotto)."""
    w, h = im.size
    alpha = np.zeros((h, 1), np.float32)
    for y in range(h):
        if verso == "giu":
            t = 0 if y < da else (1 if y > a else (y - da) / (a - da))
        else:
            t = 0 if y > a else (1 if y < da else (a - y) / (a - da))
        alpha[y, 0] = (t ** 1.4) * forza
    alpha = np.repeat(alpha, w, axis=1)
    velo = Image.new("RGB", (w, h), colore)
    return Image.composite(velo, im, Image.fromarray((alpha * 255).astype(np.uint8)))


def intestazione_foto(d, i, n):
    R.scrivi(d, (M, 78), "Dott. Alessandro Promenzio", R.F(600, 30), (255, 255, 255), -0.008)
    R.scrivi(d, (M, 118), "Biologo Nutrizionista", R.F(400, 24), (225, 230, 238), 0.01)
    f = R.F(500, 26)
    t = f"{i:02d} / {n:02d}"
    R.scrivi(d, (W - M - R.larghezza(t, f, 0.02), 84), t, f, (225, 230, 238), 0.02)


def piede_foto(d):
    d.line((M, H - 118, W - M, H - 118), fill=(255, 255, 255, 90), width=2)
    f = R.F(500, 26)
    R.scrivi(d, (M, H - 90), "@dott_promenzio", f, (225, 230, 238), 0.01)
    t = "Verona e online"
    R.scrivi(d, (W - M - R.larghezza(t, f, 0.01), H - 90), t, f, (225, 230, 238), 0.01)


def stelle(d, xy, n, size, fill):
    import math
    x0, y0 = xy
    for k in range(n):
        cx, cy, r = x0 + k * size * 1.15 + size / 2, y0 + size / 2, size / 2
        pts = []
        for j in range(10):
            ang = -math.pi / 2 + j * math.pi / 5
            rr = r if j % 2 == 0 else r * 0.45
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        d.polygon(pts, fill=fill)

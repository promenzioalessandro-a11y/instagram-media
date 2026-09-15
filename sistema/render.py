"""Generatore delle immagini dei caroselli di @dott_promenzio.

Stile "sito": ricalca il design system del sito (Navy AP e Carta).
Uso: render(carosello, cartella_uscita, cartella_font) -> lista di percorsi JPEG.
Tipi di slide: cover, point, quote, cta.
"""
import colorsys, os, random
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 92


def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return (round(r * 255), round(g * 255), round(b * 255))


C = dict(
    carta=hsl(40, 33, 98), bianco=(255, 255, 255), ink=hsl(218, 17, 13),
    ink2=hsl(216, 8, 38), ink3=hsl(219, 6, 44), ink2_luce=hsl(208, 18, 29),
    navy50=hsl(216, 45, 96), navy200=hsl(215, 43, 81), navy300=hsl(217, 49, 72),
    navy600=hsl(217, 55, 35), tit500=hsl(209, 16, 44), tit900=hsl(210, 18, 17),
    riga=(224, 224, 224), su_scuro=hsl(40, 20, 98), su_scuro2=hsl(40, 8, 78),
    azione_scuro=hsl(217, 68, 68), azione_scuro_testo=hsl(220, 46, 10),
    riga_scuro=(66, 74, 82),
)

FONT_DIR = "fonts"


def F(peso, size):
    nome = {400: "Inter_400Regular", 500: "Inter_500Medium", 600: "Inter_600SemiBold", 700: "Inter_700Bold"}[peso]
    return ImageFont.truetype(os.path.join(FONT_DIR, nome + ".ttf"), size)


def larghezza(testo, font, track):
    if not testo:
        return 0
    return sum(font.getlength(ch) for ch in testo) + track * font.size * (len(testo) - 1)


def scrivi(d, xy, testo, font, fill, track=0.0):
    x, y = xy
    if track == 0:
        d.text((x, y), testo, font=font, fill=fill)
        return
    for ch in testo:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + track * font.size


def a_capo(testo, font, w, track):
    righe = []
    for par in testo.split("\n"):
        cur = ""
        for parola in [p for p in par.split(" ") if p]:
            t = (cur + " " + parola).strip()
            if larghezza(t, font, track) <= w:
                cur = t
            else:
                if cur:
                    righe.append(cur)
                cur = parola
        righe.append(cur)
    # niente parola orfana sull'ultima riga
    if len(righe) >= 2 and " " not in righe[-1] and " " in righe[-2]:
        a, b = righe[-2].rsplit(" ", 1)
        if larghezza(b + " " + righe[-1], font, track) <= w:
            righe[-2], righe[-1] = a, b + " " + righe[-1]
    return righe


def blocco(d, xy, testo, peso, size, fill, w, lh, track=0.0, max_h=None, min_size=30):
    while True:
        font = F(peso, size)
        righe = a_capo(testo, font, w, track)
        if max_h is None or len(righe) * size * lh <= max_h or size <= min_size:
            break
        size -= 2
    x, y = xy
    for r in righe:
        scrivi(d, (x, y), r, font, fill, track)
        y += round(size * lh)
    return y


def cielo():
    """Fondo azzurro del sito: bianco in alto a destra, navy 200 in basso a sinistra."""
    import numpy as np
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    t = ((W - xx) / W) * 0.55 + (yy / H) * 0.45
    xs = [0.0, 0.30, 0.62, 1.0]
    cols = [C["bianco"], C["navy50"], C["navy200"], C["navy200"]]
    out = np.zeros((H, W, 3), np.float32)
    for c in range(3):
        out[..., c] = np.interp(t, xs, [col[c] for col in cols])
    out += np.random.default_rng(7).uniform(-2.5, 2.5, (H, W, 1)).astype(np.float32)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


_CIELO = None


def intestazione(d, i, n, scuro=False):
    nome = C["su_scuro"] if scuro else C["ink"]
    sec = C["su_scuro2"] if scuro else (C["ink2_luce"] if not scuro else C["ink3"])
    scrivi(d, (M, 78), "Dott. Alessandro Promenzio", F(600, 30), nome, -0.008)
    scrivi(d, (M, 118), "Biologo Nutrizionista", F(400, 24), sec, 0.01)
    f = F(500, 26)
    t = f"{i:02d} / {n:02d}"
    scrivi(d, (W - M - larghezza(t, f, 0.02), 84), t, f, C["su_scuro2"] if scuro else C["tit500"], 0.02)


def piede(d, scuro=False):
    d.line((M, H - 118, W - M, H - 118), fill=C["riga_scuro"] if scuro else C["riga"], width=2)
    f = F(500, 26)
    scrivi(d, (M, H - 90), "@dott_promenzio", f, C["su_scuro2"] if scuro else C["ink3"], 0.01)
    t = "Verona e online"
    scrivi(d, (W - M - larghezza(t, f, 0.01), H - 90), t, f, C["su_scuro2"] if scuro else C["ink3"], 0.01)


def occhiello(d, xy, testo, fill):
    scrivi(d, xy, testo.upper(), F(600, 26), fill, 0.09)


def pillola(d, xy, testo, bg, fg, size=32):
    f = F(600, size)
    w = larghezza(testo, f, 0)
    x, y = xy
    h = size + 48
    d.rounded_rectangle((x, y, x + w + 80, y + h), radius=h // 2, fill=bg)
    d.text((x + 40, y + h / 2), testo, font=f, fill=fg, anchor="lm")


def render(car, outdir, font_dir="fonts"):
    global FONT_DIR, _CIELO
    FONT_DIR = font_dir
    os.makedirs(outdir, exist_ok=True)
    slides = car["slides"]
    n = len(slides)
    tw = W - 2 * M
    paths = []
    for i, sl in enumerate(slides, 1):
        k = sl.get("type", "point")
        scuro = k == "cta"
        if k == "cover":
            if _CIELO is None:
                _CIELO = cielo()
            im = _CIELO.copy()
        else:
            im = Image.new("RGB", (W, H), C["tit900"] if scuro else C["carta"])
        d = ImageDraw.Draw(im)
        intestazione(d, i, n, scuro)

        if k == "cover":
            occhiello(d, (M, 330), sl.get("kicker", ""), C["navy600"])
            y = blocco(d, (M, 385), sl["title"], 600, 104, C["ink"], tw, 1.04, -0.028, max_h=560, min_size=64)
            if sl.get("subtitle"):
                blocco(d, (M, y + 44), sl["subtitle"], 400, 40, C["ink2_luce"], tw - 80, 1.45)
            pillola(d, (M, H - 250), "Scorri  →", C["navy600"], C["bianco"])

        elif k == "point":
            y0 = 300
            d.line((M, y0, W - M, y0), fill=C["riga"], width=3)
            d.line((M, y0, M + round(tw * (i - 1) / max(1, n - 2)), y0), fill=C["navy600"], width=3)
            if sl.get("num") is not None:
                scrivi(d, (M, y0 + 48), f"{int(sl['num']):02d}", F(500, 34), C["tit500"], 0.02)
            y = blocco(d, (M, y0 + 110), sl["title"], 600, 80, C["ink"], tw, 1.10, -0.022, max_h=330, min_size=48)
            blocco(d, (M, y + 40), sl.get("body", ""), 400, 46, C["ink2"], tw, 1.55,
                   max_h=H - 170 - (y + 40), min_size=30)

        elif k == "quote":
            d.rounded_rectangle((M - 8, 250, W - M + 8, H - 170), radius=20, fill=C["bianco"], outline=C["riga"], width=2)
            x0 = M + 44
            stelle = "★" * int(sl.get("stars", 5))
            try:
                fs = ImageFont.truetype(os.path.join(font_dir, "DejaVuSans.ttf"), 40)
            except OSError:
                fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
            d.text((x0, 300), stelle, font=fs, fill=C["navy600"])
            y = blocco(d, (x0, 380), "“" + sl["text"] + "”", 400, 44, C["ink"], tw - 88, 1.5,
                       max_h=H - 170 - 380 - 150, min_size=28)
            scrivi(d, (x0, H - 170 - 110), sl.get("author", ""), F(600, 30), C["ink"])
            scrivi(d, (x0, H - 170 - 70), sl.get("source", "Recensione Google"), F(400, 26), C["ink3"], 0.01)

        elif k == "cta":
            occhiello(d, (M, 330), sl.get("kicker", "Prenota"), C["azione_scuro"])
            y = blocco(d, (M, 385), sl["title"], 600, 80, C["su_scuro"], tw, 1.08, -0.022, max_h=340, min_size=52)
            y = blocco(d, (M, y + 40), sl.get("body", ""), 400, 40, C["su_scuro2"], tw, 1.55, max_h=330, min_size=30)
            pillola(d, (M, max(y + 60, H - 330)), sl.get("button", "Scrivimi INFO in DM"), C["azione_scuro"], C["azione_scuro_testo"])

        piede(d, scuro)
        p = os.path.join(outdir, f"{i:02d}.jpg")
        im.save(p, "JPEG", quality=92, subsampling=0)
        paths.append(p)
    return paths

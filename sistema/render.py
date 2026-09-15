"""Renderer caroselli @dott_promenzio. Uso: render(carosello, stile, cartella, fonts_dir)"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 96

STYLES = {
    "clinico": dict(bg="#F7F5F0", fg="#1C2321", muted="#6B736F", accent="#3F7D5E", panel="#E8EEE9",
                    head="Inter_800ExtraBold.ttf", body="Inter_400Regular.ttf", label="Inter_700Bold.ttf"),
    "editoriale": dict(bg="#F3EDE3", fg="#2A2420", muted="#7A6E64", accent="#B5573A", panel="#E9DFD0",
                       head="Fraunces_600SemiBold.ttf", body="Inter_400Regular.ttf", label="Inter_700Bold.ttf"),
    "contrasto": dict(bg="#12161F", fg="#F4F1EA", muted="#9AA0AB", accent="#F2C94C", panel="#1C2230",
                      head="Inter_800ExtraBold.ttf", body="Inter_400Regular.ttf", label="Inter_700Bold.ttf"),
}

def _f(d, name, size):
    return ImageFont.truetype(os.path.join(d, name), size)

def _wrap(draw, text, font, width):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=font) <= width:
                cur = t
            else:
                if cur: lines.append(cur)
                cur = w
        lines.append(cur)
    return lines

def _block(draw, xy, text, fd, fname, size, fill, width, lh=1.25, max_h=None, min_size=40):
    while True:
        font = _f(fd, fname, size)
        lines = _wrap(draw, text, font, width)
        h = int(len(lines) * size * lh)
        if max_h is None or h <= max_h or size <= min_size:
            break
        size -= 4
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += int(size * lh)
    return y

def _footer(draw, s, fd, i, n):
    f = _f(fd, s["label"], 26)
    draw.line((M, H - 130, W - M, H - 130), fill=s["muted"], width=2)
    draw.text((M, H - 100), "DOTT. ALESSANDRO PROMENZIO  ·  BIOLOGO NUTRIZIONISTA", font=f, fill=s["muted"])
    t = f"{i}/{n}"
    draw.text((W - M - draw.textlength(t, font=f), H - 100), t, font=f, fill=s["muted"])

def render(car, style, outdir, fd):
    s = STYLES[style]
    os.makedirs(outdir, exist_ok=True)
    slides, paths = car["slides"], []
    n = len(slides)
    for i, sl in enumerate(slides, 1):
        im = Image.new("RGB", (W, H), s["bg"])
        d = ImageDraw.Draw(im)
        tw = W - 2 * M
        k = sl.get("type", "point")
        if k == "cover":
            d.rectangle((M, 150, M + 90, 162), fill=s["accent"])
            _block(d, (M, 200), sl.get("kicker", "").upper(), fd, s["label"], 32, s["accent"], tw)
            y = _block(d, (M, 290), sl["title"], fd, s["head"], 112, s["fg"], tw, 1.08, max_h=620)
            if sl.get("subtitle"):
                _block(d, (M, y + 40), sl["subtitle"], fd, s["body"], 42, s["muted"], tw, 1.35)
            f = _f(fd, s["label"], 32)
            d.text((M, H - 220), "Scorri  →", font=f, fill=s["accent"])
        elif k == "cta":
            d.rounded_rectangle((M - 20, 250, W - M + 20, 900), 36, fill=s["panel"])
            y = _block(d, (M + 30, 310), sl["title"], fd, s["head"], 76, s["fg"], tw - 60, 1.12, max_h=300)
            _block(d, (M + 30, y + 30), sl.get("body", ""), fd, s["body"], 40, s["fg"], tw - 60, 1.4, max_h=300, min_size=30)
            f = _f(fd, s["label"], 40)
            d.text((M, 980), "@dott_promenzio", font=f, fill=s["accent"])
        else:
            num = sl.get("num")
            y = 170
            if num:
                f = _f(fd, s["head"], 150)
                d.text((M, y - 20), str(num), font=f, fill=s["accent"])
                y += 190
            y = _block(d, (M, y), sl["title"], fd, s["head"], 72, s["fg"], tw, 1.12, max_h=330)
            _block(d, (M, y + 40), sl.get("body", ""), fd, s["body"], 42, s["fg"], tw, 1.42, max_h=H - 200 - y - 40 - 60, min_size=30)
        _footer(d, s, fd, i, n)
        p = os.path.join(outdir, f"{i:02d}.jpg")
        im.save(p, "JPEG", quality=90)
        paths.append(p)
    return paths

# Rigenera le tre schermate 1080x1920 della storia del sito.
# Serve Pillow e il font Poppins. Uso: python3 genera_storia_sito.py <cartella_di_uscita>
# La schermata 3 qui NON contiene lo screenshot della home: e' la versione con l'elenco delle sedi.

import sys, os
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
BG = (13, 42, 34)
BG2 = (10, 32, 26)
TXT = (243, 248, 245)
ACC = (137, 206, 170)
MUT = (168, 192, 180)

FONT_DIR = "/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"


def f(style, size):
    return ImageFont.truetype(FONT_DIR % style, size)


def bg():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(BG[i] + (BG2[i] - BG[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img, d


def wrap(d, text, font, maxw):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def block(d, text, font, y, color=TXT, maxw=880, lh=1.28, x=100):
    for ln in wrap(d, text, font, maxw):
        d.text((x, y), ln, font=font, fill=color)
        y += int(font.size * lh)
    return y


def kicker(d, y, text="DOTT. ALESSANDRO PROMENZIO"):
    d.text((100, y), text, font=f("Medium", 30), fill=ACC)


# 1: sondaggio, nessun link
img, d = bg()
kicker(d, 250)
y = block(d, "Sai gia' da dove partire con l'alimentazione?".replace("gia'", "già"), f("Bold", 86), 330)
block(d, "Rispondi qui sotto.", f("Regular", 44), y + 40, MUT)
img.save(os.path.join(OUT, "storia-sito-1.jpg"), quality=95)

# 2: quiz, adesivo link
img, d = bg()
kicker(d, 250)
y = block(d, "Sei domande, un minuto.", f("Bold", 86), 330)
y = block(d, "Ti dico da dove partire.", f("Bold", 86), y, ACC)
block(d, "Non è una diagnosi, è un orientamento. Il quiz è sul mio sito.", f("Regular", 44), y + 40, MUT)
d.text((100, 1560), "Tocca qui sotto", font=f("Medium", 38), fill=ACC)
img.save(os.path.join(OUT, "storia-sito-2.jpg"), quality=95)

# 3: sedi, adesivo link, tag delle sedi
img, d = bg()
kicker(d, 220)
y = block(d, "Cinque sedi in provincia di Verona, più la videochiamata.", f("Bold", 76), 300)
y += 50
fo = f("Medium", 48)
for s in ["Verona", "Settimo di Pescantina", "Peschiera del Garda", "San Pietro in Cariano", "Villafranca"]:
    d.ellipse([100, y + 18, 120, y + 38], fill=ACC)
    d.text((152, y), s, font=fo, fill=TXT)
    y += 84
block(d, "Sedi, orari e prenotazione sul sito.", f("Regular", 42), y + 40, MUT)
d.text((100, 1600), "Tocca qui sotto", font=f("Medium", 38), fill=ACC)
img.save(os.path.join(OUT, "storia-sito-3.jpg"), quality=95)

print("fatto:", OUT)

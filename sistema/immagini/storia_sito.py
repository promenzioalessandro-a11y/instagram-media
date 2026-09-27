# Rigenera le tre schermate della storia sito (1080x1920).
# Uso: python3 storia_sito.py   -> scrive storia-sito-1.png, -2.png, -3.png nella cartella corrente.
# Serve Pillow e il font Poppins (google-fonts). Cambiare P se il percorso dei font e' diverso.
# Le immagini generate in chat spariscono a fine sessione: questo script e' la copia permanente.

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG = (12, 38, 31); FG = (242, 247, 244); ACC = (127, 209, 174); DIM = (150, 178, 167)
P = "/usr/share/fonts/truetype/google-fonts/"

def f(w, s):
    return ImageFont.truetype(P + "Poppins-%s.ttf" % w, s)

def bg():
    im = Image.new("RGB", (W, H), BG)
    return im, ImageDraw.Draw(im)

def wrap(d, txt, font, maxw):
    out = []
    for para in txt.split("\n"):
        if not para.strip():
            out.append(""); continue
        line = ""
        for w in para.split():
            t = (line + " " + w).strip()
            if d.textlength(t, font=font) <= maxw:
                line = t
            else:
                out.append(line); line = w
        out.append(line)
    return out

def block(d, txt, font, y, maxw=880, x=100, fill=FG, lh=1.32):
    step = int(font.size * lh)
    for ln in wrap(d, txt, font, maxw):
        d.text((x, y), ln, font=font, fill=fill); y += step
    return y

def kicker(d, txt, y):
    d.text((100, y), txt.upper(), font=f("Medium", 34), fill=ACC)
    return y + 70

def save(im, name):
    im.convert("P", palette=Image.ADAPTIVE, colors=32).save(name, "PNG", optimize=True)

# 1 - sondaggio, nessun link
im, d = bg()
y = kicker(d, "una domanda veloce", 260)
y = block(d, "Sai gia' da dove\npartire per mettere\nin ordine i pasti?".replace("gia'", "già"), f("Bold", 80), y + 10)
block(d, "Rispondi qui sotto, ci vuole un secondo.", f("Light", 40), y + 40, fill=DIM)
save(im, "storia-sito-1.png")

# 2 - quiz, adesivo link
im, d = bg()
y = kicker(d, "se hai risposto no", 260)
y = block(d, "Ho messo online\nun quiz di sei\ndomande.", f("Bold", 80), y + 10)
block(d, "Ti dice da dove conviene partire\nnel tuo caso, senza impegno.", f("Light", 44), y + 40, fill=DIM)
save(im, "storia-sito-2.png")

# 3 - sedi, adesivo link e tag delle sedi
im, d = bg()
y = kicker(d, "dove mi trovi", 230)
y = block(d, "Cinque studi\nin provincia di\nVerona.", f("Bold", 80), y + 10)
y += 50
sedi = ["Verona", "Settimo di Pescantina", "Peschiera del Garda",
        "San Pietro in Cariano", "Villafranca", "Oppure in videochiamata"]
for i, s in enumerate(sedi):
    last = (i == len(sedi) - 1)
    d.ellipse([104, y + 16, 124, y + 36], fill=DIM if last else ACC)
    d.text((160, y), s, font=f("Light", 46) if last else f("Regular", 46), fill=DIM if last else FG)
    y += 92
save(im, "storia-sito-3.png")

print("fatto: storia-sito-1.png, storia-sito-2.png, storia-sito-3.png")

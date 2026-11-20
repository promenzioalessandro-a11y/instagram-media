# Rigenera la schermata della storia di seguito al reel SportPlatz (1080x1920).
# Uso: python3 storia_dopo_reel.py   -> scrive dopo-reel-1.png nella cartella corrente.
# Serve Pillow e il font Poppins (google-fonts). Cambiare P se il percorso dei font e' diverso.
# Spazio libero in basso per l'adesivo link al quiz del sito.

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

im, d = bg()
y = kicker(d, "se arrivi dal reel", 250)
y = block(d, "Alleni seriamente,\nma mangi come\ncapita?", f("Bold", 80), y + 10)
y += 30
y = block(d, "Sei domande veloci per capire da dove\nconviene partire. Nessun dato sensibile,\nnessuna mail.", f("Light", 42), y, maxw=900, fill=DIM)
y += 50
block(d, "Il quiz è qui sotto.", f("Regular", 44), y, maxw=900)
save(im, "dopo-reel-1.png")

print("fatto: dopo-reel-1.png")

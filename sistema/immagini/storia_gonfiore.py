# Rigenera le due schermate della storia gonfiore, variante B (1080x1920).
# Uso: python3 storia_gonfiore.py   -> scrive gonfiore-1.png e gonfiore-2.png nella cartella corrente.
# Serve Pillow e il font Poppins (google-fonts). Cambiare P se il percorso dei font e' diverso.

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

# 1 - sondaggio: Spesso / Quasi mai
im, d = bg()
y = kicker(d, "dimmi la tua", 260)
y = block(d, "Ti capita di\nsentirti gonfio\ndopo mangiato?", f("Bold", 80), y + 10)
block(d, "Due opzioni qui sotto.", f("Light", 40), y + 40, fill=DIM)
save(im, "gonfiore-1.png")

# 2 - risposta, spazio in basso per l'adesivo link al quiz
im, d = bg()
y = kicker(d, "quello che vedo in studio", 230)
y = block(d, "La prima cosa che\nchiedo non è cosa\nmangi, ma come.", f("Bold", 72), y + 10)
y += 30
y = block(d, "Fretta, bibite gassate e fibre aumentate\ndi colpo spiegano buona parte dei gonfiori.\nIl glutine c'entra molto meno di quanto\nsi creda.", f("Light", 42), y, maxw=900, fill=DIM)
y += 40
block(d, "Se ti torna quasi ogni giorno, sentiamoci.\nScrivimi INFO nei DM.", f("Regular", 42), y, maxw=900)
save(im, "gonfiore-2.png")

print("fatto: gonfiore-1.png, gonfiore-2.png")

import os
import sys; BASE = os.environ.get('IG_BASE', '/home/claude/ig'); sys.path.insert(0, BASE + '/sistema' if os.path.exists(BASE + '/sistema/foto.py') else BASE)
from PIL import Image, ImageDraw
import render as R, foto as FT
R.FONT_DIR = os.environ.get('IG_FONTS', BASE + '/fonts')
C, W, H, M = R.C, R.W, R.H, R.M
MAT = os.environ.get('IG_MAT', BASE + '/libreria/')
OUT = os.environ.get('IG_OUT', BASE + '/out') + '/plicometro'
import os; os.makedirs(OUT, exist_ok=True)
N = 6
tw = W - 2 * M
bianco = (255, 255, 255)

def salva(im, i):
    im.save(f'{OUT}/{i:02d}.jpg', quality=92, subsampling=0)

# 1 copertina
im = FT.riempi(Image.open(MAT + 'plicometria-braccio.jpg'), W, H, fx=0.42, fy=0.5)
im = FT.sfuma(im, 0, 260, forza=0.55, verso="su")
im = FT.sfuma(im, 470, 1090, forza=0.92)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 1, N)
R.occhiello(d, (M, 700), "Dentro la visita", C["navy300"])
y = R.blocco(d, (M, 752), "Cosa misura davvero il plicometro?", 600, 96, bianco, tw, 1.04, -0.028)
R.blocco(d, (M, y + 26), "Stesso peso, corpi diversi.", 400, 40, (225, 230, 238), tw, 1.4)
FT.piede_foto(d)
salva(im, 1)

# 2 schema della piega
im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
R.intestazione(d, 2, N)
R.occhiello(d, (M, 250), "Come funziona", C["navy600"])
y = R.blocco(d, (M, 300), "Una piega, due strati", 600, 80, C["ink"], tw, 1.1, -0.022)
R.blocco(d, (M, y + 24), "Si solleva una piega di pelle con il grasso che sta sotto. Lo strumento ne misura lo spessore, in millimetri.", 400, 40, C["ink2"], tw, 1.5)
# disegno in sezione
pelle, grasso, muscolo = (233, 200, 180), (246, 226, 160), (190, 116, 108)
x0, x1 = M, M + 600
yp, yg, ym, yb = 1000, 1022, 1092, 1160
d.rectangle((x0, yp, x1, yg), fill=pelle)
d.rectangle((x0, yg, x1, ym), fill=grasso)
d.rectangle((x0, ym, x1, yb), fill=muscolo)
cx = (x0 + x1) // 2; top = 700
d.rounded_rectangle((cx - 86, top, cx + 86, yg + 6), radius=86, fill=pelle)
d.rounded_rectangle((cx - 64, top + 22, cx + 64, ym - 10), radius=64, fill=grasso)
g = C["tit500"]
for sgn in (-1, 1):
    xe = cx + sgn * 86
    d.rectangle((min(xe, xe + sgn * 60), top + 150, max(xe, xe + sgn * 60), top + 172), fill=g)
    xb = xe + sgn * 60
    d.rectangle((min(xb, xb + sgn * 18), top - 40, max(xb, xb + sgn * 18), top + 172), fill=g)
pass
yq = top + 110
d.line((cx - 86, yq, cx + 86, yq), fill=C["navy600"], width=5)
for x in (cx - 86, cx + 86):
    d.line((x, yq - 16, x, yq + 16), fill=C["navy600"], width=5)
R.scrivi(d, (cx - 60, top + 200 - 80 - 58), "", R.F(600, 10), C["navy600"])
fl = R.F(500, 30); xl = x1 + 40
for testo, yy, yc in (("Pelle", 930, (yp + yg) // 2), ("Grasso sotto la pelle", 1010, (yg + ym) // 2), ("Muscolo", 1110, (ym + yb) // 2)):
    d.line((x1 - 10, yc, xl - 8, yy + 18), fill=C["ink3"], width=2)
    R.blocco(d, (xl, yy), testo, 500, 30, C["ink"], W - M - xl, 1.2)
R.scrivi(d, (xl, top + 88), "Spessore", R.F(500, 30), C["ink3"])
R.scrivi(d, (xl, top + 126), "12 mm", R.F(600, 48), C["navy600"])
d.line((cx + 100, yq, xl - 10, top + 150), fill=C["navy600"], width=2)
R.piede(d)
salva(im, 2)

# 3 i punti
im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
R.intestazione(d, 3, N)
R.occhiello(d, (M, 250), "Dove si misura", C["navy600"])
y = R.blocco(d, (M, 300), "Non un punto solo, ma diversi", 600, 80, C["ink"], tw, 1.1, -0.022)
R.blocco(d, (M, y + 24), "Di solito da 3 a 7 pliche, a seconda del metodo scelto.", 400, 40, C["ink2"], tw, 1.5)
punti = ["Bicipite", "Tricipite", "Sottoscapolare", "Soprailiaca", "Pettorale", "Addominale", "Coscia"]
yy = 680; col = [M, M + tw // 2 + 10]
for k, p in enumerate(punti):
    x = col[k % 2]; yk = yy + (k // 2) * 108
    d.rounded_rectangle((x, yk, x + tw // 2 - 10, yk + 88), radius=20, fill=C["bianco"], outline=C["riga"], width=2)
    d.ellipse((x + 28, yk + 32, x + 52, yk + 56), fill=C["navy600"] if k < 4 else C["navy200"])
    R.scrivi(d, (x + 76, yk + 24), p, R.F(500, 36), C["ink"])
R.blocco(d, (M, yy + 4 * 108 + 10), "In blu scuro le quattro pliche del metodo Durnin e Womersley, tra i più usati.", 400, 28, C["ink3"], tw, 1.4)
R.piede(d)
salva(im, 3)

# 4 dai millimetri alla percentuale
im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
R.intestazione(d, 4, N)
R.occhiello(d, (M, 250), "Il calcolo", C["navy600"])
y = R.blocco(d, (M, 300), "Dai millimetri alla percentuale", 600, 80, C["ink"], tw, 1.1, -0.022)
R.blocco(d, (M, y + 24), "Una formula validata trasforma la somma delle pliche in una stima del grasso corporeo.", 400, 40, C["ink2"], tw, 1.5)
yb = 760
d.rounded_rectangle((M, yb, W - M, yb + 330), radius=28, fill=C["bianco"], outline=C["riga"], width=2)
fnum = R.F(600, 64)
xx = M + 44
for k, v in enumerate(["6", "10", "14", "16"]):
    R.scrivi(d, (xx, yb + 60), v, fnum, C["ink"]); xx += R.larghezza(v, fnum, 0) + 16
    if k < 3:
        R.scrivi(d, (xx, yb + 60), "+", fnum, C["ink3"]); xx += R.larghezza("+", fnum, 0) + 16
R.scrivi(d, (xx, yb + 82), "mm", R.F(500, 36), C["ink3"])
R.scrivi(d, (M + 44, yb + 170), "→", R.F(600, 64), C["ink3"])
R.scrivi(d, (M + 140, yb + 150), "20,6 %", R.F(600, 104), C["navy600"], -0.02)
R.scrivi(d, (M + 44, yb + 272), "di massa grassa stimata", R.F(400, 30), C["ink2"])
R.blocco(d, (M, yb + 370), "Esempio con l'equazione di Durnin e Womersley a 4 pliche: uomo di 30 anni.", 400, 28, C["ink3"], tw, 1.4)
R.piede(d)
salva(im, 4)

# 5 foto degli strumenti + perché conta
im = Image.new("RGB", (W, H), C["carta"])
ph = FT.riempi(Image.open(MAT + 'strumenti-plicometro-metro.jpg'), W, 640, fx=0.5, fy=0.5)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 380, forza=0.92, verso="su")
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 5, N)
R.occhiello(d, (M, 700), "Perché conta", C["navy600"])
y = R.blocco(d, (M, 750), "Dice cosa cambia, non solo quanto", 600, 72, C["ink"], tw, 1.1, -0.022)
R.blocco(d, (M, y + 24), "Separa il grasso da tutto il resto. Ripetuta nel tempo, con gli stessi punti e lo stesso operatore, mostra se il piano sta funzionando.", 400, 38, C["ink2"], tw, 1.5)
R.piede(d)
salva(im, 5)

# 6 chiusura
im = Image.new("RGB", (W, H), C["tit900"])
ph = FT.riempi(Image.open(MAT + 'visita-studio.jpg'), W, 600, fx=0.45, fy=0.45)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 300, forza=0.7, verso="su")
im = FT.sfuma(im, 380, 600, colore=C["tit900"], forza=1.0)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 6, N)
R.occhiello(d, (M, 660), "Prenota", C["azione_scuro"])
y = R.blocco(d, (M, 700), "Vuoi conoscere la tua composizione?", 600, 70, C["su_scuro"], tw, 1.08, -0.022)
yb = R.blocco(d, (M, y + 26), "In studio la misuriamo con plicometria e bioimpedenza, in una delle cinque sedi in provincia di Verona.", 400, 35, C["su_scuro2"], tw, 1.5)
R.pillola(d, (M, yb + 44), "Scrivimi INFO nei DM", C["azione_scuro"], C["azione_scuro_testo"])
R.piede(d, scuro=True)
salva(im, 6)
print('ok')

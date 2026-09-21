import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('sistema'))
from PIL import Image, ImageDraw
import render as R, foto as FT

R.FONT_DIR = 'sistema/fonts'
C, W, H, M = R.C, R.W, R.H, R.M
MAT = 'libreria/'
OUT = 'out/gonfiore'; os.makedirs(OUT, exist_ok=True)
N = 7; tw = W - 2 * M
bianco = (255, 255, 255); chiaro = (225, 230, 238)

# ---------- 01 copertina ----------
im = FT.riempi(Image.open(MAT + 'ritratto-studio-scrivania.jpg'), W, H, fx=0.5, fy=0.53, zoom=1.3)
im = FT.sfuma(im, 0, 290, forza=0.55, verso="su")
im = FT.sfuma(im, 440, 1000, forza=0.95)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 1, N)
R.occhiello(d, (M, 712), "Salute intestinale", (150, 186, 240))
y = R.blocco(d, (M, 762), "Ti gonfi dopo mangiato? Non sempre è colpa del glutine", 600, 74, bianco, tw, 1.06, -0.026)
R.blocco(d, (M, y + 30), "Quattro cause comuni che spesso si sistemano a tavola.", 400, 36, chiaro, tw - 60, 1.45)
FT.piede_foto(d)
im.save(f'{OUT}/01.jpg', quality=92, subsampling=0)

# ---------- 02-06 ----------
PUNTI = [
    ("Causa 1", "Mangi in fretta",
     "Quando mangi veloce, o parli molto a tavola, ingoi aria. Una parte del gonfiore è solo questa.\n\n"
     "Prova a posare la forchetta tra un boccone e l'altro e a masticare di più."),
    ("Causa 2", "Bollicine e gomme",
     "Le bibite gassate portano gas nello stomaco.\n\n"
     "Gomme e caramelle senza zucchero contengono spesso polioli, come sorbitolo e xilitolo: nell'intestino fermentano e producono gas."),
    ("Causa 3", "Troppe fibre, tutte insieme",
     "Legumi, cereali integrali e verdure fanno bene. Ma se passi da poco a tanto in pochi giorni, l'intestino protesta.\n\n"
     "Aumenta un po' alla volta e bevi abbastanza acqua."),
    ("Causa 4", "Intestino pigro",
     "Se vai in bagno poco e con fatica, il gonfiore spesso arriva da lì.\n\n"
     "Acqua, fibre, movimento e orari regolari sono il primo passo."),
    ("Prima di togliere un alimento", "Non eliminare il glutine da solo",
     "Toglierlo senza esami rende la dieta più povera e può falsare gli esami per la celiachia, che vanno fatti mentre il glutine lo mangi ancora.\n\n"
     "Se il gonfiore è frequente, o arriva con dolore, perdita di peso o sangue, parlane con il medico."),
]
for k, (et, tit, body) in enumerate(PUNTI, 2):
    im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
    R.intestazione(d, k, N)
    y0 = 300
    d.line((M, y0, W - M, y0), fill=C["riga"], width=3)
    d.line((M, y0, M + round(tw * (k - 1) / (N - 2)), y0), fill=C["navy600"], width=3)
    R.scrivi(d, (M, y0 + 46), et.upper(), R.F(600, 26), C["tit500"], 0.09)
    y = R.blocco(d, (M, y0 + 112), tit, 600, 80, C["ink"], tw, 1.10, -0.022, max_h=200, min_size=52)
    R.blocco(d, (M, y + 44), body, 400, 44, C["ink2"], tw, 1.55, max_h=H - 200 - (y + 44), min_size=32)
    R.piede(d)
    im.save(f'{OUT}/{k:02d}.jpg', quality=92, subsampling=0)

# ---------- 07 chiusura ----------
im = Image.new("RGB", (W, H), C["tit900"])
ph = FT.riempi(Image.open(MAT + 'legumi-cereali.jpg'), W, 520, fx=0.5, fy=0.5)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 320, forza=0.9, verso="su")
im = FT.sfuma(im, 320, 520, colore=C["tit900"], forza=1.0)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, N, N)
R.occhiello(d, (M, 592), "Capiamolo insieme", C["azione_scuro"])
y = R.blocco(d, (M, 644), "Il gonfiore ha quasi sempre una causa", 600, 72, C["su_scuro"], tw, 1.08, -0.022)
yb = R.blocco(d, (M, y + 30), "In visita ricostruiamo cosa mangi, come e quando.\n"
                              "In studio, in cinque sedi in provincia di Verona, oppure in videochiamata.",
              400, 38, C["su_scuro2"], tw, 1.5, max_h=300, min_size=32)
R.pillola(d, (M, min(max(yb + 56, H - 300), H - 270)), "Scrivimi INFO nei DM", C["azione_scuro"], C["azione_scuro_testo"])
R.piede(d, scuro=True)
im.save(f'{OUT}/07.jpg', quality=92, subsampling=0)
print('ok')

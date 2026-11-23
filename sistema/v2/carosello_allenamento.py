import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('sistema'))
from PIL import Image, ImageDraw
import render as R, foto as FT

R.FONT_DIR = 'sistema/fonts'
C, W, H, M = R.C, R.W, R.H, R.M
MAT = 'libreria/'
OUT = 'out/allenamento'; os.makedirs(OUT, exist_ok=True)
N = 6; tw = W - 2 * M
bianco = (255, 255, 255); chiaro = (225, 230, 238)

im = FT.riempi(Image.open(MAT + 'ritratto-camice-camicia-blu.jpg'), W, H, fx=0.5, fy=0.34)
im = FT.sfuma(im, 0, 290, forza=0.55, verso="su")
im = FT.sfuma(im, 430, 1000, forza=0.95)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 1, N)
R.occhiello(d, (M, 712), "Nutrizione sportiva", (150, 186, 240))
y = R.blocco(d, (M, 762), "Mangiare prima o dopo l'allenamento conta meno di quanto credi", 600, 74, bianco, tw, 1.06, -0.026)
R.blocco(d, (M, y + 30), "Quello che sposta i risultati sta nel resto della giornata.", 400, 36, chiaro, tw - 60, 1.45)
FT.piede_foto(d)
im.save(f'{OUT}/01.jpg', quality=92, subsampling=0)

PUNTI = [
    ("Punto 1", "Prima viene il totale della giornata",
     "Quante proteine e quanta energia arrivano in tutta la giornata pesa molto più dell'ora in cui arrivano.\n\n"
     "Se il totale non torna, nessun orario lo sistema."),
    ("Punto 2", "La finestra non è di mezz'ora",
     "Dopo una seduta con i pesi il muscolo resta più sensibile alle proteine per diverse ore.\n\n"
     "Non serve bere qualcosa di corsa negli spogliatoi: serve che nel giro di qualche ora arrivi un pasto completo."),
    ("Punto 3", "Prima si mangia per non arrivare a secco",
     "Se ti alleni presto e stai bene a stomaco vuoto, va bene così.\n\n"
     "Se invece cali a metà seduta, uno spuntino con carboidrati una o due ore prima cambia la resa. Più è vicino all'allenamento, più deve essere leggero."),
    ("Punto 4", "Le proteine, distribuite",
     "Negli studi sull'allenamento con i pesi i guadagni si fermano intorno a 1,6 grammi di proteine per chilo di peso al giorno. Oltre, in media, non si aggiunge altro.\n\n"
     "Conta anche come le distribuisci: tre o quattro pasti, non tutte alla sera."),
]
for k, (et, tit, body) in enumerate(PUNTI, 2):
    im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
    R.intestazione(d, k, N)
    y0 = 300
    d.line((M, y0, W - M, y0), fill=C["riga"], width=3)
    d.line((M, y0, M + round(tw * (k - 1) / (N - 2)), y0), fill=C["navy600"], width=3)
    R.scrivi(d, (M, y0 + 46), et.upper(), R.F(600, 26), C["tit500"], 0.09)
    y = R.blocco(d, (M, y0 + 112), tit, 600, 80, C["ink"], tw, 1.10, -0.022, max_h=260, min_size=48)
    R.blocco(d, (M, y + 44), body, 400, 44, C["ink2"], tw, 1.55, max_h=H - 200 - (y + 44), min_size=32)
    R.piede(d)
    im.save(f'{OUT}/{k:02d}.jpg', quality=92, subsampling=0)

im = Image.new("RGB", (W, H), C["tit900"])
ph = FT.riempi(Image.open(MAT + 'bowl-salmone.jpg'), W, 520, fx=0.5, fy=0.5)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 320, forza=0.9, verso="su")
im = FT.sfuma(im, 320, 520, colore=C["tit900"], forza=1.0)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, N, N)
R.occhiello(d, (M, 592), "Nutrizione sportiva", C["azione_scuro"])
y = R.blocco(d, (M, 644), "Il piano si costruisce sulla tua programmazione", 600, 72, C["su_scuro"], tw, 1.08, -0.022)
yb = R.blocco(d, (M, y + 30), "Orari di allenamento, lavoro, recupero: il piano parte da lì.\n"
                              "In studio, in cinque sedi in provincia di Verona, oppure in videochiamata.",
              400, 38, C["su_scuro2"], tw, 1.5, max_h=300, min_size=32)
R.pillola(d, (M, min(max(yb + 56, H - 300), H - 270)), "Scrivimi INFO nei DM", C["azione_scuro"], C["azione_scuro_testo"])
R.piede(d, scuro=True)
im.save(f'{OUT}/06.jpg', quality=92, subsampling=0)
print('ok')

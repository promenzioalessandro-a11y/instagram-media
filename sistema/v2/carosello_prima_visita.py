import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('sistema'))
from PIL import Image, ImageDraw
import render as R, foto as FT

R.FONT_DIR = 'sistema/fonts'
C, W, H, M = R.C, R.W, R.H, R.M
MAT = 'libreria/'
OUT = 'out/prima-visita'; os.makedirs(OUT, exist_ok=True)
N = 6; tw = W - 2 * M
bianco = (255, 255, 255); chiaro = (225, 230, 238)

# ---------- 01 copertina ----------
im = FT.riempi(Image.open(MAT + 'ritratto-camice-grigio.jpg'), W, H, fx=0.52, fy=0.30)
im = FT.sfuma(im, 0, 290, forza=0.55, verso="su")
im = FT.sfuma(im, 420, 980, forza=0.95)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 1, N)
R.occhiello(d, (M, 742), "La prima visita", (150, 186, 240))
y = R.blocco(d, (M, 792), "Cosa succede davvero alla prima visita", 600, 78, bianco, tw, 1.06, -0.026)
R.blocco(d, (M, y + 34), "Te lo spiego passo per passo, così arrivi tranquillo.", 400, 36, chiaro, tw - 60, 1.45)
FT.piede_foto(d)
im.save(f'{OUT}/01.jpg', quality=92, subsampling=0)

# ---------- 02-05 passaggi ----------
PUNTI = [
    (1, "Valutazione iniziale",
     "Anamnesi completa, obiettivi definiti insieme e analisi della composizione corporea con plicometria e bioimpedenza. Circa 60 minuti.\n\n"
     "La composizione corporea si misura in studio. In videochiamata partiamo da anamnesi, obiettivi e dati che hai già."),
    (2, "Strategia personalizzata",
     "Costruisco il piano sulle evidenze e sulla tua giornata vera: orari, allenamenti, quello che ti piace mangiare.\n\n"
     "Ti spiego il perché di ogni scelta, perché quando lo sai il piano lo mantieni."),
    (3, "Monitoraggio e adattamento",
     "A ogni controllo rileggiamo insieme i dati e aggiorno il piano su come ha risposto il tuo corpo.\n\nIl piano non resta uguale per mesi: cambia con te."),
    (None, "Cosa portare",
     "Si comincia in ogni caso, anche a mani vuote.\n\n"
     "Se le hai: analisi del sangue degli ultimi 12 mesi, referti, lista di farmaci o integratori in uso."),
]
for k, (num, tit, body) in enumerate(PUNTI, 2):
    im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
    R.intestazione(d, k, N)
    y0 = 300
    d.line((M, y0, W - M, y0), fill=C["riga"], width=3)
    d.line((M, y0, M + round(tw * (k - 1) / (N - 2)), y0), fill=C["navy600"], width=3)
    et = f"Passo {num}" if num else "Prima di venire"
    R.scrivi(d, (M, y0 + 46), et.upper(), R.F(600, 26), C["tit500"], 0.09)
    y = R.blocco(d, (M, y0 + 112), tit, 600, 80, C["ink"], tw, 1.10, -0.022, max_h=200, min_size=52)
    R.blocco(d, (M, y + 44), body, 400, 44, C["ink2"], tw, 1.55, max_h=H - 200 - (y + 44), min_size=32)
    R.piede(d)
    im.save(f'{OUT}/{k:02d}.jpg', quality=92, subsampling=0)

# ---------- 06 chiusura ----------
im = Image.new("RGB", (W, H), C["tit900"])
ph = FT.riempi(Image.open(MAT + 'visita-studio.jpg'), W, 520, fx=0.45, fy=0.45)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 320, forza=0.9, verso="su")
im = FT.sfuma(im, 320, 520, colore=C["tit900"], forza=1.0)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, N, N)
R.occhiello(d, (M, 592), "Prenota", C["azione_scuro"])
y = R.blocco(d, (M, 644), "Prima visita da 120 euro", 600, 76, C["su_scuro"], tw, 1.08, -0.022)
yb = R.blocco(d, (M, y + 30), "Il costo varia in base alla sede. Detraibile al 19% con pagamento tracciabile.\n"
                              "In studio, in cinque sedi in provincia di Verona, oppure in videochiamata.",
              400, 38, C["su_scuro2"], tw, 1.5, max_h=300, min_size=32)
R.pillola(d, (M, min(max(yb + 56, H - 300), H - 270)), "Scrivimi INFO nei DM", C["azione_scuro"], C["azione_scuro_testo"])
R.piede(d, scuro=True)
im.save(f'{OUT}/06.jpg', quality=92, subsampling=0)
print('ok')

import sys, os; BASE = os.environ.get('IG_BASE', '/home/claude/ig'); sys.path.insert(0, BASE + '/sistema' if os.path.exists(BASE + '/sistema/foto.py') else BASE)
from PIL import Image, ImageDraw
import render as R, foto as FT
R.FONT_DIR = os.environ.get('IG_FONTS', BASE + '/fonts')
C, W, H, M = R.C, R.W, R.H, R.M
MAT = os.environ.get('IG_MAT', BASE + '/libreria/')
OUT = os.environ.get('IG_OUT', BASE + '/out') + '/recensioni'; os.makedirs(OUT, exist_ok=True)
N = 5; tw = W - 2 * M; bianco = (255, 255, 255)
REC = [
 ("Giulia S.", "Professionale, puntuale e attento alle esigenze. Umano e ti aiuta, ascoltandoti e modifica il piano in itinere per seguire i tuoi bisogni e i tuoi gusti. Disponibile, telefonicamente, per chiarimenti."),
 ("Saverio N.", "A maggio ho iniziato il percorso nutrizionale, per la prima volta nella mia vita, con il Dott. Promenzio. Mi sto trovando benissimo, ho ottenuto da subito ottimi risultati sia in termini di peso che di benessere. Questo mi motiva molto a proseguire. È molto competente, disponibile e spiega in modo chiaro. Lo consiglio a tutti!"),
 ("Barbara F.", "Finalmente un biologo nutrizionista preparato, seppur giovane, mi ha aiutata a perdere quei chili in più dovuti alla menopausa. Fa un'analisi approfondita del tuo corpo e in base alle tue preferenze ti prepara la dieta, che dieta non è perché ho finalmente imparato a mangiare correttamente, senza sentire la fame. Consiglio vivamente il dott. Promenzio."),
]
# copertina
im = FT.riempi(Image.open(MAT + 'ritratto-studio-scrivania.jpg'), W, H, fx=0.5, fy=0.42)
im = FT.sfuma(im, 0, 300, forza=0.6, verso="su")
im = FT.sfuma(im, 470, 980, forza=0.94)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, 1, N)
R.occhiello(d, (M, 800), "Recensioni Google", C["navy300"])
R.scrivi(d, (M, 840), "5,0", R.F(600, 170), bianco, -0.03)
FT.stelle(d, (M + 300, 900), 5, 62, (242, 201, 76))
R.blocco(d, (M, 1030), "24 recensioni. Tre, parola per parola.", 400, 42, (225, 230, 238), tw, 1.4)
FT.piede_foto(d)
im.save(f'{OUT}/01.jpg', quality=92, subsampling=0)
# citazioni
for k, (aut, txt) in enumerate(REC, 2):
    im = Image.new("RGB", (W, H), C["carta"]); d = ImageDraw.Draw(im)
    R.intestazione(d, k, N)
    R.scrivi(d, (M - 8, 190), "“", R.F(600, 260), C["navy200"])
    FT.stelle(d, (M, 450), 5, 40, C["navy600"])
    size = 50 if len(txt) < 250 else 42
    y = R.blocco(d, (M, 530), txt, 500, size, C["ink"], tw, 1.42, -0.01, max_h=H - 330 - 530, min_size=34)
    R.scrivi(d, (M, H - 250), aut, R.F(600, 34), C["ink"])
    R.scrivi(d, (M, H - 206), "Recensione su Google", R.F(400, 28), C["ink3"])
    R.piede(d)
    im.save(f'{OUT}/{k:02d}.jpg', quality=92, subsampling=0)
# chiusura
im = Image.new("RGB", (W, H), C["tit900"])
ph = FT.riempi(Image.open(MAT + 'visita-studio.jpg'), W, 600, fx=0.45, fy=0.45)
im.paste(ph, (0, 0))
im = FT.sfuma(im, 0, 380, forza=0.9, verso="su")
im = FT.sfuma(im, 380, 600, colore=C["tit900"], forza=1.0)
d = ImageDraw.Draw(im)
FT.intestazione_foto(d, N, N)
R.occhiello(d, (M, 660), "Prenota", C["azione_scuro"])
y = R.blocco(d, (M, 712), "Il prossimo percorso può essere il tuo", 600, 76, C["su_scuro"], tw, 1.08, -0.022)
yb = R.blocco(d, (M, y + 26), "Cinque sedi in provincia di Verona, oppure online.", 400, 38, C["su_scuro2"], tw, 1.5)
R.pillola(d, (M, max(yb + 56, H - 300)), "Scrivimi INFO nei DM", C["azione_scuro"], C["azione_scuro_testo"])
R.piede(d, scuro=True)
im.save(f'{OUT}/05.jpg', quality=92, subsampling=0)
print('ok')

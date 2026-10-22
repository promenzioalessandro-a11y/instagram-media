"""Post gonfiore (22/10/2026): "In studio la prima cosa che chiedo non e' cosa mangi, ma come mangi".

Nasce dalla storia sondaggio sul gonfiore, l'unico contenuto che Alessandro ha
detto di aver apprezzato e che ha pubblicato. Una sola immagine 1080x1350,
nessun testo sopra, foto gia' in libreria.

Uso:
    IG_BASE=/percorso/del/repo python3 post_gonfiore.py
Esce in <IG_OUT>/gonfiore-post/01.jpg
"""
import os, sys

BASE = os.environ.get('IG_BASE', '/home/claude/ig')
sys.path.insert(0, BASE + '/sistema/v2')
from PIL import Image
import render as R, foto as FT

R.FONT_DIR = os.environ.get('IG_FONTS', BASE + '/sistema/fonts')
MAT = os.environ.get('IG_MAT', BASE + '/libreria/')
OUT = os.environ.get('IG_OUT', BASE + '/out') + '/gonfiore-post'
os.makedirs(OUT, exist_ok=True)

im = FT.riempi(Image.open(MAT + 'ritratto-studio-scrivania.jpg'), R.W, R.H, fx=0.5, fy=0.47)
im.save(OUT + '/01.jpg', quality=92, subsampling=0)
print(OUT + '/01.jpg')

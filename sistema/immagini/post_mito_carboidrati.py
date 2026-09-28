"""Post del 29/09/2026: "I carboidrati la sera non fanno ingrassare".

Una sola immagine, 1080x1350, nessun testo sopra: linea contenuti del 22/09
(foto vera, niente grafiche a modello). Foto gia' in libreria, nessuno scatto
nuovo richiesto.

Uso:
    IG_BASE=/percorso/del/repo python3 post_mito_carboidrati.py
Esce in <IG_OUT>/mito-carboidrati/01.jpg
"""
import os, sys

BASE = os.environ.get('IG_BASE', '/home/claude/ig')
sys.path.insert(0, BASE + '/sistema/v2')
from PIL import Image
import render as R, foto as FT

R.FONT_DIR = os.environ.get('IG_FONTS', BASE + '/sistema/fonts')
MAT = os.environ.get('IG_MAT', BASE + '/libreria/')
OUT = os.environ.get('IG_OUT', BASE + '/out') + '/mito-carboidrati'
os.makedirs(OUT, exist_ok=True)

im = FT.riempi(Image.open(MAT + 'ritratto-scrivania.jpg'), R.W, R.H, fx=0.5, fy=0.42)
im.save(OUT + '/01.jpg', quality=92, subsampling=0)
print(OUT + '/01.jpg')

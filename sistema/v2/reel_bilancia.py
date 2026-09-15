import sys, os, subprocess, shutil
BASE = os.environ.get('IG_BASE', '/home/claude/ig'); sys.path.insert(0, BASE + '/sistema' if os.path.exists(BASE + '/sistema/foto.py') else BASE)
import numpy as np
from PIL import Image, ImageDraw
import render as R, foto as FT
R.FONT_DIR = os.environ.get('IG_FONTS', BASE + '/fonts')
C = R.C
MAT = os.environ.get('IG_MAT', BASE + '/libreria/')
W, H, FPS = 1080, 1920, 30
M = 90
OUT = os.environ.get('IG_OUT', BASE + '/out') + '/reel'; FR = OUT + '/frames'
os.makedirs(FR, exist_ok=True)
RANGE = os.environ.get('IG_RANGE')  # es. '0:300' per lavorare a blocchi
SOLO_VIDEO = os.environ.get('IG_SOLO_VIDEO') == '1'
bianco = (255, 255, 255); evid = C["navy300"]

# (foto, fx, fy, durata, righe testo [(testo, peso, size, colore)], zoom da, a)
SCENE = [
 ('ritratto-camice-grigio.jpg', .5, .35, 3.5, [("Ti pesi e segna", 600, 84, bianco), ("un chilo in più", 600, 84, evid), ("di ieri?", 600, 84, bianco)], 1.00, 1.10),
 ('metro-girovita.jpg', .5, .5, 4.5, [("Quasi certamente", 600, 76, bianco), ("non è grasso.", 600, 76, evid), ("Per un chilo di grasso servono circa 7.000 calorie in più del necessario.", 400, 46, bianco)], 1.12, 1.00),
 ('cena-tavola.jpg', .5, .5, 4.5, [("Una cena salata", 600, 76, bianco), ("fa trattenere acqua,", 600, 76, bianco), ("per qualche giorno.", 600, 76, evid)], 1.00, 1.12),
 ('piatto-riso-verdure.jpg', .5, .5, 4.5, [("Ogni grammo di glicogeno", 600, 70, bianco), ("nei muscoli si porta dietro", 600, 70, bianco), ("circa 3 grammi d'acqua.", 600, 70, evid)], 1.10, 1.00),
 ('strumenti-plicometro-metro.jpg', .5, .5, 5.0, [("Pesati sempre alla stessa ora", 600, 62, bianco), ("e guarda la media delle settimane.", 600, 62, bianco), ("Meglio ancora: misura il girovita.", 600, 62, evid)], 1.00, 1.10),
 ('visita-studio.jpg', .45, .45, 4.0, [("Ti aiuto a leggere", 600, 84, bianco), ("i numeri giusti.", 600, 84, evid)], 1.08, 1.00),
]
XF = 0.4  # dissolvenza

def base(nome, fx, fy):
    img = Image.open(MAT + nome).convert("RGB")
    s = max(W / img.width, H / img.height) * 1.14
    return img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS), fx, fy

def inquadra(b, z, zmax=1.14):
    img, fx, fy = b
    w, h = round(W * zmax / z), round(H * zmax / z)
    cx, cy = img.width * fx, img.height * fy
    x = min(max(round(cx - w / 2), 0), img.width - w); y = min(max(round(cy - h / 2), 0), img.height - h)
    return img.crop((x, y, x + w, y + h)).resize((W, H), Image.BILINEAR)

VELO = None
def velo(im):
    global VELO
    if VELO is None:
        a = np.zeros((H, 1), np.float32)
        for y in range(H):
            t1 = max(0, 1 - y / 420) * 0.55
            if y < 820: t2 = 0
            elif y < 1080: t2 = ((y - 820) / 260) ** 1.5
            else: t2 = 1
            a[y, 0] = max(t1, 0.8 * t2)
        VELO = Image.fromarray((np.repeat(a, W, 1) * 255).astype(np.uint8))
    return Image.composite(Image.new("RGB", (W, H), (10, 14, 22)), im, VELO)

def testo(d, righe, t_scena, alpha_glob):
    y = 1100
    for k, (tx, peso, size, col) in enumerate(righe):
        t0 = 0.25 + k * 0.45
        a = min(1, max(0, (t_scena - t0) / 0.35)) * alpha_glob
        if a <= 0:
            f = R.F(peso, size); y += len(R.a_capo(tx, f, W - 2 * M, -0.02 if peso == 600 else 0)) * round(size * 1.15) + 10; continue
        off = round((1 - a) * 24)
        colore = tuple(round(c * a + 20 * (1 - a)) for c in col)
        y = R.blocco(d, (M, y + off), tx, peso, size, colore, W - 2 * M, 1.15 if peso == 600 else 1.35, -0.02 if peso == 600 else 0) - off + 10

def firma(d):
    R.scrivi(d, (M, 150), "Dott. Alessandro Promenzio", R.F(600, 36), bianco, -0.008)
    R.scrivi(d, (M, 196), "Biologo Nutrizionista", R.F(400, 28), (225, 230, 238), 0.01)

basi = [base(s[0], s[1], s[2]) for s in SCENE]
n = 0
starts = []; t = 0
for s in SCENE: starts.append(t); t += s[3]
TOT = t + 2.2  # chiusura
def scena_frame(i, ts):
    s = SCENE[i]; p = ts / s[3]
    z = s[5] + (s[6] - s[5]) * p
    return inquadra(basi[i], z)

_a, _b = (int(x) for x in RANGE.split(':')) if RANGE else (0, int(TOT * FPS))
_b = min(_b, int(TOT * FPS))
for f in ([] if SOLO_VIDEO else range(_a, _b)):
    tt = f / FPS
    if tt < t:
        i = max(k for k in range(len(SCENE)) if starts[k] <= tt)
        ts = tt - starts[i]
        im = scena_frame(i, ts)
        if i + 1 < len(SCENE) and SCENE[i][3] - ts < XF:
            a = 1 - (SCENE[i][3] - ts) / XF
            im = Image.blend(im, scena_frame(i + 1, 0), a)
        im = velo(im)
        d = ImageDraw.Draw(im)
        firma(d)
        fade = 1 if SCENE[i][3] - ts > XF else (SCENE[i][3] - ts) / XF
        testo(d, SCENE[i][4], ts, fade)
    else:
        # chiusura su fondo antracite
        ts = tt - t
        im = Image.new("RGB", (W, H), C["tit900"]); d = ImageDraw.Draw(im)
        a = min(1, ts / 0.4)
        mono = None
        R.occhiello(d, (M, 1000), "Prima visita a Verona e online", C["azione_scuro"])
        R.blocco(d, (M, 1060), "Scrivimi INFO in DM", 600, 96, C["su_scuro"], W - 2 * M, 1.05, -0.028)
        R.scrivi(d, (M, 1200), "@dott_promenzio", R.F(500, 44), C["su_scuro2"])
        firma(d)
        if a < 1:
            im = Image.blend(Image.new("RGB", (W, H), C["tit900"]), im, a)
    im.save(f'{FR}/{f:05d}.jpg', quality=90)
    if f == int(0.9 * FPS):
        im.save(OUT + '/copertina.jpg', quality=92)
if RANGE and not SOLO_VIDEO:
    print('blocco', _a, _b, 'di', int(TOT * FPS)); raise SystemExit
subprocess.run([os.environ.get('IG_FFMPEG', 'ffmpeg'), '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{FR}/%05d.jpg',
                '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest',
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '19', '-movflags', '+faststart',
                '-c:a', 'aac', '-b:a', '128k', OUT + '/reel_bilancia.mp4'], check=True)
print('durata', TOT)

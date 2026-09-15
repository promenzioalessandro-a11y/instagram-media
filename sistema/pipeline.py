"""Pipeline Instagram @dott_promenzio, da usare nel workbench Composio.

from pipeline import *
sync()                      # scarica render.py, piano.json e font dal repo
prossimo()                  # primo post del piano ancora in bozza
urls = prepara(post_id)     # genera le immagini e le carica nel repo, restituisce gli indirizzi pubblici
segna(post_id, "pubblicato", media_id="...")   # aggiorna lo stato nel piano
"""
import base64, json, os, sys, time, requests
from concurrent.futures import ThreadPoolExecutor

OWNER, REPO = "promenzioalessandro-a11y", "instagram-media"
RAW = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main/"
BASE = "/mnt/files/ig"
FONTS = ["Inter_400Regular.ttf", "Inter_500Medium.ttf", "Inter_600SemiBold.ttf", "Inter_700Bold.ttf"]


def _get(path):
    r = requests.get(RAW + path + f"?t={int(time.time())}", timeout=60)
    r.raise_for_status()
    return r.content


def sync():
    os.makedirs(BASE + "/fonts", exist_ok=True)
    open(BASE + "/render.py", "wb").write(_get("sistema/render.py"))
    open(BASE + "/piano.json", "wb").write(_get("sistema/piano.json"))
    for f in FONTS:
        p = BASE + "/fonts/" + f
        if not os.path.exists(p):
            open(p, "wb").write(_get("sistema/fonts/" + f))
    if BASE not in sys.path:
        sys.path.insert(0, BASE)
    return piano()


def piano():
    return json.load(open(BASE + "/piano.json"))


def trova(post_id):
    return next(p for p in piano() if p["id"] == post_id)


def prossimo():
    return next((p for p in piano() if p.get("stato", "bozza") == "bozza" and p.get("tipo") == "settimanale"), None)


def carica(path_repo, data_bytes, msg, run):
    res, err = run("GITHUB_CREATE_OR_UPDATE_FILE_CONTENTS", {
        "owner": OWNER, "repo": REPO, "path": path_repo, "branch": "main",
        "message": msg, "content": base64.b64encode(data_bytes).decode()})
    if err:
        raise RuntimeError(f"{path_repo}: {err}")


def prepara(post_id, run, versione=None):
    import importlib, render
    importlib.reload(render)
    post = trova(post_id)
    v = versione or time.strftime("%Y%m%d%H%M")
    out = f"{BASE}/out/{post_id}-{v}"
    paths = render.render(post, out, BASE + "/fonts")
    def up(p):
        rp = f"media/{post_id}/{v}/{os.path.basename(p)}"
        carica(rp, open(p, "rb").read(), f"Immagini {post_id}", run)
        return RAW + rp
    urls = [up(p) for p in paths]
    time.sleep(3)
    for u in urls:
        h = requests.head(u, timeout=30)
        assert h.status_code == 200 and h.headers.get("content-type") == "image/jpeg", (u, h.status_code)
    return urls


def segna(post_id, stato, run, **extra):
    raw = _get("sistema/piano.json")
    dati = json.loads(raw)
    for p in dati:
        if p["id"] == post_id:
            p["stato"] = stato
            p.update(extra)
    testo = json.dumps(dati, ensure_ascii=False, indent=1)
    carica("sistema/piano.json", testo.encode(), f"{post_id}: {stato}", run)
    open(BASE + "/piano.json", "w").write(testo)

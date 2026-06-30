#!/usr/bin/env python3
"""Squint — a minimal local proofreading viewer for Peirce transcriptions.

A companion to a coding agent, NOT a standalone editor. You squint at the page
image beside the machine scaffold; the agent (Claude Code / codex) edits the
.txt files. Each view emits a copy-pasteable block bundling the text with its
pointer: the local file path to fix AND the archive.org page image (the source).
Hand that block to your agent. Hit Refresh to re-read a file the agent just edited.

Run:  python3 tools/squint/server.py   (then open http://localhost:8731)
No dependencies; Python 3 stdlib only. Read-only: it never writes your files.
"""
import http.server, json, os, re, csv, urllib.parse

PORT = 1913
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TX     = os.path.join(ROOT, "transcriptions")
BYITEM = os.path.join(ROOT, "houghton-export", "by-item")
THUMB  = os.path.join(ROOT, "houghton-export", "thumb")

SAFE_ROBIN = re.compile(r'^\d{1,4}$')
SAFE_IMG   = re.compile(r'^[A-Za-z0-9_]+$')

def robin_folders():
    m = {}
    if os.path.isdir(BYITEM):
        for f in os.listdir(BYITEM):
            mo = re.match(r'^(\d+)', f)
            if mo: m[mo.group(1)] = f
    return m
FOLDERS = robin_folders()

def ia_map():
    m = {}
    p = os.path.join(ROOT, "references", "archive-org-items.tsv")
    if os.path.exists(p):
        for row in csv.DictReader(open(p), delimiter='\t'):
            m[row['robin']] = row
    return m
IA = ia_map()

def title_of(robin):
    fol = FOLDERS.get(robin, "")
    slug = re.sub(r'^\d+_?', '', fol).replace('-', ' ').strip()
    return slug.title() if slug else f"R{robin}"

def pointer(robin, img):
    ia = IA.get(robin, {})
    ident = ia.get('ia_identifier') or (f"peirce-msam1632-{int(robin):04d}" if robin.isdigit() else "")
    url = f"https://archive.org/download/{ident}/{img}.jpg" if ident else ""
    cite = f'C. S. Peirce, "{title_of(robin)}" (MS Am 1632 ({robin})), leaf {img}'
    return cite, url

def list_items():
    out = []
    if not os.path.isdir(TX): return out
    for d in sorted(os.listdir(TX)):
        mo = re.match(r'^R(\d+)$', d)
        if not mo: continue
        robin = mo.group(1)
        pages = sorted(x[:-4] for x in os.listdir(os.path.join(TX, d)) if x.endswith('.txt'))
        if pages:
            out.append({"robin": robin, "title": title_of(robin), "pages": pages})
    out.sort(key=lambda x: int(x['robin']))
    return out

def img_path(robin, img, size):
    if size == "thumb":
        p = os.path.join(THUMB, img + ".jpg")
        if os.path.exists(p): return p
    fol = FOLDERS.get(robin)
    if fol:
        p = os.path.join(BYITEM, fol, img + ".jpg")
        if os.path.exists(p): return p
    # fall back to thumb if full missing
    p = os.path.join(THUMB, img + ".jpg")
    return p if os.path.exists(p) else None

def txt_path(robin, img):
    return os.path.join(TX, f"R{robin}", img + ".txt")

class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _send(self, code, body, ctype="application/json", extra=None):
        if isinstance(body, (dict, list)): body = json.dumps(body).encode()
        elif isinstance(body, str): body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        if extra:
            for k, v in extra.items(): self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        if u.path in ("/", "/index.html"):
            with open(os.path.join(HERE, "index.html"), "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if u.path == "/api/items":
            return self._send(200, list_items())
        if u.path == "/api/txt":
            robin = q.get("robin", [""])[0]; img = q.get("img", [""])[0]
            if not (SAFE_ROBIN.match(robin) and SAFE_IMG.match(img)):
                return self._send(400, {"error": "bad params"})
            p = txt_path(robin, img)
            text = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
            cite, url = pointer(robin, img)
            relpath = os.path.relpath(p, ROOT)
            return self._send(200, {"text": text, "cite": cite, "url": url, "path": relpath})
        m = re.match(r'^/img/(\d{1,4})/([A-Za-z0-9_]+)$', u.path)
        if m:
            robin, img = m.group(1), m.group(2)
            size = q.get("size", ["full"])[0]
            p = img_path(robin, img, size)
            if not p: return self._send(404, {"error": "no image"})
            with open(p, "rb") as f:
                return self._send(200, f.read(), "image/jpeg",
                                  extra={"Cache-Control": "max-age=86400"})
        return self._send(404, {"error": "not found"})

if __name__ == "__main__":
    items = list_items()
    npages = sum(len(i["pages"]) for i in items)
    print(f"Squint: {len(items)} items, {npages} pages.  http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()

#!/usr/bin/env python3
"""Attach a full-text layer (<ident>_djvu.txt) to every transcribed Peirce IA item,
and stamp each item's description with credit + a backlink to june.kim/peirce.
Idempotent: re-uploads the text (overwrites), appends the credit only if missing.
Run from the peirce repo root. Requires an authenticated `ia` CLI."""
import os, re, csv, json, sys, time, subprocess, urllib.request

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TX=os.path.join(ROOT,"transcriptions")
BACKLINK="https://june.kim/peirce"
CREDIT=(" A machine-assisted full-text transcription (under human correction) is "
        f"included with this item; browse the page images alongside the text at {BACKLINK} .")
CONTRIB=f"June Kim (transcription), {BACKLINK}"

def clean(t):
    t=re.sub(r'\{del\}(.*?)\{/del\}', r'\1', t, flags=re.S)
    t=re.sub(r'\{add\}(.*?)\{/add\}', r'\1', t, flags=re.S)
    t=re.sub(r'\[unclear:\s*(.*?)\??\]', r'\1', t, flags=re.S)
    t=re.sub(r'\[hand:\s*(.*?)\]', r'\1', t, flags=re.S)
    t=re.sub(r'\[illegible\]', '', t)
    t=re.sub(r'\[formula:[^\]]*\]', '', t)
    t=re.sub(r'\[diagram:\s*(.*?)\]', r'[\1]', t, flags=re.S)
    return t.strip()

def meta(ident):
    for _ in range(4):
        try:
            return json.load(urllib.request.urlopen(f"https://archive.org/metadata/{ident}",timeout=30))
        except Exception as e:
            time.sleep(3)
    raise RuntimeError(f"metadata fetch failed: {ident}")

# robin -> ia
ia={}
for row in csv.DictReader(open(os.path.join(ROOT,"references","archive-org-items.tsv")),delimiter="\t"):
    ia[row["robin"]]=row["ia_identifier"]

robins=[d[1:] for d in sorted(os.listdir(TX)) if d.startswith("R") and os.path.isdir(os.path.join(TX,d))]
only=sys.argv[1:] or None
print(f"{len(robins)} transcribed items; targeting {only or 'ALL'}")
ok=skip=fail=0
for robin in robins:
    if only and robin not in only: continue
    ident=ia.get(robin)
    if not ident: print(f"  R{robin}: NO ia identifier, skip"); skip+=1; continue
    try:
        d=meta(ident)
        mtype=d.get("metadata",{}).get("mediatype")
        imgs=sorted(f["name"] for f in d["files"] if f["name"].lower().endswith(".jpg")
                    and "thumb" not in f["name"].lower() and "thumb" not in f.get("format","").lower())
        pages=[]; have=0
        for im in imgs:
            p=os.path.join(TX,f"R{robin}",os.path.splitext(im)[0]+".txt")
            if os.path.exists(p) and os.path.getsize(p)>0:
                pages.append(clean(open(p,encoding="utf-8").read())); have+=1
            else: pages.append("")
        out=f"/tmp/{ident}_djvu.txt"
        open(out,"w",encoding="utf-8").write("\x0c".join(pages))
        # upload text layer
        up=subprocess.run(["ia","upload",ident,out,"--retries","3"],capture_output=True,text=True)
        if up.returncode!=0: raise RuntimeError("upload: "+up.stderr[-200:])
        # metadata: append credit only if backlink not already present
        desc=d.get("metadata",{}).get("description","") or ""
        mods=["--modify=contributor:"+CONTRIB]
        if BACKLINK not in desc:
            mods.append("--modify=description:"+(desc+CREDIT))
        md=subprocess.run(["ia","metadata",ident]+mods,capture_output=True,text=True)
        if md.returncode!=0: raise RuntimeError("metadata: "+md.stderr[-200:])
        print(f"  R{robin} {ident} [{mtype}]: {len(imgs)}pp/{have}tx  uploaded+credited")
        ok+=1
    except Exception as e:
        print(f"  R{robin} {ident}: FAIL {e}"); fail+=1
    time.sleep(1)
print(f"DONE ok={ok} skip={skip} fail={fail}")

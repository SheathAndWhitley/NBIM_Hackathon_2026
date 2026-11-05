"""Fotavtrykk av leveransetekstene i Case 1 (arkitekt #2384).

Kl. 15.06 endret en agent tre .md-filer i leveranse/ uten at noen merket det. Dette verktøyet
gjør slike endringer synlige etter frysen kl. 16. Det stopper ingenting: tekster kan endres
med vilje etter 16 (#1975 JURY.md), men da skal det synes hvilke filer og når.

  lag    skriver sha256, størrelse og mtime for alle filer i leveranse/ til state/c1_tekstavtrykk.json
         (kl. 16.03 via LaunchAgent no.landsby.c1tekstavtrykk). Finnes fila, røres den ikke (--tving).
  sjekk  viser ENDRET/NY/BORTE siden avtrykket, med filens endringstid. Siste linje:
         "TEKSTAVTRYKK: uendret (N filer, avtrykk HH:MM)" eller "TEKSTAVTRYKK: K endret ...".
         Utgang 0 = uendret eller ikke tatt ennå, 3 = endret (bare informasjon), 2 = feil.

  --rot DIR   annen leveransemappe (demo på kopi).   --fil F   annen avtrykkfil (demo).
"""
import argparse, datetime, hashlib, json, os, sys

LAND = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ROT = os.path.join(LAND, "arbeid/hack/c1/leveranse")
FIL = os.path.join(LAND, "state/c1_tekstavtrykk.json")
HOPP = {"__pycache__", ".DS_Store"}


def tid(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def skann(rot):
    ut = {}
    for d, mapper, filer in os.walk(rot):
        mapper[:] = sorted(m for m in mapper if m not in HOPP)
        for f in sorted(filer):
            if f in HOPP or f.endswith(".pyc"):
                continue
            p = os.path.join(d, f)
            with open(p, "rb") as fh:
                sha = hashlib.sha256(fh.read()).hexdigest()
            st = os.stat(p)
            ut[os.path.relpath(p, rot)] = {"sha256": sha, "bytes": st.st_size, "mtime": tid(st.st_mtime)}
    return ut


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("kommando", choices=["lag", "sjekk"])
    a.add_argument("--rot", default=ROT)
    a.add_argument("--fil", default=FIL)
    a.add_argument("--tving", action="store_true")
    g = a.parse_args()
    if not os.path.isdir(g.rot):
        print(f"TEKSTAVTRYKK: FEIL, finner ikke {g.rot}"); return 2

    if g.kommando == "lag":
        if os.path.exists(g.fil) and not g.tving:
            print(f"TEKSTAVTRYKK: finnes fra før ({g.fil}), røres ikke (--tving overskriver)"); return 0
        filer = skann(g.rot)
        os.makedirs(os.path.dirname(os.path.abspath(g.fil)), exist_ok=True)
        with open(g.fil, "w") as fh:
            json.dump({"tatt": tid(datetime.datetime.now().timestamp()), "rot": os.path.abspath(g.rot),
                       "filer": filer}, fh, indent=1, ensure_ascii=False)
        print(f"TEKSTAVTRYKK: tatt {len(filer)} filer i {g.rot} -> {g.fil}"); return 0

    if not os.path.exists(g.fil):
        print(f"TEKSTAVTRYKK: ikke tatt ennå ({g.fil}; tas kl. 16.03)"); return 0
    with open(g.fil) as fh:
        av = json.load(fh)
    gammel, ny = av["filer"], skann(g.rot)
    rader = []
    for f in sorted(set(gammel) | set(ny)):
        if f not in ny:
            rader.append(f"BORTE   {f}  (var {gammel[f]['bytes']} B)")
        elif f not in gammel:
            rader.append(f"NY      {f}  endret {ny[f]['mtime']}, {ny[f]['bytes']} B")
        elif ny[f]["sha256"] != gammel[f]["sha256"]:
            rader.append(f"ENDRET  {f}  endret {ny[f]['mtime']}, {gammel[f]['bytes']} -> {ny[f]['bytes']} B")
    for r in rader:
        print(r)
    kl = av["tatt"][11:16]
    if not rader:
        print(f"TEKSTAVTRYKK: uendret ({len(ny)} filer, avtrykk {kl})"); return 0
    navn = ", ".join(r.split()[1] for r in rader[:6]) + (" ..." if len(rader) > 6 else "")
    print(f"TEKSTAVTRYKK: {len(rader)} endret siden avtrykk {kl}: {navn}"); return 3


if __name__ == "__main__":
    sys.exit(main())

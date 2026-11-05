"""Sporbarhet: hver anbefaling lagres som én linje i en jsonl, med kilde-punkt og konfidens.

Bruk fra modell/agent:
    from sporlogg import Sporlogg
    with Sporlogg("ut/anbefalinger.jsonl", kjoring="modell-v1") as logg:
        logg.skriv(forslag_id="0001-3", selskap="Apple Inc", motedato="2026-02-25",
                   forslag="Advisory vote on executive compensation",
                   anbefaling="MOT", styret="FOR", konfidens=0.71,
                   kilde_punkt="NBIM retningslinjer 4.2 Godtgjørelse", kilde_url="https://...",
                   begrunnelse="Variabel lønn uten langsiktig mål", modell="lr-tfidf")

Sjekk en fil:  python sporlogg.py sjekk ut/anbefalinger.jsonl
"""

import datetime as dt
import json
import sys

ANBEFALINGER = {"FOR", "MOT", "AVSTÅ"}
PAAKREVD = ["forslag_id", "selskap", "motedato", "forslag", "anbefaling", "styret",
            "konfidens", "kilde_punkt", "begrunnelse", "til_menneske"]
TERSKEL_MENNESKE = 0.6  # under denne konfidensen rutes saken til menneske (justeres av måleren)


class Sporlogg:
    def __init__(self, sti, kjoring, terskel=TERSKEL_MENNESKE):
        self.sti, self.kjoring, self.terskel = sti, kjoring, terskel
        self.f = None

    def __enter__(self):
        self.f = open(self.sti, "w", encoding="utf-8")
        return self

    def __exit__(self, *a):
        self.f.close()

    def skriv(self, **rad):
        rad.setdefault("til_menneske", rad.get("konfidens", 0) < self.terskel)
        rad["kjoring"] = self.kjoring
        rad["tid"] = dt.datetime.now().isoformat(timespec="seconds")
        feil = valider(rad)
        if feil:
            raise ValueError(f"ugyldig anbefaling {rad.get('forslag_id')}: {feil}")
        self.f.write(json.dumps(rad, ensure_ascii=False) + "\n")


def valider(rad):
    feil = [f"mangler {k}" for k in PAAKREVD if k not in rad]
    if rad.get("anbefaling") not in ANBEFALINGER:
        feil.append(f"anbefaling={rad.get('anbefaling')!r}")
    k = rad.get("konfidens")
    if not isinstance(k, (int, float)) or not 0 <= k <= 1:
        feil.append(f"konfidens={k!r}")
    if not str(rad.get("kilde_punkt", "")).strip():
        feil.append("tomt kilde_punkt")
    return feil


def sjekk(sti):
    n, feil, mennesker = 0, 0, 0
    with open(sti, encoding="utf-8") as f:
        for linje in f:
            n += 1
            rad = json.loads(linje)
            mennesker += bool(rad.get("til_menneske"))
            if valider(rad):
                feil += 1
                if feil <= 5:
                    print("FEIL:", rad.get("forslag_id"), valider(rad))
    print(f"{sti}: {n} anbefalinger, {feil} ugyldige, {mennesker} rutet til menneske")
    return feil == 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "sjekk":
        sys.exit(0 if sjekk(sys.argv[2]) else 1)
    raise SystemExit(__doc__)

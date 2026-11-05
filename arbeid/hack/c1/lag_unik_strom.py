"""Strømmende variant av lag_tabell.py for store forvaltere (iShares: 3,2 mill. poster).
Skriver bare én rad per unikt forslag (samme kolonner som votes_unik.csv).

Bruk: python lag_unik_strom.py data/votes_raa_ishares.csv data/votes_ishares_unik.csv
"""
import csv, hashlib, sys
from collections import Counter, defaultdict
from lag_tabell import MOT, FREKVENS

csv.field_size_limit(10**7)


def h(*x):
    return hashlib.md5("\x1f".join(x).encode()).digest()


def main(inn, ut):
    # Pass 1: semantikk per forvalter og største post per (serie, forslag)
    sh = defaultdict(lambda: [0, 0]); stoerst = {}
    for r in csv.DictReader(open(inn, encoding="utf-8")):
        if not r["stemme"]:
            continue
        if r["kilde"] == "SECURITY HOLDER" and r["stemme"] in ("FOR", "AGAINST") and r["ledelsen"] in ("FOR", "AGAINST"):
            sh[r["forvalter_cik"]][0] += 1; sh[r["forvalter_cik"]][1] += r["stemme"] == r["ledelsen"]
        k = h(r["forvalter_cik"], r["serie"], r["cusip"], r["moetedato"], r["forslag"])
        a = float(r["aksjer"] or 0)
        if k not in stoerst or a > stoerst[k]:
            stoerst[k] = a
    sem = {c: ("med_ledelsen_flagg" if v[1] / max(1, v[0]) < 0.25 else "anbefaling") for c, v in sh.items()}
    for c, v in sh.items():
        print(f"CIK {c}: {v[0]} aksjonærposter, stemme==felt {v[1]/max(1,v[0]):.1%} -> {sem[c]}")
    # Pass 2: bare hovedposter, gruppert per forslag
    grupper = defaultdict(lambda: {"n": Counter(), "rad": {}, "aksjer": 0.0})
    brukt = set()
    for r in csv.DictReader(open(inn, encoding="utf-8")):
        if not r["stemme"]:
            continue
        k = h(r["forvalter_cik"], r["serie"], r["cusip"], r["moetedato"], r["forslag"])
        a = float(r["aksjer"] or 0)
        if k in brukt or a != stoerst.get(k):
            continue
        brukt.add(k)
        g = grupper[h(r["forvalter_cik"], r["cusip"], r["moetedato"], r["forslag"])]
        s = r["stemme"]; g["n"][s] += 1; g["aksjer"] += a
        if s not in g["rad"]:
            frek = s in FREKVENS or "FREQUENCY" in r["kategori"].upper()
            styret = "ONE YEAR" if frek else ("AGAINST" if r["kilde"] == "SECURITY HOLDER" else "FOR")
            if sem.get(r["forvalter_cik"]) == "med_ledelsen_flagg":
                avvik = int(r["ledelsen"] == "AGAINST")
            else:
                avvik = int(s != (r["ledelsen"] or styret))
            rr = {k2: v for k2, v in r.items() if k2 not in ("serie", "serienavn", "accession", "manager", "ledelsen")}
            rr.update(styret=styret, mot=int(s in MOT), mot_ledelsen=avvik,
                      felt_semantikk=sem.get(r["forvalter_cik"], ""), aar=r["moetedato"][:4],
                      mgmt_felt_LEKKER=r["ledelsen"])
            g["rad"][s] = rr
    del stoerst, brukt
    unik = []
    for g in grupper.values():
        st = g["n"].most_common(1)[0][0]
        rr = g["rad"][st]
        rr["n_fond"] = sum(g["n"].values()); rr["fond_uenige"] = int(len(g["n"]) > 1); rr["aksjer"] = g["aksjer"]
        unik.append(rr)
    unik.sort(key=lambda r: (r["moetedato"], r["cusip"]))
    kol = ["forvalter_cik", "forvalter", "innsendt", "utsteder", "cusip", "isin", "moetedato", "forslag",
           "kategori", "kilde", "aksjer", "stemme", "mot_ledelsen", "delt", "n_rec", "styret", "mot",
           "felt_semantikk", "aar", "mgmt_felt_LEKKER", "n_fond", "fond_uenige"]
    with open(ut, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kol, extrasaction="ignore"); w.writeheader(); w.writerows(unik)
    print(f"Skrev {len(unik)} unike forslag til {ut}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

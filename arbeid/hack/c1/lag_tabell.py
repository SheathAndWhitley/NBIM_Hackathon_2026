"""Rå N-PX-tabell -> felles votes.csv med utledet styreanbefaling og rettet mål.

Bruk: python lag_tabell.py data/votes_raa.csv data/votes.csv

VIKTIG (funn 05.11): Vanguard fyller managementRecommendation med «stemte med
ledelsen» (FOR) / «mot ledelsen» (AGAINST), ikke styrets anbefaling. På
aksjonærforslag finnes bare (stemme AGAINST, felt FOR) og (FOR, AGAINST).
Feltet ER derfor fasiten for avvik og må aldri brukes som feature.
Vi utleder styrets anbefaling fra forslagskilden: ISSUER -> FOR,
SECURITY HOLDER -> AGAINST (frekvensstemmer: ONE YEAR).
Semantikken avgjøres per forvalter: 'med_ledelsen_flagg' når feltet på
aksjonærforslag sjelden (< 25 %) er lik stemmen, ellers 'anbefaling'.

Nye kolonner:
  styret          utledet styreanbefaling (FOR / AGAINST / ONE YEAR)
  mot             1 hvis stemmen er AGAINST/WITHHOLD (startpakkens mål)
  mot_ledelsen    1 hvis stemmen avviker fra styret (rettet mål)
  felt_semantikk  hvordan forvalteren bruker managementRecommendation
  hoved           1 for største post per (serie, utsteder, møte, forslag)
  aar             møteåret
Kolonnen 'ledelsen' er omdøpt til 'mgmt_felt_LEKKER'.
Lager også <ut>_unik.csv: én rad per forslag (flertall over fondenes hovedposter),
med n_fond og fond_uenige. Anbefalt modelltabell.
"""
import csv, sys
from collections import Counter, defaultdict

MOT = {"AGAINST", "WITHHOLD"}
FREKVENS = {"ONE YEAR", "TWO YEARS", "THREE YEARS", "1 YEAR", "2 YEARS", "3 YEARS", "1.0", "2.0", "3.0"}


def main(inn, ut):
    rader = [r for r in csv.DictReader(open(inn, encoding="utf-8")) if r["stemme"]]
    sem = {}
    for cik in {r["forvalter_cik"] for r in rader}:
        sh = [r for r in rader if r["forvalter_cik"] == cik and r["kilde"] == "SECURITY HOLDER"
              and r["stemme"] in ("FOR", "AGAINST") and r["ledelsen"] in ("FOR", "AGAINST")]
        lik = sum(r["stemme"] == r["ledelsen"] for r in sh) / max(1, len(sh))
        sem[cik] = "med_ledelsen_flagg" if lik < 0.25 else "anbefaling"
        print(f"CIK {cik}: {len(sh)} aksjonærforslag, stemme==felt {lik:.1%} -> {sem[cik]}")
    stoerst = {}
    for i, r in enumerate(rader):
        k = (r["forvalter_cik"], r["serie"], r["cusip"], r["moetedato"], r["forslag"])
        if k not in stoerst or float(r["aksjer"] or 0) > float(rader[stoerst[k]]["aksjer"] or 0):
            stoerst[k] = i
    hoved = set(stoerst.values())
    for i, r in enumerate(rader):
        s = r["stemme"]
        frek = s in FREKVENS or "FREQUENCY" in r["kategori"].upper()
        if frek:
            styret = "ONE YEAR"
        else:
            styret = "AGAINST" if r["kilde"] == "SECURITY HOLDER" else "FOR"
        if sem[r["forvalter_cik"]] == "med_ledelsen_flagg":
            avvik = int(r["ledelsen"] == "AGAINST")
        else:
            avvik = int(s != (r["ledelsen"] or styret))
        r["styret"] = styret
        r["mot"] = int(s in MOT)
        r["mot_ledelsen"] = avvik
        r["felt_semantikk"] = sem[r["forvalter_cik"]]
        r["hoved"] = int(i in hoved)
        r["aar"] = r["moetedato"][:4]
        r["mgmt_felt_LEKKER"] = r.pop("ledelsen")
    kol = list(rader[0].keys())
    with open(ut, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kol); w.writeheader(); w.writerows(rader)
    print(f"Skrev {len(rader)} rader ({len(hoved)} hovedposter) til {ut}")
    # Én rad per unikt forslag (forvalter, cusip, møte, tekst): flertall over fondenes hovedposter.
    g = defaultdict(list)
    for r in rader:
        if r["hoved"]:
            g[(r["forvalter_cik"], r["cusip"], r["moetedato"], r["forslag"])].append(r)
    unik = []
    for rs in g.values():
        st = Counter(r["stemme"] for r in rs).most_common(1)[0][0]
        rr = next(r for r in rs if r["stemme"] == st).copy()
        rr["n_fond"] = len(rs)
        rr["fond_uenige"] = int(len({r["stemme"] for r in rs}) > 1)
        rr["aksjer"] = sum(float(r["aksjer"] or 0) for r in rs)
        for k in ("serie", "serienavn", "accession", "manager", "hoved"):
            rr.pop(k, None)
        unik.append(rr)
    unik.sort(key=lambda r: (r["moetedato"], r["cusip"]))
    ut_u = ut.replace(".csv", "_unik.csv")
    with open(ut_u, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(unik[0].keys())); w.writeheader(); w.writerows(unik)
    print(f"Skrev {len(unik)} unike forslag til {ut_u}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

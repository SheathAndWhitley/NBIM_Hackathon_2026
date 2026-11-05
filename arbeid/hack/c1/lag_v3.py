"""Case 1 holdout v3 (dommer, #1966): NBIMs EGNE stemmer fra N-PX (Norges Bank, CIK 1374170).

Bruk: python3 -I arbeid/hack/c1/lag_v3.py [arbeid/arkitekt/hack1942/nbim_votes.csv]
Skriver to mapper med samme skjema som v2 (maaler.py og smedenes run.sh virker uendret):
  data_v3_val/  train = N-PX 2024 (møter 07.2023-06.2024), holdout = N-PX 2025 (07.2024-06.2025)  -> tuning
  data_v3/      train = N-PX 2024+2025,                     holdout = N-PX 2026 (07.2025-06.2026)  -> HOVEDTALL
Mål: python3 -I arbeid/hack/c1/maaler.py PRED.csv --fasit arbeid/hack/c1/data_v3/fasit.csv

Låst:
- N-PX-feltet managementRecommendation betyr hos NBIM «stemte med/mot ledelsen» (411 say-on-pay-rader har
  AGAINST/AGAINST; ingen styrer anbefaler mot egen lønnspakke). Det er fasiten og leses aldri som styret.
- Styret utledes: say-on-pay er selskapets eget forslag (kilde ISSUER) -> styret = FOR.
- Frekvensstemmer (ONE/TWO/THREE YEARS) holdes utenfor: styrets frekvensanbefaling kan ikke utledes
  uten lekk-feltet. Antallet står i split_info.txt.
- Enhet = forslag (cusip, møtedato, tekst); duplikatrader slås sammen (flertall).
- Ingen selskapssplitt: tidligere års stemmer om samme selskap er offentlige på beslutningstidspunktet.
"""
import csv, hashlib, os, sys
from collections import Counter, defaultdict

HER = os.path.dirname(os.path.abspath(__file__))
KILDE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HER, "..", "..", "arkitekt", "hack1942", "nbim_votes.csv")
AAR = {"000137417024000042": 2024, "000137417025000082": 2025, "000137417026000072": 2026}
KLASSE = {"FOR": "FOR", "AGAINST": "MOT", "WITHHOLD": "MOT", "ABSTAIN": "AVSTÅ"}
INPUT = ["id", "forvalter_cik", "forvalter", "accession", "npx_aar", "utsteder", "cusip", "isin", "moetedato",
         "forslag", "kategori", "kilde", "aksjer", "aar", "styret", "antall_fond"]
TRAIN = INPUT + ["stemme", "fasit", "avvik"]


def iso(v):
    return f"{v[6:10]}-{v[:2]}-{v[3:5]}" if len(v) >= 10 and v[2] == "/" else v[:10]


def forslag():
    grupper, andre = defaultdict(list), Counter()
    for r in csv.DictReader(open(KILDE, encoding="utf-8", newline="")):
        if r["stemme"] not in KLASSE:
            andre[r["stemme"]] += 1; continue
        d = iso(r["dato"])
        grupper[(r["cusip"] or r["isin"] or r["issuer"].upper(), d, " ".join(r["tekst"].split()).lower())].append(r)
    ut = []
    for (sel, d, _), rs in grupper.items():
        r = rs[0]
        fasit = Counter(KLASSE[x["stemme"]] for x in rs).most_common(1)[0][0]
        ut.append({"id": hashlib.sha1(f"{sel}|{d}|{r['tekst']}".encode()).hexdigest()[:12],
                   "forvalter_cik": "1374170", "forvalter": "NORGES BANK", "accession": r["fil"],
                   "npx_aar": AAR[r["fil"]], "utsteder": r["issuer"], "cusip": sel, "isin": r["isin"],
                   "moetedato": d, "forslag": r["tekst"], "kategori": r["kategori"], "kilde": "ISSUER", "aksjer": "",
                   "aar": d[:4], "styret": "FOR", "antall_fond": len(rs), "stemme": r["stemme"],
                   "fasit": fasit, "avvik": "1" if fasit != "FOR" else "0"})
    ut.sort(key=lambda r: (r["moetedato"], r["id"]))
    return ut, andre


def skriv(sti, rader, felt):
    with open(sti, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=felt, extrasaction="ignore"); w.writeheader(); w.writerows(rader)


def lag(mappe, tren_aar, test_aar, alle, andre):
    os.makedirs(mappe, exist_ok=True)
    train = [r for r in alle if r["npx_aar"] in tren_aar]
    test = [r for r in alle if r["npx_aar"] == test_aar]
    assert max(r["moetedato"] for r in train) < min(r["moetedato"] for r in test), "tidssplitt brutt"
    skriv(os.path.join(mappe, "train.csv"), train, TRAIN)
    skriv(os.path.join(mappe, "test_input.csv"), test, INPUT)
    skriv(os.path.join(mappe, "fasit.csv"), test, ["id", "fasit", "styret", "avvik", "moetedato", "cusip"])
    a = lambda rs: sum(r["avvik"] == "1" for r in rs)
    info = [f"kilde {os.path.relpath(KILDE, HER)}: NBIM N-PX, kategori SAY-ON-PAY, {len(alle)} unike forslag (FOR/MOT)",
            f"train N-PX {tren_aar}: {len(train)} forslag, avvik {a(train)} ({a(train) / len(train):.1%}), "
            f"møter {train[0]['moetedato']}..{train[-1]['moetedato']}",
            f"holdout N-PX {test_aar}: {len(test)} forslag, avvik {a(test)} ({a(test) / len(test):.1%}), "
            f"møter {test[0]['moetedato']}..{test[-1]['moetedato']}",
            f"følg styret (FOR) accuracy på holdout: {1 - a(test) / len(test):.4f}",
            f"selskap i holdout som også finnes i train: {len({r['cusip'] for r in test} & {r['cusip'] for r in train})}"
            f" av {len({r['cusip'] for r in test})}",
            "styret utledet = FOR (say-on-pay er selskapets forslag); managementRecommendation lest aldri",
            f"frekvensstemmer holdt utenfor (alle år): {dict(andre)}"]
    open(os.path.join(mappe, "split_info.txt"), "w").write("\n".join(info) + "\n")
    print(f"== {os.path.basename(mappe)}"); print("\n".join(info))


if __name__ == "__main__":
    alle, andre = forslag()
    lag(os.path.join(HER, "data_v3_val"), (2024,), 2025, alle, andre)
    lag(os.path.join(HER, "data_v3"), (2024, 2025), 2026, alle, andre)

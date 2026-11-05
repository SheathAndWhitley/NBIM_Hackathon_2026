"""Lekkasjesjekk for historikkgulvet (#1976). Bare stdlib.
Bruk: python3 -I lekkasjesjekk.py DATAMAPPE PRED.csv   (exit 1 hvis en sjekk feiler)
Sjekker at gulv_v3.py bare kan ha brukt NBIM-stemmer strengt før hver testrads møtedato:
 1) train har bare NORGES BANK  2) maks train-dato < min test-dato (ingen samme-dag)
 3) ingen id/forslag (cusip, dato, tekst) går igjen i train og test  4) test_input har ingen fasitkolonner
 5) uavhengig reimplementering med eksplisitt datofilter per rad (bare train-rader med dato < radens dato)
    gir nøyaktig samme anbefaling og p_avvik som PRED.csv
 6) negativ kontroll: samme regel MED fasit fra test (lekket) skal gi en annen (høyere) treffrate."""
import csv, sys
from collections import defaultdict
d, pred = sys.argv[1], sys.argv[2]
les = lambda p: list(csv.DictReader(open(p, encoding="utf-8")))
tr, te, fa, pr = les(f"{d}/train.csv"), les(f"{d}/test_input.csv"), les(f"{d}/fasit.csv"), les(pred)
feil = []
def sjekk(navn, ok, info):
    print(("OK   " if ok else "FEIL ") + navn + ": " + info)
    if not ok: feil.append(navn)
fv = sorted({r["forvalter"] for r in tr} | {r["forvalter"] for r in te})
sjekk("1 bare NBIM", fv == ["NORGES BANK"], f"forvaltere i train+test = {fv}")
mx, mn = max(r["moetedato"] for r in tr), min(r["moetedato"] for r in te)
sjekk("2 strengt før", mx < mn, f"siste train-møte {mx} < første test-møte {mn}")
nok = lambda r: (r["cusip"], r["moetedato"], r["forslag"].strip())
sjekk("3 ingen overlapp", not ({r["id"] for r in tr} & {r["id"] for r in te}) and not ({nok(r) for r in tr} & {nok(r) for r in te}),
      f"{len(tr)} train, {len(te)} test, felles id/forslag = 0")
lekk = {"fasit", "avvik", "stemme", "mot", "ledelsen", "mgmt_felt_LEKKER", "managementRecommendation"} & set(te[0])
sjekk("4 ingen fasit i test_input", not lekk, f"kolonner i test_input: {len(te[0])}, lekk = {sorted(lekk)}")
# 5) uavhengig reimplementering med eksplisitt datofilter
basis = sum(r["avvik"] == "1" for r in tr) / len(tr)
per = defaultdict(list)
for r in tr: per[r["cusip"]].append((r["moetedato"], r["avvik"] == "1"))
p_ = {r["id"]: r for r in pr}
avvik_n, brukt, ufilt, maks_brukt = 0, 0, 0, ""
for r in te:
    hist = [a for dt, a in per[r["cusip"]] if dt < r["moetedato"]]
    brukt += len(hist); ufilt += len(per[r["cusip"]])
    maks_brukt = max([maks_brukt] + [dt for dt, a in per[r["cusip"]] if dt < r["moetedato"]])
    m, n = sum(hist), len(hist)
    a, p = ("MOT" if m else "FOR"), round((m + basis) / (n + 1), 4)
    q = p_.get(r["id"])
    if not q or q["anbefaling"] != a or abs(float(q["p_avvik"]) - p) > 1e-4: avvik_n += 1
sjekk("5 reimplementering", avvik_n == 0 and len(p_) == len(te),
      f"{len(te)} rader, {avvik_n} avvik; med datofilter {brukt}, uten filter {ufilt} (like = all historikk er fra før)")
# 6) negativ kontroll: lekket variant (bruker test-fasit for samme selskap, inkl. samme dag) må avvike
fasit = {r["id"]: r["avvik"] == "1" for r in fa}
mot_test = defaultdict(int)
for r in te: mot_test[r["cusip"]] += fasit[r["id"]]
tp_l = sum(fasit[r["id"]] for r in te if mot_test[r["cusip"]] or sum(a for _, a in per[r["cusip"]]))
tp = sum(fasit[r["id"]] for r in te if p_[r["id"]]["anbefaling"] == "MOT")
sjekk("6 negativ kontroll", tp_l > tp, f"treff på avvik: gulv {tp} av {sum(fasit.values())}, lekket variant {tp_l} (sjekken ville sett lekkasjen)")
print("RESULTAT", "FEIL " + ",".join(feil) if feil else "INGEN LEKKASJE FUNNET")
sys.exit(1 if feil else 0)

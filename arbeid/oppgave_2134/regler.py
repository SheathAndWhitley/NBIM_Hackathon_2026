"""#2134: enkle regler på real test 2026, løpende historikk (møter strengt før radens dato, alle år).
Regel a: MOT hvis NBIM stemte MOT mot styret i samme selskap før.  Regel b: MOT hvis samme forslagstekst
(normalisert som i oppgave_2044/train.py) fikk MOT mot styret før, i hvilket som helst selskap.
Regel b2 (ekstra): samme selskap og samme tekst. Etikett = nbim_vote MOT og against_board 1 (som v3 --score mot).
Skriver id,anbefaling(0/1 avvik),p_avvik for test 2026, formatet maaler_offisiell_v3.py leser."""
import csv, re, sys
REAL = "state/opplastet/20261105_114241_real_votes.csv"
R = [r for r in csv.DictReader(open(REAL, encoding="utf-8")) if r.get("injection_flag") != "1"]
norm = lambda s: " ".join(re.sub(r"[^a-z ]", " ", (s or "").lower()).split())
nok = {"a": lambda r: r["company_id"], "b": lambda r: norm(r["proposal_text"]),
       "b2": lambda r: r["company_id"] + "|" + norm(r["proposal_text"])}
for navn, k in nok.items():
    mot_dato = {}  # nøkkel -> tidligste dato med MOT mot styret
    for r in R:
        if r["nbim_vote"] == "MOT" and r["against_board"] == "1.0":
            d = r["meeting_date"]; kk = k(r)
            if kk not in mot_dato or d < mot_dato[kk]: mot_dato[kk] = d
    ut = open(f"arbeid/oppgave_2134/regel_{navn}_test.csv", "w", newline=""); w = csv.writer(ut)
    w.writerow(["id", "anbefaling", "p_avvik"]); n = f = 0
    for r in R:
        if int(r["year"]) != 2026: continue
        hit = k(r) in mot_dato and mot_dato[k(r)] < r["meeting_date"]
        w.writerow([f"{r['meeting_id']}|{r['item_no']}", int(hit), float(hit)]); n += 1; f += hit
    ut.close(); print(navn, n, "rader,", f, "flagget")

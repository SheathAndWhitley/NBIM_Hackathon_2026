"""#1952: enkle historikkregler som baseline for Case 1 (real_votes, test 2026). Bare stdlib.
Regel: avvik=1 hvis nøkkelen hadde against_board=1 tidligere. h1 = bare år < 2026, h2 = møter strengt før datoen.
Nøkkel: selskap, eller selskap+forslagstype. Etiketter brukes bare fra tidligere rader (fasit kun til historikk)."""
import csv, sys
F = "state/opplastet/20261105_114241_real_votes.csv"
R = list(csv.DictReader(open(F, encoding="utf-8")))
for navn, nk in [("selskap", lambda r: r["company_id"]), ("selskap_type", lambda r: r["company_id"] + "|" + r["proposal_type"])]:
    for h in (1, 2):
        mot = {}  # nøkkel -> sorterte datoer med MOT-etikett (against_board=1)  # lov: fasit fra tidligere møter
        for r in R:
            if r.get("injection_flag") == "1" or r["against_board"] not in ("1", "1.0"): continue
            mot.setdefault(nk(r), []).append(r["meeting_date"][:10])
        with open(f"regel_{navn}_h{h}.csv", "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "anbefaling"])
            for r in R:
                if not r["meeting_date"].startswith("2026"): continue
                d = r["meeting_date"][:10]
                tid = [x for x in mot.get(nk(r), []) if (x < "2026" if h == 1 else x < d)]
                w.writerow([f"{r['meeting_id']}|{r['item_no']}", int(bool(tid))])

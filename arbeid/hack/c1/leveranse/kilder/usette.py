"""#2592: MOT som ingen ser (ikke flagget, ikke rutet) for en agent.csv, samme fasit som menneske_tabell.py."""
import csv, sys, collections
FASIT = "state/opplastet/20261105_114241_real_votes.csv"
A = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig", newline=""))}
F = [r for r in csv.DictReader(open(FASIT, encoding="utf-8", newline="")) if r.get("injection_flag") != "1" and r["year"] == "2026" and r["against_board"] != ""]
us = []; utenfor = collections.Counter()
for f in F:
    a = A[f"{f['meeting_id']}|{f['item_no']}"]; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
    x = a["anbefaling"] == "MOT" and (f["mgmt_rec"] or "FOR") != "MOT"; r = a["til_menneske"] == "1"
    if x and not r: utenfor["ekte" if y else "falsk"] += 1
    if y and not x and not r: us.append((float(a["p_mot"] or 0), f["country"], f["proposal_type"]))
print("usette MOT", len(us), "maks p_mot", max(p for p, _, _ in us), "land", collections.Counter(c for _, c, _ in us).most_common(4))
print("typer", collections.Counter(t for _, _, t in us).most_common(4)); print("MOT-flagg utenfor sonen", dict(utenfor))

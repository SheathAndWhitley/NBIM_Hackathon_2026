"""Trekker 5 demo-saker tilfeldig fra test 2026 (real_votes), speider #2070. Ikke håndplukk.
Populasjon: alle saker i test 2026 med fasit (against_board satt, 1539 saker), sortert på id.
Seed 0, 1, 2, ...: numpy default_rng(seed).choice(n, 5, replace=False). Første seed der minst 2 har
fasit MOT (avvik fra styret) og minst 1 er sendt til menneske av agenten, vinner. Alle forsøkte seeds skrives.
Bruk: python3 demo_trekk_2026.py AGENT_CSV (agent.csv fra kjor_agent.py på hele test 2026) [UT_INN_CSV]
"""
import csv, sys
import numpy as np
REAL = "state/opplastet/20261105_114241_real_votes.csv"
INN = "arbeid/hack/c1/data_off/real_test_input.csv"
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open(REAL)) if r["year"] == "2026" and r["against_board"] != ""}
ag = {r["id"]: r for r in csv.DictReader(open(sys.argv[1]))}
ids = sorted(fas)
for seed in range(10000):
    valgt = [ids[i] for i in np.random.default_rng(seed).choice(len(ids), 5, replace=False)]
    n_mot = sum(fas[i]["against_board"] == "1.0" for i in valgt)
    n_rut = sum(ag[i]["til_menneske"] == "1" for i in valgt)
    ok = n_mot >= 2 and n_rut >= 1
    print(f"seed {seed}: fasit MOT {n_mot}, til menneske {n_rut} -> {'OK' if ok else 'nytt trekk'}")
    if ok: break
print("VALGT seed", seed, ":", " ".join(valgt))
if len(sys.argv) > 2:
    rr = [r for r in csv.DictReader(open(INN)) if r["id"] in valgt]
    w = csv.DictWriter(open(sys.argv[2], "w", newline=""), fieldnames=rr[0].keys()); w.writeheader(); w.writerows(rr)

# Tillegg (sitatdemo): én sak trukket med seed 0 blant sakene der agenten selv går MOT styret (sitat gis bare ved MOT).
mot = sorted(i for i in ids if ag[i]["mot_styret"] == "1")
s = mot[np.random.default_rng(0).integers(len(mot))]
print(f"SITATSAK seed 0 blant {len(mot)} agent-MOT: {s}  fasit against_board {fas[s]['against_board']}")
if len(sys.argv) > 3:
    rr = [r for r in csv.DictReader(open(INN)) if r["id"] == s]
    w = csv.DictWriter(open(sys.argv[3], "w", newline=""), fieldnames=rr[0].keys()); w.writeheader(); w.writerows(rr)

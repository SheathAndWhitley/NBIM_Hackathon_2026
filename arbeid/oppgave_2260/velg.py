# Velger tre demosaker fra den frosne agentens agent.csv: den FØRSTE i fila av hver type (ingen håndplukking).
import csv, sys
ag = sys.argv[1]
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open("state/opplastet/20261105_114241_real_votes.csv"))}
first = {}
for i, r in enumerate(csv.DictReader(open(ag)), start=2):
    f = fas.get(r["id"])
    if f is None or f["against_board"] == "": continue
    pm = r["anbefaling"] == "MOT" and r["styret"] != "MOT"          # agent: MOT mot styret
    ym = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"     # fasit: MOT mot styret (#231)
    rut = r["til_menneske"] == "1"
    for k, ok in (("treff_maskin", pm and ym and not rut), ("bom_maskin", pm != ym and not rut),
                  ("til_menneske", rut), ("treff_alle", pm and ym), ("bom_alle", pm != ym)):
        if ok and k not in first: first[k] = (i, r["id"])
for k, v in first.items(): print(k, "linje", v[0], v[1])

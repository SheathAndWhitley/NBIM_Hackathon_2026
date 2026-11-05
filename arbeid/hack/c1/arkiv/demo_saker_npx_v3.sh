#!/usr/bin/env bash
# Gjenskaper de tre demo-sakene i DEMO_MANUS.md (VAL 2025, modell trent på N-PX 2024). Kjør fra landsbymappen:
#   bash arbeid/hack/c1/demo_saker.sh [UTMAPPE]     (standard /tmp/c1_demo, ca. 10 s)
set -euo pipefail
UT="${1:-/tmp/c1_demo}"; mkdir -p "$UT"
C1=arbeid/hack/c1; V=$C1/data_v3_val
AG="uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --train $V/train.csv --fasit $V/fasit.csv"
$AG --csv $V/test_input.csv --ut "$UT/val" > "$UT/val.log" 2>&1
python3 - "$UT/inj.csv" <<'P'
import csv, sys
sys.path.insert(0, "arbeid/hack/levering")
from motstandstest import INJ_FOR  # samme instruks som motstandstesten bruker
r = list(csv.DictReader(open("arbeid/hack/c1/data_v3_val/test_input.csv")))
for x in r:
    if x["id"] == "2580f8458208": x["forslag"] += INJ_FOR   # Roku 2025-06-11 får instruks om å anbefale FOR
w = csv.DictWriter(open(sys.argv[1], "w"), fieldnames=r[0].keys()); w.writeheader(); w.writerows(r)
P
$AG --csv "$UT/inj.csv" --ut "$UT/inj" > "$UT/inj.log" 2>&1
python3 - "$UT" <<'P'
import csv, sys
ut = sys.argv[1]
fas = {r["id"]: r for r in csv.DictReader(open("arbeid/hack/c1/data_v3_val/fasit.csv"))}
nb = {r["id"]: r for r in csv.DictReader(open("arbeid/hack/c1/kilder/nbim_begrunnelser_saypay.csv"))}
for tittel, d, i in (("1 riktig MOT", "val", "c3021d02016b"), ("2 usikker -> menneske", "val", "ce09597abc84"),
                     ("3 instruks i teksten", "inj", "2580f8458208"), ("3 samme sak uten instruks", "val", "2580f8458208")):
    r = next(x for x in csv.DictReader(open(f"{ut}/{d}/agent.csv")) if x["id"] == i)
    print(f"== Sak {tittel}: {i} {r['utsteder']} {r['moetedato']}")
    print(f"   forslag: {r['forslag']}")
    print(f"   agent: {r['anbefaling']}  P(MOT) {r['p_mot']}  rå {r['raa_score']}  til menneske {r['til_menneske']}  {r['rutingsgrunn']}")
    print(f"   punkt: {r['punkt']}\n   sitat: {r['sitat']}\n   grunn: {r['sitat_grunn']}")
    print(f"   fasit (NBIM stemte): {fas[i]['fasit']}   NBIMs egen begrunnelse: {nb.get(i, {}).get('begrunnelse', '-')[:160]}...")
P
grep -h "F1" "$UT/val.log" | head -1

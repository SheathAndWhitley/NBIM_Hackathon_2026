#!/usr/bin/env bash
# Live-skjerm for DEMO_MANUS.md (#2340): kjører agenten på hele test 2026 og viser FØRST de tre manussakene
# (treff, bom, til menneske: første i fila av hver type, regnet ut av vis_manussaker.py, med varsel ved avvik fra manus).
# Deretter tillegget fra DEMO_MANUS_5min_tilfeldige.md (speider #2070): 5 saker trukket med fast seed fra test 2026,
# pluss én sitatsak trukket med seed 0 blant agentens egne MOT (reserven bruker demo5/ og sitat/). Kjør fra landsbymappen (ca. 15 s):
#   bash arbeid/hack/c1/demo_saker_2026.sh [UTMAPPE]     (standard /tmp/c1_demo2026)
set -euo pipefail
UT="${1:-/tmp/c1_demo2026}"; rm -rf "$UT"; mkdir -p "$UT"
PY="uv run --project arbeid/kandidater/smed2_c1_mot python"
AG="$PY arbeid/hack/levering/kjor_agent.py"
$AG --ut "$UT/full" > "$UT/full.log" 2>&1                       # hele test 2026 (manussakene og rutingen i trekket)
echo "######## De tre sakene i DEMO_MANUS.md (første i agent.csv av hver type)"
python3 -I arbeid/hack/c1/vis_manussaker.py "$UT/full/agent.csv"
echo "######## Tillegg: 5 saker trukket med fast seed + 1 sitatsak (DEMO_MANUS_5min_tilfeldige.md)"
$PY arbeid/hack/c1/demo_trekk_2026.py "$UT/full/agent.csv" "$UT/inn5.csv" "$UT/inn_sitat.csv" 2>/dev/null | tee "$UT/trekk.log" | tail -2
$AG --csv "$UT/inn5.csv" --ut "$UT/demo5" > "$UT/demo5.log" 2>&1     # kald kjøring på bare de 5
$AG --csv "$UT/inn_sitat.csv" --ut "$UT/sitat" > "$UT/sitat.log" 2>&1
python3 - "$UT" <<'P'
import csv, sys
ut = sys.argv[1]
fas = {f"{r['meeting_id']}|{r['item_no']}": r for r in csv.DictReader(open("state/opplastet/20261105_114241_real_votes.csv"))}
for d in ("demo5", "sitat"):
    for r in csv.DictReader(open(f"{ut}/{d}/agent.csv")):
        f = fas[r["id"]]
        print(f"== {r['id']} {r['company']} {r['meeting_date']} ({f['country']}, {f['proposal_type']})\n   forslag: {r['proposal_text'][:120]}")
        print(f"   agent: {r['anbefaling']} (mot styret {r['mot_styret']})  rå {r['raa_score']}  sjanse for MOT {r['p_mot']}  til menneske {r['til_menneske']} {r['rutingsgrunn']}")
        print(f"   sitat: {r['punkt']} {r['sitat'][:160]}  [{r['sitat_kilde'][:80]}]")
        print(f"   fasit: NBIM stemte {f['nbim_vote_raw']} (mot styret {f['against_board']})  NBIMs begrunnelse: {f['rationale_text'][:120]}")
P
echo "agentens egen sjekk, avvik inkl. avstå (sidetall, ikke hovedtallet): $(grep -h "^SCORE" "$UT/full.log" | head -1)"
M="$(python3 -I arbeid/hack/c1/maaler_offisiell_v3.py "$UT/full/_pred_uten_ruting.csv" test --data real --score mot)"
echo "$M" | grep "MOT mot styret"
echo "HOVEDTALL maaler_offisiell_v3.py full/_pred_uten_ruting.csv test --data real --score mot: F1 MOT $(echo "$M" | sed -n 's/^SCORE *//p' | tail -1)"

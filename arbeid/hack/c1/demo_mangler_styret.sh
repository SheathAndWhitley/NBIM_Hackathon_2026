#!/usr/bin/env bash
# Demo (#2157): samme ekte 2026-sak (Arbonia AG, 2041102|2, sak 2 i DEMO_MANUS.md) to ganger, med og uten
# styrets anbefaling (mgmt_rec og mgmt_rec_raw tomme). Uten anbefaling skal agenten sende saken til et menneske
# med grunn (#2152). Modellen er urørt. Kjør fra landsbymappen (ca. 15 s):
#   bash arbeid/hack/c1/demo_mangler_styret.sh [UTMAPPE]     (standard /tmp/c1_demo_mangler)
set -euo pipefail
UT="${1:-/tmp/c1_demo_mangler}"; rm -rf "$UT"; mkdir -p "$UT"
AG="uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py"
SAK='{"meeting_id":"2041102","item_no":"2","company_id":"510171","company":"Arbonia AG","country":"Switzerland","market":"DM","meeting_date":"2026-04-24","proposal_text":"Approve Non-Financial Report","proposal_type":"OTHER_MGMT","proponent":"Management"'
$AG --sak "$SAK,\"mgmt_rec_raw\":\"For\",\"mgmt_rec\":\"FOR\"}" --ut "$UT/med" > "$UT/med.log" 2>&1
$AG --sak "$SAK,\"mgmt_rec_raw\":\"\",\"mgmt_rec\":\"\"}" --ut "$UT/uten" > "$UT/uten.log" 2>&1
python3 - "$UT" <<'P'
import csv, sys
for d, t in (("med", "styret anbefaler For"), ("uten", "styrets anbefaling mangler")):
    r = next(csv.DictReader(open(f"{sys.argv[1]}/{d}/agent.csv")))
    print(f"== {r['id']} {r['company']} {r['meeting_date']}: {t}\n   forslag: {r['proposal_text']}")
    print(f"   agent: {r['anbefaling']} (styret lest som {r['styret']}, mot styret {r['mot_styret']})  rå {r['raa_score']}  sjanse for MOT {r['p_mot']}")
    print(f"   til menneske: {r['til_menneske']}  grunn: {r['rutingsgrunn'] or '-'}")
P

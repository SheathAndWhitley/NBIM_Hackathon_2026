#!/bin/sh
# Case 1 (#2191): lager ferdige demo-utskrifter fra en ekte kjøring, så demoen kan vises uten nett og uten agent.
# Kjør fra landsbymappen (ca. 1 min): sh arbeid/hack/levering/demo/reserve/lag_reserve.sh
# Etter frys kl. 16 må dette kjøres på nytt, ellers gjelder utskriftene den gamle modellen (sjekk SHA.txt).
set -eu
KILDE="$(cd "$(dirname "$0")/../../../../.." && pwd)"
R="$KILDE/arbeid/hack/levering/demo/reserve"
cd "$KILDE"
# 1) demo-manusets saker 1-6 og sak 7 (DEMO_MANUS.md), fra landsbymappen slik de kjøres live
bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_res_saker > "$R/1_saker_2026.txt" 2>&1
bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/c1_res_mangler > "$R/2_mangler_styret.txt" 2>&1
# 2) demo.sh-veien (kald kopi + demo_vis.py) uten å skrive over leveranse/demo_utskrift.txt
M=/tmp/c1_res_kald
sh arbeid/hack/levering/fremmed.sh "$M" > "$R/3_fremmed_kald_kopi.txt" 2>&1
env -i HOME="$M/home" PATH="$M/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 "$M/.venv/bin/python" -I \
  arbeid/hack/c1/leveranse/demo_vis.py "$M/ut/agent.csv" "$M/state/opplastet/20261105_114241_real_votes.csv" > "$R/4_demo_vis_3_saker.txt" 2>&1
# 3) rådata å vise hvis noen spør: agentens svar på demosakene og hele test 2026
rm -rf "$R/csv"; mkdir -p "$R/csv"
cp /tmp/c1_res_saker/demo5/agent.csv "$R/csv/demo5_agent.csv"
cp /tmp/c1_res_saker/sitat/agent.csv "$R/csv/sitat_agent.csv"
cp /tmp/c1_res_mangler/uten/agent.csv "$R/csv/mangler_styret_agent.csv"
cp "$M/ut/agent.csv" "$R/csv/test2026_agent.csv"
cp "$M/ut/KJORING.txt" "$R/csv/test2026_KJORING.txt"
{ echo "laget $(date '+%Y-%m-%d %H:%M:%S')"
  shasum -a 256 arbeid/hack/levering/kjor_agent.py
  python3 -I arbeid/verktoy/c1_frys.py sjekk 2>&1 | tail -3; } > "$R/SHA.txt"
echo "reserve skrevet i $R"; cat "$R/SHA.txt"

#!/bin/sh
# Case 1 #2572: bytt frossen modell (#2044 miks h2) til repo4 (oppgave_2490/abl.py + 4 repotrekk) HVIS dommer2 sier BYTT (#2570).
# Standard er tørrkjøring (viser stegene). Utfør bare med --utfor etter skriftlig BYTT-dom. Se arbeid/hack/c1/BYTTEPLAN.md.
# Bruk (fra landsbymappen): sh arbeid/hack/c1/bytte/bytt.sh [--utfor]
set -eu
LAND="$(cd "$(dirname "$0")/../../../.." && pwd)"; cd "$LAND"
B=arbeid/hack/c1/bytte; L=arbeid/hack/levering; T=/tmp/bytte2572
U=0; [ "${1:-}" = "--utfor" ] && U=1
k() { echo "+ $*"; [ $U = 1 ] && sh -c "$*" || true; }
[ $U = 1 ] || echo "TØRRKJØRING (ingenting endres). Bruk --utfor etter BYTT-dom."
# 0) sikkerhetspunkt: frosne filer må være rene i git, og vi noterer HEAD for tilbakerulling
k "git diff --quiet -- $L/c1_real.py arbeid/verktoy/c1_frys.py $L/fremmed.sh $L/pakk_jury.sh && git rev-parse HEAD > /tmp/bytte2572_head.txt && cp state/c1_frys.json /tmp/bytte2572_c1_frys.json"
# 1) nye modellfiler inn i levering/ (staget og testet #2572: identiske prediksjoner med oppgave_2490/repo4_test.csv)
k "cp $B/modell_repo4.py $B/c1_real.py $L/ && rm -rf $L/stemmeagent && cp -R $B/stemmeagent $L/stemmeagent && rm -rf $L/stemmeagent/__pycache__"
# 2) frysliste, kaldkopi og pakke: nye filer inn (train.py blir stående: fremmed.sh sin rotsjekk krever den)
k "python3 -I $B/oppdater_lister.py"
# 3) agentens frosne utdata på nytt (maskin alene = pred_maaler.csv, rutingen endrer ikke svarene)
k "rm -rf $T && arbeid/kandidater/smed2_c1_mot/.venv/bin/python $L/kjor_agent.py --ut $T > $T.log 2>&1 && cp $T/pred_maaler.csv $L/kjor_agent_real_maskin_alene.csv && cp $T/pred_maaler.csv $L/kjor_agent_real_pred_maaler.csv && cp $T/KJORING.txt $L/kjor_agent_real_test2026.txt"
k "python3 -I arbeid/hack/c1/maaler_offisiell_v3.py $L/kjor_agent_real_maskin_alene.csv test --data real --score mot | grep -E 'MOT mot styret|^SCORE'   # skal gi TP 32 FP 35 FN 26 F1 0.5120"
# 4) tallene i tekstene (hovedtallet); resten fanges av tallvakta i steg 6
k "python3 -I $B/bytt_tall.py --skriv"
# 5) ny frys (--tving, grunn på tavla) og ny fasit for frys_diff
k "python3 -I arbeid/verktoy/c1_frys.py frys --tving && python3 -I arbeid/verktoy/c1_frys.py sjekk --krev"
k "python3 -I $L/frys_fasit.py > $L/frys_fasit_1600.sha256 && sh $L/frys_diff.sh --kilde"
# 6) vakter og kald start (samme som dommerens 18:30-sjekk)
k "python3 -I arbeid/verktoy/c1_tallvakt.py --vis | tail -30"
k "bash arbeid/verktoy/c1_etterfrys.sh"
echo "Ferdig. Grønt: commit (se BYTTEPLAN.md steg 7). Rødt: tilbakerull (BYTTEPLAN.md «Tilbake»)."

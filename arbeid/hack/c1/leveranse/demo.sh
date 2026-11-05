#!/bin/sh
# Case 1-demo med ett kall: den ekte agenten (kjor_agent.py), på kjøringen fra sh KJOR.sh.
# 1) Mangler ut/agent.csv eller miljøet, kjøres sh KJOR.sh først (ca. 1 min).
# 2) vis_manussaker.py viser de tre sakene i DEMO_MANUS.md (første i fila av hver type) og varsler ved avvik fra manuset.
# 3) demo_vis.py trekker tre saker til med seed 0 (MOT funnet med sitat, rutet til menneske, FOR) og viser
#    NBIMs egne stemmer (real_votes) som fasit.
# Bruk (fra roten av repoet):  sh arbeid/hack/c1/leveranse/demo.sh
# (Et argument, f.eks. "$PWD" som i eldre instrukser, godtas og ignoreres.)
set -eu
ROT="$(cd "$(dirname "$0")/../../../.." && pwd)"
mkdir -p "$ROT/home"
LOGG="$ROT/home/KJOR.log"  # i home/, som er gitignorert
pyk() { for v in .venv_kjor .venv; do [ -x "$ROT/$v/bin/python" ] && { echo "$ROT/$v/bin/python"; return; }; done; echo ""; }
if ! { [ -f "$ROT/ut/agent.csv" ] && [ -f "$ROT/ut/pred_maaler.csv" ] && [ -n "$(pyk)" ]; }; then
  echo "demo: ut/ eller miljøet mangler, kjører først  sh KJOR.sh  (ca. 1 min) ..."
  sh "$ROT/KJOR.sh" > "$LOGG" 2>&1 || { cat "$LOGG"; echo "DEMO STOPPET: sh KJOR.sh feilet (utskrift over)."; exit 5; }
  grep -E '^(HOVEDTALL|FRYSVAKT|TALLVAKT|PLATTFORMAVVIK)' "$LOGG" || true
fi
PYK="$(pyk)"
UT="$ROT/arbeid/hack/c1/leveranse/demo_utskrift.txt"
REAL="$ROT/state/opplastet/20261105_114241_real_votes.csv"
cd "$ROT"
E() { env -i HOME="$ROT/home" PATH="$(dirname "$PYK"):/usr/bin:/bin" LANG=C.UTF-8 "$@"; }
HOVED="$(E "$PYK" -I "$ROT/arbeid/hack/c1/maaler_offisiell_v3.py" "$ROT/ut/pred_maaler.csv" test --data real --score mot | grep -E "^SCORE" | cut -d" " -f2)"
VAKT="$( [ -f "$LOGG" ] && grep -h -E '^(TALLVAKT|FRYSVAKT)' "$LOGG" | head -2 | tr '\n' ' ' || echo "tallvakt/frysvakt: se utskriften fra sh KJOR.sh")"
{
  echo "# Case 1 demo, $(date '+%Y-%m-%d %H:%M'), kjøring fra sh KJOR.sh i repo-roten ($(head -1 "$ROT/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
  echo "# agent: arbeid/hack/levering/kjor_agent.py (modell repo4, kalibrert P(MOT) og til menneske ved P i [0,15, 0,85) + ukjent selskap, injeksjon, datafeil)"
  echo "# HOVEDTALL F1 MOT mot styret (v3 --score mot): $HOVED   (avvik-sidetall: $(grep -h '^SCORE' "$ROT/ut/KJORING.txt" | tail -1))"
  echo "# $VAKT"
  echo
  echo "######## De tre sakene i DEMO_MANUS.md (første i agent.csv av hver type)"
  E "$PYK" -I "$ROT/arbeid/hack/c1/vis_manussaker.py" "$ROT/ut/agent.csv" "$REAL"
  echo "######## Tre saker til, trukket med seed 0 (demo_vis.py)"
  E "$PYK" -I "$ROT/arbeid/hack/c1/leveranse/demo_vis.py" "$ROT/ut/agent.csv" "$REAL"
} | tee "$UT"
echo "skrev $UT"
# ordvakt: utskriften skal ikke inneholde lokale stier eller interne navn
if grep -n -E '/Users|landsby|smed|sak [0-9]{4}' "$UT"; then echo "ORDVAKT RØD: interne ord i $UT (linjer over)"; exit 6; fi
echo "ORDVAKT GRØNN: ingen lokale stier eller interne navn i utskriften"

#!/bin/sh
# Case 1 demo med ett kall (ett kall): den ekte agenten (kjor_agent.py, frosset modell repo4), ikke stubben.
# 1) fremmed.sh lager en kald kopi i MÅL og kjører agenten på hele test 2026 der (env -i, låste pakker, ca. 40 s).
#    Finnes kopien alt (MÅL/ut/agent.csv og MÅL.log med HOVEDTALL, f.eks. fra `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald`
#    startet i bakgrunnen ved 0:00), brukes den som den er: ingen dobbel kald kjøring i en 3-minutters demo.
#    Vil du tvinge ny kopi: slett MÅL eller gi `--ny` som andre argument.
# 2) vis_manussaker.py viser de tre sakene i DEMO_MANUS.md (første i fila av hver type) og varsler ved avvik fra manuset.
# 3) demo_vis.py trekker tre saker til med seed 0 (MOT funnet med sitat, rutet til menneske, FOR) og viser
#    NBIMs egne stemmer (real_votes) som fasit. Ingen N-PX.
# Bruk (fra rotmappa i repoet): sh arbeid/hack/c1/leveranse/demo.sh [/tmp/c1_kald] [--ny]
# GitHub-klone og jury-zip (#2897): sh KJOR.sh, så  sh arbeid/hack/c1/leveranse/demo.sh "$PWD". Der er MÅL roten selv;
# mangler ut/ eller miljøet, kjører demo.sh  sh KJOR.sh  først. fremmed.sh brukes bare i landsbymappa (state/c1_frys.json).
set -eu
KILDE="$(cd "$(dirname "$0")/../../../.." && pwd)"
MAAL="${1:-/tmp/c1_kald}"
LOGG="$MAAL.log"
# jury-zipen og GitHub-klonen: ingen fremmed.sh eller ingen state/c1_frys.json; kopien er roten selv etter `sh KJOR.sh`
if [ ! -f "$KILDE/arbeid/hack/levering/fremmed.sh" ] || [ ! -f "$KILDE/state/c1_frys.json" ]; then
  MAAL="$KILDE"; mkdir -p "$KILDE/home"; LOGG="$KILDE/home/KJOR.log"  # loggen i home/ (gitignorert), ikke utenfor repoen
  pyk() { for v in .venv_kjor .venv; do [ -x "$MAAL/$v/bin/python" ] && { echo "$MAAL/$v/bin/python"; return; }; done; echo ""; }
  if ! { [ -f "$MAAL/ut/agent.csv" ] && [ -f "$MAAL/ut/pred_maaler.csv" ] && [ -n "$(pyk)" ]; }; then
    [ -f "$KILDE/KJOR.sh" ] || { echo "DEMO STOPPET: fant verken ut/agent.csv eller KJOR.sh i $KILDE. Stå i roten av repoen."; exit 5; }
    echo "demo: ut/ eller miljøet mangler, kjører først  sh KJOR.sh  (ca. 1 min) ..."
    sh "$KILDE/KJOR.sh" > "$LOGG" 2>&1 || { cat "$LOGG"; echo "DEMO STOPPET: sh KJOR.sh feilet (utskrift over)."; exit 5; }
    grep -E '^(HOVEDTALL|FRYSVAKT|TALLVAKT|PLATTFORMAVVIK)' "$LOGG" || true
  fi
  [ -f "$KILDE/arbeid/hack/c1/vis_manussaker.py" ] || { echo "DEMO STOPPET: arbeid/hack/c1/vis_manussaker.py mangler i pakka"; exit 5; }
  PYK="$(pyk)"
else
  PYK="$MAAL/.venv/bin/python"
fi
UT="$KILDE/arbeid/hack/c1/leveranse/demo_utskrift.txt"
cd "$KILDE"
if [ "$MAAL" = "$KILDE" ]; then
  KOPI="kjøring fra sh KJOR.sh i repo-roten ($(head -1 "$MAAL/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
elif [ "${2:-}" != "--ny" ] && [ -f "$MAAL/ut/pred_maaler.csv" ] && [ -f "$MAAL/ut/agent.csv" ] && [ -x "$PYK" ]; then
  KOPI="gjenbrukt kald kopi i $MAAL ($(head -1 "$MAAL/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
else
  sh arbeid/hack/levering/fremmed.sh "$MAAL" > "$LOGG" 2>&1 || { cat "$LOGG"; exit 1; }
  KOPI="ny kald kopi i $MAAL ($(head -1 "$MAAL/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
fi
# hovedtallet regnes på nytt i kopien (samme kall som fremmed.sh, 0,1 s), så det ikke avhenger av hvor fremmed.sh-utskriften ble sendt
HOVED="$(env -i HOME="$MAAL/home" PATH="$(dirname "$PYK"):/usr/bin:/bin" LANG=C.UTF-8 \
  "$PYK" -I "$MAAL/arbeid/hack/c1/maaler_offisiell_v3.py" "$MAAL/ut/pred_maaler.csv" test --data real --score mot | grep -E "^SCORE" | cut -d" " -f2)"
VAKT="$( [ -f "$LOGG" ] && grep -h -E '^(TALLVAKT|FRYSVAKT)' "$LOGG" | head -2 | tr '\n' ' ' || echo "tallvakt/frysvakt: se utskriften fra fremmed.sh (i jury-zipen: fra sh KJOR.sh)")"
if [ "$MAAL" = "$KILDE" ]; then  # klone/zip: bruk filene der de ligger, ingen kopier i roten (#2897)
  DV="$KILDE/arbeid/hack/c1/leveranse/demo_vis.py"; VM="$KILDE/arbeid/hack/c1/vis_manussaker.py"
else
  cp arbeid/hack/c1/leveranse/demo_vis.py "$MAAL/demo_vis.py"
  cp arbeid/hack/c1/vis_manussaker.py "$MAAL/vis_manussaker.py"
  DV="$MAAL/demo_vis.py"; VM="$MAAL/vis_manussaker.py"
fi
REAL="$MAAL/state/opplastet/20261105_114241_real_votes.csv"
{
  echo "# renset utskrift: modellnavnet i første linje av ut/KJORING.txt (skrevet av den frosne kjor_agent.py, et internt lagnavn) er byttet til «modell repo4» (repo4 = #2044-oppskriften + 4 historikktrekk, byttet inn 17:03); ingen tall er endret"
  echo "# Case 1 demo, $(date '+%Y-%m-%d %H:%M'), $KOPI"
  echo "# agent: arbeid/hack/levering/kjor_agent.py (standard real_votes, modell repo4, kalibrert P(MOT) og til menneske ved P i [0,15, 0,85) + ukjent selskap, injeksjon, datafeil)"
  echo "# måler i kopien: HOVEDTALL F1 MOT mot styret (v3 --score mot): $HOVED   (avvik-sidetall: $(grep -h '^SCORE' "$MAAL/ut/KJORING.txt" | tail -1))"
  echo "# $VAKT"
  echo
  echo "######## De tre sakene i DEMO_MANUS.md (første i agent.csv av hver type)"
  env -i HOME="$MAAL/home" PATH="$(dirname "$PYK"):/usr/bin:/bin" LANG=C.UTF-8 \
    "$PYK" -I "$VM" "$MAAL/ut/agent.csv" "$REAL"
  echo "######## Tre saker til, trukket med seed 0 (demo_vis.py)"
  env -i HOME="$MAAL/home" PATH="$(dirname "$PYK"):/usr/bin:/bin" LANG=C.UTF-8 \
    "$PYK" -I "$DV" "$MAAL/ut/agent.csv" "$REAL"
} | tee "$UT"
echo "skrev $UT"
# ordvakt: utskriften skal ikke inneholde lokale stier eller interne navn
if grep -n -E '/Users|landsby|smed|sak [0-9]{4}' "$UT"; then echo "ORDVAKT RØD: interne ord i $UT (linjer over)"; exit 6; fi
echo "ORDVAKT GRØNN: ingen lokale stier eller interne navn i utskriften"

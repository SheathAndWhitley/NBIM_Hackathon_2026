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
set -eu
KILDE="$(cd "$(dirname "$0")/../../../.." && pwd)"
MAAL="${1:-/tmp/c1_kald}"
# jury-zipen: der finnes ikke fremmed.sh; kopien er pakkeroten selv etter `sh KJOR.sh`
if [ ! -f "$KILDE/arbeid/hack/levering/fremmed.sh" ]; then
  MAAL="$KILDE"
  [ -f "$MAAL/ut/agent.csv" ] && [ -f "$MAAL/ut/pred_maaler.csv" ] && [ -x "$MAAL/.venv/bin/python" ] || {
    echo "DEMO STOPPET: kjør først  sh KJOR.sh  i roten av den utpakkede zipen (lager .venv og ut/agent.csv), så  sh arbeid/hack/c1/leveranse/demo.sh"; exit 5; }
  [ -f "$KILDE/arbeid/hack/c1/vis_manussaker.py" ] || { echo "DEMO STOPPET: arbeid/hack/c1/vis_manussaker.py mangler i pakka"; exit 5; }
fi
UT="$KILDE/arbeid/hack/c1/leveranse/demo_utskrift.txt"
cd "$KILDE"
PYK="$MAAL/.venv/bin/python"
if [ "${2:-}" != "--ny" ] && [ -f "$MAAL/ut/pred_maaler.csv" ] && [ -f "$MAAL/ut/agent.csv" ] && [ -x "$PYK" ]; then
  KOPI="gjenbrukt kald kopi i $MAAL ($(head -1 "$MAAL/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
else
  sh arbeid/hack/levering/fremmed.sh "$MAAL" > "$MAAL.log" 2>&1 || { cat "$MAAL.log"; exit 1; }
  KOPI="ny kald kopi i $MAAL ($(head -1 "$MAAL/ut/KJORING.txt" | sed -e 's/smed2 #2044-modell/modell repo4/'))"
fi
# hovedtallet regnes på nytt i kopien (samme kall som fremmed.sh, 0,1 s), så det ikke avhenger av hvor fremmed.sh-utskriften ble sendt
HOVED="$(env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
  "$PYK" -I "$MAAL/arbeid/hack/c1/maaler_offisiell_v3.py" "$MAAL/ut/pred_maaler.csv" test --data real --score mot | grep -E "^SCORE" | cut -d" " -f2)"
VAKT="$( [ -f "$MAAL.log" ] && grep -h -E '^(TALLVAKT|FRYSVAKT)' "$MAAL.log" | head -2 | tr '\n' ' ' || echo "tallvakt/frysvakt: se utskriften fra fremmed.sh (i jury-zipen: fra sh KJOR.sh)")"
cp arbeid/hack/c1/leveranse/demo_vis.py "$MAAL/demo_vis.py"
cp arbeid/hack/c1/vis_manussaker.py "$MAAL/vis_manussaker.py"  # i zipen: samme fil til pakkeroten, kildene røres ikke
REAL="$MAAL/state/opplastet/20261105_114241_real_votes.csv"
{
  echo "# renset utskrift: modellnavnet i første linje av ut/KJORING.txt (skrevet av den frosne kjor_agent.py, et internt lagnavn) er byttet til «modell repo4» (repo4 = #2044-oppskriften + 4 historikktrekk, byttet inn 17:03); ingen tall er endret"
  echo "# Case 1 demo, $(date '+%Y-%m-%d %H:%M'), $KOPI"
  echo "# agent: arbeid/hack/levering/kjor_agent.py (standard real_votes, modell repo4, kalibrert P(MOT) og til menneske ved P i [0,15, 0,85) + ukjent selskap, injeksjon, datafeil)"
  echo "# måler i kopien: HOVEDTALL F1 MOT mot styret (v3 --score mot): $HOVED   (avvik-sidetall: $(grep -h '^SCORE' "$MAAL/ut/KJORING.txt" | tail -1))"
  echo "# $VAKT"
  echo
  echo "######## De tre sakene i DEMO_MANUS.md (første i agent.csv av hver type)"
  env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
    "$MAAL/.venv/bin/python" -I "$MAAL/vis_manussaker.py" "$MAAL/ut/agent.csv" "$REAL"
  echo "######## Tre saker til, trukket med seed 0 (demo_vis.py)"
  env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
    "$MAAL/.venv/bin/python" -I "$MAAL/demo_vis.py" "$MAAL/ut/agent.csv" "$REAL"
} | tee "$UT"
echo "skrev $UT"
# ordvakt: utskriften skal ikke inneholde lokale stier eller interne navn
if grep -n -E '/Users|landsby|smed|sak [0-9]{4}' "$UT"; then echo "ORDVAKT RØD: interne ord i $UT (linjer over)"; exit 6; fi
echo "ORDVAKT GRØNN: ingen lokale stier eller interne navn i utskriften"

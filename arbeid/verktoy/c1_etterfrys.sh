#!/bin/bash
# Etterfrys-sjekk for Case 1 med én kommando (arkitekt #2187, brukes av dommeren i #1972 kl. 18:30).
# Kjører i rekkefølge: 1) frysvakt (c1_frys.py sjekk --krev)  2) c1_tallvakt.py på landsbymappen
#                      3) fremmed.sh (kald kopi under env -i, med egen frysvakt og tallvakt)
# Alle stegene kjøres selv om et tidligere er rødt, så rapporten viser hele bildet.
# Skriver én rapport med GRØNN/RØD per steg, tid per steg og total tid.
#
# Bruk (fra hvor som helst):
#   bash arbeid/verktoy/c1_etterfrys.sh                 rapport til state/rapporter/c1_etterfrys.md
#   bash arbeid/verktoy/c1_etterfrys.sh --prove         før frys: midlertidig frys i /tmp (C1_FRYS),
#                                                        rapport til state/rapporter/c1_etterfrys_prove.md
#   --rapport FIL  annen rapportfil.   --maal DIR  kald kopi (standard /tmp/c1_etterfrys, ikke /tmp/fremmed)
# Utgang 0 = alle grønne, 1 = minst ett rødt steg.
set -u
LAND="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$LAND"
PROVE=0; RAPPORT=""; MAAL="/tmp/c1_etterfrys"
while [ $# -gt 0 ]; do
  case "$1" in
    --prove) PROVE=1 ;;
    --rapport) RAPPORT="$2"; shift ;;
    --maal) MAAL="$2"; shift ;;
    *) echo "ukjent valg: $1"; exit 2 ;;
  esac
  shift
done
[ -z "$RAPPORT" ] && { [ $PROVE = 1 ] && RAPPORT="state/rapporter/c1_etterfrys_prove.md" || RAPPORT="state/rapporter/c1_etterfrys.md"; }
LOGG="$(mktemp -d /tmp/c1_etterfrys_logg.XXXX)"

KREV="--krev"
if [ $PROVE = 1 ]; then
  # prøve før kl. 16: frys nå i /tmp, så frysvakta i steg 1 og 3 har noe å sjekke mot (som generalprøve #2174)
  export C1_FRYS="$LOGG/prove_frys.json"
  python3 -I arbeid/verktoy/c1_frys.py frys > "$LOGG/0_frys.txt" 2>&1
  MODUS="PRØVE: midlertidig frys $C1_FRYS (ikke den ekte state/c1_frys.json)"
else
  [ "$(date +%H)" -lt 16 ] && echo "ADVARSEL: klokka er før 16, ekte frys finnes kanskje ikke ennå (bruk --prove)"
  MODUS="EKTE: state/c1_frys.json, --krev (ikke frosset = rødt)"
fi

T_START=$(date +%s)
NAVN=(); STATUS=(); TID=(); KODE=()
steg() {  # steg <navn> <loggfil> <kommando...>
  local navn="$1" fil="$2"; shift 2
  local t0=$(date +%s)
  echo ">>> $navn"
  "$@" > "$fil" 2>&1
  local k=$?
  local t=$(( $(date +%s) - t0 ))
  tail -5 "$fil"
  NAVN+=("$navn"); KODE+=("$k"); TID+=("$t")
  if [ $k = 0 ]; then STATUS+=("GRØNN"); else STATUS+=("RØD"); fi
  echo "<<< $navn: $([ $k = 0 ] && echo GRØNN || echo RØD) (utgang $k, $t s)"
}

steg "1 frysvakt" "$LOGG/1_frys.txt" python3 -I arbeid/verktoy/c1_frys.py sjekk $KREV
steg "2 tallvakt (landsbymappen)" "$LOGG/2_tallvakt.txt" python3 -I arbeid/verktoy/c1_tallvakt.py
steg "3 fremmed.sh (kald kopi)" "$LOGG/3_fremmed.txt" sh arbeid/hack/levering/fremmed.sh "$MAAL"
T_TOT=$(( $(date +%s) - T_START ))

ALLE=GRØNN
for s in "${STATUS[@]}"; do [ "$s" = RØD ] && ALLE=RØD; done
HOVED="$(grep -E '^HOVEDTALL' "$LOGG/3_fremmed.txt" | tail -1)"

{
  echo "# Case 1 etterfrys-sjekk: $ALLE ($(date '+%Y-%m-%d %H:%M'))"
  echo
  echo "Kommando: \`bash arbeid/verktoy/c1_etterfrys.sh$([ $PROVE = 1 ] && echo ' --prove')\`  "
  echo "Modus: $MODUS  "
  echo "Total tid: $T_TOT s. Kald kopi: $MAAL. Fulle logger: $LOGG"
  echo
  echo "| Steg | Status | Utgang | Tid |"
  echo "|---|---|---|---|"
  for i in "${!NAVN[@]}"; do
    echo "| ${NAVN[$i]} | ${STATUS[$i]} | ${KODE[$i]} | ${TID[$i]} s |"
  done
  echo
  [ -n "$HOVED" ] && echo "$HOVED (fra kald kopi)" && echo
  for f in "$LOGG"/[123]_*.txt; do
    echo "## $(basename "$f" .txt): siste linjer"
    echo '```'
    tail -12 "$f"
    echo '```'
  done
  echo
  echo "Utgangskoder: frysvakt 2 = avvik/ikke frosset; tallvakt 1 = tall i .md avviker, 2 = måleren feilet;"
  echo "fremmed.sh 4 = frysvakt rød i kopien, 1 = tallvakt rød i kopien, annet = kjøringen krasjet."
} > "$RAPPORT"

echo "TOTALT: $ALLE på $T_TOT s. Rapport: $RAPPORT"
[ "$ALLE" = GRØNN ]

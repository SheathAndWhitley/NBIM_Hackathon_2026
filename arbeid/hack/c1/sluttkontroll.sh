#!/usr/bin/env bash
# Case 1 sluttkontroll (arkitekt #2150): én kommando, PASS/FAIL per krav. For dommeren kl. 19:30 (#1972).
#   bash arbeid/hack/c1/sluttkontroll.sh          (fra hvor som helst, ca. 1 min)
# Gjenbruker: levering/fremmed.sh (kald kopi under env -i, frysvakt, tallvakt), måler v3 --score mot,
#   verktoy/c1_tallvakt.py, verktoy/c1_frys.py (#2142) og c1/sitatvakt.py (#2150).
# Krav:  1 kald start   2 F1 MOT = 0,476 på frossen modell   3 modellfiler uendret siden frys
#        4 ingen utdaterte tall (kald kjøring og pakkas lagrede filer)   5 alle sitater har kilde   6 varighet < 10 min
# Skriver tabellen til skjermen og state/rapporter/c1_sluttkontroll.md (overskrives hver kjøring).
# Valg (miljø): REF=0.476190  TOL=0.0005  MAAL=/tmp/c1_sluttkontroll (kald kopi, står igjen for innsyn)  RAPP=<rapportfil>.
# Utgang 0 = alle PASS, 1 = minst én FAIL. Krav 3 er VENTER (ikke FAIL) før frys kl. 16.
set -uo pipefail
LAND="$(cd "$(dirname "$0")/../../.." && pwd)"
ARB="$LAND/arbeid"
REF="${REF:-0.476190}"; TOL="${TOL:-0.0005}"
MAAL="${MAAL:-/tmp/c1_sluttkontroll}"
RAPP="${RAPP:-$LAND/state/rapporter/c1_sluttkontroll.md}"
LOGG="$(mktemp /tmp/c1_sluttkontroll_logg.XXXXXX)"
T0=$(date +%s)
RADER=(); DETALJ=(); FEIL=0
rad() {  # rad <PASS|FAIL|VENTER> <krav> <bevis>
  RADER+=("| $1 | $2 | $3 |"); [ "$1" = FAIL ] && FEIL=$((FEIL + 1))
  echo "[$(date '+%T') +$(( $(date +%s) - T0 ))s] $1  $2: $3"; }
F1() { python3 -I "$ARB/hack/c1/maaler_offisiell_v3.py" "$1" test --data real --score mot 2>&1 | sed -n 's/^SCORE *//p' | tail -1; }
likt() { python3 -I -c "import sys; sys.exit(0 if abs(float(sys.argv[1] or 'nan')-float(sys.argv[2]))<=float(sys.argv[3]) else 1)" "$1" "$REF" "$TOL" 2>/dev/null; }
cd "$LAND"
GIT="$(git rev-parse --short HEAD)"

# 1 kald start: fremmed.sh kopierer bare det agenten trenger og kjører under env -i
echo "kjører fremmed.sh -> $MAAL (logg $LOGG)"
sh "$ARB/hack/levering/fremmed.sh" "$MAAL" > "$LOGG" 2>&1; RC=$?
TID="$(grep -E '^tid:' "$LOGG" | tail -1)"
if [ "$RC" = 4 ]; then rad FAIL "1 kald start" "frysvakta stoppet kopien (utgang 4), se logg"
elif [ "$RC" != 0 ] && [ "$RC" != 1 ]; then rad FAIL "1 kald start" "fremmed.sh utgang $RC (bare 0, eller 1 = tallvakta, er lov), se logg"; tail -15 "$LOGG"
elif [ -s "$MAAL/ut/pred_maaler.csv" ] && [ -s "$MAAL/ut/agent.csv" ] && [ -n "$TID" ]; then
  rad PASS "1 kald start" "fremmed.sh fra tom mappe under env -i, uv sync --frozen; ${TID#tid: }; utgang $RC$([ "$RC" = 1 ] && echo ' (tallvakta, se krav 4)')"
else rad FAIL "1 kald start" "agenten ga ikke svarfiler (fremmed.sh utgang $RC), se logg"; tail -15 "$LOGG"; fi

# 2 F1 MOT på frossen modell: kald kopi (maskin alene og med ruting) og de frosne testprediksjonene fra #2103
A="$(F1 "$MAAL/ut/_pred_uten_ruting.csv")"; B="$(F1 "$MAAL/ut/pred_maaler.csv")"; C="$(F1 "$ARB/oppgave_2103/full_test.csv")"
MSHA="$(shasum -a 256 "$ARB/hack/c1/maaler_offisiell_v3.py" | cut -c1-10)"
if likt "$A" && likt "$B" && likt "$C"; then
  rad PASS "2 F1 MOT = 0,476" "kald uten ruting ${A}, kald med ruting ${B}, frossen #2103 ${C} (REF $REF ± $TOL, måler v3 sha ${MSHA})"
else rad FAIL "2 F1 MOT = 0,476" "kald uten ruting ${A:-mangler}, kald med ruting ${B:-mangler}, frossen #2103 ${C:-mangler}; REF $REF ± $TOL"; fi

# 3 modellfiler uendret siden frys (#2142). Før kl. 16 finnes ikke frysfila: VENTER. Etter kl. 16 uten frys: FAIL.
FRYS="$(python3 -I "$ARB/verktoy/c1_frys.py" sjekk 2>&1)"; FRC=$?
FRYS1="$(echo "$FRYS" | tr '\n' ' ' | cut -c1-220)"
if [ "$FRC" != 0 ]; then rad FAIL "3 modellfiler uendret siden frys" "$FRYS1"
elif echo "$FRYS" | grep -q "ikke frosset"; then
  if [ "$(date +%H%M)" -ge 1600 ]; then rad FAIL "3 modellfiler uendret siden frys" "klokka er over 16 og frysen mangler: $FRYS1"
  else rad VENTER "3 modellfiler uendret siden frys" "ikke frosset ennå (frys kl. 16 via LaunchAgent): $FRYS1"; fi
else rad PASS "3 modellfiler uendret siden frys" "$FRYS1"; fi

# 4a tallvakta på kald kjøring (svarfil og KJORING.txt fra kopien) mot pakkas .md
TV="$(python3 -I "$ARB/verktoy/c1_tallvakt.py" --svar "$MAAL/ut/pred_maaler.csv" --kjoring "$MAAL/ut/KJORING.txt" 2>&1)"; TRC=$?
TV1="$(echo "$TV" | grep -E 'påstander' | tail -1)"
if [ "$TRC" = 0 ] && echo "$TV" | grep -q ", 0 avviker"; then rad PASS "4a ingen utdaterte tall (kald kjøring)" "$TV1"
else rad FAIL "4a ingen utdaterte tall (kald kjøring)" "${TV1:-tallvakta feilet}; avvik: $(echo "$TV" | grep -E '^AVVIK' | cut -d: -f1,2 | sort -u | head -4 | tr '\n' ' ')"
  DETALJ+=("$(echo "$TV" | grep -E '^AVVIK' | head -12)"); fi
# 4b tallvakta på pakkas lagrede filer (levering/kjor_agent_real_maskin_alene.csv og kjor_agent_real_test2026.txt)
TV="$(python3 -I "$ARB/verktoy/c1_tallvakt.py" 2>&1)"; TRC=$?
TV1="$(echo "$TV" | grep -E 'påstander' | tail -1)"
if [ "$TRC" = 0 ] && echo "$TV" | grep -q ", 0 avviker"; then rad PASS "4b ingen utdaterte tall (pakkas lagrede filer)" "$TV1"
else rad FAIL "4b ingen utdaterte tall (pakkas lagrede filer)" "${TV1:-tallvakta feilet}; $(echo "$TV" | grep -E '^Kjøring' | head -1)"
  DETALJ+=("$(echo "$TV" | grep -E '^(Kjøring|AVVIK)' | head -12)"); fi

# 5 alle sitater har kilde og står ordrett der (sitatvakt på kald kjørings agent.csv)
SV="$(python3 -I "$ARB/hack/c1/sitatvakt.py" "$MAAL/ut/agent.csv" 2>&1)"; SRC=$?
SV1="$(echo "$SV" | tail -1)"
if [ "$SRC" = 0 ]; then rad PASS "5 alle sitater har kilde" "$SV1"
else rad FAIL "5 alle sitater har kilde" "$SV1"; DETALJ+=("$(echo "$SV" | head -12)"); fi

# 6 varighet
SEK=$(( $(date +%s) - T0 ))
if [ "$SEK" -lt 600 ]; then rad PASS "6 varighet under 10 min" "${SEK} s"; else rad FAIL "6 varighet under 10 min" "${SEK} s"; fi

SAMLET=$([ "$FEIL" = 0 ] && echo "PASS" || echo "FAIL ($FEIL krav)")
{
  echo "# Case 1 sluttkontroll: $SAMLET ($(date '+%Y-%m-%d %H:%M'), git $GIT, ${SEK} s)"
  echo
  echo "Kommando: \`bash arbeid/hack/c1/sluttkontroll.sh\` (arkitekt #2150, for dommeren i #1972). Kald kopi i \`$MAAL\`, logg \`$LOGG\`."
  echo
  echo "| status | krav | bevis |"; echo "|---|---|---|"
  printf '%s\n' "${RADER[@]}"
  if [ "${#DETALJ[@]}" -gt 0 ]; then echo; echo "## Avvik (første linjer)"; echo '```'; printf '%s\n' "${DETALJ[@]}"; echo '```'; fi
} > "$RAPP"
echo; sed -n '5,$p' "$RAPP"
echo "SLUTTKONTROLL $SAMLET (rapport: $RAPP)"
[ "$FEIL" = 0 ]

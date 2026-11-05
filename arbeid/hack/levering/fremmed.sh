#!/bin/sh
# Case 1: kjør hele stemmeagenten fra en ren kopi, som på en fremmed maskin (#2016).
# Bruk (fra landsbymappen): sh arbeid/hack/levering/fremmed.sh [/tmp/fremmed [--til-menneske 15]]
# 1) kopierer bare de filene agenten trenger til MÅL, med samme relative stier
# 2) eget uv-prosjekt i MÅL med låste avhengigheter (uv.lock, uv sync --frozen)
# 3) kjører kjor_agent.py under env -i (ingen arvede miljøvariabler) og skriver tida
# 4) tallvakta (#2131/#2136): tallene i pakkas .md mot måleren på kopiens egen kjøring; avvik gir utgang 1
set -eu
KILDE="$(cd "$(dirname "$0")/../../.." && pwd)"
MAAL="${1:-/tmp/fremmed}"
[ $# -gt 0 ] && shift  # resten sendes til kjor_agent.py, f.eks. --til-menneske 15
# rotsjekk (#2339): levering/ alene er ikke nok; gi en klar feil i stedet for en villedende FRYSVAKT RØD
[ -f "$KILDE/arbeid/oppgave_2044/train.py" ] && [ -f "$KILDE/arbeid/verktoy/c1_frys.py" ] || {
  echo "FEIL STED: fant ikke repo-roten ($KILDE mangler arbeid/oppgave_2044/train.py eller arbeid/verktoy/c1_frys.py)."
  echo "Kjør fra roten av repoet (mappa med arbeid/ og state/): sh arbeid/hack/levering/fremmed.sh /tmp/fremmed"
  echo "Mappa levering/ alene er ikke nok, se README.md («Hvor du står»)."; exit 6; }
# frysvakt (#2142): etter frys kl. 16 stopper vi hvis modell/prediksjoner/agent er endret
python3 -I "$KILDE/arbeid/verktoy/c1_frys.py" sjekk || { echo "FRYSVAKT RØD: kald kopi stoppet (se over)"; exit 4; }
rm -rf "$MAAL"
mkdir -p "$MAAL/home"
cd "$KILDE"
kopier() { for f in "$@"; do mkdir -p "$MAAL/$(dirname "$f")"; cp -R "$f" "$MAAL/$f"; done; }
# bare arrangørens data (ordre #242): real_votes.csv og data_off/real_test_input.csv laget av den
kopier arbeid/hack/levering/kjor_agent.py \
  arbeid/hack/levering/modell_repo4.py arbeid/hack/levering/stemmeagent \
  arbeid/hack/levering/c1_real.py arbeid/hack/levering/injeksjon_hoflig.py arbeid/hack/levering/retningslinje_oppslag.py arbeid/hack/c1/retningslinjer/punkter.jsonl \
  arbeid/oppgave_2044/train.py arbeid/oppgave_2047/vern.py \
  arbeid/oppgave_2046/case1_mot.py arbeid/hack/c1/maaler_offisiell_v2.py arbeid/hack/c1/maaler_offisiell_v3.py \
  arbeid/hack/c1/data_off/real_test_input.csv state/opplastet/20261105_114241_real_votes.csv \
  arbeid/hack/levering/sjekk_treffsikkerhet.sh
# pakkas tekster og tallvakta, så vakta sjekker kopien og ikke landsbymappen (#2136)
kopier arbeid/verktoy/c1_tallvakt.py $(ls arbeid/hack/levering/*.md arbeid/hack/c1/leveranse/*.md)
# real_votes-delene (#2094): standard siden #2053. Målerne har gudens filsti hardkodet; i kopien peker den på kopiens fil,
# ellers ville en kald kopi lese fra landsbymappen. Regnestykket er uendret.
sed -i '' "s#$KILDE/#$MAAL/#g" "$MAAL/arbeid/hack/c1/maaler_offisiell_v2.py" "$MAAL/arbeid/hack/c1/maaler_offisiell_v3.py"
# eget prosjekt, samme låste versjoner som modellen ble målt med
cp arbeid/kandidater/smed2_c1_mot/pyproject.toml arbeid/kandidater/smed2_c1_mot/uv.lock "$MAAL/"
echo "kopi: $(du -sh "$MAAL" | cut -f1) i $MAAL"
T0=$(date +%s)
(cd "$MAAL" && UV_PROJECT_ENVIRONMENT="$MAAL/.venv" uv sync --frozen --no-install-project -q)
T1=$(date +%s)
env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
  "$MAAL/.venv/bin/python" "$MAAL/arbeid/hack/levering/kjor_agent.py" --ut "$MAAL/ut" "$@"
T2=$(date +%s)
echo "tid: uv sync $((T1 - T0)) s, kjøring $((T2 - T1)) s, totalt $((T2 - T0)) s"
# Hovedtallet til slutt (dommer #2127): SCORE-linjene over er avvik fra styret inkl. AVSTÅ (v2, sidetall).
# Hovedtallet er F1 på MOT mot styret, måler v3 --score mot, på maskinens egne svar (rutingen endrer dem ikke).
printf "HOVEDTALL F1 MOT mot styret (v3 --score mot): "
env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 \
  "$MAAL/.venv/bin/python" -I "$MAAL/arbeid/hack/c1/maaler_offisiell_v3.py" "$MAAL/ut/pred_maaler.csv" test --data real --score mot \
  | grep -E "^SCORE" | cut -d" " -f2
# tallsjekk (#2273): tall i pakkas .md uten kilde i tall-tabellen/målerutskriftene (landsbymappen, der kildene bor).
# Bare varsel, endrer ikke utgangskoden.
TS="$(python3 -I "$KILDE/arbeid/verktoy/c1_tallsjekk.py" --bare-ikke 2>&1)" || TS="tallsjekken feilet: $(echo "$TS" | tail -1)"
echo "TALLSJEKK (varsel): $(echo "$TS" | tail -1)"
echo "$TS" | sed '$d' | head -20 | sed 's/^/  ikke funnet: /'
# 4) tallvakta på kopiens egen kjøring: F1/P/R/TP på MOT, 58 MOT, 66 avvik, andel til menneske (#2136)
if env -i HOME="$MAAL/home" PATH="$MAAL/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 "$MAAL/.venv/bin/python" -I \
    "$MAAL/arbeid/verktoy/c1_tallvakt.py" --rot "$MAAL" --svar "$MAAL/ut/pred_maaler.csv" --kjoring "$MAAL/ut/KJORING.txt"; then
  echo "TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring"
else
  echo "TALLVAKT RØD: tall i pakka avviker fra kald kjøring (fil:linje over, stiene er i kopien $MAAL). Pakka er IKKE verifisert."
  exit 1
fi

#!/bin/sh
# Case 1: kjør hele stemmeagenten fra en ren kopi, som på en fremmed maskin (#2016).
# Bruk (fra landsbymappen): sh arbeid/hack/levering/fremmed.sh [/tmp/fremmed [--til-menneske 15]]
# 1) kopierer bare de filene agenten trenger til MÅL, med samme relative stier
# 2) eget uv-prosjekt i MÅL med låste avhengigheter (uv.lock, uv sync --frozen)
# 3) kjører kjor_agent.py under env -i (ingen arvede miljøvariabler) og skriver tida
set -eu
KILDE=<repo>
MAAL="${1:-/tmp/fremmed}"
[ $# -gt 0 ] && shift  # resten sendes til kjor_agent.py, f.eks. --til-menneske 15
rm -rf "$MAAL"
mkdir -p "$MAAL/home"
cd "$KILDE"
kopier() { for f in "$@"; do mkdir -p "$MAAL/$(dirname "$f")"; cp -R "$f" "$MAAL/$f"; done; }
kopier arbeid/hack/levering/kjor_agent.py \
  arbeid/kandidater/smed2_c1_mot/train_v3.py arbeid/kandidater/smed2_c1_mot/sec_feats.py \
  arbeid/kandidater/smed2_c1_mot/sec \
  arbeid/hack/varianter/smed3_utf_sitat/agent.py arbeid/hack/varianter/smed3_utf_sitat/fakta.py \
  arbeid/hack/varianter/smed3_utf_sitat/rl arbeid/hack/varianter/smed3_utf_sitat/data/def14a \
  arbeid/hack/c1/maaler.py arbeid/hack/c1/data_v3 arbeid/hack/c1/data_v3_val \
  arbeid/hack/levering/c1_real.py arbeid/oppgave_2044/train.py arbeid/oppgave_2047/vern.py \
  arbeid/oppgave_2046/case1_mot.py arbeid/hack/c1/maaler_offisiell_v2.py arbeid/hack/c1/maaler_offisiell_v3.py \
  arbeid/hack/c1/data_off/real_test_input.csv state/opplastet/20261105_114241_real_votes.csv
# real_votes-delene (#2094): standard siden #2053. Målerne har gudens filsti hardkodet; i kopien peker den på kopiens fil,
# ellers ville en kald kopi lese fra landsbymappen. Regnestykket er uendret.
sed -i '' "s##$MAAL/#g" "$MAAL/arbeid/hack/c1/maaler_offisiell_v2.py" "$MAAL/arbeid/hack/c1/maaler_offisiell_v3.py"
# eget prosjekt, samme låste versjoner som modellen ble målt med
cp arbeid/kandidater/smed2_c1_mot/pyproject.toml arbeid/kandidater/smed2_c1_mot/uv.lock "$MAAL/"
echo "kopi: $(du -sh "$MAAL" | cut -f1) i $MAAL"
T0=$(date +%s)
(cd "$MAAL" && UV_PROJECT_ENVIRONMENT="$MAAL/.venv" uv sync --frozen --no-install-project -q)
T1=$(date +%s)

#!/bin/sh
# Agenten på tre testår (2024, 2025, 2026). For hvert testår T trenes modellen på nytt (agent/modell_rullende.py):
# trent på år før T, C og grense valgt på T-1. Svarfila måles med maaling/maaler.py (F1 på MOT mot styret).
# Bruk (fra repo-roten, etter sh KJOR.sh):  sh maaling/testaar.sh      (ca. 15 s)
set -eu
ROT="$(cd "$(dirname "$0")/.." && pwd)"
PY="$ROT/.venv_kjor/bin/python"
D="$ROT/data/real_votes.csv"
[ -x "$PY" ] || { echo "Kjør  sh KJOR.sh  først (lager miljøet .venv_kjor)."; exit 1; }
K=$(mktemp -d "${TMPDIR:-/tmp}/testaar.XXXXXX")
trap 'rm -rf "$K"' EXIT
cd "$K"
P=""
for T in 2024 2025 2026; do
  "$PY" "$ROT/agent/modell_rullende.py" "$D" --ut svar_$T.csv --hist 2 --variant miks --testaar $T \
    --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate > logg_$T.txt 2>&1 &
  P="$P $!"
done
for p in $P; do wait "$p" || { echo "FEIL: trening feilet:"; tail -5 logg_*.txt; exit 1; }; done
S=""
for T in 2024 2025 2026; do
  "$PY" -I "$ROT/maaling/maaler.py" svar_${T}_test.csv y$T --score mot > maal_$T.txt
  F=$(grep "MOT mot styret" maal_$T.txt | sed -E 's/.*F1 ([0-9.]+).*/\1/')
  echo "$T  $(grep 'MOT mot styret' maal_$T.txt | sed 's/^ *//')"
  S="$S $F"
done
echo $S | awk '{printf "F1 MOT mot styret: 2024 %.4f  2025 %.4f  2026 %.4f  snitt %.4f\n", $1, $2, $3, ($1+$2+$3)/3}'

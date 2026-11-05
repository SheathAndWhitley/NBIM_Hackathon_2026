#!/bin/bash
# Gjenskaper testårstallene for frossen repo4 (dom #2713: F1 MOT 0,5057 / 0,5309 / 0,5120, snitt 0,5162).
# Flyttbar kopi av arbeid/oppgave_2727/testaar.sh (#2733): bare relative stier, kjøres fra pakkas rot eller hvor som helst.
# For hvert testår T: abl_rull.py trener frossen repo4-oppsett på nytt (C/grense valgt på T-1, trent på år < T),
# og maaler_aar.py (offisiell måler, --data real --score mot) måler svarfila. Utdata skrives i en fersk tom mappe i /tmp.
# Bruk:  bash arbeid/hack/c1/leveranse/verktoy/testaar.sh           (trener på nytt, ca. 10 sek)
#        bash arbeid/hack/c1/leveranse/verktoy/testaar.sh --rask    (måler bare de lagrede svarfilene i lagret/)
set -euo pipefail
V="$(cd "$(dirname "$0")" && pwd)"
ROT="$(cd "$V/../../../../.." && pwd)"   # pakkas rot: pyproject.toml, uv.lock og state/opplastet/
D="${C1_DATA:-$ROT/state/opplastet/20261105_114241_real_votes.csv}"
[ -f "$D" ] || { echo "FEIL: finner ikke datafila $D (sett C1_DATA=<sti til real_votes.csv>)"; exit 1; }
K=$(mktemp -d "${TMPDIR:-/tmp}/c1_testaar.XXXXXX")
cd "$K"
echo "rot: $ROT"
echo "utdata: $K"
if [ "${1:-}" = "--rask" ]; then
  cp "$V"/lagret/repo4_202[456]_test.csv .
else
  for T in 2024 2025 2026; do
    uv run --project "$ROT" python "$V/abl_rull.py" "$D" --ut repo4_$T.csv --hist 2 --variant miks --testaar $T \
      --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate > repo4_$T.log 2>&1 &
  done
  for j in $(jobs -p); do wait "$j" || { echo "FEIL: trening feilet, se $K/repo4_*.log"; tail -5 "$K"/repo4_*.log; exit 1; }; done
fi
S=""
for T in 2024 2025 2026; do
  C1_DATA="$D" python3 -I "$V/maaler_aar.py" repo4_${T}_test.csv y$T --data real --score mot > maal_$T.txt
  head -1 maal_$T.txt | grep -q "sha256 71ba5135" || { echo "FEIL: datavakt $T"; cat maal_$T.txt; exit 1; }
  F=$(grep "MOT mot styret" maal_$T.txt | sed -E 's/.*F1 ([0-9.]+).*/\1/')
  echo "$T  $(grep 'MOT mot styret' maal_$T.txt | sed 's/^ *//')"
  S="$S $F"
done
echo $S | awk '{printf "F1 MOT mot styret: 2024 %.4f  2025 %.4f  2026 %.4f  snitt %.4f\n", $1, $2, $3, ($1+$2+$3)/3}'
echo "fasit (dom #2713): 2024 0.5057  2025 0.5309  2026 0.5120  snitt 0.5162"

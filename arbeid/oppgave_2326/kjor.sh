#!/bin/bash
# #2326: kopi av frossen #2044 (via #2320), India AV, std + 5 LGBM-seed, val 2025 og test 2026.
cd "$(dirname "$0")"
D=state/opplastet/20261105_114241_real_votes.csv
P="uv run --project ../oppgave_2023 python"
for s in std 1 2 3 4 5; do
  if [ $s = std ]; then S=""; else S="--seed $s"; fi
  $P train.py $D --variant miks --hist 2 --india 0 $S --val-ut val_$s.csv --test-ut test_$s.csv --ut pred_$s.csv > log_$s.txt 2>&1 &
done
wait

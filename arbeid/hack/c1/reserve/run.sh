#!/bin/bash
# Reserveleveranse Case 1 (#1976): historikkgulvet. Ett kall, bare python3 stdlib, ingen nett.
# Bruk: bash reserve/run.sh [DATAMAPPE med train.csv+test_input.csv] [UT.csv]
# Standard: ../data_v3 -> reserve/pred.csv. Kjører lekkasjesjekk og måler hvis fasit.csv finnes.
set -euo pipefail
HER="$(cd "$(dirname "$0")" && pwd)"
D="$(cd "${1:-$HER/../data_v3}" && pwd)"
UT="${2:-$HER/pred.csv}"
python3 -I "$HER/gulv.py" "$D" "$UT"
echo "skrev $UT ($(($(wc -l < "$UT") - 1)) rader)"
if [ -f "$D/fasit.csv" ]; then
  python3 -I "$HER/lekkasjesjekk.py" "$D" "$UT" | tail -1
  python3 -I "$HER/../maaler.py" "$UT" --fasit "$D/fasit.csv" | tail -1
fi

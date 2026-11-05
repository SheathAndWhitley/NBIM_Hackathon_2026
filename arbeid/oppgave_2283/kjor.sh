#!/bin/bash
# Bruk: bash kjor.sh <t1> <tau>   -> val_t1<t1>_tau<tau>.csv + v3-score (bare val 2025)
D=state/opplastet/20261105_114241_real_votes.csv; P=arbeid/kandidater/smed2_c1_mot
cd "$(dirname "$0")"
uv run --project $P python train_t1.py $D --variant miks --hist 2 --t1 $1 --tau $2 --ut val_t1$1_tau$2.csv 2>&1 | grep -E "VAL|STYRE|Error|error" > log_t1$1_tau$2.txt
python3 -I ../hack/c1/maaler_offisiell_v3.py val_t1$1_tau$2.csv val --data real --score mot | grep SCORE >> log_t1$1_tau$2.txt
echo "== t1=$1 tau=$2"; cat log_t1$1_tau$2.txt

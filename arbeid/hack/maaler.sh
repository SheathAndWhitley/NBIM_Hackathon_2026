#!/bin/bash
# Rundens måler (dommer2 #2020): Case 1 på NBIMs ekte stemmer (gudens filer 05.11 11:42).
# Bruk: bash arbeid/hack/maaler.sh SVAR [VINDU]   VINDU = npx_val (standard) | npx_test | real_val | real_test | npx_train | real_train
# Siste linjer: SCORE <F1 på avvik fra styret>, RETNING maks. Ugyldig svarfil: exit 1.
V="${2:-npx_val}"
exec python3 -I arbeid/hack/c1/maaler_nbim.py "$1" "${V#*_}" --data "${V%%_*}"

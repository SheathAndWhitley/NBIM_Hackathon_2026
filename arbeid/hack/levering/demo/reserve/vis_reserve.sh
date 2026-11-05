#!/bin/sh
# Case 1 (#2191): viser demoen fra ferdige utskrifter. Ingen nett, ingen Python, ingen agent: bare cat.
# Bruk: sh vis_reserve.sh [1|2|3|4|alle]   (1 saker 1-6, 2 sak 7 styret mangler, 3 kald kopi + tall, 4 demo_vis 3 saker)
D="$(cd "$(dirname "$0")" && pwd)"
vis() { echo "################ RESERVE: $1 (ferdig kjøring, $(head -1 "$D/SHA.txt"))"; cat "$D/$1"; echo; }
case "${1:-alle}" in
  1) vis 1_saker_2026.txt ;; 2) vis 2_mangler_styret.txt ;; 3) vis 3_fremmed_kald_kopi.txt ;; 4) vis 4_demo_vis_3_saker.txt ;;
  *) for f in 1_saker_2026.txt 2_mangler_styret.txt 3_fremmed_kald_kopi.txt 4_demo_vis_3_saker.txt; do vis "$f"; done ;;
esac

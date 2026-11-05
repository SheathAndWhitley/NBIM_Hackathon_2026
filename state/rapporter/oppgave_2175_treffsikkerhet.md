# #2175 Case 1 treffsikkerhet i klartekst: ferdig

`arbeid/hack/levering/TREFFSIKKERHET.md` med 2x2 regnet fra `kjor_agent_real_pred_maaler.csv`
med `maaler_offisiell_v3.py` og nytt `treffsikkerhet.py` (importerer målerens regler).
- Alle 1539: TP 30 FP 38 FN 28 TN 1443. Accuracy 95,7 % mot følg styret 96,2 %. Recall MOT 51,7 %, presisjon MOT 44,1 %, riktig på FOR 97,4 %.
- Ikke til menneske (konfidens ≥ 0,6, 1356 saker): TP 9 FP 0 FN 17 TN 1330.
- Til menneske (183): TP 21 FP 38 FN 11 TN 113.
README/JURYSVAR ikke rørt.

# Case 1: dommerens kontroll av TREFFSIKKERHET.md (dommer #2178, 05.11 kl. 13.15)

**Dom: GODKJENT.** Hvert tall i `arbeid/hack/levering/TREFFSIKKERHET.md` (smed3 #2175) er stemt
mot både måleren og mitt eget telleskript, som leser fasitfila direkte og ikke bruker smed3s kode.

Prediksjonsfil: `arbeid/hack/levering/kjor_agent_real_pred_maaler.csv`, sha256 `b113b545…3653`.
Den er lik den frosne fila i `c1_nye_vakter_sjekk.md` (#2155).

| Tall i tabellen | Mitt tall | Status |
|---|---|---|
| Alle: TP 30 / FP 38 / FN 28 / TN 1443 (n 1539) | 30 / 38 / 28 / 1443 | stemmer |
| Accuracy 95,7 % / følg styret 96,2 % | 0,9571 / 0,9623 | stemmer |
| Recall 51,7 %, presisjon 44,1 %, FOR-riktig 97,4 %, F1 0,476 | 0,5172 / 0,4412 / 0,9743 / 0,4762 | stemmer |
| Følg styret F1 0,000 (TP 0, FN 58) | baseline: TP 0 FN 58 F1 0 | stemmer |
| Konfidens ≥ 0,6: TP 9 / FP 0 / FN 17 / TN 1330 (n 1356) | 9 / 0 / 17 / 1330 | stemmer |
| ≥ 0,6: accuracy 98,75 %, følg styret 98,1 %, P 100 %, R 34,6 % | 0,9875 / 0,9808 / 1,0 / 0,3462 | stemmer |
| Konfidens < 0,6: TP 21 / FP 38 / FN 11 / TN 113 (n 183, 11,9 %) | 21 / 38 / 11 / 113; måleren: 183 til menneske | stemmer |

Merknad (ikke feil): real-fila har 1578 rader i 2026; 39 mangler `against_board` og er utelatt.
Tabellen sier «1539 saker med fasit», som er riktig. Juryen kan spørre om de 39, og svaret er at de ikke har fasit.

Kommandoer (fra landsbymappen):
```
python3 -I arbeid/oppgave_2178/tell.py arbeid/hack/levering/kjor_agent_real_pred_maaler.csv
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_pred_maaler.csv test --data real
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py baseline --data real test
shasum -a 256 arbeid/hack/levering/kjor_agent_real_pred_maaler.csv
```

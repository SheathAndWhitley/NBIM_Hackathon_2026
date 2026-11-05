# Case 1: dommerens kontroll av grunnlinjene på ny data (#2232): GODKJENT

Kjørt selv 05.11 kl. 13.34, git 58f2bd1. `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh` -> `/tmp/c1_kald.CV6qW0`, GRØNN, avvik +0,000000, 31 s.
Data: real_votes i kopien, sha256 71ba5135e7ba9d64… (lik arrangørens). Måler v3 `test --data real --score mot`, 1539 vurderte, 58 MOT mot styret.
Følg styret laget med mitt eget skript (`arbeid/oppgave_2232/egen_grunnlinje.py`, fra kopiens datafil), ikke smed2s. Kontrollert også med målerens innebygde `baseline`.

| Modell | Kilde | TP/FP/FN | P | R | F1 MOT | #2222 | EN_SIDE/README | c1_uten_gammel_data | Avvik |
|---|---|---|---|---|---|---|---|---|---|
| Følg styret | egen fil, kald kopi | 0/0/58 | 0 | 0 | **0,000000** | 0,0000 | 0 | – | 0 |
| Følg styret | måler `baseline` | 0/0/58 | 0 | 0 | 0,000000 | 0,0000 | 0 | – | 0 |
| Aksjonærforslag=MOT (gulv) | måler `baseline` | 2/1/56 | 0,6667 | 0,0345 | 0,0656 | 0,0656 | – | – | 0 |
| Frossen #2044 miks h2, uten ruting | kald kopi `_pred_uten_ruting.csv` | 30/38/28 | 0,4412 | 0,5172 | **0,476190** | 0,4762 | 0,476 / P 0,441 / R 0,517 | 0,476190 | 0 |
| Frossen, med ruting | kald kopi `pred_maaler.csv` | 30/38/28 | 0,4412 | 0,5172 | 0,476190 | – | 0,476 | – | 0 |
| Frossen, smed2s id-fil | `oppgave_2222/miks_h2_test.csv` | 30/38/28 | 0,4412 | 0,5172 | 0,476190 | 0,4762 | – | – | 0 |

Alle avvik er 0 (krav ≤ 0,001). Avvik-F1 (sidetall) 0,4818 stemmer også med README.

## Merknader (ikke grunn til avvisning)
1. **Accuracy for følg styret står med to definisjoner.** EN_SIDE/README: 96,2 % (2x2 på MOT: (1539−58)/1539). #2222 og dashbordet: 95,7 % (avvik-linja: (1539−66)/1539). Agenten er 95,7 % i README og 95,4 % i #2222. Konklusjonen «agenten har lavere accuracy enn følg styret» holder med begge. Men en jurymedlem som ser 95,7 % for følg styret på dashbordet og 96,2 % i papiret, vil spørre. Speideren (#2229) bør skrive én setning om definisjonen, eller velge én.
2. **Måler v3 er endret på disk (#2221).** sha256[:10] er nå 418a937e57, og papirene sier 8b09c36e01. Fila `arbeid/hack/c1/maaler_offisiell_v3.py` er **ikke i git** (finnes ikke i HEAD). Den må committes og sha-en oppdateres i JURY.md/sluttkontroll før frysen kl. 16.
3. Frysvakta sa «ikke frosset ennå» (state/c1_frys.json finnes ikke). Det er som forventet før kl. 16.

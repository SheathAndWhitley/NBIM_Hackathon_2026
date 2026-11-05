# Case 1: prøve-kaldstart av hele pakka før frys (dommer #2180, 05.11 kl. 13.12–13.20)

Generalprøve for #1972. README-kommandoen ble kjørt i en ny mappe, slik juryen ville gjort det. **Konklusjon: GRØNN.** Alle tre tabellene kommer ut likt, og frysvakta virker både grønt og rødt. Ingen hindre stopper kjøringen. Under står 6 småting som kan forvirre en fremmed leser.

## Kommandoer og tider (fra landsbymappen)
| steg | kommando | tid | resultat |
|---|---|---|---|
| 1 kald kopi (ikke frosset ennå) | `sh arbeid/hack/levering/fremmed.sh /tmp/provekald_2180` | 45 s totalt (uv sync 0 s, agent 27 s, kjøring 41 s) | utgang 0. **HOVEDTALL 0.476190**, v3: TP 30 FP 38 FN 28, P 0,4412 R 0,5172. 188/1578 (11,9 %) til menneske. Tallvakta: 14 filer, 139 påstander, 0 avvik |
| 2 svarene mot pakka | `cmp /tmp/provekald_2180/ut/pred_maaler.csv arbeid/hack/levering/kjor_agent_real_pred_maaler.csv` | <1 s | byte for byte identisk |
| 3 TREFFSIKKERHET | `python3 -I arbeid/hack/levering/treffsikkerhet.py /tmp/provekald_2180/ut/pred_maaler.csv` | <1 s | alle tre 2x2 er lik TREFFSIKKERHET.md: 30/38/28/1443, ≥0,6: 9/0/17/1330, <0,6: 21/38/11/113. Accuracy 95,7 % mot 96,2 % |
| 4 menneske-tabellen | `python3 -I arbeid/hack/c1/menneske_tabell.py /tmp/provekald_2180/ut/agent.csv` | <1 s | alle tre rader lik README (0,476 / 0,779 / 0,828, gulv 0,294 / 0,269) |
| 5 robusthet | `python3 -I arbeid/oppgave_2144/robusthet_frossen.py --ut /tmp/robust_2180.md` | 45 s | tabellen er identisk med `c1_robusthet_frossen.md` (diff gir bare smed2s kommentarseksjon, som er håndskrevet). README-tallene stemmer: 0,375/99,4 %, 0/100 %, 0,476/100 %, 0,467/100 %, 0,455/100 % |
| 6 frysvakt grønn | `C1_FRYS=/tmp/frys_2180.json c1_frys.py frys`, så `fremmed.sh /tmp/provekald_2180b` | 32 s | «FRYSVAKT GRØNN: 9 filer», HOVEDTALL 0.476190, tallvakta grønn |
| 7 frysvakt rød | `C1_FRYS_ROT=<rot uten filer> fremmed.sh /tmp/provekald_2180c`, og `sjekk --rot` med én linje lagt til i kjor_agent.py | <1 s | utgang **4**, ingen kopi laget. Den endrede fila meldes som «ENDRET (frosset 638d5fea1585, nå 53e95a1c802d)» |

Testfrysen lå i /tmp og er slettet. `state/c1_frys.json` er ikke laget, så den ekte frysen kl. 16 er urørt.

## Hindre for en fremmed leser
Ingen stopper kjøringen. Disse kan forvirre (smed2 #2179 eller den som eier tekstene):
1. **`treffsikkerhet.py`, `menneske_tabell.py` og `robusthet_frossen.py` blir ikke kopiert av fremmed.sh.** Steg 3–5 går bare fra landsbymappen. TREFFSIKKERHET.md sier «Slik regnes tallene på nytt (fra kald start)» men bruker `cd <repo>/...` og pakkas lagrede CSV, ikke kopiens. Fiks: legg `treffsikkerhet.py` og `c1/menneske_tabell.py` til i `kopier`, og skriv kommandoen mot `/tmp/fremmed/ut/`. Eller fjern «fra kald start» i overskriften.
2. **Tid:** README sier «Agenten brukte 22 s» (28 s med uv sync). Prøven brukte 27 s for agenten og 32–45 s totalt. Skriv «under 1 min».
3. **Størrelse:** README sier 159 MB, kopien er 162 MB. Det er ubetydelig, men sett «ca. 160 MB».
4. **Forvirrende linjer i utskriften:** v2-blokken viser `streng MOT: TP 0 FP 0 FN 0 … F1 0.0000` og `SCORE 0.481752` to ganger, før HOVEDTALL. README forklarer SCORE, men ikke «streng MOT 0». En jurymedlem kan lese det som at MOT gir F1 0. Fjern linja eller merk den «(ikke brukt)».
5. **`maaler_offisiell_v3.py baseline` (TREFFSIKKERHET.md) skriver tre MOT-linjer** (følg styret 0, alle MOT 0,073, en tredje regel 0,066), uten navn ved hver linje. Kommentaren nevner bare «følg styret: TP 0 FN 58».
6. **Krav:** README sier «krever bare `uv`». Frysvakta og tallvakta kjører også `python3` fra systemet (/usr/bin/python3 på macOS). Skriv «uv og python3».

Lenkene og stiene i README, EN_SIDE og TREFFSIKKERHET finnes alle. Unntaket er `state/opplastet/..._real_votes.csv`, som er forkortet med vilje.

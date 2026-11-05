# Case 1 (#2622): STÅR-reserven tørrkjørt i kald kopi: GRØNN

Dato 05.11 kl. 17:15–17:20, smed3. Pakken og frysen er ikke rørt.

## Hva som ble gjort
1. Kald kopi: `state/levering/c1_gronn/SISTE_GRONNE.zip` (= `jurypakke_c1_1647_83f152c.zip`, sha 1e0260d3…) pakket ut i `/tmp/staar_kald/`.
2. `lag_staar.py --sjekk`: README.md LIK, kravrespons.md LIK (STÅR-tekstene er i takt med gjeldende BYTT-tekst).
3. STÅR-tekstene fra `arbeid/hack/c1/reserve_staar/` kopiert inn i kopiens `arbeid/hack/c1/leveranse/` (sha README 648d7a28…, kravrespons c0a4dd2a…).
4. `sh KJOR.sh` fra kopiens rot. Full utskrift: `state/rapporter/c1_staar_reserve_torrkjort_KJOR_ut.txt`.

## Resultat av kjøringen
- exit 0. Frysvakt GRØNN: 15 frosne filer like FROSNE_SHA256.txt (leveranse-tekstene er ikke i frysen, så bytte av dem rører ikke frysvakta).
- HOVEDTALL F1 MOT mot styret (v3 --score mot): **0.476190**, P 0.4412 R 0.5172, TP 30 FP 38 FN 28, 58 MOT i fasit, 66 avvik.
- Tallvakt GRØNN: 18 filer, 170 påstander om hovedtallet stemmer, 0 avviker.
- Tid: uv sync 1 s, kjøring 55 s (34 s agent).

## Tall-for-tall i STÅR-tekstene mot kjøringen
| påstand i README/kravrespons | kjøringen | |
|---|---|---|
| F1 MOT 0,476 / 0.4762 | 0.476190 | LIK |
| P 0,44, R 0,52 | 0.4412 / 0.5172 | LIK |
| TP 30 FP 38 FN 28 TN 1443 | 30/38/28, TN = 1539−96 = 1443 | LIK |
| 1539 med fasit, 58 MOT, 66 avvik | 1539 / 58 / 66 | LIK |
| accuracy 95,7 %, følg styret 96,2 % | 1473/1539 = 95,71 %, 1481/1539 = 96,23 % | LIK |
| til menneske 188 av 1578 (11,9 %), 183 av 1539 | 188/1578, 183/1539 (11.9 %) | LIK |
| 127 usikre + 60 ukjent selskap + 1 instruks | agent.csv: 117 usikre + 10 usikre∧ukjent = 127, 60 ukjent, 1 instruks = 188 | LIK |
| val 2025 0,520 | VAL 2025 F1 0.5217 | LIK |
| sidetall SCORE 0,482 / 0.481752 | SCORE 0.481752 | LIK |
| utskriftsblokk (TP 33 FP 38 FN 33, P 0.4648, F1 0.4818, PR-AUC 0.5245) | identisk | LIK |
| real_votes sha 71ba5135…, 13 757 rader | DATA-linja: samme sha, rader 13757 | LIK |
| «15 frosne filer»: ikke påstått i tekstene | – | ingen påstand å sjekke |

Ikke målbart fra KJOR.sh (ett år, én kjøring), kontrollert mot kilden i stedet:
- KI [0,36; 0,59] og rader [0,37; 0,59], sidetall-KI [0,375; 0,580]: bootstrap, dekkes av tallvakta/`tall_tabell.md`, ikke rekjørt.
- Rullende testår repo4 0,5057/0,5309/0,5120 mot frossen 0,4545/0,5143/0,4762, snitt +0,0345, verste år +0,017, KI [−0,005; +0,078], BYTT kl. 17:02, frist 18:45: ord for ord lik `state/rapporter/c1_byttedom_265.md` (tabell linje 21–22, linje 25, 29). 2026-tallet 0,4762 er det samme som kjøringen gir.

## Avvik
- Ingen avvik i tekstene.
- Oppgaveteksten sier «hovedtall F1 MOT 0,4817». Det er feil tall: 0,4817 er den frosne agentens *sidetall* (avvik fra styret inkl. AVSTÅ, kolonnen «SCORE» i byttedommen). Hovedtallet for frossen er 0,4762, og det er det STÅR-tekstene og kjøringen sier. Så sjekken er GRØNN mot 0,4762, ikke mot 0,4817.
- Frys-json (`c1_frys_1600_frossen.json`) har 17 filer, zipens FROSNE_SHA256.txt 15: målerne v2/v3 står ikke i zipens frysliste. Det er slik siste grønne zip alt er pakket, ikke noe STÅR-reserven endrer. Noteres bare.

## Konklusjon
GRØNN. Legges STÅR-tekstene inn i siste grønne zip, kjører KJOR.sh grønt fra fersk mappe og alle tall i tekstene stemmer med kjøringen og frysen. Ta-i-bruk-oppskriften i `reserve_staar/LES.md` holder (cp inn, så tallvakt/frys_fasit/pakk_jury).

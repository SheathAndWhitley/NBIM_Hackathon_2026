# Case 1: feilanalyse av MOT mot styret på val-år for frossen repo4 (#2866, smed2)

**Data:** bare val-filene `arbeid/oppgave_2567/repo4_{2023,2024,2025}_val.csv`, altså NBIMs år 2022, 2023 og 2024. Testårene er ikke brukt. NB: val-året 2024 er også teståret for repo4_2024. Tallene for 2024 er derfor ikke nye tall for den testen.
**Definisjon:** som i `maaler_aar.py --score mot`. Fasit: nbim_vote MOT og against_board 1. Svaret er MOT når anbefaling=1 og styret ikke sier MOT.
**Samlet:** TP 122, FP 182, FN 138, F1 0,4326 (0,4378 / 0,3535 / 0,5212). Tallene stemmer med måleren for hvert år.
**Gjenskap:** `cd arbeid/oppgave_2866 && python3 -I feil.py` (skriver feil_rader.csv), `python3 -I sistemote.py 5`, `python3 -I person.py`.

## De 5 største feilgruppene
Gruppene overlapper. Andelen er regnet av alle FN (138) eller alle FP (182).

| # | gruppe | type | antall | andel | TP i gruppa | hva som skjer |
|---|---|---|---|---|---|---|
| 1 | Første MOT i selskapet: NBIM har aldri stemt MOT der før (bare FOR før eller ingen historikk) | FN | 68 | 49,3 % av FN | 4 | Modellen lever på historikk og finner nesten aldri en første MOT. Største delgrupper: US DIRECTOR_ELECTION 18, China OTHER_MGMT 7, Japan DIRECTOR_ELECTION 7. |
| 2 | Volkswagen DISCHARGE 2022–23 | FP | 61 | 33,5 % av FP | 9 | NBIM stemte MOT på all ansvarsfrihet 2019–21, men gikk over til FOR fra 2022 (2022: 9 MOT av 32, 2023: 0 av 38). Modellen henger igjen på flertallet av gamle år. I 2024 har den lært det (32 TN). |
| 3 | NBIM har stemt MOT i selskapet før, men siste stemme på samme tekst var FOR | FN | 32 | 23,2 % av FN | 1 | NBIM bytter hvem de stemmer mot. Kinder Morgan 2024 står for 14 FN og 12 FP: MOT gikk fra én gruppe styremedlemmer til en annen. |
| 4 | Siste stemme på samme tekst var MOT, men NBIM stemte FOR nå | FP | 49 | 26,9 % av FP | 79 | Det er den andre siden av gruppe 3. Kinder Morgan 12 og ORLEN 10. Signalet er sterkt (79 TP), så det skal ikke fjernes, bare veies ned der selskapet bytter. |
| 5 | Siste stemme på samme tekst var AVSTÅ | FP | 15 | 8,2 % av FP | **0** | Det gjelder TCC 7, DFDS 3, Lundbeck 4 og ASMedia 1. Når NBIM avsto sist, avsto de igjen eller stemte FOR. Ikke én av disse ble MOT. |

Andre mønstre: 67 % av FN (92) ligger i møter der modellen ikke flagger noe i det hele tatt. 59 % av FP (107) ligger i møter som har ekte MOT, så modellen treffer møtet men flagger for mange saker i det. Forslagsstiller sier ingenting: alle feil gjelder ledelsens forslag (proponent=Management, mgmt_rec FOR). Datasettet har ingen sektor-kolonne. I stedet viser marked: DM står for 80 % av FP, og EM for 47 % av FN.

## Trekk som kunne rettet dem
Alle er målt bare på val. Ingen er målt på test.
1. **«avstå»-regel (gruppe 5):** fjern MOT-flagget når NBIMs siste tidligere stemme på samme selskap og tekst var AVSTÅ. På val går F1 fra 0,4326 til **0,4444** (0,4378→0,4513, 0,3535→0,3684, 0,5212→0,5244). Den er bedre alle tre år og koster 0 TP. Den er beslektet med «av» (#2701), men er et eget og nytt tilfelle. Kan legges oppå «av» og bør prøves som natt-kandidat med REGEL.md før måling.
2. **Nylighetstrekk for regimeskifte (gruppe 2 og 4):** andel MOT i *siste* møte for samme selskap og forslagstype, og endringen fra snittet over tidligere år, som nye features i repo4. Den enkle regelversjonen («siste møte alle FOR, ≥K saker, fjern flagg») er testet og *hjelper ikke*: K=1 gir 0,4117, K=3 gir 0,4150, K=5 gir 0,4388 (2023 blir dårligere). Den fanger ikke VW 2023, fordi 2022-møtet fortsatt hadde 9 MOT. Det må derfor være en vektet feature og ikke en hard regel.
3. **Første MOT (gruppe 1), egen modell uten historikk:** for selskaper uten MOT før trengs signal fra teksten og fra typen alene, for eksempel en egen kalibrert terskel eller et eget hode for «ingen MOT-historikk» med US-styrevalg, kinesiske OTHER_MGMT/RPT/ARTICLES og japanske styrevalg som fokus. Ellers er dette 49 % av FN, og modellen står på 4 TP.

Lukket i denne analysen: en person-nøkkel (etternavn + selskap på tvers av DISCHARGE og styrevalg) fjerner bare 6 FP (0,4326 → 0,4373). Den fanger ikke VW, fordi de samme personene faktisk hadde MOT før 2022.

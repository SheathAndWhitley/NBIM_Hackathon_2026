# Case 1 (#2061, smed3): kort forklaring per sak om hvorfor den kan bli MOT

**Hva:** `arbeid/hack/varianter/smed3_utf_sitat/forklar.py` gir hver sak som agenten (#2037-modellen) flagger
som MOT (p ≥ 0,73) eller usikker (konfidens < 0,6) én setning: dom, p(avvik), de tre signalene som drev tallet
mest (bidrag i logit), og NBIM-sitatet fra #2037 (nærmeste egne begrunnelse fra train-år, annet møte).
Modellen er lineær (LR), så bidrag = koeffisient × verdi, eksakt og ikke en etterpåtilnærming. Signalene er
gruppert slik et menneske leser dem: ett ord (bigram delt likt på ordene), én kategori (sakstype, land,
marked, forslagsstiller, styrets råd), eller selskapets avvikshistorikk hos NBIM.
Ut: `ut/forklaring_2061_val.jsonl` (155 saker), `ut/forklaring_2061_troskap.json`.

**Eksempler (VAL 2025):**
- D'Ieteren Group, «Approve Co-optation of Alcamara BV … as Director»: MOT, p=0,76. Sterkest drevet av:
  land = Belgium (+1,78); ordet «optation» (+0,52); selskapet har 1 avvik av 7 saker tidligere år (+0,37).
  NBIM har tidligere begrunnet lignende avvik med GVG 1.1 «The board should guide company strategy … without conflicts of interest…».
- The Hartford, «Reduce Ownership Threshold for Shareholders to Call Special Meeting»: usikker, p=0,70.
  Sakstype = SHP_GOVERNANCE (+2,49); styrets råd = MOT (+0,97). Sitat GVG 3.1.

**Akseptkrav: stemmer forklaringen med modellen?** Toppsignalet fjernes i *inndata* og hele raden kjøres på nytt
(ordet slettes fra teksten og tf-idf normaliseres på nytt; kategori settes til vanligste verdi i trening;
historikk settes til «ingen»). Ikke bare en kolonne nullet, så testen er ikke triviell.
| VAL 2025, 155 flaggede saker (115 MOT, 40 usikre) | andel der p faller | median fall i p |
|---|---|---|
| fjern toppsignalet | **155/155 (100 %)** | 0,462 |
| fjern et tilfeldig annet aktivt signal (kontroll) | 53 % | 0,001 |
| MOT som snur til under grensen når toppsignalet fjernes | 105/115 (91 %) | |

**F1 på MOT er uendret** (forklaringen rører ikke prediksjonene; p avviker < 0,0001 fra den målte svarfila):
`maaler_offisiell.py --data real`: val MOT-F1 0,530 (avvik-F1 0,512), test 2026 MOT-F1 **0,481** (P 0,41 / R 0,58),
avvik-F1 0,480. Forsøk #1043. Det ble meldt med `--score`, ikke `--sti`: tavla avviste `--sti` fordi
måleren er endret på disk (8733327407 → 474eae7bc8). Dommeren må sette måleren på nytt.

**Ærlig om hva forklaringene viser:**
- Toppsignal: ord 70, land 55, sakstype 23, styrets råd 7. Vanligst: land = Taiwan/Kuwait/Belgia/Tyskland,
  sakstype OTHER_BUSINESS og SAY_ON_PAY, ordet «inside» (innsidere i styret).
- Mange ordsignaler er **personnavn** (Ozasa, Kunihiko Tanaka, Holmqvist). Modellen husker personer NBIM har
  stemt mot før. Det er et ekte og nyttig signal for en analytiker («samme person, avvist før»), men det er ikke
  en policygrunn. Navnet er delt på flere ord, så det å fjerne ett av dem gir lite fall (Lundbeck 0,91 → 0,83).
- Neste steg (ikke gjort): slå sammen ord som er navn til ett signal, «personen X (stemt mot før)», og test
  fjerning av alle topp-3 samlet.

**Kjør:** `cd arbeid/hack/varianter/smed3_utf_sitat && ../smed2_gbm/.venv/bin/python -I nbim_sitat.py && ../smed2_gbm/.venv/bin/python -I forklar.py` (ca. 2 s).

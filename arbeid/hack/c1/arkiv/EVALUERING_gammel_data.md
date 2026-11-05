# Case 1: ærlig evaluering (dommer2, #1979, 05.11 kl. 11:45, før modellfrys)

Hvert tall under står på forsøkstavla (`uv run python tavle.py forsok-list --alle`) med forsøks-id `#nnn`.
Tall merket «avledet» er regnet fra prediksjonsfilene til de oppgitte forsøkene med `arbeid/oppgave_1979/boot.py`.
**Kapittelet oppdateres etter modellfrys kl. 16.**

## 1. Måleren
- Hovedmåler: `python3 -I arbeid/hack/c1/maaler.py PRED.csv --fasit arbeid/hack/c1/data_v3/fasit.csv`.
  - Tavle-sha **cb9243ddee** (#1969, test) og **5707495ef8** (#1979, val).
  - Kl. 11:19 fikk målerfila split-argumenter (#1974), så gammel sha 823c9610fe ble ugyldig. Målelogikken er uendret: #984 og #994 er samme fil og gir begge 0,383275. #990 og #993 er samme fil og gir begge 0,465753.
- Hovedtall: F1 på **avvik fra styret**, der NBIM stemmer MOT et forslag styret anbefaler. Sekundært: PR-AUC. Accuracy rapporteres, men brukes aldri alene.
- Data: NBIMs egne N-PX-stemmer (CIK 1374170). Det er **bare amerikanske say-on-pay-forslag**, altså ingen styrevalg og ingen aksjonærforslag (`state/rapporter/hack_c1_maaler_v3_nbim.md`).
- Lekkasjevern: `managementRecommendation` er «med/mot ledelsen», altså selve fasiten. Feltet leses aldri, og styret utledes fra kilden (ISSUER → FOR). Måleren nekter å kjøre hvis fasitkolonner dukker opp i test_input.

## 2. Tidssplitt og basisrate
| sett | periode (møter) | forslag | avvik | basisrate |
|---|---|---|---|---|
| train | N-PX 2024 (07.2023–06.2024) | 1631 | 149 | 9,1 % |
| val | N-PX 2025 (07.2024–06.2025), trent på 2024 | 1506 | 136 | 9,0 % (#995: PR-AUC 0,0903) |
| **test** | N-PX 2026 (07.2025–06.2026) | **1246** | **129** | **10,4 %** (#989: PR-AUC 0,1035) |

Splitten krever at alle treningsmøter ligger før testmøtene. Selskaper går igjen fra år til år (1121 av 1225 testselskaper finnes i train). Det er bevisst: fjorårets stemme er offentlig når årets stemme avgis.

## 3. Grunnlinje og gulv
| form | P | R | F1 | PR-AUC | acc | forsøk |
|---|---|---|---|---|---|---|
| følg styret (alltid FOR), test | 0 | 0 | **0,000** | 0,1035 | 0,897 | #989 (#983) |
| følg styret, val | 0 | 0 | 0,000 | 0,0903 | – | #995 |
| **gulv: MOT hvis NBIM stemte MOT på selskapet tidligere**, test | 0,348 | 0,426 | **0,383** | 0,328 | 0,858 | #994 (#984) |
| gulv, val | 0,387 | 0,338 | 0,361 | 0,212 | – | #996 |

Accuracy-fella: å følge styret gir 89,7 % riktige på test (#989) og finner null avvik. En ettlinjes historikkregel (#994) er det ærlige nivået å slå.

## 4. Formene, test 2026
| form | P | R | F1 | PR-AUC | acc | forsøk | val F1 (forsøk) |
|---|---|---|---|---|---|---|---|
| **smed2 lgbm v3: NBIM-historikk + Vanguards publiserte stemmer + SEC lønn/TSR** | 0,567 | 0,395 | **0,466** | **0,441** | 0,906 | #993 (#990) | 0,350 (#997) |
| arkitekt #1970 selskapsnivå: NBIM-historikk + Vanguards MOT-andel (logit) | 0,422 | 0,380 | 0,400 | 0,376 | 0,882 | #992 | se pkt. 5 (#998) |
| gulvet (referanse) | 0,348 | 0,426 | 0,383 | 0,328 | 0,858 | #994 | 0,361 (#996) |
| smed2 #1949 lgbm, første versjon (Vanguard-trekk) | 0,269 | 0,411 | 0,325 | 0,262 | 0,823 | #987 (#985) | – |
| smed3 #1950 sitatagent v5 | 0 | 0 | 0,000 | 0,1035 | 0,897 | #988 (#986) | 0,362 (#999) |

Ruting til menneske (konfidens < 0,6), smed2 v3 (#993): 58 saker (4,7 %), og 25 av dem er ekte avvik. Blant sakene som ikke rutes har avvikene presisjon 0,81 og recall 0,25.

## 5. Er forbedringen ekte? (avledet, parret bootstrap, 2000 trekk, frø 0)
| sammenligning | ΔF1 | 95 % KI | andel > 0 | filer |
|---|---|---|---|---|
| smed2 v3 − gulv, **test** | +0,083 | [+0,004; +0,166] | 0,98 | #993 vs #994 |
| smed2 v3 − gulv, **val** | −0,010 | [−0,104; +0,088] | 0,42 | #997 vs #996 |
| arkitekt − gulv, test | +0,017 | [−0,040; +0,070] | 0,73 | #992 vs #994 |

Overlapp på de 129 test-avvikene (avledet fra #993 og #994): begge fanger 35, bare smed2 16, bare gulvet 20, ingen av dem 58.

**Ærlig lesning:**
- smed2 v3 slår gulvet på test med et intervall som så vidt holder seg over null. På val slår modellen **ikke** gulvet (0,350 mot 0,361). Forbedringen er altså ikke stabil på tvers av år.
- smed2 v3 ble laget etter at testtallene for gulvet var kjent (#984, kl. 11:14). Vi kan ikke utelukke at valg av trekk er påvirket av test. Det ærlige tallet å love er derfor **«på nivå med gulvet til litt over»**, ikke 0,47.
- Arkitektens form er ikke skilt fra gulvet (KI over null). #998 på val er en terskelfeil: alt ble predikert MOT, så F1 er 0,166 mens PR-AUC er 0,261. Valfila er ikke terskelsatt slik testfila er.
- 58 av 129 avvik (45 %) fanges av ingen av formene. Det er grensen for hva historikk og andre fonds stemmer kan forklare.
- Gulv og modell finner delvis ulike saker (16 mot 20). En kombinasjon (#1978) er derfor verdt å måle, men den må velges på val og ikke på test.

## 6. Hva som feilet, og hvorfor
1. **Måler v0/v1 på Vanguard-data (sha bdad4444d1):** feltet `ledelsen` var Vanguards «med/mot ledelsen», altså lekkasje. Med feltet gir «følg styret» 0,357 (#964), uten lekkasje gir den 0,839 (#968). Alle formene havnet på eller rett over baseline (#966 0,839, #970 0,860). MOT-F1 på Vanguard-data måler bare at aksjonærforslag får MOT.
2. **Måler v2 (sha 52292737df), avvik på Vanguard:** bare 22 positive. Én sak flytter F1 med ca. 0,05. smed3 0,24 (#976, #981, tp 2 av 18 ISSUER-MOT) og smed2 0 (#978, #979). For lite til å skille formene, så v2 er bare sekundær.
3. **smed3 sitatagent på v3:** 0 på test (#988) mot 0,362 på val (#999). Kalibreringen på train 2024+2025 slår av `presedens_pay`-regelen. Regelen virker, men terskelen er ustabil. Rettes i #1959. Kald start avvek også (`data/def14a` følger ikke med koden, se `state/rapporter/dommer_c1_nbim_rescore.md`).
4. **smed2 første versjon (#987):** under gulvet. Trekkene var laget for Vanguard-typer (direktør, aksjonærforslag) som ikke finnes i NBIMs N-PX.
5. **Selvrapporterte tall som ikke gjelder:** smed2 3-klasse 0,408 (#982) er målt på egen fasit (dataF), ikke på v3. Speiderens historikkregel 0,153 ble avvist av måleren (UGYLDIG). Ingen av dem brukes.
6. **Casens 93–94 % «følg styret»** lar seg ikke reprodusere på N-PX. Vi får 89,7 % (#989), fordi N-PX bare dekker amerikansk say-on-pay, der NBIM er strengere.

## 7. Begrensninger juryen skal vite om
- Testsettet består bare av say-on-pay. Styrevalg og aksjonærforslag er ikke målt på NBIMs egne stemmer.
- Ett testår, 129 positive. Én sak flytter F1 med ca. 0,005.
- Lekkasjesjekken av smed2 v3 sine eksterne trekk (Vanguards stemmer «publisert før møtet», SEC Pay-vs-Performance) er ikke dommerverifisert ennå. Gulvet sjekkes i #1976.

## Til oppdateringen kl. 16
Kjør `tavle.py forsok-list --alle | grep -E "cb9243ddee|5707495ef8"` og ta inn nye forsøk. Kjør så `python3 -I arbeid/oppgave_1979/boot.py <fasit> <modell> <gulv>` for test og val. Den frosne modellen skal ha **både** et test- og et val-forsøk.

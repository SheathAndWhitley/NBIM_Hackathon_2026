# Case 1: konfidens som sender usikre say-on-pay-saker til et menneske (smed2, #1955)

**Kort fortalt:** Hvis maskinen sender de 10 % av sakene som ligger nærmest beslutningsgrensen til et menneske, stiger MOT-presisjonen på sakene den avgjør selv fra 0,38 til 0,50 på 2026-test. Recall stiger fra 0,57 til 0,63. 22 av 129 MOT-saker (17 %) havner hos mennesket. Alt ble låst på val 2025 før test ble kjørt én gang.

## Metode (alt låst på val før test)
- Modell: smed2 v3 fra #1949 (`train_v3.py`, LightGBM, snitt av 5 frø, samme features). Ingen lån.
- Val: trent på N-PX 2024 og predikert på 2025 (1506 saker, 136 MOT). Test: trent på 2024+2025 og predikert på 2026 (1246 saker, 129 MOT).
- Kalibrering: isotonisk regresjon fra rå score til P(MOT), tilpasset på val 2025. På test er snittet av p 0,111 mot faktisk MOT-andel 0,104, og ECE (10 bøtter) er 0,013. Kalibreringen holder seg altså på et nytt år.
- Beslutningsgrense: den F1-beste på val (rå score 0,203, kalibrert p 0,151).
- Ruting, strategi A («rundt grensen»): saken går til et menneske når |logit(score) − logit(grense)| ligger innenfor et bånd. Båndbredden er satt slik at X % av val-sakene rutes. Båndet brukes uendret på test, så den faktiske rutingsandelen på test blir 4,7 / 10,0 / 19,2 %.
- Strategi B («mest MOT-aktige først», altså høyest min(p, 1−p)) ble også prøvd på val og forkastet der. Den sender bare saker maskinen allerede ville flagget. Maskinens F1 faller da fra 0,43 til 0,16 ved 10 %, og systemets recall øker ikke.

## Tabell: 2026-test (val 2025 i parentes)
| ruting | rutet | MOT hos menneske | MOT-presisjon, maskinens saker | MOT-recall, maskinens saker | systemets recall* |
|---|---|---|---|---|---|
| 0 % | 0 | 0 av 129 | 0,379 (0,365) | 0,574 (0,507) | 0,574 |
| 5 % | 58 (4,7 %) | 11 av 129 = 9 % (10 av 136) | 0,436 (0,391) | 0,610 (0,484) | 0,643 |
| 10 % | 125 (10,0 %) | 22 av 129 = 17 % (29 av 136) | 0,500 (0,416) | 0,626 (0,486) | 0,690 |
| 20 % | 239 (19,2 %) | 38 av 129 = 29 % (55 av 136) | 0,560 (0,500) | 0,615 (0,469) | 0,729 |

\* Systemets recall forutsetter at mennesket avgjør de rutede sakene riktig, så det er en øvre grense.

Bootstrap på test (2000 trekk, 95 %):
- 5 %: presisjon 0,36–0,51, recall 0,52–0,70, andel av MOT-sakene hos menneske 4–14 %.
- 10 %: presisjon 0,41–0,58, recall 0,54–0,72, andel hos menneske 11–24 %.
- 20 %: presisjon 0,46–0,66, recall 0,51–0,72, andel hos menneske 22–37 %.

Kurven (0–30 %, test heltrukket, val stiplet): `state/rapporter/case1_ruting.png`.

## Ærlige forbehold
- **Med denne grensen er tallet uten ruting lavere enn i #1006.** F1-grensen valgt på val gir F1 0,457 over alle sakene på test. Regelen fra #1006, 1,25 × basisraten, ga 0,509, men den ble ikke valgt på val på samme måte. SCORE i forsøk #1017–1019 er derfor 0,457, den samme for alle tre rutingsnivåene: måleren regner SCORE over alle sakene, også de rutede. Rutingsgevinsten står i linjene «rutet» og «ikke-rutet».
- **Gevinsten er større på test enn på val.** På val stiger presisjonen 0,37 → 0,42 → 0,50 ved 0 / 10 / 20 %, mens recall ligger flatt på cirka 0,48. Riktig forventning er altså presisjon +0,05 til +0,12 og en recall som holder seg, ikke testtallene alene.
- **Ruting koster dekning.** Mennesket må faktisk se på de rutede sakene. Ved 10 % er det 125 saker i året, og 22 av dem er MOT.
- Konfidens-kolonnen i `pred_rut*.csv` er satt til 0,5 for rutede saker, slik at måleren (grense 0,6) teller dem riktig. For de andre er den kalibrert sikkerhet med gulv på 0,6. Den er et rutingsflagg og ikke en ren sannsynlighet. Den rene sannsynligheten står i p_avvik.

## Steg 2: skjevt bånd, der mennesket kontrollerer maskinens svakeste MOT-flagg
Båndets senter ble forskjøvet c logit-enheter fra grensen (c fra −2 til +1 i steg på 0,25). c ble valgt på val etter **system-F1**. System-F1 er maskinens MOT-flagg utenfor båndet pluss de MOT-sakene mennesket får, og det forutsetter at mennesket avgjør dem riktig, så det er en øvre grense. Test ble kjørt én gang (`ruting_skjev.py`, `ruting_skjev.txt`).

| ruting | c* (val) | system-F1 val (c=0) | system-F1 test (c=0) | MOT hos menneske | maskinens P / R | systemets recall |
|---|---|---|---|---|---|---|
| 5 % | +0,25 | 0,515 (0,470) | 0,554 (0,544) | 10 av 129 | 0,50 / 0,54 | 0,574 |
| 10 % | +0,75 | 0,630 (0,559) | 0,658 (0,625) | 36 av 129 | 0,63 / 0,41 | 0,574 |
| 20 % | +1,00 | 0,773 (0,697) | 0,827 (0,704) | 74 av 129 | 0,86 / 0,35 | 0,721 |

- Både på val og på test lønner det seg å legge båndet over grensen. Mennesket bør altså **bekrefte maskinens usikre MOT-flagg** (fjerne falske MOT), ikke lete etter MOT-saker som er oversett blant FOR-sakene. Ved 5 og 10 % øker ikke systemets recall; hele gevinsten kommer fra presisjon.
- Ved 20 % ligger c* på kanten av rutenettet (+1,0), så optimum kan ligge enda høyere. Det er ikke testet, for å holde test urørt.
- Valget mellom symmetrisk og skjevt bånd avhenger av hva brukeren vil: symmetrisk gir maskinen høyest recall på egen hånd, skjevt gir best kombinert system når mennesket er pålitelig.

## Hva slags saker havner hos mennesket (test, 10 %, symmetrisk bånd; `ruting_hvem.py`)
| gruppe | n | MOT-andel | NBIM stemte MOT på selskapet før | fusjons-/golden parachute-forslag | uten NBIM-historikk |
|---|---|---|---|---|---|
| rutet til menneske | 125 | 0,18 | 0,25 | 0,16 | 0,10 |
| maskinen sier MOT | 134 | 0,50 | 0,71 | 0,13 | 0,13 |
| maskinen sier FOR | 987 | 0,04 | 0,03 | 0,01 | 0,08 |

De rutede sakene er de med **blandede signaler**. Sjelden har NBIM en MOT-historikk på selskapet å lene seg på, mens fusjonsrelatert lønn (golden parachute) er 16 ganger så vanlig som blant FOR-sakene. Eksempler på rutede MOT-saker: Pacific Premier, Synovus og Comerica (alle med fusjonsrelatert lønn), Nextracker og Microchip. Dette passer med at agenten bør sitere retningslinjene om fusjonsrelatert lønn i nettopp disse sakene.

## Anbefaling til agenten
10 % ruting rundt grensen. Det gir det tydeligste presisjonshoppet per sak mennesket må se på (val 0,37 → 0,42, test 0,38 → 0,50) og en arbeidsmengde på cirka 125 saker i året. Kan mennesket ta 20 %, stiger presisjonen videre til 0,56. Er målet best mulig kombinert system, og kan vi stole på at mennesket avgjør riktig: bruk det skjeve båndet (c = +0,75 ved 10 %). Da ser mennesket maskinens svakeste MOT-flagg, og system-F1 blir 0,66 på test.

## Filer og forsøk
- Kode: `arbeid/kandidater/smed2_c1_mot/ruting.py` (kjøres på cirka 3 s) og `plot_ruting.py`.
- Data: `ruting_kurve.csv`, `ruting_info.json` (grenser og bånd) og `pred_rut{5,10,20}.csv`.
- Forsøkstavla: #1017, #1018 og #1019, målt med måler cb9243ddee (v3-test, samme som #1006).

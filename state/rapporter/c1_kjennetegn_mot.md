# Case 1: hva har stemmene der NBIM gikk mot styret felles (arkitekt, #2074, ordre #234)

Data: real_votes, train+val (2019–2025), injeksjonsrader tatt ut. **Test 2026 er ikke lest.** 11 785 saker, 678 MOT (5,8 %).
Kode: `arbeid/oppgave_2074/kjennetegn.py` (kjøres med `python3 -I ... state/opplastet/20261105_114241_real_votes.csv`), og hele utskriften ligger i `ut.txt`.
KP: forventet val 2025 med 1909 rader og 103 MOT (c1_feilanalyse_mot), fikk 1909 rader og 103 MOT.

## Tabeller (n = antall saker, rate = andel MOT)
| Sakstype | n | MOT | rate |
|---|---|---|---|
| Andre saker på møtet (OTHER_BUSINESS) | 38 | 38 | **1,00** |
| Ansvarsfrihet (DISCHARGE) | 671 | 114 | **0,17** |
| Vedtektsendring | 282 | 31 | 0,11 |
| Say-on-pay (årlig) | 489 | 42 | 0,086 |
| Nærstående transaksjoner | 152 | 12 | 0,079 |
| Styrevalg | 5803 | 322 | 0,055 (men 47 % av alle MOT) |
| Revisor, utbytte, regnskap, aksjeplaner, tilbakekjøp | 3 400+ | 43 | ≤ 0,02 |
| Aksjonærforslag (alle typer) | 134 | 42 | 0,31 |

| Land (n ≥ 60) | n | MOT | rate |
|---|---|---|---|
| **Tyskland** | 479 | 133 | **0,28** (ansvarsfrihet 101 av 269) |
| Sveits / Sør-Korea / Taiwan | 493 / 411 / 296 | 43 / 35 / 26 | 0,085–0,09 |
| USA | 2110 | 152 | 0,072 (styrevalg 93, say-on-pay 16) |
| India | 540 | 30 | 0,056 (0,10 i 2025) |
| Kina | 837 | 38 | 0,045 |
| Japan | 2129 | 38 | 0,018 |
| Storbritannia / Hongkong / Malaysia | 913 / 197 / 263 | 3 / 0 / 0 | ≈ 0 |

| Selskapshistorikk (møter strengt før) | n | MOT | rate |
|---|---|---|---|
| MOT før i samme selskap | 5252 | 455 | **0,087** |
| Nytt selskap (ingen tidligere) | 2022 | 130 | 0,064 |
| Bare FOR før | 4511 | 93 | **0,021** (0,012 i 2025) |

| Andre kjennetegn | n | MOT | rate |
|---|---|---|---|
| Styreleder = daglig leder i forslagsteksten | 12 | 7 | **0,58** (alle 12 i India) |
| Øvrige saker | 11 773 | 671 | 0,057 |
| Golden parachute / fusjonslønn (regex) | 2 | 0 | for lite data |
| Årlig say-on-pay | 489 | 42 | 0,086 |

| Klynger per møte | tall |
|---|---|
| Møter med minst én MOT | 350 av 1016 |
| Møter med 3+ MOT | 50 av 1016 (5 %) |
| **Andel av alle MOT som ligger i møter med 3+ MOT** | **328 av 678 = 48 %** |
| MOT-rate når 3+ andre saker i samme møte er MOT | 0,34 (mot 0,034 ellers) |
| Styrevalgsmøter med MOT: snitt andel kandidater stemt mot | 0,36 (64 av 231 møter: halve styret eller mer) |

## Fem funn i vanlig norsk
1. **NBIM gjentar seg selv.** Har NBIM stemt mot styret i et selskap før, er sjansen for MOT fire ganger så høy som når de bare har stemt FOR (8,7 % mot 2,1 %). Nye selskaper ligger midt imellom.
   *Modellen:* ja, dette er det sterkeste trekket. Uten selskapshistorikken faller F1 på test fra 0,48 til 0,37 (c1_mot_ablasjon). Blindsonen er «bare FOR før» (7 MOT på val, 0 truffet).
2. **MOT kommer i klynger.** Halvparten av all MOT (48 %) ligger i 5 % av møtene, nemlig de med 3 eller flere MOT. Typisk straffes hele styret eller flere kandidater samtidig. Når NBIM er misfornøyd med et selskap, stemmer de mot flere saker på samme møte.
   *Modellen:* nei. Å spre modellens egen p utover møtet ble testet og ga lavere F1 (0,52 → 0,28–0,40, c1_feilanalyse_mot). Signalet krever fakta på styrenivå som datasettet mangler.
3. **Noen få sakstyper og land står for mye.** Ansvarsfrihet i Tyskland alene gir 101 av 678 MOT (15 %, rate 38 %). «Andre saker» er alltid MOT (38 av 38). Storbritannia, Hongkong og Malaysia har nesten aldri MOT, og Japan har 1,8 %.
   *Modellen:* ja, gjennom forslagstype, land og tekst. Ablasjonen viser at hvert av dem bidrar lite når historikken er med, fordi historikken allerede fanger det.
4. **Styreleder som også er daglig leder.** Bare 12 saker, alle i India, og 7 av dem er MOT (58 %, ti ganger snittet). Det følger NBIMs uttalte prinsipp om å skille rollene.
   *Modellen:* ikke ennå. Det bygges nå som trekk (#2075 smed3, #2076 smed2). På val gir det +0,03 F1, men n er lite.
5. **Lønn: årlig say-on-pay ja, golden parachute ukjent.** Årlig say-on-pay har 8,6 % MOT (42 av 489, mest USA). Golden parachute og fusjonslønn finnes bare i 2 saker i datasettet, begge FOR, så vi kan ikke si noe om dem.
   *Modellen:* say-on-pay ja (forslagstype og tekst), golden parachute nei, siden det ikke finnes data.

## Forbehold
Tallene er beskrivende og ikke kausale. Små grupper (duality n = 12, aksjonærforslag n = 134) har bred usikkerhet. Klyngetallet bruker alle stemmer i møtet, også de som ikke er kjent når man predikerer. Det forklarer mønsteret, men er ikke et trekk modellen kan bruke direkte.

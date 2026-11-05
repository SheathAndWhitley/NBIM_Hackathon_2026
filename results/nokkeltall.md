# Nøkkeltall

Generert av `python run.py` 05.11.2026 16:43 (commit `8ba8f8c`). **Ikke rediger for hånd.** Alle tall i presentasjon, kravrespons og README skal hentes herfra.

## 1. Data og revisjon

- **Fasit:** `ny_data/real_votes.csv` (NBIMs egne stemmer, API-data fra arrangørene): 13 757 saker, 1 161 møter, 194 selskaper, 2019-01-23 til 2026-09-30.
- NBIM stemte **mot styret i 5,3 %** av sakene med etikett, altså **94,7 % med styret** (2025: 94,6 %). AVSTÅ (68 stemmer) regnes verken som med eller mot styret.
- Teller man AVSTÅ som «ikke med styret», slik NBIM gjør i sin egen statistikk: 94,4 %. NBIM oppgir selv 94 % for 2025.
- **`npx_votes.csv` er feilmerket:** styrets anbefaling (`mgmt_rec`) speiler NBIMs stemme. 2 538 ledelsesforslag står med «styret anbefaler MOT» (NBIM stemte MOT på 1 770). Filens egen etikett gir 96,0 % med styret; med rettet styreanbefaling blir det 93,8 %, på linje med NBIMs egne data.
- **Krysssjekk mot NBIMs egen SEC-filing** (say-on-pay i USA): `real_votes.csv` stemmer i 97,7 % av 87 saker. `npx_votes.csv` fanger bare 11 av 58 MOT-stemmer.
- `npx_votes.csv` har 141 instrukslignende sakstekster (brukes i motstandstesten).

## 2. Hele stemmeseddelen (hovedresultat)

Mål: stemte NBIM **mot** styrets anbefaling? (MOT når styret sier FOR, FOR når styret sier MOT.)

| Del | År | Saker | Avvik | Andel |
|---|---|---|---|---|
| train | 2019–2023 (trening) | 7 960 | 444 | 5,6 % |
| valid | 2024 (valg av modell og terskler) | 1 882 | 97 | 5,2 % |
| test | 2025–2026 (test, kjørt én gang) | 3 443 | 164 | 4,8 % |

Modell: logistisk regresjon (`logreg(C=3.0,cw=None)`, valgt på 2024 blant 7 kandidater). Én lært modell, ingen håndlagde regler: NBIMs presedens (samme sak/person før) er en variabel med lært vekt. Terskler (valgt på 2024): flagg «NBIM stemmer trolig mot» ved p ≥ 0,300, analytikerkø ved p ≥ 0,027.

**Testresultat 2025–26** (3 443 saker, 164 avvik):

| System | Presisjon | Recall | F1 | PR-AUC | Recall ved 20 % lest | Accuracy |
|---|---|---|---|---|---|---|
| Følg alltid styret | 0,0 % | 0,0 % | 0,00 | 0,048 | 20,0 % | 95,2 % |
| Gjenta forrige beslutning | 65,7 % | 40,9 % | 0,50 | 0,297 | 51,2 % | 96,2 % |
| Flertall per sakstype | 73,9 % | 10,4 % | 0,18 | 0,157 | 29,3 % | 95,6 % |
| **Modell (vår)** | 61,5 % | 34,1 % | 0,44 | 0,392 | 72,1 % | 95,8 % |

- **95 %-intervall for modellen** (bootstrap trukket per selskap): presisjon 51,2 % til 71,6 %, recall 24,8 % til 43,8 %, PR-AUC 0,300 til 0,489, recall ved 20 % lest 62,7 % til 81,4 %.
- **Modell minus «gjenta forrige beslutning»:** PR-AUC 0,098 (0,038 til 0,158); recall ved 20 % lest 20,9 % (14,3 % til 27,6 %); F1 -0,066 (-0,134 til -0,004). Et intervall som ikke inneholder 0 betyr at forskjellen ikke er tilfeldig.
- **Analytikerkø:** analytikeren leser 40,0 % av sakene og fanger 144 av 164 avvik (87,8 %). 20 avvik godkjennes automatisk med styret (bom). Bom per type: styrevalg 7, øvrige ledelsesforslag 5, regnskap 2, aksjeutstedelse 2, say-on-pay 1, fusjon 1, aksjeprogram 1, revisor 1.
- **Kalibrering:** Brier 0,0342 mot 0,0454 for en konstant basisrate (lavere er bedre).
- **Per testår:** 2025: P 66,0 %, R 30,1 %, PR-AUC 0,406; 2026: P 56,8 %, R 41,0 %, PR-AUC 0,396.

**Hvor treffene kommer fra (vær ærlig om dette):**
- 102 testsaker har presedens (NBIM avvek på samme sak eller person før); 67 av dem er avvik nå.
- Modellen flagger 91 saker og treffer 56: 46 har presedens, 10 har ikke. Av de 102 presedenssakene flagges 66.
- 97 avvik har ingen presedens. Modellen flagger 10 av dem, og analytikerkøen fanger 77. (64 er saker/personer NBIM aldri har stemt på før; i 33 fulgte NBIM styret forrige gang.)
- Avvik per land (test): United States 36, Japan 18, India 18, Switzerland 11, Indonesia 11, South Korea 7.

**Valg av modell: hvorfor ingen håndregel** (hvert år trent på årene før; testårene er ikke brukt):

| Valideringsår | Avvik | PR-AUC modell / «presedens først» | Fanget ved 20 % lest: modell / «presedens først» / gjenta forrige |
|---|---|---|---|
| 2021 | 89 | 0,718 / 0,662 | 79,8 % / 79,8 % / 36,0 % |
| 2022 | 103 | 0,356 / 0,409 | 69,9 % / 69,9 % / 50,1 % |
| 2023 | 81 | 0,269 / 0,311 | 64,2 % / 64,2 % / 45,9 % |
| 2024 | 97 | 0,503 / 0,498 | 82,5 % / 82,5 % / 46,3 % |

- Varianten «presedens først» (håndregel: alle saker der NBIM avvek før legges øverst) ga **samme analytikerkø hvert år** og uavgjort PR-AUC (2–2). Den enkleste modellen ble derfor valgt. Ingen av dem svekkes over tid.
- Åpenhet: på testsettet ville varianten sett bedre ut (PR-AUC 0,444, recall 47,0 %), men valg av modell skjer på valideringsår, aldri på testsettet.

**Grunnlinjer for sitering** (riktig GVG-seksjon på de 164 testavvikene der NBIM oppga seksjon; agenten må slå disse):
- Flertall per sakstype: 38,4 % riktig seksjon (40,9 % riktig kapittel).
- Forrige seksjon på samme sak/person: finnes for 42,1 %, og er da riktig i 97,1 %.
- Forrige seksjon, ellers flertall per type: **61,0 %** riktig seksjon.

**Motstandstest for triagemodellen** (injeksjonstekst lagt til i alle testsaker; trenger ingen API-nøkkel):
- `no_plain`: gjennomsnittlig endring i sannsynlighet 0,0144 (maks 0,486); 205 saker byttet rute (andel lest etterpå 45,9 %, de fleste flyttes *inn* i køen); **0 avvik flyttet fra analytikerkø til automatisk godkjenning**; køen fanger 150 avvik etterpå.
- `en_system`: gjennomsnittlig endring i sannsynlighet 0,0490 (maks 0,486); 995 saker byttet rute (andel lest etterpå 68,9 %, de fleste flyttes *inn* i køen); **0 avvik flyttet fra analytikerkø til automatisk godkjenning**; køen fanger 158 avvik etterpå.
- `buried`: gjennomsnittlig endring i sannsynlighet 0,0155 (maks 0,486); 254 saker byttet rute (andel lest etterpå 44,9 %, de fleste flyttes *inn* i køen); **1 avvik flyttet fra analytikerkø til automatisk godkjenning**; køen fanger 149 avvik etterpå.
  (Maks-endringen er stor fordi den kalibrerte sannsynligheten er en trappefunksjon: et lite skift kan krysse et trinn. Gjennomsnittet er det representative tallet.)

## 3. Say-on-pay i USA (dypdykk, NBIMs SEC N-PX + lønn fra møtets egen innkalling)

Sesonger: 2023-24: 1 609 møter, 141 MOT (8,8 %); 2024-25: 1 491 møter, 135 MOT (9,0 %); 2025-26: 1 217 møter, 120 MOT (9,9 %). Trening 2024-25, test 2025-26.

| System | Presisjon | Recall | F1 | PR-AUC | Recall ved 20 % lest | Accuracy |
|---|---|---|---|---|---|---|
| Følg alltid styret | 0,0 % | 0,0 % | 0,00 | 0,099 | 20,0 % | 90,1 % |
| Gjenta forrige beslutning | 45,5 % | 37,5 % | 0,41 | 0,232 | 45,6 % | 89,4 % |
| NBIMs egen lønnsregel | 53,6 % | 67,5 % | 0,60 | 0,556 | 75,8 % | 91,0 % |
| **Modell (vår)** | 55,4 % | 68,3 % | 0,61 | 0,597 | 80,7 % | 91,5 % |

- **Modell minus NBIMs regel:** PR-AUC 0,036 (-0,035 til 0,108), F1 0,014 (-0,018 til 0,046). Ikke signifikant: funnet er at NBIM følger sin egen regel.
- **Policy vs praksis:** over NBIMs terskel (USD 20m, 25m fra 2025) stemte NBIM MOT i 53,6 % (n = 151), under i 2,9 %. 74,3 % av MOT-stemmene ligger over terskelen. CEO-skifte i året: 14,4 % MOT, ellers 8,6 %.
- **Kobling til SEC (utvalgsskjevhet):** 2023-24: uten kobling 235 møter, 9,4 % MOT, med kobling 1374 møter, 8,7 % MOT; 2024-25: uten kobling 137 møter, 11,7 % MOT, med kobling 1354 møter, 8,8 % MOT; 2025-26: uten kobling 60 møter, 10,0 % MOT, med kobling 1157 møter, 9,9 % MOT.

## 4. LLM-agenten

_Ikke kjørt ennå._ Kjøres med API-nøkkel (`python run_agent.py --run`); tallene fylles inn her automatisk.

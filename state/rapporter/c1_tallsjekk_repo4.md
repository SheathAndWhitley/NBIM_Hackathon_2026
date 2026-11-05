# Case 1 (#2624): tallene i jury-tekstene mot repo4-kjøringen i zipen

Zip: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (SISTE_GRONNE, sha fc0dbc55). Pakket ut i `/tmp/speider_2624`, kjørt `sh KJOR.sh` kl. 17:35:
HOVEDTALL 0.512000, TALLVAKT GRØNN. **Men tallvakta sjekker bare påstander om hovedtallet.** Under er hånd-sjekken av de andre tallene.

**Kilde (fasit) fra kjøringen:** måler v3 `--score mot`: TP 32 FP 35 FN 26 (TN 1446), P 0,4776, R 0,5517, F1 0,5120, 58 MOT, 1539 saker med fasit;
avvik inkl. AVSTÅ: F1 0,5294 (66 avvik); `ut/KJORING.txt`: 1578 inn, til menneske 164 (10,4 %), 161 av 1539 (10,5 %), rå grense 0,92321, kalibrert grense 0,232, val-F1 0,5251;
`ut/agent.csv` rutingsgrunner (overlapper): usikker 102, ukjent selskap 70, instruks 1. Accuracy: agent 1478/1539 = 96,0 %, følg styret 1481/1539 = 96,2 %.

| tall i teksten | fil:linje | kilde | stemmer |
|---|---|---|---|
| F1 MOT 0.512000 | README.md (rot):7, 24 | måler v3 | ja |
| SCORE 0.529412 (sidetall avvik) | README.md (rot):27 | måler v3 avvik | ja |
| TP 32 FP 35 FN 26 TN 1446 | README.md (rot):51 | måler v3 | ja |
| p_mot-grense **0,191**, rå grense **0,919** | README.md (rot):39-40 | KJORING.txt: kalibrert 0,232, rå 0,92321 | **NEI** (frossen-tall) |
| F1 0,512, KI [0,40; 0,62], 32 av 58, 35 av 67 falske | leveranse/JURY.md:5, 35, 71 | måler v3 (KI fra kilde) | ja |
| «Tallet er **under målet 0,5**» | leveranse/JURY.md:5 | 0,512 > 0,5 | **NEI** |
| «Den frosne agenten (modell «miks h2»)», tabellrad «Hovedmodell, miks h2» 0,512 | leveranse/JURY.md:9, 16 | levert modell er repo4 | **NEI** (navn) |
| «finner **30** av 58 MOT og overser **28**» | leveranse/JURY.md:24 | 32 / 26 | **NEI** (frossen, ikke merket tydelig) |
| accuracy 96,2 % / 96,0 % | leveranse/JURY.md:28 | utregnet | ja |
| «F1 **0,482** på avvik» | leveranse/JURY.md:29 | måler v3 avvik 0,5294 | **NEI** (frossen) |
| 161 av 1539 (10,5 %), tabellrad repo4 161 | leveranse/JURY.md:34, 47 | KJORING.txt | ja |
| KI **[0,36; 0,59]** | leveranse/JURY.md:72 | samme fil sier [0,40; 0,62] linje 5/35 | **NEI** (intern motsigelse) |
| 18 av 26 bommer ser ingen | leveranse/JURY.md:73 | FN 26 ja; 18 fra kilde | ja (26) |
| 164 av 1578 (10,4 %) | leveranse/JURY.md:78 | KJORING.txt | ja |
| «**127** usikre, **60** ukjent selskap, 1 instruks» | leveranse/JURY.md:78 | agent.csv: 102 / 70 (overlapp), README sier 101/61/1/+1 | **NEI** (frossen) |
| «26 av de **38** falske MOT» | leveranse/JURY.md:82 | FP 35 | **NEI** (frossen) |
| F1 0,512, P 0,478, R 0,552, KI [0,40; 0,62] | ERLIG_EVALUERING.md:6, 33, 71 | måler v3 | ja |
| TP 32 FP 35 FN 26 | ERLIG_EVALUERING.md:38 | måler v3 | ja |
| «Modell: den frosne «miks h2»» | ERLIG_EVALUERING.md:3, 71 | repo4 | **NEI** (navn) |
| «les 0,512 (0,40–0,62), **under målet 0,5**» | ERLIG_EVALUERING.md:53 | 0,512 > 0,5 | **NEI** |
| full modell 0,482 på avvik | ERLIG_EVALUERING.md:7 | ablasjon på frossen; repo4 0,529 | delvis (riktig for frossen, ikke merket) |
| repo4 2026-kolonne 0,512 | ERLIG_EVALUERING.md:86 | måler v3 | ja |
| 0,512, KI, 1539/58, TP32 FP35 FN26, 96,2 % | leveranse/README.md:8-9, 31, 51-52 | måler v3 | ja |
| 164 av 1578 (10,4 %), 161 (10,5 %) | leveranse/README.md:10, 18 | KJORING.txt | ja |
| sidetall avvik 0,529 | leveranse/README.md:17 | måler v3 0,5294 | ja |
| 101 usikre / 61 ukjent / 1 instruks / +1 | leveranse/README.md:17-18 | agent.csv 102/70 overlappende, sum 164 | ja (eksklusiv oppdeling, plausibel) |
| 4,8 s for agenten | leveranse/README.md:58 | kjøring her 35-54 s inkl. trening; ikke målt likt | ikke sjekket |

## Avvik til smed4 (prioritert)
1. JURY.md:5 og ERLIG:53 «under målet 0,5» → «over målet 0,5» (samme som #2658).
2. README (rot):39-40 grenser 0,191/0,919 → 0,232/0,923 (KJORING.txt).
3. JURY.md:29 avvik-F1 0,482 → 0,529 (eller merk «frossen»); JURY.md:82 «38 falske» → 35 eller merk frossen; JURY.md:78 «127 usikre, 60 ukjent» → «101 usikre, 61 ukjent» som README.
4. JURY.md:72 KI [0,36; 0,59] motsier [0,40; 0,62] på linje 5/35.
5. JURY.md:24 «30 av 58 / 28» er frossen: merk tydelig eller bytt til 32/26.
6. Modellnavn «miks h2 / frosne» i JURY.md:9,16 og ERLIG:3,71 → repo4.

Tallvakta (157 påstander, 0 avvik) fanger ikke disse fordi den bare leser hovedtall-påstander.

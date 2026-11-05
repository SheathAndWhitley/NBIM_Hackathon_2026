# Case 1: tallkonsistens i hele pakka (dommer2 #2122)

**Kildesjekk:** `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real --score mot` (måler sha 8b09c36e01), kjørt av meg 05.11:
MOT mot styret TP 30 FP 38 FN 28, **P 0,4412 R 0,5172 F1 0,4762, 58 i fasit**. Avvik (inkl. 5 AVSTÅ): P 0,4648 R 0,5000 F1 0,4818, 66 saker. Hovedtallet stemmer.

Søkt: levering/*.md, levering/demo/ (ingen hovedtall der, bare regelkonfidenser), c1/*.md, c1/leveranse/*.md. Ikke arkiv/ og data. `DEMO_MANUS_npx_utkast.md` er merket utkast for gammel N-PX-modell og er utelatt.

| fil:linje | tall | status |
|---|---|---|
| levering/README.md:6, METODE.md:3-6, JURYSVAR.md:5-11, KRAVRESPONS.md:9-12,55-59,77 | 0,476 / 0,441 / 0,517, KI [0,36; 0,59]; avvik 0,4818 merket sidetall | stemmer |
| c1/leveranse/README.md:7-9,26-31,65,92 | 0,476 P 0,44 R 0,52; råutskrift 0,4818 merket som avvik | stemmer |
| c1/leveranse/BEGRENSNINGER.md:3,7; ERLIG_EVALUERING.md:6; JURY.md:3; kravrespons.md:4 | 0,476 / 0,44 / 0,52 | stemmer |
| c1/JURY_METODE.md:11,26; SVAKHETER.md:4-5 | 58 MOT, 66 avvik, KI 0,36–0,59 / 0,375–0,580 | stemmer |
| METODE.md:44, JURYSVAR.md:8, KRAVRESPONS.md:3,69, BEGRENSNINGER.md:5 | 0,474 / 0,47 / 0,383 | merket som eldre N-PX-modell, ok |
| KRAVRESPONS.md:82 | 0,500 uten sakstype | stemmer med #1109 |
| BESLUTNINGSSTOTTE.md:42 | 58 MOT, 0,476 [0,36; 0,59], avvik 0,48 | stemmer |
| **c1/DEMO_MANUS.md:23** | «(0,48)» som F1 MOT | avvek (avvikstall) → **rettet** til 0,476 |
| **c1/DEMO_MANUS.md:39** | recall 0,50 | avvek → **rettet** til 0,52 |
| **c1/SVAKHETER.md:70-71** | 0.482, P 0.465, R 0.50, 66 AGAINST, CI 0.37–0.58 | avvek → **rettet** til 0.476/0.441/0.517, 58, CI 0.36–0.59 (avvik nevnt som sidetall) |
| **levering/BESLUTNINGSSTOTTE.md:5** | «66 ekte MOT-stemmer» | avvek → **rettet** til «66 avvik (58 MOT)» |
| **BESLUTNINGSSTOTTE.md:24, 54** | «MOT-stemmer … av 66», «23 av 66» | etikett feil (tabellen teller avvik) → **rettet** til «avvik» |
| **BESLUTNINGSSTOTTE.md:59** | «MOT-stemmene (R 0,50, P 0,47)» | avvek → **rettet**: MOT R 0,52 P 0,44, avvik R 0,50 P 0,47 |
| **c1/tall_tabell.md:3,10,12** | «66 stemmer mot styret», #2044 0.482/0.46/0.50 | generert med v2 på avvik → **smed-oppgave #2126** |
| **c1/terskeltabell_ut.md:3** | «MOT=66» | generert, samme feil → **#2126** |

**Merk:** Terskeltabellen i BESLUTNINGSSTOTTE (rad 24–27) er fortsatt målt på avvik, ikke MOT. Etiketten er nå ærlig; ny kjøring med v3 `--score mot` ligger i #2126.
Gjenstår for #1975 (speider, etter frys): DEMO_MANUS-plassholderne {F1_TEST} osv. fylles fra v3 `--score mot`, ikke fra `SCORE`-linja i v2 (0,4818).

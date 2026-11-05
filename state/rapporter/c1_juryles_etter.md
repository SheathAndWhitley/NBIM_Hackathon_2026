# Case 1: jurylesingens 10 funn sjekket mot pakka etter rettingene (speider #2169, 05.11)

Sjekket etter at smed2 (#2167) og smed3 (#2168) var done, med grep og lesing av hver fil. Stier er fra `arbeid/hack/`.
Jeg har selv rettet `levering/JURY_SPORSMAL.md:31` (min egen fil): «På MOT alene er h1 ikke målt» er byttet ut med 0,476 → 0,415 [0,30; 0,53] (#2134).
Kode, kjor.sh og demo_utskrift er ikke rørt (frysvakt).

| # | Funn | Status | Bevis (fil:linje) |
|---|---|---|---|
| 1 | README beskriver gammel N-PX-agent | **rettet** | `c1/leveranse/README.md:3-5` (real_votes, bånd [0,15; 0,85), GVG); `:64` logreg + LightGBM; N-PX bare i vedlegget fra `:68` merket «grunnlinje, ikke levert» |
| 2 | BEGRENSNINGER: Vanguard, fritekst, marked, #2144 mangler | **rettet** | `c1/leveranse/BEGRENSNINGER.md:13-18` #2144 inn; `:24` NBIM GVG; «fritekst» og «amerikansk» er borte fra hoveddelen; N-PX-punktene ligger under `:31`/`:48` og er merket grunnlinje |
| 3 | JURYSVAR svar 8 gjelder feil testsett | **rettet** | `levering/JURYSVAR.md:49` 1539 saker, alle typer og markeder, F1 per gruppe ikke målt; `:50` N-PX merket; `:8` innledningen lister nå 3, 5–8, 10 |
| 4 | Baseline-regelen sprikte, b2 manglet | **rettet** | `c1/leveranse/kravrespons.md:14,21` b2 0,365 og +0,11 [0,01; 0,22]; `levering/JURYSVAR.md:23`; `levering/JURY_SPORSMAL.md:77`; `c1/leveranse/BEGRENSNINGER.md:7`; `levering/EN_SIDE.md:23`; +0,38 er borte |
| 5 | Fallet uten løpende historikk hadde fire tall | **rettet** | 0,415 [0,30; 0,53] i `levering/BESLUTNINGSSTOTTE.md:44`, `levering/EN_SIDE.md:38`, `c1/leveranse/ERLIG_EVALUERING.md:29`, `c1/leveranse/kravrespons.md:15,21`, `c1/leveranse/BEGRENSNINGER.md:10-11`; METODE har 0,386 bare som avvik-tall (#1038); `JURY_SPORSMAL.md:31` rettet av meg |
| 6 | Kommandoen ender med SCORE 0.481752 | **rettet i tekst** (kjor.sh er frosset, så det er riktig valg) | `levering/README.md:29-30`, `c1/leveranse/README.md:26,34`: HOVEDTALL 0,4762 står før SCORE-linja |
| 7 | Treningsperiode strider mot METODE | **rettet** | `c1/leveranse/ERLIG_EVALUERING.md:3`: val 2019–2024, test 2019–2025 |
| 8 | «Følg styret» ser ut som produktet | **rettet** | `levering/BESLUTNINGSSTOTTE.md:10`, `levering/EN_SIDE.md:5,30`, `c1/leveranse/kravrespons.md:4`: «FOR (ingen grunn til MOT funnet)», 17 av 58; «Trenger ikke leses» og «resten kan følge styret» er borte |
| 9 | Sitatet lover for mye | **stort sett rettet** | `c1/leveranse/kravrespons.md:4` «ligner mest; 15 av 20 / 4 delvis / 1 feil»; `levering/EN_SIDE.md:7-8` GVG; `levering/KRAVRESPONS.md:84` rad 30. **Ikke rettet:** `c1/leveranse/demo_utskrift.txt:14` sier fortsatt «P(MOT) 100% kalibrert» (frysvakt, men `:8` forklarer kalibreringen) |
| 10 | Gamle og interne filer i pakka | **delvis** | Rettet: `levering/KRAVRESPONS.md:1` og `levering/demo/README.md:1` merket INTERN; `EN_SIDE` #2132; `JURYSVAR.md:3` sier ikke «ingen tall er nye» lenger; avvikstypene 58/5/3 er like i `levering/README.md:6,31`, `levering/JURYSVAR.md:7` og `c1/leveranse/ERLIG_EVALUERING.md:7`. **Ikke rettet:** `c1/leveranse/JURY.md` har fortsatt 12 treff på N-PX/Vanguard (skrives om i #1975 fra 16:05); `levering/kjor_agent_real_test2026.txt` og `kjor_agent_holdout2026.txt` ligger fortsatt i pakka (forklart i `_LES.md`); `levering/KRAVRESPONS.md:38,83` viser til «BEGRENSNINGER pkt. 9», som nå er pkt. 6 (fila er intern) |

**Konklusjon:** 8 av 10 er rettet, og 2 er delvis rettet. Det som gjenstår er lite. Det viktigste er JURY.md, som #1975 må skrive helt om etter frys og ikke bare gi ny topptekst. Ellers står «100 % kalibrert» i demoutskriften, og de gamle loggene bør enten flyttes til arkivet eller stå som de gjør med LES-fila.

# Case 1: én slide med funn og avgrensning i 1-sideren (#2332)

Tetter krav 22 og 26 fra kravdekningen (#2327).

- **Ny:** `arbeid/hack/levering/SLIDE.md`: problem, data/avgrensning, metode, tabell (følg styret F1 0 / beste enkle regel 0,365 / agenten **0,476** [0,36; 0,59], P 0,441, R 0,517), ruting av usikre saker (183 av 1539, 32 av 58 MOT), én ærlig begrensning (17 av 58 MOT blir verken flagget eller sett). Hvert tall har fotnote med kildefil og linje.
- **Ny:** `levering/omfang.py` + `omfang.txt` (reproduserbar): real_votes 13 757 saker, 194 selskaper, 37 land, 1161 møter, 2019–2026, DM 8791 / EM 4966. Test 2026: 1578 saker, 136 selskaper, 31 land.
- **EN_SIDE.md:** avgrensningslinje øverst i «2. Metode» (bare NBIM, 194 selskaper, 37 land, 2019–2026, DM+EM, alle sakstyper).
- **README.md:** peker til `SLIDE.md` og til `c1/leveranse/README.md` (kilder, URL-er, AI-bruk).
- Agentkode ikke rørt.

**Tall mot tavla:** F1 0,476190 = tavlas leverte hovedtall. 

**Avvik funnet (ikke rettet, ikke min fil):** dashbordets accuracy-linje (#2214/#2242) viser «acc 95,39 %, følg styret 95,71 %», mens pakka sier 95,7 % / 96,2 % (`TREFFSIKKERHET.md:14`, 1473/1539 og 1481/1539). 95,39 = (1539−38−33)/1539 og 95,71 = (1539−66)/1539: `server.py:_accuracy` leser **avvik**-linja (66 avvik, FN 33), ikke «MOT mot styret»-linja. Juryen som ser dashbordet får andre accuracy-tall enn pakka. Forslag: regexen `_ACC_T`/`_ACC_N` peker på MOT-linja.

**Merk:** METODE.md:10 oppgir DM 8577 / EM 4747 rader (13 324), mens hele fila har 8791 / 4966 (13 757). Trolig uten 2026-input uten fasit eller injeksjonsrader; ikke sjekket videre.

# Case 1: India-regelen som av/på-bryter i en kopi av frossen #2044 (#2303)

Kopien ligger i `arbeid/oppgave_2303/train.py`. Den er frossen `arbeid/oppgave_2044/train.py` med fire nye flagg:
`--india 0|1` (av som standard), `--vaar` (valår, standard 2025), `--val-ut` (skriver val-svarfil) og `--kun-val 1` (stopper før test 2026).
Regelen: land = India og teksten inneholder «chairman» og en av «managing director», «whole time director», «chief executive» eller «ceo». Da settes MOT oppå modellens flagg. Den leser bare radens land og tekst, aldri etiketter.
Frossen pakke er ikke rørt. Sha256 for `oppgave_2044/train.py` er fortsatt 772fb715…, og `git status` er rent for 2044, levering, 2103 og v3-måleren.

## Akseptkrav
1. **Uten flagg er fila byte-lik med frossen (val 2025).** `ref_frossen.py` kjører frossen train.py som den er, bare fram til test-delen, og skriver en val-svarfil.
   Begge filene har sha256 **c1138c9d911d43274466ac5feaffa8707008e798e224892677de8fbab11f01bc**: `val_frossen_2025.csv` = `val_av_2025.csv` (= `oppgave_2294/pred_i0_2025.csv`). v3 `--score mot` gir 0,520231.
2. **Med flagg (v3-måleren):**
   - val 2025: **0,561798**, gjenskapt (`val_india_2025.csv`, sha 38ab1615…).
   - 2024 (trent på år < 2024, grense valgt på 2024): **0,5743 gjenskapes, men bare som train.py sitt interne avviks-F1** (0,5672 → 0,5743).
     v3 kan ikke måle 2024 direkte, fordi vinduet «train» er alle år ≤ 2024. Derfor importerer `maal_aar.py` v3 uendret (sha256 418a937e…) og bytter bare vindu-funksjonen til «år == 2024».
     Med `--score mot` blir 2024 **0,536313 → 0,544444** (+0,008). 0,5743 er altså ikke et v3 MOT-tall. Det bør rettes i #1157 og i NESTE_VERSJON.md.
     Sjekk: den samme innpakningen gir 0,520231 og 0,561798 på 2025, akkurat som v3 direkte.
3. **Stemmer regelen snur:**

   | år | regelen treffer | snudd FOR→MOT | riktige (fasit MOT) | v3 MOT av → på |
   |---|---|---|---|---|
   | 2025 (val, regelen ble funnet her) | 5 | 5 | 5 av 5 | 0,520231 → 0,561798 |
   | 2024 (holdt ut) | 1 | 1 | 1 av 1 | 0,536313 → 0,544444 |

   Snudde id-er i 2025: 1972132|8, 1979284|14, 1996189|7, 1997222|5, 1997473|4. I 2024: 1886920|4.
   Ingen snudde stemmer var gale. Grunnlaget er likevel tynt: 2024 bygger på én sak, og 2025 er stedet regelen ble funnet.
4. **Test 2026 er ikke rørt.** Alle kjøringer brukte `--kun-val 1` og ingen logg har en TEST-linje. Uten `--kun-val` stopper kopien hvis `--vaar` ikke er 2025.

## Hvis dommer #2297 sier ja (før kl. 16)
`c1_real.py` kjører i dag frossen `oppgave_2044/train.py` gjennom runpy med en fast sti. For å ta regelen inn må TRAIN peke på `oppgave_2303/train.py`, og argv må få `--india 1`. Da gjelder regelen også test-flaggene (`flagg()` i test-delen).
Én ting å se på: p_avvik endres ikke for saker regelen snur (p ligger på 0,66–0,89). Kalibrering og ruting kan derfor sende dem til et menneske. Det må sjekkes i agenten før frys, og c1_frys-sha må fryses på nytt.

Kommando: `bash arbeid/oppgave_2303/kjor.sh` (rundt 3 min), deretter `python3 -I arbeid/oppgave_2303/maal_aar.py <svar> <år>`.

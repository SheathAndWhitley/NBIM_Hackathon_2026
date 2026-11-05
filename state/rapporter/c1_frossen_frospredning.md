# Case 1 #2933: frossen repo4 med 5 LightGBM-frø på 2023-2026 (målestokk for natt-dommen #2874)

**Svar: ja, v2+av-gevinsten står seg.** Mot frossen-snittet over 5 frø er gevinsten +0,043 på snitt 24-26 (0,5571 mot 0,5142).
Det er større enn de +0,041 vi hadde mot frossens ene tall (0,5162), fordi frossens pinnede tall ligger litt over eget frøsnitt.
Ingen år taper på snitt (minst +0,024 i 2026). Regelen i REGEL.md (gevinst ≥ +0,02 og intet år under -0,02, snitt mot snitt) er oppfylt.

Dette er målestokk, ikke kandidat. Pakka er ikke rørt. Kopi av `abl_rull.py` med bare `random_state=--seed` lagt til
(`arbeid/oppgave_2933/abl_seed.py`), samme oppsett som `testaar.sh` (miks, hist 2, de fire repo-trekkene, ingen av-regel).
Måler: `maaler_aar.py --data real --score mot` (byte-lik leveransens), datavakt sha256 71ba5135 sjekket i alle 24 kjøringer.
Regel skrevet før måling: `arbeid/oppgave_2933/REGEL.md`.

Kontroll: frø None gjenskaper de pinnede tallene eksakt (0,3350 / 0,5057 / 0,5309 / 0,5120). Frø 0-4 gir nøyaktig de samme
snittene som #2886 (0,3373 / 0,4945 / 0,5128 / 0,5354), så tallene er gjentatt uavhengig.

F1 MOT, snitt (sd) [min-maks] over frø 0-4:

| år | frossen 5 frø | frossen pinnet (None) | v2+av 5 frø (#2903) | v2+av minus frossen, snitt |
|---|---|---|---|---|
| 2023 vakt | 0,3373 (0,0079) [0,3238-0,3431] | 0,3350 | 0,3735 (0,0027) [0,3704-0,3763] | +0,036 |
| 2024 | 0,4945 (0,0114) [0,4805-0,5057] | 0,5057 | 0,5591 (0,0079) [0,5509-0,5714] | +0,065 |
| 2025 | 0,5128 (0,0124) [0,5032-0,5342] | 0,5309 | 0,5530 (0,0122) [0,5340-0,5667] | +0,040 |
| 2026 | 0,5354 (0,0210) [0,5161-0,5714] | 0,5120 | 0,5593 (0,0082) [0,5487-0,5714] | +0,024 |
| **snitt 24-26** | **0,5142 (0,0136) [0,5008-0,5371]** | 0,5162 | **0,5571 (0,0047) [0,5519-0,5618]** | **+0,043** |

Frø for frø (samme LGBM-frø, snitt 24-26), v2+av minus frossen: +0,048 / +0,051 / +0,049 / **+0,015** / +0,051.

Ærlige forbehold:
- Frø 3 er svakt punkt: der får frossen 0,5714 i 2026 (høyeste enkelttall i hele tabellen), og v2+av er -0,023 under frossen i 2026
  og bare +0,015 på snitt. Det ene frøet alene ville ikke klart +0,02. Over frø er det støy i frossen, ikke svakhet i v2+av:
  frossens sd i 2026 er 0,021, mer enn dobbelt så stor som v2+av sin.
- Verste v2+av-frø (0,5519) ligger +0,015 over frossens beste frø (0,5371). Fordelingene overlapper ikke.
- Frossen er like ustabil som v2+av eller mer i alle år (sd 0,008-0,021 mot 0,003-0,012). Frøet alene flytter frossen 2026 fra 0,516 til 0,571.
- Samme frønummer gir ikke "samme tilfeldighet" i to ulike modeller; parvis-tallene er bare en ekstra visning, snitt mot snitt er dommen.

Filer: `arbeid/oppgave_2933/` (REGEL.md, abl_seed.py, kjor.sh, resultat.txt, tabell.txt, ut/fr_<år>_s<frø>_maal.txt).
Gjenkjøring: `cd arbeid/oppgave_2933 && bash kjor.sh <år> <frø>` (ca. 6 sek per kjøring).

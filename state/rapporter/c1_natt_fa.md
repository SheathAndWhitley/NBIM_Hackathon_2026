# Case 1 natt (#2871): kandidat mot største feilgruppe «første MOT i selskapet», dom STÅR

**Gruppa:** feilgruppe 1 i c1_feilanalyse_natt.md. NBIM har aldri stemt MOT mot styret i selskapet før. Den står for 49 % av FN, og frossen repo4 treffer 4 av dem.
**Målt kandidat:** «tekstmal oppå repo4» (`arbeid/c1_natt/fa/REGEL.md`, skrevet 19:40:27 før svarfilene). Den legger til et MOT-flagg på første-MOT-rader når samme tekst i samme land (små bokstaver, tall fjernet) har hatt MOT-andel ≥ 0,30 over minst 5 saker i tidligere år, i alle selskaper.

| år | frossen | kandidat | diff | TP/FP/FN |
|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3535 | +0,0000 | 35/86/42 |
| 2024 | 0,5057 | 0,5143 | +0,0085 | 45/42/43 |
| 2025 | 0,5309 | 0,5309 | +0,0000 | 43/20/56 |
| 2026 | 0,5120 | 0,5120 | +0,0000 | 32/35/26 |
| snitt 2024-26 | 0,5162 | 0,5191 | **+0,0028** | |

**STÅR** (kravet er +0,02). Regelen la til ett eneste flagg, i 2024, og det traff. Forsøket står på tavla som #1241. DOM.md ligger i `arbeid/c1_natt/fa/`.

## Hvorfor gruppa nesten ikke lar seg nå (alt prøvd på val 2022-2025, ikke på test)
1. **Lavere terskel på p_avvik for gruppa:** gir dårligere F1 alle år, også ved 0,85. p_avvik rangerer bra innen gruppa (AUC 0,70–0,89), men bare 2–3 % av gruppa er MOT (13–29 av 800–1000 saker per år). Presisjonen blir derfor for lav til at nye flagg løfter F1.
2. **Andel første-MOT per (land, type) fra tidligere år:** beste variant gir snitt −0,002. Modellen har allerede dette signalet.
3. **Tekstmal på tvers av selskaper:** dette er den målte kandidaten, +0,002 på val.
4. **Eget tekst-hode** (`hode.py`: logistisk regresjon på tfidf(tekst) + land/type, trent bare på første-MOT-rader fra år < Y): dårligere enn frossen på alle fire år for C = 0,3, 1 og 3 og terskel 0,5–0,97. Ikke målt på test.
5. Heller ikke injection_flag, mgmt_rec_raw, proponent eller møtestørrelse skiller gruppa (alt er Management/For).

Første-MOT kommer i klynger per møte. Kinder Morgan 2023 har for eksempel 14 styrevalg, og et kinesisk møte har 6–8 vedtektsendringer. I de møtene flagger modellen ingenting. Uten et signal på møtenivå fra før avstemningen er gruppa i praksis uten løsning med dataene vi har. NBIMs begrunnelser (rationale_text) kommer først etter stemmen og er lekkasje.

**Spor lukket:** terskel for gruppa, (land, type)-rate og eget tekst-hode for første-MOT.
**Neste forslag:** avstå-regelen (gruppe 5, +0,012 på val, koster 0 TP) og et nylighetstrekk for regimeskifte (gruppe 2 og 4) er mer lovende enn gruppe 1.
**Gjenskap:** `cd arbeid/c1_natt/fa && python3 -I` med regel_mal.py (lager fa_*.csv), deretter `bash ../mal_kandidat.sh .`. For hode.py: `../../dommer_k43/.venv/bin/python`.

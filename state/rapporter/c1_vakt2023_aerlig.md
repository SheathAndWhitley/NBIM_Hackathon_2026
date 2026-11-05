# Case 1 (#2927): ærlig vakt-år 2023. Grense valgt på 2022, ikke på 2023. v2+av holder vakta, men 2023-gevinsten var pynt

dommer2, 05.11 20:30. Regel skrevet før måling: `arbeid/oppgave_2927/REGEL.md` (20:15). Måler: `maaler_aar.py --data real --score mot`,
F1 på MOT mot styret, datavakt sha256 71ba5135. Frosne filer er ikke rørt. Utdata: `arbeid/oppgave_2927/ut/`.

## Hva som var galt
Gammel 2023 = val-fila fra `--testaar 2024`. Der velges C og grensen t for best F1 på 2023 selv (v2_rull.py/abl_rull.py, «VAL 2023»),
og fila skrives med samme t. 2023-tallet er dermed tilpasset på seg selv. Ærlig 2023 = `--testaar 2023`: C og t valgt på val 2022,
modell trent på <2023, målt én gang på 2023, nøyaktig som 2024–2026 måles. Av-regelen ser bare år <2023 og er uendret.

## Tall, side om side (F1 MOT 2023)
| modell | gammel (optimistisk, t valgt på 2023) | ærlig (t valgt på 2022) | tap av pynt |
|---|---|---|---|
| frossen repo4 | 0,3535 | **0,3350** | −0,0185 |
| v2 uten av (k=32) | 0,3592 | 0,3452 | −0,0140 |
| **v2+av, k=64 (k valgt på val 2022, regelen)** | – | **0,3385** | – |
| v2+av, k=32 (k fra 2024-låsen) | 0,3723 | 0,3676 | −0,0047 |
| v2+av, k=48 | – | 0,3497 | – |
| diff v2+av − frossen | +0,0188 (k=32) | **+0,0035** (k=64) / +0,0326 (k=32) / +0,0147 (k=48) | |

Gammel frossen 0,3535 og gammel v2+av 0,3723 er reprodusert nøyaktig, og ærlig frossen 0,3350 stemmer med c1_natt_referanse.md.
Valg av k på val 2022: F1 val 0,514 (k=32), 0,5205 (k=48), 0,5286 (k=64), så regelen gir k=64. Val valgte altså den k som ble dårligst
på test 2023. Det er ett år og én kjøring (frøspredning på 2023 er ca. sd 0,01, c1_frospredning_tidsvekt_av.md), så det er støy, ikke bevis,
men det viser at «k låst på val» ikke er stabilt år for år.

## Svar på akseptkravene
1. Tallene står i tabellen over, begge metoder for frossen og v2+av.
2. **Ja, v2+av holder «intet år −0,02» mot frossen på ærlig 2023**, med alle tre k (laveste avstand +0,0035 ved k=64, grensen er −0,02,
   margin 0,0235, omtrent 2 sd av frøstøyen). Men den gamle 2023-gevinsten +0,0188 forsvinner nesten helt når begge måles ærlig.
   2023 støtter ikke v2+av, den feller den bare ikke. Snittet 2024–26 (+0,0409 frøsnitt / +0,0434 std) er fortsatt grunnlaget for BYTT.
3. Kommando for natt-dommen (#2874), ca. 10 sek, fersk tom mappe i /tmp, datavakt innebygd:
   ```
   bash arbeid/oppgave_2927/vakt2023.sh                       # frossen og v2+av (k=64) ærlig på 2023, HOLDER/BRUTT
   K=32 bash arbeid/oppgave_2927/vakt2023.sh                  # annen k
   bash arbeid/oppgave_2927/vakt2023.sh <kandidat_2023.csv>   # i tillegg: en kandidats 2023-svarfil laget med --testaar 2023
   ```
   Fasit fra ren kjøring 20:28: frossen 0.3350, v2+av k=64 0.3385, diff +0.0035, HOLDER. Kandidat-eksempel (k=32-fila) 0.3676, HOLDER.

## Råd til 02:00-dommen
- Bruk ærlig 2023 som vakt bare når kandidaten også leverer en `--testaar 2023`-fil. Bland aldri gammel kandidat-2023 (tunet på 2023)
  med ærlig frossen 0,3350: det gir kandidaten +0,02 gratis. `mal_kandidat.py` peker fortsatt på `repo4_2024_val.csv` (gammel metode) og
  er rettferdig så lenge kandidatene leverer samme konvensjon. Begge sammenligninger er like-mot-like; bare absoluttnivået var pyntet.
- Kandidater bygd på v2_rull.py (K1–K3, tidsvekt, frøsnitt #2926) kan lage ærlig 2023 med `v2f_rull.py/v2_rull.py ... --testaar 2023 --k 64`
  + `av_regel.py <data> <ut>_test.csv 2023 <svar>` og måle med skriptet over.

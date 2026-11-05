# Case 1: referansetall for natt-måleren (#2867) på 2023-2026 (dommer2 #2878, 2026-11-05 19:43)

Alle natt-kandidater sammenlignes med disse. Måler: `arbeid/c1_natt/mal_kandidat.sh`, F1 MOT mot styret (oppgave_2567/maaler_aar.py --score mot).
2023 er vakt-år (val-året til T=2024-kjøringen, grense valgt der), ikke hovedtall. Snitt = 2024-26.

| kandidat | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | diff snitt | dom | forsøk |
|---|---|---|---|---|---|---|---|---|
| frossen repo4 (oppgave_2575) | 0,3535 | 0,5057 | 0,5309 | 0,5120 | **0,5162** | 0 | STÅR (referanse) | #1243 |
| repo4 midt-terskel + av (#2703) | 0,3556 | 0,5083 | 0,5276 | 0,5424 | **0,5261** | +0,0099 | STÅR (verste år 2025 -0,0033) | #1246 |
| av alene (#2701, leder, målt i #2867) | 0,3736 | 0,5269 | 0,5375 | 0,5246 | 0,5297 | +0,0135 | STÅR | #1238 |
| v2 SVD-tekst i LGBM, k valgt på val (#2882, smed) | 0,3592 | 0,5326 | 0,5436 | 0,5299 | 0,5354 | +0,0192 | STÅR (0,0008 under kravet) | #1258 |
| **v2 + av-regel (#2887, smed)** | 0,3723 | 0,5731 | 0,5667 | 0,5391 | **0,5596** | **+0,0434** | **BYTT-kandidat** (verste år 2023 +0,019) | #1259 |
| midt+av med sanntids løpende terskel S2 (#2883, smed2) | 0,3636 | 0,5028 | 0,5276 | 0,5289 | 0,5198 | +0,0036 | STÅR (ærlighetstall, ikke kandidat) | #1260 |
| tidsvekt tv valgt på val + av (#2885, smed3) | 0,3966 | 0,4000 | 0,5244 | 0,5487 | 0,4910 | −0,0252 | STÅR (2024 −0,106) | #1262 |
| kontroll tv=1,0 + av (#2885) = #2701 | 0,3736 | 0,5269 | 0,5375 | 0,5246 | 0,5297 | +0,0135 | STÅR (gjenskaper #2701 eksakt) | #1263 |

Bølge 2 (dommer2 #2890, 19:49): mapper `arbeid/oppgave_2890/k*/` (cp -p fra smedenes svarmapper, REGEL.md eldre enn csv-ene i alle, DOM.md i hver). Detaljer i c1_natt_bolge2.md.

Mapper: `arbeid/oppgave_2878/frossen/` og `arbeid/oppgave_2878/midt_av/` (REGEL.md skrevet før filene, DOM.md i hver).

## Slik ble 2023 laget for midt+av (#2703 hadde bare 2024-26)
Base = frossens 2023-fil (oppgave_2575/repo4_2024_val.csv), så differansen er mot samme utgangspunkt. Midt-terskelen trenger en
flaggandel fra året før: ny repo4-kjøring med `--testaar 2023` (abl_rull.py, samme flagg som frossen, 10 s) gir 2022-val
(modell <2022), andel 0,0678. k = round((0,0678·1761 + 129 rå)/2) = 126, så av-regelen med historikk før 2023 → 109 flagg.
midt alene 2023: 0,3367 (−0,017), midt+av 0,3556 (+0,002). Kode: `arbeid/oppgave_2878/midt_av_2023.py`.

Info, ikke kandidat: ren repo4 med testår 2023 (grense fra 2022-val, modell <2023) gir 0,3350 på 2023 (log-F1 0,3628 er avvik-målet,
ikke MOT mot styret). Frossens 2023-tall 0,3535 er altså litt pyntet av at grensen ble valgt på 2023 selv; derfor er 2023 bare vakt.

## Lærdom for natta
- Måleren er stabil: frossen gjennom hele løpet gir nøyaktig de pinnede tallene (exit 0, diff 0,0000).
- 2026 er det eneste året midt+av løfter tydelig (+0,030); 2024 og 2025 står stille. En kandidat må løfte 2024/2025 for å nå +0,02.
- Smeder som bygger på #2703-typen kan hente 2022-val fra `arbeid/oppgave_2878/r4_2023/repo4_2023_val.csv` i stedet for å kjøre på nytt.

## Uavhengig omkjøring av v2 + av-regel (dommer2 #2895, 19:58): reproduserer eksakt, BYTT står

Kjørt fra rene mapper under `arbeid/oppgave_2895/`, uten smedens utdata:
- `kald_v2/`: selve v2-modellen (`v2_rull.py`, uendret kopi) kjørt på nytt fra scratch for de tre låste k/T (k32/2024, k64/2025, k48/2026),
  samme flagg som frossen repo4 (`oppgave_2575/kjor.sh`: `--hist 2 --variant miks --repo prev_same_item,...`). Alle seks val/test-csv-er er
  byte-identiske med `arbeid/c1_natt/v2/` (cmp). SCORE i loggene 0,5631 / 0,5469 / 0,5437, som smedens.
- `kald_v2av/`: `v2av.py` (uendret kopi) kjørt uten val/ og svar-csv-er. De fire svarfilene er byte-identiske med `arbeid/c1_natt/v2av/svar/`.
  Valget ingen/av på val T-1: 2024 av (0,3723 > 0,3592), 2025 av (0,5943 > 0,5532), 2026 av (0,5595 > 0,5581). Ingen testtall brukt i valget.
- k-valget fra #2882 kontrollert mot alle ni logger: høyest val-F1 er k=32 for T=2024 (0,3853), k=64 for T=2025 (0,5810), k=48 for T=2026 (0,5543). Stemmer.
- REGEL.md (19:46:27, kopiert med mtime) er eldre enn alle svarfiler (19:46:36 hos smed, 19:52:45 hos meg). Måleren godtok begge.

Natt-måler på min kopi: 2023 0,3723 (+0,0188), 2024 0,5731 (+0,0674), 2025 0,5667 (+0,0358), 2026 0,5391 (+0,0271), snitt **0,5596 (+0,0434)**,
identisk til 4 desimaler med #1259. Dommer-forsøk #1266 på tavla. Ingen avvik funnet; BYTT-dommen fra #2887 står til 02-dommen.
Forbehold som før: k og av-regelen er ledd som alt var sett på test i tidligere oppgaver (#2701, #2882), så +0,043 er et øvre anslag.

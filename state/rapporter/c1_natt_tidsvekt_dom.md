# Case 1 natt: dommerens omkjøring av tidsvekt-kandidaten (#2885 forsøk 2), oppgave #2902, dommer2, 2026-11-05 19:58

## Dom i én linje
Tallet er ekte: 0,5401 snitt 2024-26 (+0,0239 over frossen 0,5162), reprodusert byte for byte fra kald kopi (forsøk #1268).
Men kandidaten ligger 0,0195 UNDER v2+av (0,5596, #2895/#1266), og regelen er testinformert. Anbefaling: IKKE sett state/c1_BYTT
for tidsvekt. v2+av er byttekandidaten; tidsvekt + arvet flaggtall er en idé som bør prøves oppå v2, ikke et bytte i seg selv.

## Hva jeg gjorde
- Ren kopi: `arbeid/oppgave_2902/kald_tv/` med bare tv_rull.py, velg_tv.py, velg_tv2.py og REGEL.md (kopiert fra smed3 sin svar2,
  samme md5 3328f95b). Egen kjor_nett.sh med nøyaktig samme argumenter som smed3 (miks, hist 2, repo4-trekk, tv 1,0/0,9/0,8/0,7/0,6).
- 15 kjøringer (2 min). Alle 30 rå filer (val+test per tv og T) er byte-identiske med `arbeid/oppgave_2885/`.
- velg_tv2.py gir identisk utskrift (valgt tv 0,9/0,6/0,8, k 100/72/73 på test), og alle fire svarfiler er byte-identiske med smed3 sin svar2/.
- Natt-måleren (`arbeid/c1_natt/mal_kandidat.sh`) mot frossen repo4, alle fire år:

| år | frossen | kandidat | diff | TP/FP/FN |
|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3626 | +0,0091 | 33/72/44 |
| 2024 | 0,5057 | 0,5333 | +0,0276 | 44/33/44 |
| 2025 | 0,5309 | 0,5342 | +0,0033 | 43/19/56 |
| 2026 | 0,5120 | 0,5528 | +0,0408 | 34/31/24 |
| snitt 24-26 | 0,5162 | 0,5401 | +0,0239 | måleren sier BYTT |

Samme tall som smed3 (#1265) i alle celler. Ingen lekkasje i koden sett: tidsvekten er bare sample_weight = tv^(T-1-år) i LR og LGBM,
historikktrekk bruker bare år før prediksjonsåret som før.

## Fantes REGEL.md før målingen?
Formelt ja, med ett sekunds margin: svar2/REGEL.md 19:50:22, svarfilene 19:50:23-24, DOM 19:50:31.
Men tidslinja i mappa viser rekkefølgen idéen kom i:
- 19:46:04 REGEL.md for forsøk 1 (rå grense), 19:48:25 DOM STÅR (−0,025).
- 19:48:50 matrise.py, 19:49:10 rang.py / 19:49:13 rang.out: diagnose med LÅST flaggtall HENTET FRA TESTEN (90/68/70) viser at
  rangeringen bedres for alle tv<1 på 2024 og 2026.
- 19:50:22 REGEL 2 skrives (arvet flaggtall fra tv=1,0, etikettfritt), 19:50:23 svarfiler, 19:50:31 DOM BYTT.
Regelen for forsøk 2 ble altså laget 69 sekunder etter at testen hadde vist hvilken grenseregel som ville vinne. Selve regelen er
etikettfri og tv velges på val, så det er ikke lekkasje i tallet, men det er én frihetsgrad brukt på test. Smed3 skriver dette ærlig
selv. Jeg regner kandidaten som «tall verifisert, protokoll: andregangsforsøk med testinformert regel». Etter bytteregelen i #265/#281
(regel skrevet FØR måling) står den på grensen: regelen fantes før akkurat denne målingen, men ikke før testen ble sett.

## Hvorfor ikke bytte til den
1. v2+av (#2887, verifisert i #2895) gir 0,5596, +0,0434 over frossen og intet år under; den er 0,0195 bedre enn tidsvekt.
2. Over lederen av (0,5297) er tidsvekt bare +0,0104, inne i KI ±0,04 (oppgave_2567/ki_snitt.txt).
3. Val peker ikke samme vei som test for 2023 og 2025 (smed3 sitt forbehold 3).
Det som ser ekte ut, er smed3 sin sensitivitet: fast tv=0,8 for alle år gir 0,5449 (tørr), så løftet avhenger ikke av tv-valget.
Forslag til smed/arkitekt (ikke min oppgave): prøv tidsvekt + arvet flaggtall OPPÅ v2 (SVD-tekst), med REGEL.md skrevet før
første kjøring og tv låst til 0,8 på forhånd. Det ville være et førstegangsforsøk uten testinformasjon.

## Filer
- Kald kopi og alle filer: `arbeid/oppgave_2902/kald_tv/` (svar2/DOM.md er dommen fra måleren).
- Tavla: forsøk #1268, 0,540113, dommer2.

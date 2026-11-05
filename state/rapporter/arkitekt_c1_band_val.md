# Case 1: rutebåndet valgt på val 2025 i stedet for test (arkitekt #2279)

**Svar: val 2025 velger samme bånd, [0,15; 0,85).** Ingenting i pakka endres. Bare måling; agent, grense (rå p ≥ 0,919), kalibrering og prediksjoner er urørt.

KP: forventet maskin alene F1 MOT mot styret 0,476 (TP 30 FP 38 FN 28) på test og 0,520 på val; fikk 0,4762 (30/38/28) og 0,5202. Tallene stemmer med hovedtallet.

## Regelen
#2128 valgte båndet med skjønn på test («2 MOT til for 45 saker mer» var ikke verdt det). Jeg har gjort skjønnet om til en regel og brukt den bare på val:
utvid båndet trinnvis [0,3; 0,7) → [0,15; 0,85) → [0,08; 0,95) så lenge de nye sakene som sendes til menneske har **MOT-andel ≥ 10 %**. Stopp ved første trinn under.

| trinn | val 2025: nye saker, nye MOT (andel) | test 2026 (bare til sammenligning) |
|---|---|---|
| [0,3; 0,7) → [0,15; 0,85) | +86, +22 (25,6 %): utvid | +71, +10 (14,1 %) |
| [0,15; 0,85) → [0,08; 0,95) | +67, +6 (9,0 %): stopp | +45, +2 (4,4 %) |

Følsomhet: val velger [0,15; 0,85) for enhver terskel mellom 9,1 % og 25,6 %. Under 9 % ville val valgt det brede båndet [0,08; 0,95), over 25,6 % det smale.

## Test 2026, bare båndet, MOT mot styret (1 539 saker, 58 MOT, 28 MOT-bom hos maskinen alene)

| bånd | valgt på | til menneske | MOT i menneskekøen | MOT-bom i menneskekøen | F1 MOT på det agenten avgjør selv (TP/FP/FN) |
|---|---|---|---|---|---|
| **[0,15; 0,85)** | **test (#2128)** | 122 (7,9 %) | 27 av 58 | 7 av 28 | 0,488 (10/0/21) |
| **[0,15; 0,85)** | **val 2025 (#2279)** | 122 (7,9 %) | 27 av 58 | 7 av 28 | 0,488 (10/0/21) |
| [0,08; 0,95) | val ved terskel < 9 % | 167 (10,9 %) | 29 av 58 | 8 av 28 | 0,474 (9/0/20) |
| [0,3; 0,7) | val ved terskel > 25,6 % | 51 (3,3 %) | 17 av 58 | 0 av 28 | 0,433 (13/6/28) |

«MOT-bom» = ekte MOT mot styret som maskinen alene sa FOR til. De andre 20 MOT i køen er saker maskinen allerede flagget riktig. 21 MOT-bom blir liggende i FOR-bunken med q under 0,08, og dem fanger intet bånd.
Tabellen gjelder bare båndet. Standardrutingen i pakka (bånd + ukjent selskap, injeksjon osv., 188 saker) er ikke målt på nytt her.

## Forbehold
- Kalibreringen er lært på val, så q på val er i utvalget. Trinnene (0,09; 0,17; 0,19; 0,52; …) er de samme på val og test, så båndene skiller de samme trinnene.
- Terskelen 10 % er min formalisering av skjønnet fra #2128, laget etter at testtabellen fantes. Den er ikke låst på forhånd. Det som holder: val alene gir samme bånd for et bredt spenn av terskler (9,1–25,6 %).
- Val har 99 MOT mot styret, ikke 103 (103 er alle avvik).

## Én setning til juryen
«Båndet [0,15; 0,85) ble først valgt fra en tabell på test 2026. Når vi bruker samme regel bare på val 2025 (utvid så lenge minst 10 % av de nye sakene er MOT), får vi samme bånd, og det holder for enhver terskel mellom 9 % og 26 %. Testtallene er derfor de samme: 7,9 % til menneske, F1 0,488 på det agenten avgjør selv, og 7 av 28 MOT-bom i menneskekøen.»

## Reprodusere
`uv run python arbeid/oppgave_2279/band_val.py` (utskrift i `arbeid/oppgave_2279/utskrift.txt`; leser `arbeid/oppgave_2109/{val,test}_pred.csv`, `kal_resultat.json` og real_votes 20261105_114241).

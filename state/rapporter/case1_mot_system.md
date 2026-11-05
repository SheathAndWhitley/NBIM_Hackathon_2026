# Case 1 (#2046): systemet flagger stemmer MOT styret, F1 på MOT mot følg-styret-gulvet

Én kommando fra kald start: `uv run python arbeid/oppgave_2046/case1_mot.py` (ca. 8 s, arrangørens filer i arbeid/hack/CASE/).
Resultater: `arbeid/oppgave_2046/resultat.json`, prediksjoner per sak: `pred_<data>_2026.csv`.

Protokoll: tren ≤2024, alt valgt på val 2025 (C, terskel, rutegrense), test 2026 kjørt ÉN gang, ingen refit.
Logreg på forslagstype, forslagsstiller, styrets anbefaling, land, marked, tf-idf på forslagsteksten,
selskapets MOT-historikk fra strengt tidligere møter, møtestruktur. Forbudte kolonner (nbim_vote*, rationale_*,
position_paper, funds_disagree, n_funds) brukes ikke; sjekkes med assert i koden. Injeksjonsrader holdes utenfor.

## Test 2026, real_votes (NBIM API, 1539 saker, 66 MOT)
| system | flagget MOT | P | R | F1 | treff | til menneske |
|---|---|---|---|---|---|---|
| følg styret (gulv) | 0 | 0 | 0 | **0** | 0,957 | 0 |
| regel: alle aksjonærforslag MOT | 16 | 0,50 | 0,12 | 0,20 | 0,957 | 0 |
| maskin alene | 83 | 0,41 | 0,52 | **0,456** (KI95 0,36–0,54) | 0,947 | 0 |
| maskin + ruting 5 %-grense | 40 | 0,88 | 0,53 | 0,66 (0,56–0,75) | 0,977 | 93 (6,0 %, 20 av dem MOT) |
| maskin + ruting 10 %-grense | 40 | 0,98 | 0,59 | 0,74 (0,64–0,82) | 0,982 | 166 (10,8 %, 27 MOT) |

## Test 2026, npx (16455 saker, 634 MOT)
| system | flagget | P | R | F1 | treff | til menneske |
|---|---|---|---|---|---|---|
| følg styret | 0 | 0 | 0 | 0 | 0,962 | 0 |
| maskin alene | 598 | 0,84 | 0,79 | **0,812** | 0,986 | 0 |
| bare styrets egne forslag (maskin alene) | 296 | 0,67 | 0,60 | 0,631 | 0,986 | 0 |
| ruting 5 %-grense | 517 | 1,00 | 0,82 | 0,90 | 0,993 | 569 (3,5 %) |

## Ærlig lesning
- Agenten predikerer MOT på en reell andel saker (83 av 1539 på real, 598 av 16455 på npx). Følg styret gir F1 0.
- På real_votes taper maskinen alene treff mot gulvet (0,947 mot 0,957): den bytter treff mot å finne halvparten av MOT.
  F1 0,456 er under målet 0,5, og val (0,536) var høyere enn test, så tallet er ikke pyntet.
- npx-tallene er pene delvis fordi aksjonærforslag der nesten er alltid MOT (321/323 på val). Ærlig npx-tall er styrets
  egne forslag: F1 0,63.
- Ruting: grensen for forventet feil er satt på val og brukt uendret på test; antall rutede er målt (93 / 166).
  Tallene "med ruting" antar at mennesket stemmer som NBIM, så de er en øvre grense. Maskinen på de ikke-rutede
  sakene alene: F1 0,455 (5 %) og 0,462 (10 %), presisjon 0,75 / 0,92.
- Neste: smed2s modell fra #2044 kan settes inn i samme ramme (samme split, samme rutelogikk) når den finnes.
- smed2 (#2044) melder kl. 11:53 en streng modell med test-F1 0,386, lavere enn 0,456 her. Derfor er denne logregen
  systemets modell inntil noe slår den på val, med test som kontroll.

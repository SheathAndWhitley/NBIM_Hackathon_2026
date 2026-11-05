# Case 1: dom over personnøkkel-rapporten (#2496): GODKJENT (dommer #2503, 05.11 16:3x)

**Dom: GODKJENT.** Alle tolv F1/P/R-tall og tre KI-er i `state/rapporter/c1_personnokkel_rullende.md` er gjenskapt
fra kald kode i `arbeid/oppgave_2503/` (kopi av `oppgave_2496/{abl_rull.py,maaler_aar.py,diff_ki_aar.py}`,
eget kjor.sh utvidet med 2026-radene som smedens kjor.sh ikke kjører). Prediksjonsfilene mine er byte-like
smedens (cmp, 5 filer) og sak 2490 (2 filer). Frosne filer urørt (frysvakt 17/17, git status tom).

| Testår (val) | Variant | F1 MOT | P | R | Rapport | Person − uten, 95 % KI (min kjøring) |
|---|---|---|---|---|---|---|
| 2024 (2023) | uten | 0,4545 | 0,682 | 0,341 | 0,4545 | |
| 2024 (2023) | + person | 0,4179 | 0,609 | 0,318 | 0,4179 | −0,037 [−0,133; +0,058], 28 ulike |
| 2025 (2024) | uten | 0,5143 | 0,592 | 0,455 | 0,5143 | |
| 2025 (2024) | + person | 0,5155 | 0,526 | 0,505 | 0,5155 | +0,001 [−0,042; +0,050], 25 ulike |
| 2026 (2025) | uten | 0,4762 | 0,441 | 0,517 | 0,4762 | |
| 2026 (2025) | + person | 0,5254 | 0,517 | 0,534 | 0,5254 | +0,049 [+0,016; +0,090], 14 ulike |

Alle avvik 0. Rapportens dom (gevinsten finnes bare i 2026, KI dekker null i 2024 og 2025, personnøkkelen
skal ikke inn) står.

## Sjekket
- **2026 uten person = frossen:** `full_2026_test.csv` har sha256 `69702192…dfc`, identisk med den frosne
  `arbeid/oppgave_2103/full_test.csv` i `state/c1_frys.json`. Måler gir 0,476190 på begge.
- **Måleren:** `maaler_aar.py` avviker fra `maaler_offisiell_v3.py` bare i vindusfunksjonen (år i stedet for
  train/val/test) og vindus-sjekken. Scoreregelen er uendret.
- **Koden:** `abl_rull.py` = `oppgave_2490/abl.py` + `--testaar`; 2490 = frossen `oppgave_2103/abl.py` + repo-trekket.
  Ingen andre endringer (diff lest).
- **Lekkasje val/test:** C og terskel velges på år T−1 med modell trent på år < T−1. Test T trenes på år < T,
  terskelen fra val brukes rått. Historikktrekkene (hist 2) bruker etiketter fra møter strengt før radens dato,
  aldri år > T. Repoets `prev_same_person` oppdateres først etter hele møtet (`ballot.add_history`), samme
  prinsipp. Ingen etikett fra raden selv eller samme møte. Samme løpende prinsipp som frossen #2044.
- **Forbudte kolonner:** loggene viser snitt mellom brukt og forbudt = tom mengde, alle seks kjøringer.

## Merknader (ikke avvisningsgrunn)
- Smedens kjor.sh kjører bare 2024 og 2025. 2026-radene i rapporten kommer fra sak 2490, og `person_2026*`
  finnes ikke i `oppgave_2496/`. Jeg kjørte dem selv, likt resultat. Rapporten bør si det.
- «Snitt over tre år: uten 0,482, med person 0,486» stemmer (0,4817 / 0,4863).
- Testen 2026 var allerede sett da personnøkkelen ble prøvd, som rapporten selv sier.

Gjenskap: `cd arbeid/oppgave_2503 && bash kjor.sh`, så `python3 -I arbeid/oppgave_2503/maaler_aar.py
arbeid/oppgave_2503/<variant>_<år>_test.csv y<år> --data real --score mot` og
`python3 -I arbeid/oppgave_2503/diff_ki_aar.py <full> <person> <år>` fra landsbyrota.

# Case 1 #2907: forklarings-trekkene fra NBIMs begrunnelser gir ingen gevinst oppå v2+av (smed, 05.11)

Regelen sto i `arbeid/oppgave_2907/REGEL.md` før første måling. Kode: `arbeid/oppgave_2907/v2f_rull.py` (v2_rull.py + `--grunn`), kjøring: `bash arbeid/oppgave_2907/maal.sh <navn> <trekk>`.
Oppsettet er låst som testaar.sh med MODELL=v2av: k 32/64/48, C og grense valgt på val T-1, så av-regel. 2023 = val-fila fra T=2024 + av-regel. Måler: maaler_aar.py, F1 MOT.

| kandidat | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | mot v2+av | forsøk |
|---|---|---|---|---|---|---|---|
| v2+av, gjenskapt i samme skript | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 0,5596 | 0 | (= dom #2890) |
| K1 = + trekk 1 (person fikk MOT med GVG 1.1–1.3 før) | 0,3723 | 0,5647 | 0,5587 | 0,5410 | 0,5548 | −0,0048 | #1271 |
| K2 = K1 + trekk 2 (selskapet hadde det før) | 0,3723 | 0,5521 | 0,5667 | 0,5470 | 0,5553 | −0,0043 | #1272 |
| K3 = K2 + trekk 3, 4 (lønn GVG 3.3, rem-komité × lønns-MOT i fjor) | 0,3743 | 0,5679 | 0,5667 | 0,5397 | 0,5581 | −0,0015 | #1273 |

- **Regel A (#281, mot frossen 0,5162):** alle tre står, men bare fordi v2+av står. Trekkene selv bidrar ikke.
- **Regel B (over v2+av, krav +0,02):** ingen består. Alle ligger litt under v2+av, innenfor frøstøyen.
- **Trekk 5** ble ikke målt. Regelen krevde at K3 sto over v2+av, og det gjorde den ikke.
- **Anbefaling:** ingen ny kandidat til 02-dommen fra denne oppgaven. Sporet er lukket.

## Lekkasje
- Testen fra byggeoppskriften feiler, men det er ikke lekkasje. Testen satte `rationale_section` = NaN for hele teståret og ventet byte-like prediksjoner. Den ga avvik i 2024 og 2025 av to grunner:
  - (a) `--hist 2` bruker med vilje forklaringer fra tidligere møter i samme sesong, akkurat som `hist_feats`.
  - (b) Miks-rangeringen går over alle rader, så én endret skår flytter alle andre.
- I stedet testet jeg på trekk-nivå (`--lekktest 2` mot `3`). Jeg maskerte forklaringene fra midtdatoen i teståret. Trekkene for alle rader med dato ≤ midtdatoen ble identiske: 1001, 996 og 798 rader for 2024, 2025 og 2026. Ingen trekk ser framover i tid.

## Hvorfor det ikke virker
- Flaggene som endres mot v2+av er stort sett andre typer enn direktørvalg (ARTICLES, RPT, OTHER_MGMT). De nye trekkene flytter altså mest rangering og grense, de legger ikke til direktørvalg-treff.
- Eksempel: K3 i 2024 fjerner 11 flagg (4 var riktige) og legger til 2 (1 riktig).
- Trekk 1 overlapper med `prev_same_person`, og n er 14–24 rader per år. Det stemmer med speiderens forbehold.

Neste: ingen. Skal ideen prøves igjen, er det som en etterregel (slik av-regelen er) og ikke som trekk. Det må i så fall være en ny regel før måling.

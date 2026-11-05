# Case 1: hvor bommer den frosne agenten? Feil per land, marked, sakstype og forslagsstiller (#2272)

Frossen agent #2044 (`arbeid/hack/levering/kjor_agent_real_maskin_alene.csv`), test 2026 i arrangørens ekte fil (sha 71ba5135…), måler v3 `--score mot`.
Totalt: F1 på MOT mot styret 0,476 (TP 30, FP 38, FN 28 av 58 MOT i fasit), 95 % klyngebootstrap-KI 0,35–0,59 over 140 møter.
Tallene under summerer nøyaktig til målerens tall. Reproduser: `python3 -I arbeid/oppgave_2272/feil_per_gruppe.py` (bare stdlib, frø 2272, 1000 bootstrap-trekk over meeting_id).

## Tre setninger til juryen

1. Agenten er svakest på amerikanske selskaper: den treffer 0 av 7 MOT i USA og legger 9 falske MOT der, nesten alle på styrevalg i banker og grunnleggerstyrte selskaper (Dell, Public Storage), mens den savner NBIMs MOT på flytting til Texas, forslagsterskler og aksjeplaner.
2. Styrevalg er den store feilkilden i volum (26 av 38 falske MOT, 13 av 28 bom), men ikke den verste i andel; verst er «andre styresaker» (OTHER_MGMT, 1 av 6 MOT truffet) og revisorvalg (3 av 7), der NBIMs begrunnelse (GVG 4.3 og 5.1) ikke står i forslagsteksten.
3. Agenten er sikker der den sier MOT (laveste p blant MOT-anbefalinger er 0,92), men 18 av 28 bom har p ≥ 0,5 og 11 har p ≥ 0,8: feilene ligger rett under agentens egen grense, så presisjonen på styrevalg (0,37) er problemet, ikke at saken er usynlig for modellen.

## Forbehold

- Sektor finnes ikke i arrangørens data (ingen kolonne, ikke i startpakka). Jeg har brukt marked (DM/EM) som nærmeste erstatning og ikke gjettet sektor fra selskapsnavn. Bruker juryen sektor, må det sies at vi ikke har det.
- Grupper med under 5 MOT i fasit er merket «for få MOT til å si noe»; F1 står for ordens skyld, men KI er ikke regnet. OTHER_BUSINESS (6 av 6, alle «Other Business»-poster) er en regel, ikke modellstyrke.
- Bare lesing og måling; agent og terskel er urørt (frys kl. 16).

## Tabeller

### Per sakstype

| sakstype | saker | MOT i fasit | TP | FP | FN | presisjon | treff (recall) | F1 | 95 % KI (klynge) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DIRECTOR_ELECTION | 739 | 28 | 15 | 26 | 13 | 0.37 | 0.54 | 0.43 | 0.29–0.56 |
| AUDITOR | 130 | 7 | 3 | 0 | 4 | 1.00 | 0.43 | 0.60 | 0.00–0.91 |
| OTHER_MGMT | 87 | 6 | 1 | 1 | 5 | 0.50 | 0.17 | 0.25 | 0.00–0.80 |
| OTHER_BUSINESS | 6 | 6 | 6 | 0 | 0 | 1.00 | 1.00 | 1.00 | 1.00–1.00 |
| SAY_ON_PAY | 61 | 3 | 3 | 8 | 0 | – | – | 0.43 | for få MOT til å si noe |
| ARTICLES | 55 | 3 | 1 | 1 | 2 | – | – | 0.40 | for få MOT til å si noe |
| SHARE_ISSUANCE | 34 | 2 | 0 | 0 | 2 | – | – | 0.00 | for få MOT til å si noe |
| FIN_STATEMENTS | 100 | 1 | 0 | 0 | 1 | – | – | 0.00 | for få MOT til å si noe |
| RPT | 29 | 1 | 1 | 0 | 0 | – | – | 1.00 | for få MOT til å si noe |
| EQUITY_PLAN | 22 | 1 | 0 | 0 | 1 | – | – | 0.00 | for få MOT til å si noe |
| DISCHARGE | 88 | 0 | 0 | 1 | 0 | – | – | 0.00 | for få MOT til å si noe |
| DIVIDEND | 81 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| DIRECTOR_PAY | 50 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| ROUTINE | 25 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| SHARE_REPURCHASE | 24 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| SHP_OTHER | 2 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| SHP_GOVERNANCE | 2 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| MERGER | 2 | 0 | 0 | 1 | 0 | – | – | 0.00 | for få MOT til å si noe |
| SHP_INDEP_CHAIR | 1 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| SHP_SUSTAINABILITY | 1 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |

### Per land

| land | saker | MOT i fasit | TP | FP | FN | presisjon | treff (recall) | F1 | 95 % KI (klynge) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Japan | 274 | 7 | 4 | 3 | 3 | 0.57 | 0.57 | 0.57 | 0.20–0.82 |
| United States | 217 | 7 | 0 | 9 | 7 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| Indonesia | 17 | 7 | 6 | 1 | 1 | 0.86 | 0.86 | 0.86 | 0.50–1.00 |
| India | 103 | 4 | 1 | 6 | 3 | – | – | 0.18 | for få MOT til å si noe |
| Switzerland | 68 | 4 | 4 | 3 | 0 | – | – | 0.73 | for få MOT til å si noe |
| China | 129 | 3 | 0 | 2 | 3 | – | – | 0.00 | for få MOT til å si noe |
| Germany | 69 | 3 | 3 | 2 | 0 | – | – | 0.75 | for få MOT til å si noe |
| Cayman Islands | 64 | 3 | 2 | 0 | 1 | – | – | 0.80 | for få MOT til å si noe |
| Thailand | 26 | 3 | 2 | 0 | 1 | – | – | 0.80 | for få MOT til å si noe |
| British Virgin Islands | 15 | 3 | 1 | 1 | 2 | – | – | 0.40 | for få MOT til å si noe |
| South Korea | 77 | 2 | 0 | 1 | 2 | – | – | 0.00 | for få MOT til å si noe |
| United Kingdom | 52 | 2 | 0 | 0 | 2 | – | – | 0.00 | for få MOT til å si noe |
| Poland | 39 | 2 | 1 | 0 | 1 | – | – | 0.67 | for få MOT til å si noe |
| Belgium | 26 | 2 | 2 | 6 | 0 | – | – | 0.40 | for få MOT til å si noe |
| Kuwait | 16 | 2 | 2 | 0 | 0 | – | – | 1.00 | for få MOT til å si noe |
| Taiwan | 49 | 1 | 0 | 1 | 1 | – | – | 0.00 | for få MOT til å si noe |
| Vietnam | 17 | 1 | 1 | 0 | 0 | – | – | 1.00 | for få MOT til å si noe |
| Jersey | 14 | 1 | 0 | 1 | 1 | – | – | 0.00 | for få MOT til å si noe |
| Mexico | 8 | 1 | 1 | 0 | 0 | – | – | 1.00 | for få MOT til å si noe |
| Sweden | 62 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Canada | 47 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Malaysia | 38 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| South Africa | 27 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Bermuda | 18 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Denmark | 16 | 0 | 0 | 1 | 0 | – | – | 0.00 | for få MOT til å si noe |
| Hong Kong | 15 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| United Arab Emirates | 11 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Colombia | 9 | 0 | 0 | 1 | 0 | – | – | 0.00 | for få MOT til å si noe |
| Singapore | 9 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |
| Australia | 7 | 0 | 0 | 0 | 0 | – | – | – | for få MOT til å si noe |

### Per marked (DM/EM)

| marked (DM/EM) | saker | MOT i fasit | TP | FP | FN | presisjon | treff (recall) | F1 | 95 % KI (klynge) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DM | 876 | 29 | 14 | 26 | 15 | 0.35 | 0.48 | 0.41 | 0.25–0.54 |
| EM | 663 | 29 | 16 | 12 | 13 | 0.57 | 0.55 | 0.56 | 0.34–0.72 |

### Per forslagsstiller

| forslagsstiller | saker | MOT i fasit | TP | FP | FN | presisjon | treff (recall) | F1 | 95 % KI (klynge) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Management | 1523 | 56 | 29 | 38 | 27 | 0.43 | 0.52 | 0.47 | 0.35–0.59 |
| Shareholder | 16 | 2 | 1 | 0 | 1 | – | – | 0.67 | for få MOT til å si noe |

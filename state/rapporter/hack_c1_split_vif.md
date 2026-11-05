# Case 1: ny split fra full Vanguard-tabell (dommer, #1974)

Gammel split (`data/train.csv`, 11:07) bygde på v1 = én innsending (21k poster). Den står urørt, men er utdatert.
Ny split ligger i `arbeid/hack/c1/data_vif/` (fryst kopi av `data/votes_unik.csv`, sha1 deb383ff, fordi smed skrev om `data/votes.csv` mens jeg jobbet).

## Oppskrift (fra `arbeid/hack/c1/`)
    python3 -I maaler.py split data_vif/kilde_votes_unik.csv --grense 2025-07-01 --selskap historikk --ut data_vif
    python3 -I maaler.py split data_vif/train.csv --grense 2024-07-01 --selskap historikk --ut data_vif_val
    python3 -I maaler.py PRED.csv --fasit data_vif/fasit.csv        # tavle-måler #1974: 64f9ecb0c7

## Tall
| sett | n | MOT | avvik fra styret | datoer |
|---|---|---|---|---|
| train | 70 636 (1 024 frekvensstemmer uten fasit) | 4 252 | 3 206 (4,5 %) | 2023-07-05..2025-06-30 |
| holdout | 64 191 | 5 127 | 5 553 (8,7 %) | 2025-07-01..2026-06-30 |
| val-train (innenfor train) | 35 788 | 2 482 | 1 901 | ..2024-06-28 |
| val-holdout | 34 409 | 1 770 | 1 305 (3,8 %) | 2024-07-01..2025-06-30 |

Holdout = siste N-PX-år (48 % av forslagene). Selskapsmodus `historikk`: tidligere møter for samme selskap er lov
i train (3 517 selskaper på begge sider); `strikt` ville tømt train. Ingen møtedag deles.

## Nivåer på holdout (SCORE = F1 på avvik fra styret)
| prediksjon | SCORE | PR-AUC | MOT-F1 |
|---|---|---|---|
| følg styret | 0,000 | 0,087 | 0,175 (P 0,90 R 0,10) |
| alltid FOR | 0,017 | 0,087 | 0 |
| gulv: avvik hvis cusip+kategori hadde avvik i train (>30 %) | **0,155** | 0,155 | 0,256 |
Gulv på val: SCORE 0,190. Kode: `data_vif/gulv/gulv_vif.py`.

## Funn og rettelser
- `fond_uenige` (fondene stemte ulikt) er avledet av stemmen og var med i test_input. Lagt i LEKK_KOL, fjernet.
- `maaler.py split` fikk `--grense` og `--ut`; train fra en tidligere split ga dobbel `antall_fond`, rettet.
  Målelogikken er uendret: gammel fasit gir samme tall. Målerne på #1949/#1950/#1955/#1959 satt på nytt (feec230783), samme kommando.
- Fordelingsskift: avvik 4,5 % i train mot 8,7 % i holdout, og AVSTÅ 5 i train mot 873 i holdout. En modell som
  kalibreres på train vil underpredikere avvik. Bruk val-splitten til terskelvalg, og si det i evalueringen.
- 136 456 rader i votes_unik ble 135 329 forslag etter normalisert tekst (1 127 tekstduplikater, 31 med ulik stemme).

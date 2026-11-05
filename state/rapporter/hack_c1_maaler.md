# Case 1: måler med tidssplitt og baseline (#1947)

**Fil:** `arbeid/hack/c1/maaler.py` (bare stdlib). Måler-sha `f3bd169028`, aktiv runde-måler, også satt på #1949 og #1950.
SCORE = F1 på MOT over hele holdout, høyere er bedre.

## Bruk
```
# én gang når arbeid/hack/c1/data/votes.csv finnes (#1946):
python3 -I arbeid/hack/c1/maaler.py split arbeid/hack/c1/data/votes.csv      # -> train.csv, test_input.csv, fasit.csv, split_info.txt
python3 -I arbeid/hack/c1/maaler.py baseline                                  # følg styret + alltid FOR
python3 -I arbeid/hack/c1/maaler.py PRED.csv [--terskel 0.6]                  # PRED: id,anbefaling,konfidens
```
Smedene trener på `train.csv` og predikerer `test_input.csv` (har id og styrets anbefaling, ikke stemmen).

## Låste definisjoner
- MOT = AGAINST/WITHHOLD (som arrangørens baseline.py), FOR, AVSTÅ = ABSTAIN. «1 YEAR» o.l. holdes utenfor holdout.
- Enhet = forslag (selskap, møtedato, tekst). Samme forslag fra flere fond slås sammen til flertallsstemmen; antall uenige rapporteres.
- Holdout = siste 20 % av forslagene etter møtedato. En møtedag deles aldri.
- `--selskap strikt` (standard): selskaper i holdout fjernes fra train, så ingen selskapshistorikk krysser grensen. `historikk` er valgfritt og må i så fall oppgis.
- Ruting: konfidens < 0,6 går til menneske. Måleren skriver ut andel rutet, MOT-recall/presisjon blant de ikke-rutede, og «maskin+menneske» (øvre grense: mennesket treffer på de rutede).
- I tillegg: «mot styret»-presisjon/recall/F1 (stemt annerledes enn styret anbefalte). Det er de 6 % casen snakker om. Leveransen bør vise begge.
- Ugyldig fil (manglende/duplikat id, ukjent anbefaling, konfidens utenfor [0,1]) gir `SCORE nan` og exit 1. Testet.

## Testet på syntetisk tabell (`arbeid/hack/c1/test/`, IKKE ekte data)
875 rader, 456 forslag, holdout 78: følg styret F1 MOT 0,897, alltid FOR 0,000. Strikt selskapsfilter fjerner et innplantet tidlig møte for et holdout-selskap (1 rad), og `historikk` beholder det. Tallene er bare en røyktest.

## Viktig for smedene
«Følg styret» får høy MOT-recall gratis på aksjonærforslag, fordi styret anbefaler AGAINST der. Det er grunnlinja som må slås på F1 MOT. Den får 0 på «mot styret», så den målingen viser verdien.

## Ekte baseline, data v0 (votes_v0.csv, Vanguard Index Funds, 21 474 rader), måler-sha bdad4444d1
Grense møtedato >= 2026-05-22. Train 7 250 forslag (198 MOT), holdout 1 544 forslag (65 MOT = 4,2 %), datoer 2026-05-22..2026-06-30.
1 092 forslag har uenige fond (flertallet gjelder). Strikt filter fjernet 10 train-forslag. «ONE YEAR», «1.0» o.l. (67) er holdt utenfor.

| Baseline | Accuracy | MOT presisjon | MOT recall | **F1 MOT (SCORE)** | F1 mot styret |
|---|---|---|---|---|---|
| Følg styret | 0,965 | 0,789 | 0,231 | **0,357** | 0,000 |
| Alltid FOR | 0,955 | 0 | 0 | **0,000** | 0,111 |

Begge står på forsøkstavla (#964, #965). **Tallet som må slås: F1 MOT 0,357.**
Kolonnen `ledelsen` brukes som styret. `mot_ledelsen`, `delt` og `n_rec` kommer fra svaret og er tatt ut av test_input.csv.

## Gjenstår
Smeden henter mer data (votes_vif). Når votes.csv byttes, kjører dommeren split og baseline på nytt og setter måleren på nytt (fasiten endres). Id-ene er stabile (hash av selskap|dato|forslag), men holdout flytter seg. Baseline-tallene over gjelder bare v0.

# Case 1: robusthetstest for agenten (#1968)

Agent: `python3 -I <repo>/arbeid/hack/c1/../varianter/smed3_utf_sitat/agent.py {train} {test} {pred}`  
Kjør: `python3 -I arbeid/hack/c1/robusthet.py` (kald start under 1 min). Måler: maaler.py v2, hovedtall AVVIK-F1 fra utledet styre; rutet = konfidens < 0,6.

## arbeid/hack/c1/data

| test | AVVIK-F1 | endring | recall | PR-AUC | rutet til menneske | MOT-F1 | hva |
|---|---|---|---|---|---|---|---|
| basis | 0.240 | +0.000 | 0.136 | 0.252 | 0.1% | 0.860 | uendret |
| nye_selskaper | 0.240 | +0.000 | 0.136 | 0.252 | 0.1% | 0.860 | 0 av 7249 train-rader fjernet (selskap i holdout) |
| siste_aar | 0.240 | +0.000 | 0.136 | 0.252 | 0.1% | 0.860 | train fra 2025-05-22: 7249 av 7249 rader |
| tom_tekst | 0.000 | -0.240 | 0.000 | 0.110 | 0.0% | 0.839 | forslag tom i alle holdout-rader |
| tomme_felt | 0.000 | -0.240 | 0.000 | 0.014 | 0.0% | 0.839 | forslag, kategori, utsteder tomme |

## arbeid/hack/c1/data_v3

| test | AVVIK-F1 | endring | recall | PR-AUC | rutet til menneske | MOT-F1 | hva |
|---|---|---|---|---|---|---|---|
| basis | 0.000 | +0.000 | 0.000 | 0.112 | 0.9% | 0.000 | uendret |
| nye_selskaper | 0.000 | +0.000 | 0.000 | 0.112 | 0.9% | 0.000 | 2181 av 3137 train-rader fjernet (selskap i holdout) |
| siste_aar | 0.363 | +0.363 | 0.318 | 0.215 | 0.9% | 0.363 | train fra 2024-07-01: 1506 av 3137 rader |
| tom_tekst | 0.000 | +0.000 | 0.000 | 0.112 | 0.9% | 0.000 | forslag tom i alle holdout-rader |
| tomme_felt | 0.000 | +0.000 | 0.000 | 0.104 | 100.0% | 0.000 | forslag, kategori, utsteder tomme |

KP: forventet basis AVVIK-F1 0,24 på data/ (smed3 #1950), fikk 0,240.

## Funn
1. **Tom tekst gir trygg FOR, ikke menneske.** På Vanguard-data (data/) faller F1 0,240 → 0,000 når forslagsteksten mangler,
   og 0,0 % rutes til menneske. Agenten faller tilbake til «selskapets forslag: støtte (PIV ¶1)» med høy konfidens.
   På data_v3 med tomme felt rutes 100 %, så oppførselen er ulik mellom datasett. Fiks (smed3, agent.py `vurder`):
   tom/kort `forslag` → konfidens < 0,6 og grunn «mangler forslagstekst».
2. **Ett år historikk slår tre år på NBIM (data_v3): F1 0,000 → 0,377** (P ≈ 0,43, R 0,333, 98 MOT).
   Årsak: `kalibrer` slår av `presedens_pay` når treffraten på train er < 0,5 (n ≥ 5). Med hele train skjer det,
   med siste år får regelen for få treff til å bli kalibrert, og den står på. En presisjon på 0,43 mot basisrate 0,10
   er sterk for F1. Grensen bør være relativ til basisraten (f.eks. p > 2 × avviksrate), ikke 0,5. Dette er trolig
   det største enkeltløftet for agenten på NBIMs egne stemmer → #1959 (smed3).
3. **Nye selskaper:** ingen endring på noen av datasettene (F1 lik), fordi agenten nesten bare bruker tekstregler.
   På data/ er splitten allerede streng (0 selskaper overlapper), så testen er en no-op der. På data_v3 fjernes
   2181 av 3137 train-rader uten endring: presedens fyrer ikke uansett når den er kalibrert av.
4. **Siste år på data/** er en no-op: train dekker bare 2025-07..2026-05.
5. **Ikke deterministisk over tid:** PR-AUC på data/ basis varierte mellom 0,229, 0,252 og 0,277 i løpet av 5 min,
   fordi smed3s DEF 14A-cache (varianter/smed3_utf_sitat/data/def14a) fylles mens vi kjører. F1 var stabil.
   Ved endelig leveranse: frys cachen eller logg hashen av den.

## Bruk på andre agenter
`--agent "python3 -I sti/modell.py {train} {test} {pred}"`, `--data <mappe med train/test_input/fasit>` (kan gjentas).
Hele kjøringen tar ca. 45 s fra kald start (10 agentkjøringer à 5 s).

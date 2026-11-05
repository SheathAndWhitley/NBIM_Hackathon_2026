# Case 1: t4-historikk og NPX inn i smed2s miks-modell (#2081, smed3)

Kode: `arbeid/oppgave_2081/train.py` (kopi av smed2s train.py fra #2075, med `--t4`, `--npx`, `--npx_vekt` og `--test`).
Data: real_votes (gudens fil 05.11 11:42). Alle varianter bruker miks (logreg+tfidf og LightGBM, rangsnitt) med `--hist 2`.

Lekkasjesjekk: historikken bruker bare etiketter fra møter strengt før saksdatoen (`merge_asof`, `allow_exact_matches=False`)
og bare fra real-rader. Modellen leser aldri rationale_text, rationale_section, position_paper, nbim_vote eller funds_disagree
(det sjekkes med assert i koden). NPX har 0 felles selskaper, møter og tickere med real, så NPX-radene er bare ekstra
treningsrader (med prefiks på company_id og `kilde` som trekk), bare split_year < 2026. Til val-trening brukes split_year 2024, altså NPX før 2025.

C og grense er valgt bare på val 2025 (trent på data før 2025). Test 2026 kjøres én gang, og bare for den valgte varianten.

| variant | val F1 | val P | val R | val PR-AUC | test F1 | test P | test R |
|---|---|---|---|---|---|---|---|
| base miks h2 (smed2) | **0,522** | 0,593 | 0,466 | 0,474 | **0,482** | 0,465 | 0,500 |
| + t4 (samme tekst i selskapet sett før, aldri MOT) | 0,506 | 0,642 | 0,418 | 0,444 | ikke kjørt | | |
| + NPX vekt 1 | 0,492 | 0,579 | 0,427 | 0,447 | ikke kjørt | | |
| + NPX vekt 0,5 | 0,489 | 0,541 | 0,447 | 0,453 | ikke kjørt | | |
| + NPX vekt 0,3 | 0,494 | 0,606 | 0,418 | 0,463 | ikke kjørt | | |
| + NPX vekt 0,1 | 0,503 | 0,592 | 0,437 | 0,433 | ikke kjørt | | |
| + t4 + NPX | 0,494 | 0,627 | 0,408 | 0,448 | ikke kjørt | | |
| bare logreg / + t4 | 0,485 / 0,476 | | | | | | |
| bare LightGBM / + t4 | 0,478 / 0,489 | | | | | | |

Valgt på val: base, uten nye trekk. Test 2026 med maaler_offisiell_v2 (real, test): F1 0,4818, P 0,465, R 0,500,
TP 33, FP 38, FN 33, PR-AUC 0,524. F1 faller fra val til test med 0,04.

Funn:
- Begge trekkene er nøytrale eller litt negative. Med bare 103 MOT i val er usikkerheten omtrent ±0,05, så ingen forskjell er signifikant.
- t4 tilfører ikke noe nytt fordi miks h2 allerede har nøkkelen selskap+tekst (antall, rate og «noen gang MOT»).
  Den eneste nye biten er «sett før, aldri MOT», og den trekker PR-AUC ned.
- NPX (amerikanske fonder, andre selskaper) senker PR-AUC på val ved alle vekter. Det er et annet stemmemønster enn NBIMs.
- Svarfil: `arbeid/oppgave_2081/svar_valgt_base.csv` (rad,p). Forsøk #1068 på tavla står selvrapportert, fordi tavla avviste
  målingen: «måleren er endret på disk (8733327407 -> 474eae7bc8)». Dommeren må sette måleren på nytt, så kan forsok-vakt måle om.
- Måleren viser «streng MOT 0» for rad,p-formatet. Det feltet regnes ikke for radformatet og er ikke et modellresultat.

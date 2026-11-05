# Case 1: tallforklaring til juryen (hvorfor «følg styret» gir 0 på MOT)

Speider, oppgave #2077, 05.11 kl. 12.30. Alle tall er fra `arbeid/hack/c1/maaler_offisiell_v2.py --data real` (NBIMs ekte stemmer, val = 2025, test = 2026), med forsøks-id fra `tavle forsok-list`.

## Norsk
**Hva hovedtallet måler.** Hovedtallet er F1 på saker der NBIM stemte *mot styrets anbefaling* (MOT eller AVSTÅ, `against_board=1`). Det er sjeldne saker: 103 av 1909 i val 2025 (5,4 %) og 66 av 1539 i test 2026 (4,3 %). F1 = harmonisk snitt av presisjon (hvor mange av de flaggede som var ekte avvik) og treff (hvor mange av de ekte avvikene vi fant). Accuracy er ubrukelig her: «følg styret» har ca. 95 % riktig uten å finne et eneste avvik.

**Hvorfor «følg styret» gir 0 per definisjon.** Grunnlinja sier aldri at NBIM går mot styret. Da blir TP = 0, treff = 0 og F1 = 0, uansett data. Det er ikke en svak modell, det er en modell som ikke prøver. Den er gulvet vi skal over, ikke løsningen (ordre #231).

**Hvorfor «alltid MOT» gir 0,102.** Flagger vi alle saker, er treff = 1 og presisjon = grunnraten 0,054. F1 = 2·0,054/(1+0,054) = 0,102 (val), 0,082 på test (presisjon 0,043). Det er det laveste tallet en modell som faktisk flagger noe bør slå.

**Felle å vite om.** Måleren skriver også et sekundært «streng MOT»-tall. Der får «følg styret» 0,20, fordi styret selv anbefaler MOT på noen aksjonærforslag. Det tallet er ikke hovedtallet og skal ikke siteres som «følg styret slår 0».

| Hva | F1 avvik | Vindu | Forsøk | Status |
|---|---|---|---|---|
| Følg styret | 0 | val 2025 | #1034 (dommer2) | målt av tavla (måler e8f70d3904) |
| Følg styret | 0 | alle vinduer | #1035 (dommer2) | selvrapportert, reprodusert av speider |
| Alltid MOT | 0,102 / 0,082 | val / test | notat i #1034 og #1035 | reprodusert av speider (baseline-kommando) |
| Agenten, maskin alene (miks LR+LGBM + NBIM-sitat, 10 % ruting), kald start | **0,482** (P 0,465, R 0,50; TP 33 FP 38 FN 33) | test 2026, én gang | #1046 (smed), samme modell #1037 (smed2) | selvrapportert; speider reproduserte 0,4818 med offisiell måler v2 kl. 12.25 (#1066). Dommerens omåling står i #2062 |
| Samme modell | 0,522 | val 2025 (grense valgt her, optimistisk) | #1056 (smed3) | selvrapportert |
| Eldre hovedtall, variant b | 0,474 | test 2026 | #1023 (dommer), byte-lik #1024 | målt av tavla, men på eldre dataversjon (måler ee16e5945c); fila passer ikke med dagens test-id-er |
| Ruting til menneske 10 % (menneske antatt riktig) | 0,648 | test 2026 | #1027 (dommer2) | selvrapportert, øvre grense |

Kort: fra 0 (følg styret) og 0,08 (alltid MOT) til 0,48 for maskinen alene på 2026-data den aldri har sett. Målet var 0,5.

## English
**What the headline number measures.** F1 on items where NBIM voted *against the board's recommendation* (AGAINST or ABSTAIN). These are rare: 103 of 1909 items in val 2025 (5.4 %), 66 of 1539 in test 2026 (4.3 %). Accuracy is meaningless here: "follow the board" is ~95 % accurate while finding zero dissent votes.

**Why "follow the board" scores 0 by definition.** It never predicts a vote against the board, so true positives = 0, recall = 0 and F1 = 0 on any data. It is the floor, not a solution.

**Why "always against" scores 0.102.** Recall = 1, precision = base rate 0.054, so F1 = 2·0.054/1.054 = 0.102 (val), 0.082 on test.

**Caveat.** The meter also prints a secondary "strict AGAINST" F1 where "follow the board" gets 0.20, because boards themselves recommend AGAINST on some shareholder proposals. That is not the headline metric.

**Our agent.** Machine alone, cold start, test 2026 run once: F1 0.482 (P 0.465, R 0.50), attempt #1046 (self-reported, reproduced by the scout on the official meter v2 as #1066; formal re-measurement by the judge pending in #2062). Val 2025: 0.522 (#1056, threshold tuned on val, optimistic). The earlier 0.474 (#1023, judge-measured) was on an older data version. Routing 10 % to a human gives an upper bound of 0.648 (#1027).

# Case 1: beste treffprosent for maskinen alene (smed2 #2018)

**Svar:** Maskinen alene kommer opp i **91,2 % treff** på test 2026 når grensa velges for treff på val 2025. Det er 1,5 poeng over «følg styret» (89,65 %), men langt fra 94 %. Taket for denne modellen ligger på ca. 91,3 %, selv om vi jukser og velger grensa på test.

Frosset modell (variant b, `train_v3.py --lekkasjefri`), ingen trening. Grenser valgt på VAL 2025 (1506 saker, 136 MOT), test 2026 kjørt én gang (1246 saker, 129 MOT).

| Variant (grense valgt på val) | Treff test 2026 | P (MOT) | R (MOT) | MOT-flagg | tp / fp / fn |
|---|---|---|---|---|---|
| Følg styret | 89,65 % | – | 0 | 0 | 0 / 0 / 129 |
| Agenten i dag (grense for F1) | 85,2 % | 0,376 | 0,643 | 221 | 83 / 138 / 46 |
| **(1) Én grense for treff: p_mot ≥ 0,537** | **91,17 %** | **0,757** | **0,217** | **37** | 28 / 9 / 101 |
| (2) Grense per selskapstype | 89,49 % | 0,491 | 0,426 | 112 | 55 / 57 / 74 |
| Tak: beste grense valgt på test (jukse-tall) | 91,33 % | 0,800 | 0,217 | 35 | 28 / 7 / 101 |

- (1) På val ga grensa 91,43 % (følg styret 90,97 %). Den holdt seg på test. `maaler.py` ga samme tall: accuracy 0,9117, F1 0,337.
- (2) Selskapstype etter NBIMs egen historikk: ny (ingen historikk, grense 0,50), historikk uten MOT (0,815), historikk med MOT (0,332). Den slo (1) på val (91,70 mot 91,43 %, målt i samme utvalg som grensene ble valgt på, altså optimistisk), men tapte på test. Den er overtilpasset: hist_mot-gruppa har bare 46 MOT på val. «Grense per sakskategori» kunne ikke prøves fordi alle sakene er say-on-pay.

**Hvorfor taket er rundt 91 %:** 94 % på 1246 saker betyr høyst 74 feil. «Følg styret» har 129 feil. Hvert MOT-flagg sparer én feil når det treffer og koster én når det bommer. For å nå 94 % må maskinen finne minst 55 flere ekte MOT enn falske alarmer. Med beste grense finner den 28 ekte og 7 falske, altså 21 netto. Under toppen av rangeringen er presisjonen under 50 %, og da koster hvert nytt flagg mer treff enn det gir. 94 % krever altså ca. 2,5 ganger så mange sikre funn, med presisjon over ~75 % helt ned til recall 0,45. PR-AUC er 0,455, og modellen er nær den grensa. Det går ikke uten nye opplysninger, og modellen fryses kl. 16.

**Avveiingen for juryen:** Velger vi grensa for treff, finner maskinen bare 28 av 129 MOT-stemmer (R 0,22). Til gjengjeld holder 3 av 4 flagg. F1-grensa finner 83 av 129, men 6 av 10 flagg er falske. Over 94 % treff krever menneske i loopen (ruting, dommer #2017), ikke en ny grense.

**Merk:** p_mot ≥ 0,114 på denne fila gir 79,5 %, ikke 85,2 %. Agenten bestemmer på rå score, og 0,114 er et trinn som rommer mange saker. Raden «Agenten i dag» er derfor hentet fra dommer #2010.

**Kjør på nytt:**
`python3 -I arbeid/oppgave_2018/treff.py arbeid/oppgave_1997/b_val.csv arbeid/hack/c1/data_v3_val arbeid/oppgave_1997/b_test.csv arbeid/hack/c1/data_v3 --test` (utdata i `arbeid/oppgave_2018/treff_kjoring.txt`). Måler: `python3 -I arbeid/hack/c1/maaler.py arbeid/oppgave_2018/treff_test2026.csv --fasit arbeid/hack/c1/data_v3/fasit.csv`. Tavleforsøk #1029.

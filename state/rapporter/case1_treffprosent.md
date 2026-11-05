# Case 1: treffprosent for hele systemet ved 0–20 % ruting til menneske (#2017, svar på #226)

**Kort svar:** Med grensa vi leverer (0,1833) må **12 % av sakene til menneske, skjevt rutet**, for å nå 94 % treff. Grense og c er låst på val 2025. Det ga **94,8 % på val og 94,4 % på test 2026** (95 % KI 93,1–95,6), med 12,3 % rutet på test. Symmetrisk ruting når ikke 94 % på test før rundt 25–30 %.

**Antagelse:** Systemtallet antar at mennesket avgjør alle rutede saker riktig. Det har vi ikke målt. Tallet er derfor en **øvre grense**. Hvis mennesket bommer på en andel f av de rutede sakene, faller systemtreffet med f × rutet andel (f.eks. 12 % rutet og 10 % menneskefeil gir −1,2 pp).

## Oppsett
- Rå p_mot fra kald start #1995 (variant b, `oppgave_1995/kald.sh`): val 2025 er trent på 2024, test 2026 på 2024+2025. Fila er byte-lik `oppgave_1993/raa_test.csv`.
- Treff = andel saker der FOR/MOT er riktig. **System** = maskinens treff på sakene den beholder + rutede saker regnet som riktige, delt på alle saker. **Maskin** = treff bare på sakene maskinen beholder.
- Ruting: |logit(p) − logit(grense) − c| ≤ bredde. Bredden er kvantilen som gir rutet andel på val. Symmetrisk: c = 0. Skjev: c velges på val fra −3 til +3 i steg på 0,25 og maksimerer systemtreff.
- Klyngebootstrap: 2000 trekk på selskap (cusip), test.
- Test er kjørt med låste verdier. Én ekstra kjøring la bare til KI for 7/12/23 %. Den er deterministisk og endret ingen valg.
- Kode: `arbeid/oppgave_2017/treff.py`. Utskrift: `treff.txt`. Låste verdier: `laast_paa_val_2017.json`.

## Grensa vi leverer (0,1833, F1-optimal på val)
Følg styret: val 91,0 %, test **89,7 %** [88,0–91,3].

| ruting (val) | type | c | val system | test rutet | **test system** [95 % KI] | test maskin alene [KI] |
|---|---|---|---|---|---|---|
| 0 % | – | – | 86,2 % | 0 % | **85,2 %** [83,2–87,2] | 85,2 % |
| 5 % | sym | 0 | 88,1 % | 4,5 % | 87,3 % [85,4–89,2] | 86,7 % [84,7–88,7] |
| 5 % | skjev | +0,50 | 90,0 % | 5,6 % | 89,4 % [87,6–91,1] | 88,8 % [86,9–90,6] |
| 10 % | sym | 0 | 90,0 % | 9,6 % | 89,1 % [87,3–90,8] | 87,9 % [86,0–89,8] |
| 10 % | skjev | +0,50 | 93,6 % | 9,8 % | **92,8 %** [91,3–94,2] | 92,0 % [90,4–93,6] |
| 12 % | skjev | +0,75 | **94,8 %** | 12,3 % | **94,4 %** [93,1–95,6] | 93,6 % [92,1–95,0] |
| 15 % | sym | 0 | 91,8 % | 15,1 % | 91,1 % [89,4–92,6] | 89,5 % [87,6–91,3] |
| 15 % | skjev | +1,25 | 96,2 % | 16,1 % | 96,3 % [95,3–97,3] | 95,6 % [94,3–96,7] |
| 20 % | sym | 0 | 93,4 % | 21,7 % | 92,6 % [91,1–94,0] | 90,6 % [88,6–92,3] |
| 20 % | skjev | +1,00 | 96,7 % | 21,0 % | **96,8 %** [95,8–97,7] | 95,9 % [94,7–97,1] |
| 23 % | sym | 0 | 94,3 % | 23,9 % | 92,9 % [91,4–94,3] | 90,7 % [88,8–92,5] |

- Minste andel med ≥ 94 % på val: **skjev 12 %** gir 94,4 % på test. **Symmetrisk 23 %** gir bare 92,9 % på test.
- Regnestykket i oppgaven stemmer: skjev 10 % gir 92,8 % og skjev 20 % gir 96,8 %.
- Skjev 10 % med c = +0,50 er samme oppsett som F1-rutingen i #1995. Her ga treff og F1 samme valg av c.

## Kontroll: grense valgt for treff i stedet for F1 (0,4503 på val, ikke levert)
Maskinen alene: test 90,6 % [88,9–92,2]. Det er 0,9 pp over følg styret, men MOT-recall faller fra 0,64 til **0,34** (F1 0,43). Ruting nær denne grensa gir sym 7 % → test 94,1 % [92,9–95,4], 12 % → 95,7 % og 20 % → 96,7 %.
Skjev ruting med stor c rundt F1-grensa gjør i praksis det samme: båndet flyttes opp mot p ≈ 0,4–0,5. Den store gevinsten kommer av å sende de **tvetydige høy-p-sakene** til menneske, ikke av selve grensevalget.

## Ærlige forbehold
1. **Menneske antatt riktig** (se over). Det er en antagelse, ikke et funn.
2. **Treff er et svakt mål her.** 89,7 % av sakene er FOR, så «følg styret» gir 89,7 % uten å finne en eneste MOT. Systemtreffet stiger mekanisk med rutet andel: hver rutet sak teller som riktig. Juryen bør se treff **sammen med** MOT-recall og F1 (skjev 10 %: system-F1 0,648, R 0,643; skjev 20 %: F1 0,820, R 0,705, `case1_ruting_verifisert.md`).
3. **Maskin alene på resten** blir bedre bare fordi de vanskelige sakene er tatt bort (seleksjon). Tallet viser ikke at modellen er blitt bedre.
4. Ca. 2 pp KI-bredde hver vei: 129 MOT-saker på test og klynging på selskap.

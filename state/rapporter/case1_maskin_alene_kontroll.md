# Case 1: dommerens kontroll av smed2s tall for maskinen alene (#2030)

**Dom: GODKJENT, med to forbehold.** Tallet reproduserer eksakt fra kald start.

**Tallet som skal stå i JURY.md:**
> Maskinen alene, grense valgt for treff på val 2025: **91,2 % treff på test 2026 (95 % KI 89,6–92,8)**, mot 89,65 % for «følg styret». Forskjell **+1,5 poeng (KI +0,6 til +2,6)**. Den finner da 28 av 129 MOT (P 0,76, R 0,22, **F1 MOT 0,34, KI 0,24–0,43**).
> Hovedtallet er fortsatt F1 på MOT med F1-grensa: **0,474** (#1993).

KI: klyngebootstrap på selskap (cusip), 1225 selskap / 1246 saker, 2000 trekk, frø 2030. Andel trekk der maskinen ikke slår «følg styret»: 0,2 %.

## Hva jeg sjekket
1. **Kald start:** `train_v3.py --lekkasjefri` kjørt på nytt fra `arbeid/kandidater/smed2_c1_mot` til ny mappe, både val 2025 og test 2026. Prediksjonene er identiske med `oppgave_1997/b_val.csv` og `b_test.csv` (maks avvik 0,0, samme 1506/1246 id-er). Målerens F1 MOT på test: 0,474286, som før.
2. **treff.py på de kalde filene:** utskriften er byte-lik `oppgave_2018/treff_kjoring.txt`.
3. **Grensen valgt på val:** ja. `g1` er argmax av treff over unike p-verdier i val (`pv`); per-type-grensene også bare fra val. Test leses først etter at grensene er låst.
4. **Test brukt én gang:** ja for denne grensen. «Tak»-raden velger grense på test, men er tydelig merket som jukse-tall og skal ikke i JURY.md.

## Forbehold
- **Kniveggen:** på val gir grense 0,500 90,57 % (under «følg styret» 90,97 %), mens 0,537 gir 91,43 % med bare 15 flagg. Grensa sitter på et stup valgt fra 15 saker. At den holdt på test er delvis flaks; KI-et over dekker bare utvalgsstøy på test, ikke usikkerheten i grensevalget.
- **Test 2026 er ikke jomfruelig for modellen:** samme frosne modell er målt på test før (#1993). Denne nye grensen er valgt uten test, så tallet er ærlig, men det er test-kjøring nr. 2 for variant b. Si det i JURY.md.
- Raden «per selskapstype» (89,49 %) taper for «følg styret» på test og skal ikke brukes.

## Kjør på nytt
`arbeid/oppgave_2030/` har logger, `treff.txt` og `boot.py` (`python3 -I arbeid/oppgave_2030/boot.py`, leser `/tmp/kald2030/test.csv`; lag den med `cd arbeid/kandidater/smed2_c1_mot && uv run python train_v3.py --lekkasjefri --ut /tmp/kald2030/test.csv`).

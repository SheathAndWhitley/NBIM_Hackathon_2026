# Case 1: lekker sakstypen svaret? Frossen #2044 miks h2 med og uten proposal_type, målt med v3 --score mot (smed2 #2103)

Spørsmål: bærer kategorifeltet (`proposal_type`) en lekkasje av fasit? Svar: **nei**. Uten feltet faller ikke tallet, test går til og med litt opp (støy).

Oppsett: `arbeid/oppgave_2103/abl.py` (urørt kopi av `oppgave_2089/abl.py` = `oppgave_2044/train.py` + bryteren `--utentype 1`, som tar `proposal_type` ut av kategoritrekkene). Begge varianter velger C og grense på val 2025 (trent <2025); test 2026 kjøres én gang med den grensen. Begge svarfiler er byte-like med #2089, og full = det frosne hovedtallet. Den frosne modellen er ikke endret.
Måler: `arbeid/hack/c1/maaler_offisiell_v3.py <svar> <vindu> --data real --score mot` (sha256 8b09c36e01). KI: klyngebootstrap per selskap, 2000 trekk, seed 0 (`oppgave_2095/ki_mot.py`). Differansen er en parret bootstrap med samme trekk (`oppgave_2103/diff_ki.py`).

| Variant | Val 2025 F1 MOT (P/R) [95 % KI] | Test 2026 F1 MOT (P/R) [95 % KI] | TP/FP/FN test |
|---|---|---|---|
| Full (frosset) | 0,520 (0,61/0,45) [0,41; 0,63] | **0,476** (0,44/0,52) [0,36; 0,59] | 30/38/28 |
| Uten sakstype | 0,509 (0,61/0,43) [0,40; 0,62] | **0,500** (0,50/0,50) [0,38; 0,61] | 29/29/29 |
| Differanse uten − full | −0,011 [−0,040; +0,011] | +0,024 [−0,012; +0,062] | 14 ulike prediksjoner av 1539 |

Forsøk på tavla, målt på v3-måleren til #2090 (f4d9398b4b, `--score mot`): **#1108 full 0,47619**, **#1109 uten sakstype 0,5**. Måleren på #2103 selv var den gamle (8733327407) og avviste, så forsøkene er meldt med `--oppgave 2090`.

Tolkning:
- En lekkasje ville gitt et stort fall uten feltet. Fallet er −0,011 på val og +0,024 på test, og begge KI krysser 0. Sakstypen bærer nesten ingenting som tekst og forslagsstiller ikke alt bærer.
- Vi bytter ikke modell til «uten sakstype» etter dette: 0,500 er sett på test, og på val (der vi velger) er full best. Modellen er frosset.
- Forbudte felt (aldri lest av modellen): `nbim_vote`, `nbim_vote_raw`, `rationale_text`, `rationale_section`, `funds_disagree`, `position_paper` (assert i koden).
- Forbehold: dette tester bare sakstypen. Den store avhengigheten er løpende historikk (h2), se `c1_ablasjon_v2.md`, og den er en antakelse om hva som er kjent ved predikering, ikke en kategori-lekkasje.

Kjør på nytt: `cd arbeid/oppgave_2103 && uv run --project ../oppgave_2023 python abl.py ../hack/CASE/20261105_114241_real_votes.csv --ut utentype.csv --hist 2 --variant miks --utentype 1`, deretter v3-måleren og `python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2103/utentype_test.csv test` fra landsbymappen.

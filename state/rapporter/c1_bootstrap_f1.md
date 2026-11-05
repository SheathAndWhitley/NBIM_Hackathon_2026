# Case 1: 95 %-intervall for F1 på MOT (bootstrap, #2086)

**Hva:** Klyngebootstrap per selskap (company_id), 2000 trekk, seed 0, på NBIMs egne stemmer (real_votes).
MOT = `against_board` (samme som rundens måler `maaler_offisiell_v2.py`). Ingen modellvalg skjer her.
**Frysekandidat:** standardløpet i `levering/kjor_agent.py` = `oppgave_2044/train.py --variant miks --hist 2`, kjørt uendret.
Punkttallet på test (0,482, TP 33 FP 38 FN 33) er det samme som måleren gir i `levering/kjor_agent_real_test2026.txt`.
**Skript:** `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2086/bootstrap_f1.py` (5 s). Utdata: `arbeid/oppgave_2086/ut.txt`.

## Til JURY.md

| Sett | Modell | F1 MOT | 95 % KI (per selskap) | P | R | flagget / MOT |
|---|---|---|---|---|---|---|
| **test 2026** (1539 saker, 135 selskaper) | frysekandidat | **0,482** | **[0,375; 0,580]** | 0,465 | 0,500 | 71 / 66 |
| test 2026 | presedensregel | 0,100 | [0,075; 0,128] | 0,053 | 0,833 | 1029 / 66 |
| test 2026 | følg styret (gulv) | 0,000 | [0,000; 0,000] | – | 0 | 0 / 66 |
| val 2025 (1909 saker, 165 selskaper) | frysekandidat | 0,522 | [0,403; 0,624] | 0,593 | 0,466 | 81 / 103 |
| val 2025 | presedensregel | 0,142 | [0,103; 0,186] | 0,077 | 0,903 | 1207 / 103 |
| val 2025 | følg styret (gulv) | 0,000 | [0,000; 0,000] | – | 0 | 0 / 103 |

Parvis forskjell (samme trekk), test 2026: frysekandidat − presedensregel +0,381 [+0,282; +0,473];
frysekandidat − følg styret +0,482 [+0,375; +0,580]. Alle 2000 trekk > 0 i begge.

## Slik leses det
- **Usikkerheten er stor:** ±0,10 rundt 0,48. Det skyldes at test bare har 66 MOT-saker. Sier vi «0,48», bør vi si «mellom 0,38 og 0,58».
- **Kandidaten slår begge grunnlinjene klart.** Hele intervallet ligger over null og over presedensregelen.
- **Val er for optimistisk.** C og grense er valgt på val 2025, så 0,522 er målt på samme data som valget. Test 2026 er det ærlige tallet. Fallet fra val til test (−0,04) ligger godt innenfor intervallene.
- Trekk per rad gir nesten like intervaller (test [0,372; 0,581]). Saker fra samme selskap henger altså lite sammen her. Vi rapporterer likevel intervallet per selskap, fordi det er det strengeste.
- Presedensregelen er beregnet slik: MOT hvis NBIM gikk mot styret i selskapet på et møte før denne datoen. Den flagger 2/3 av sakene og har lav presisjon. Den gamle regelen på N-PX (0,383 i JURY.md) er en annen regel på andre data, og tallene kan ikke sammenlignes.
- Endres frysemodellen etter dette, kjøres skriptet på nytt. Det leser train.py direkte.

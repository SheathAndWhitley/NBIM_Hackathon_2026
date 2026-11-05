# Case 1: kontroll av bootstrap-intervallene i TREFFSIKKERHET.md (#2186): GODKJENT

Dommer2, 05.11 kl. 13.2x. Kontrollerer smed3s intervaller (#2185) i `arbeid/hack/levering/TREFFSIKKERHET.md`.

## Metode
Eget skript `arbeid/oppgave_2186/ki_kontroll.py`, skrevet uten å se på `treffsikkerhet_ki.py`: persentil-bootstrap,
10 000 trekk, frø 2186 (smed3: 2000 trekk, frø 2185). Fasitregler fra `maaler_offisiell_v3.py` (test 2026, real).
Clopper-Pearson regnet på nytt med scipy `beta.ppf`. Utdata: `arbeid/oppgave_2186/mine_ki_B10000.txt`.
Punkttallene stemmer eksakt: TP 30, FP 38, FN 28, TN 1443. For konfidens ≥ 0,6: TP 9, FP 0, FN 17.

## Sammenligning (95 %, prosent)

| Del | Mål | smed3 bootstrap | dommer2 bootstrap | største avvik | CP smed3 | CP dommer2 |
|---|---|---:|---:|---:|---:|---:|
| Alle | recall | 39,1–65,2 | 38,6–64,4 | 0,8 pp | 38,2–65,0 | 38,2–65,0 |
| Alle | presisjon | 32,8–56,2 | 32,4–55,9 | 0,4 pp | 32,1–56,7 | 32,1–56,7 |
| Konf ≥ 0,6 | recall | 15,8–55,0 | 16,7–53,8 | 1,2 pp | 17,2–55,7 | 17,2–55,7 |
| Konf ≥ 0,6 | presisjon | 100–100 | 100–100 | 0 | 66,4–100 | 66,4–100 |

Alle avvik under 2 pp. Clopper-Pearson er likt på desimalen. Teksten om at presisjon 100 % bygger på 9 forslag
og at bootstrap blir degenerert, stemmer.

## Merknader (feller ikke dommen)
1. **Hovedtallet F1 på MOT mangler intervall** i fila. Mitt: F1 47,6 %, 95 % 36,2–57,7 % (alle saker). Juryen
   vekter F1 på MOT som hovedtall, så linja bør inn i tabellen (#2185 eller etterfølger).
2. Bootstrap per sak antar uavhengige saker. Trekker jeg hele møter (140 møter), blir intervallene litt bredere:
   recall alle 37,1–66,7 %, F1 alle 35,2–58,6 %, recall konf ≥ 0,6 14,3–57,7 % (opptil 2,7 pp bredere i øvre ende).
   Ærlig formulering: «per-sak-bootstrap; per møte blir det noen poeng bredere».

Kommando: `python3 -I arbeid/oppgave_2186/ki_kontroll.py arbeid/hack/levering/kjor_agent_real_pred_maaler.csv`

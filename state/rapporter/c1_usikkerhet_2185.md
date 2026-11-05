# Case 1: 95 %-intervall på recall og presisjon MOT (#2185, smed3)

Skript: `arbeid/hack/levering/treffsikkerhet_ki.py` (importerer treffsikkerhet.py og måler v3, sjekker 2x2 mot T.tell).
Kommando: `cd arbeid/hack/levering && python3 -I treffsikkerhet_ki.py kjor_agent_real_pred_maaler.csv` (2000 trekk, frø 2185, ~2 s).

| Del | Mål | Punkt | Bootstrap 95 % | Clopper-Pearson |
|---|---|---:|---:|---:|
| Alle 1539 | recall | 51,7 % | 39,1–65,2 % | 38,2–65,0 % |
| Alle 1539 | presisjon | 44,1 % | 32,8–56,2 % | 32,1–56,7 % |
| Konf ≥ 0,6 (1356) | recall | 34,6 % | 15,8–55,0 % | 17,2–55,7 % |
| Konf ≥ 0,6 (1356) | presisjon | 100 % | 100–100 (degenerert, 9/9) | 66,4–100 % |

Funn: intervallene er brede (±13 pp), så F1-forskjeller på noen få poeng mellom varianter er støy.
Presisjon 100 % i båndet ≥ 0,6 er 9 av 9; eksakt nedre grense er 66 %, og det står nå i pakka.
Lagt inn i levering/TREFFSIKKERHET.md med kommando. c1_tallvakt.py: OK (139 stemmer, 0 avvik). fremmed.sh: utgang 0, TALLVAKT GRØNN.

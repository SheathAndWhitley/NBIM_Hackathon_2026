# Case 1: terskeltabellen etter frys mot jurytekstene (#2471, smed4)

**Svar: ingen ULIK.** Ingen av de tre jurytekstene har hele terskeltabellen (t = 0,70 … 0,98). De gjengir bare den leverte raden (t = 0,9188), og den er lik den nye kjøringen i alle tall.

Grunnlag: ny tabell fra kald kopi etter frys (`state/rapporter/c1_terskeltabell_etter_frys.md`, #2381). Tekstene lest i nyeste jury-zip `/tmp/jurypakke_c1_2457.zip` (15:57), utpakket i `/tmp/smed4_2381_kald/`. JURY.md, ERLIG_EVALUERING.md og NESTE_VERSJON.md i zipen er byte-like kildene i `arbeid/hack/c1/leveranse/` (cmp, 16:05).

## Rad for rad (ny tabell → jurytekstene)
| t | Ny (TP/FP/FN, P, R, F1, flagget) | JURY.md | ERLIG_EVALUERING.md | NESTE_VERSJON.md |
|---|---|---|---|---|
| 0,70 | 44/360/14, 0,109, 0,759, 0,190, 404 | står ikke | står ikke | står ikke |
| 0,80 | 41/176/17, 0,189, 0,707, 0,298, 217 | står ikke | står ikke | står ikke |
| 0,85 | 38/108/20, 0,260, 0,655, 0,373, 146 | står ikke | står ikke | står ikke |
| 0,90 | 34/51/24, 0,400, 0,586, 0,476, 85 | står ikke | står ikke | står ikke |
| **0,9188 levert** | **30/38/28, 0,441, 0,517, 0,476190, 68** | **LIK** (l. 5: 30 av 58, 38 av 68 falske; l. 12: 0,476190; l. 66: P 0,441, R 0,517, 68 flagg, 38 falske, 28 oversett) | **LIK** (l. 6: 0,476, P 0,441, R 0,517; l. 38: TP 30 FP 38 FN 28; l. 68: 0,441/0,517/0,476) | **LIK** (l. 4–5: 0,476, TP 30 FP 38 FN 28) |
| 0,94 | 29/27/29, 0,518, 0,500, 0,509, 56 | står ikke | står ikke | står ikke |
| 0,96 | 26/13/32, 0,667, 0,448, 0,536, 39 | står ikke | står ikke | står ikke |
| 0,98 | 16/3/42, 0,842, 0,276, 0,416, 19 | står ikke | står ikke | står ikke |

## Merknader (ikke avvik)
- JURY.md l. 42–47 har en tabell over **rutingsbånd** for P(MOT) ([0,25; 0,75), [0,15; 0,85), [0,05; 0,95)). Det er ikke F1-terskeltabellen og kan ikke sjekkes mot #2381.
- KI: tekstene sier 95 % KI [0,36; 0,59] (klyngebootstrap per selskap, `kilder/oppgave_2095_ki_mot.py`). Bootstrap i #2381 er over 140 møter og gir [0,344; 0,594] for levert terskel. Ulik metode, så ikke ULIK; tekstene oppgir sin metode.
- NESTE_VERSJON l. 56 «fast budsjett k=50, F1 0,517» er et budsjett, ikke en terskelrad; ikke i tabellen.
- Skal hele terskeltabellen inn i juryteksten (f.eks. som svar på «hvorfor 0,9188 når 0,96 gir 0,536 på test?»), bør det stå at 0,94/0,96 er valgt i etterkant på test og ikke er hovedtall.

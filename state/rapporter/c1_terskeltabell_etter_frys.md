# Case 1: terskeltabellen laget på nytt fra den frosne pakka etter kl. 16 (#2381, smed4)

**Svar: tallene er like til siste desimal.** Levert terskel 0,9188 gir F1 MOT **0,476190** (TP 30, FP 38, FN 28, 68 flagget) i kald kopi.

## Slik ble det kjørt (16:01–16:10)
- Kald kopi: `/tmp/jurypakke_c1_2457.zip` (nyeste jury-zip, 15:57, #2457) pakket ut i tom mappe `/tmp/smed4_2381_kald/`.
- Frosne filer mot `state/c1_frys.json` (16:00:01): **15 av 17 like sha256**. De 2 ulike er `maaler_offisiell_v2.py` og `maaler_offisiell_v3.py`. `diff` viser at eneste forskjell er datastien (`<repo>/...` → relativ til egen fil), slik `pakk_jury.sh` steg 3 gjør med vilje. Kildemåleren i landsbyen har frys-sha `418a937e…`. Regnestykket er altså uendret.
- `arbeid/oppgave_2376/sveip.py` kjørt med cwd i den kalde kopien. Den bruker kopiens svarfil og kopiens v3-måler (`--score mot`, test 2026).
- `bootstrap.py` kjørt med stiene byttet til den kalde kopien (140 møter, 2000 trekk, samme frø).

## Resultat
- `diff` mot `arbeid/oppgave_2376/sveip_ut.txt`: **identisk** (alle 8 terskler, TP/FP/FN, P, R, F1 med 6 desimaler).
- `diff` mot `arbeid/oppgave_2376/bootstrap_ut.txt`: **identisk**.
- Kontroll: 0 rader der levert anbefaling avviker fra `p_avvik >= 0,9188`.

| t | TP | FP | FN | P | R | F1 | flagget |
|---|---|---|---|---|---|---|---|
| 0,70 | 44 | 360 | 14 | 0,1089 | 0,7586 | 0,190476 | 404 |
| 0,80 | 41 | 176 | 17 | 0,1889 | 0,7069 | 0,298182 | 217 |
| 0,85 | 38 | 108 | 20 | 0,2603 | 0,6552 | 0,372549 | 146 |
| 0,90 | 34 | 51 | 24 | 0,4000 | 0,5862 | 0,475524 | 85 |
| **0,9188 (levert)** | **30** | **38** | **28** | **0,4412** | **0,5172** | **0,476190** | **68** |
| 0,94 | 29 | 27 | 29 | 0,5179 | 0,5000 | 0,508772 | 56 |
| 0,96 | 26 | 13 | 32 | 0,6667 | 0,4483 | 0,536082 | 39 |
| 0,98 | 16 | 3 | 42 | 0,8421 | 0,2759 | 0,415584 | 19 |

## Ikke kjørt på nytt
- Val 2025-tabellen i `c1_terskeltabell.md`: den bygger på val-prediksjoner fra trening, ikke på den frosne svarfila, og sveip.py dekker bare test. Ingen av de 17 frosne filene gir den direkte.
- Selve terskeltabellen ligger ikke i jury-zipen; tallene i zipen (TREFFSIKKERHET, JURYSVAR) er ikke sjekket her.

Utskrifter: `arbeid/oppgave_2381/sveip_kald.txt`, `arbeid/oppgave_2381/bootstrap_kald.txt`.

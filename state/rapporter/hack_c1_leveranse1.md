# Case 1 leveranse 1 fra kald start (dommer #1952): GRØNN, med mangler

**Resultat:** Hovedtallet reproduseres eksakt fra kald start. F1 0,476190 på MOT mot styret (test 2026, TP 30 FP 38 FN 28),
likt tavla (#2090) og likt `oppgave_2089/full_test.csv`. Leveransen ligger i `arbeid/hack/levering/c1_v1/`.

| Sjekk | Utfall |
|---|---|
| kaldstart.sh forsøk 1 (12:44) | **RØD**: `ModuleNotFoundError: retningslinje_oppslag` (sitatoppslaget #2106 var ikke i kopilista). En annen agent la fila og `punkter.jsonl` inn 12:44. |
| kaldstart.sh forsøk 2 og 3 | GRØNN 0,476190, avvik 0, 31 s og 52 s |
| README-kallet `fremmed.sh /tmp/fremmed` | kjører (32 s), `pred_maaler.csv` byte-identisk med kaldstart |
| Lekkasje i svarfila (`sjekk_lekkasje.py svar`) | OK, ingen signatur (Jaccard 0,32) |
| Lekkasje i koden (`sjekk_lekkasje.py kode`) | 17 linjer flagget, lest: fasit bare som mål og historikk; sitat bare fra år < sakens år (`c1_real.py:101`) |
| Tidssplitt | C og grense på val 2025, test én gang. Historikken h2 bruker 2026-etiketter fra møter strengt før datoen (verifisert #2098). Uten den (h1): 0,415 |
| Baseline oppgitt | følg styret F1 0; nye historikkregler målt nå: 0,091 (selskap), 0,145 (selskap+type) |

**Rettet i kravrespons.md** (c1_v1 og c1/leveranse): (1) Den sa at historikken var «bare fra år før». Feil: h2 bruker
tidligere møter i samme år. Det står nå ærlig, med h1 = 0,415 som tall. (2) «Historikkregel ikke målt» er erstattet med målte tall.

**Mangler (til #2127 / eierne):**
1. `fremmed.sh` (README-kallet) skriver til slutt `SCORE 0.481752` (avvik-sidetallet) og «streng MOT TP 0» fra måler v2.
   Den som kjører README-kallet, ser altså feil tall som siste SCORE. Den bør bruke `maaler_offisiell_v3.py --score mot` (smed2, #2116).
2. Kopilista i kaldstart.sh og fremmed.sh må følge med når agenten får nye moduler (#2106/#2114). Neste kald start må kjøres etter sitatfiksen #2120.
3. Påstanden «NBIM publiserer stemmene løpende» bærer 0,06 av F1. Juryteksten (#1975) bør vise h1 = 0,415 ved siden av hovedtallet.
4. `c1/kaldstart.sh` og `levering/` ligger ikke i git (arbeid/ er ignorert), så det finnes ingen historikk for endringen 12:44.

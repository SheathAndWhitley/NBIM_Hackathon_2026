# Case 1 (#2654): ordsjekk-treff i STÅR-reserven rettet, kl. 18:5x

**Resultat:** `bash arbeid/oppgave_2648/ordsjekk_staar.sh` viser nå bare treff som er merket riktige i STÅR
(«[0,36; 0,59]», «under målet», «Den frosne agenten står», «valgt på test»), pluss `<!-- tallvakt`-kommentarene
(skal stå til tekststoppen) og `levering/README.md:45` («TALLVAKT GRØNN», forklart på linja, kan stå).

**Rettet (13 treff), lagt i byggeskriptene så de overlever ombygging:**
- `arbeid/oppgave_2598/lag_staar.py` (README/kravrespons): kravrespons:7 «på vilkår om grønn pakke innen 18:45» →
  «på vilkår om at hele pakken med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45»; første
  «repo4» → «repo4 (frossen + fire historikktrekk)». README:12 og MUNTLIG:13 var alt rettet i #2640.
- `arbeid/oppgave_2640/rett_staar.py` (ERLIG/JURY/MUNTLIG): ERLIG:78 og J:86 repo4 forklart i overskriften;
  ERLIG:79 «ble ikke grønt før tekststoppen» → «ble ikke reprodusert fra kald start før tekststoppen»;
  «benk A/B» → «sammenligning A/B» (ERLIG:79, 93, 102, 104); «alle grønne» → «alle besto» (ERLIG:108, J:88);
  J:52 «tallvakt» → «tallsjekk».
- Kjørt: `lag_staar.py` (LIK mot BYTT før bygging) og `rett_staar.py`. Diff: ERLIG 6 linjer, JURY 3, kravrespons 1.

**Tallvakt:** `python3 -I arbeid/verktoy/c1_tallvakt.py` på treet: GRØNN, 31 filer, 196 påstander, 0 avvik.
På STÅR-filene med en frossen svarfil (`levering/c1_v1/ut/pred_maaler.csv`, F1 0,4762): alle 35 påstander om
hovedtallet stemmer. Tre avvik om «188 av 1578 til menneske» skyldes at den eneste KJORING.txt før byttet på disk
er fra en eldre kjøring (228 til menneske); tekstene har 188, som er den frosne kjøringens tall (kilder/c1_robusthet_frossen.md).
Ingen tall er endret av meg. Full STÅR-kjede fra kald kopi (tilbake_fra_zip → cp → tallvakt → pakk) er ikke kjørt på nytt;
zip 2587 ligger ikke lenger i /tmp.

**Ikke rørt:** `levering/README.md:3` (repo4 uforklart) er BYTT-fila og står på smed2 sin liste (#2639).

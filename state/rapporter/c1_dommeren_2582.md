# Case 1 #2582: to siste «dommeren» rettet til «kontrollagenten»

- kravrespons.md:10 «kontrollert av dommeren» -> «kontrollert av kontrollagenten»
- JURY_SPORSMAL.md:52 «dommeren fikk bit-identiske svarfiler» -> «kontrollagenten fikk ...»
- grep «dommeren» i begge: 0 treff. Fasit frys_fasit_1600.sha256: bare de to sha-linjene byttet.
- Tallvakt: 0 avvik (169). Ingen nye tall.
- frys_fasit mot fasit: 2 avvik, begge andres ulagrede arbeid: ERLIG_EVALUERING (smed3 §7, #2571) og demo_utskrift.txt (endret 16:54, trolig demokjøring #2577). Må committes/fasit oppdateres før 19-zipen (#2549).
- Commit fa6fae9. NB: en annen agent regenererte frys_fasit_1600.sha256 fra arbeidstreet mens jeg jobbet, så fa6fae9 har også sha for ULAGRET ERLIG_EVALUERING (smed3 §7) og demo_utskrift.txt. Fasiten stemmer altså med arbeidstreet, ikke med HEAD, til de to filene committes.

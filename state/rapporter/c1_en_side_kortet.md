# Case 1: én-sideren kortet til én side (#2197)

Fil: `arbeid/hack/levering/EN_SIDE.md`. Før: 659 ord. **Etter: 547 ord** (`wc -w`, 51 linjer). Kopi av før-versjonen: `/tmp/EN_SIDE_for_2197.md`.

Kuttet:
- Treffsikkerhetstabellen (TP/FP/FN/TN). TP 30, FP 38, FN 28 står fortsatt i hovedtabellen, og TREFFSIKKERHET.md finnes fortsatt i pakka.
- Strammet ordlyd i punkt 1, 2, 4 og 5 (ingen tall fjernet utenom tabellen).
- Fjernet «Agenten stemmer aldri selv» (begrensning 1 sier det samme).

Står fortsatt (sjekket med grep): F1 MOT 0,476 [0,36; 0,59], «Følg styret: F1 0», #2183-funnet (56 av 58, høyst 2 av 58), til-menneske-tabellen (183 av 1539, 17 av 58).

Tallvakt etterpå (`python3 -I arbeid/verktoy/c1_tallvakt.py`):
```
Måler v3 --score mot på arbeid/hack/levering/kjor_agent_real_maskin_alene.csv: F1 0.4762  P 0.4412  R 0.5172  TP 30 FP 38 FN 28  (58 MOT i fasit, 66 avvik)
Kjøring: til menneske 188 av 1578 inn (11.9%), 183 av 1539 med fasit (11.9%)
14 filer, 139 påstander om hovedtallet stemmer, 0 avviker
OK
```

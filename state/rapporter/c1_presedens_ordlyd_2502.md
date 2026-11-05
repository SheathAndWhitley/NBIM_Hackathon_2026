# Case 1 #2502: presedensregelens ordlyd rettet (dom #2484)

- Bytte i JURYSVAR pkt 5 (`arbeid/hack/levering/JURYSVAR.md:23`) og JURY_SPORSMAL pkt 3 (`arbeid/hack/c1/leveranse/JURY_SPORSMAL.md:15`):
  «avvik hvis siste stemme på samme direktør var et avvik; er direktøren ukjent fra før, brukes siste stemme på samme sakstekst» (avvik teller også AVSTÅ).
  Samsvarer med `prev_same_person.fillna(prev_same_item)`. Pkt 13 ikke rørt.
- Tall uendret. Tallvakt: 18 filer, 169 påstander, 0 avvik, OK.
- frys_fasit_1600.sha256: bare de to linjene oppdatert (hash av committet innhold). Full regenerering ville tatt med andres ukommitterte endringer (DEMO_MANUS, ERLIG_EVALUERING, NESTE_VERSJON, nye kilder osv.), så den må kjøres på nytt når de er committet.
- Commit e5029c2. NESTE_VERSJON.md (staget av andre) holdt utenfor og staget igjen som før.

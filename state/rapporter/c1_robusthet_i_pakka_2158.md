# Case 1: robusthetstabellen inn i README og BESLUTNINGSSTOTTE (smed2 #2158)

- Nytt avsnitt «Robusthet: hva agenten gjør når inndata er rare» i `arbeid/hack/levering/README.md` (sist) og `BESLUTNINGSSTOTTE.md` (før Forbehold).
- Seks rader fra `c1_robusthet_frossen.md` (etter #2152-vaktene): vanlig 0,476 / 11,9 %, nye selskaper 0,375 / 99,4 %, tom tekst 0 / 100 %, ukjent sakstype 0,476 / 100 %, uten styreanbefaling 0,467 / 100 %, land/marked mangler 0,455 / 100 %.
- Kommandoen som gjenskaper står i avsnittet. Kjørt på nytt nå til /tmp: 42 s, tabellen er identisk med rapporten.
- Tallvakta (`c1_tallvakt.py`): 13 filer, 132 påstander stemmer, 0 avviker, OK.

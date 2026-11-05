# Case 1: ett rutingtall i pakken (#2111)

Kilde: kald kjøring 05.11 kl. 12.29 (#2094, /tmp/c1_kald/ut/KJORING.txt): **228 av 1578 saker inn (14,4 %)**,
**223 av 1539 med fasit (14,5 %)** til menneske (175 nær grensen, 52 ukjent selskap, 1 instruks).

Rettet:
- `levering/kjor_agent_real_test2026.txt`: byttet ut med loggen fra den kalde kjøringen. Den gamle (12.07, 176/171)
  ligger i `arbeid/oppgave_2111/kjor_agent_real_test2026_gammel_1207.txt`. F1-tallene er de samme (0,481752).
- `levering/kjor_agent_real_test2026_LES.md`: 228/223, linjenumre 2, 16 og 23 stemmer med den nye loggen.
- `levering/KRAVRESPONS.md`: l.13 og rad 11 med 228/223; H2 merket lukket (l.20, rad 7, rad 22, l.88).
- `levering/BESLUTNINGSSTOTTE.md` l.45: 14,4 % (228 av 1578), ikke 11,2 % (176).
- `levering/README.md` l.28: tar med 223 av 1539 også.
- `c1/leveranse/BEGRENSNINGER.md` l.3: 228/223 (lå utenfor levering/, men hadde samme gamle tall).

Akseptkrav: `grep -rn '171 av\|176 av\|11,1 %' arbeid/hack/levering` gir 0 linjer. Også 0 treff på `11,2 %`.
Ikke rørt: rad 19 i KRAVRESPONS nevner fortsatt H2 som historikk for README-tallene 0,474/0,383. Dommeren bør se på det under #2113.

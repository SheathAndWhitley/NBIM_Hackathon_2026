# Case 1 #2574: «rundt 0,5» rettet i JURY_SPORSMAL, 29–52 s i ERLIG_EVALUERING
- JURY_SPORSMAL.md:15: «Vi sier «rundt 0,5», ikke 0,476.» -> «Vi leser tallet som et sted mellom 0,36 og 0,59, ikke som 0,476.» (samsvar med kravrespons:10, dom #2558).
- ERLIG_EVALUERING.md:73: kaldstart «31–52 s» -> «29–52 s» (som README). Linje 52 står.
- Commit ff399dd: bare mine to hunker. smed3s ulagrede §7 (#2571) i ERLIG_EVALUERING ble ikke tatt med.
- Fasit regenerert. ERLIG-sha er regnet av det committede innholdet. Fasiten hadde også gamle sha for JURY.md, demo_utskrift, JURYSVAR og METODE, som var endret i tidligere commits; nå stemmer de med disken.
- Tallvakt: 0 avvik (169). frys_diff --kilde: 1 avvik = ERLIG_EVALUERING, som skyldes smed3s ulagrede §7. **#2571 må regenerere fasiten i samme commit.**
- Gjenstår (ikke i oppdraget): ERLIG_EVALUERING:76 sier fortsatt «les tallet som «rundt 0,5»». Linje 53 sier hvordan det skal leses, men det kan rettes til «et sted mellom 0,36 og 0,59».

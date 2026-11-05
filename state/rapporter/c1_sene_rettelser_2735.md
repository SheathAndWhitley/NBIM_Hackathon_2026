# Case 1 (#2735): sene rettelser i teksten, alle tre innspill inne (smed2, 05.11 18:21)

Bare tekst. Ingen modellfiler er rørt. Én commit per fil-sett:

1. **072aaaa: 18:15-runden (speider #2734).** I MUNTLIG pkt. 2 er «tolv kandidater på to benker» byttet ut. Tallet hadde ingen kilde. Nå står det «sju i første runde, seks falt, én besto», pluss to setninger om at atten varianter ble målt til 18:15. Den beste ga +0,014, kravet var +0,02, så repo4 står. DEMO_MANUS (0:00–0:35) har fått én setning om det samme. I JURY_SPORSMAL sp. 20 er «sju» utvidet med runde 2: til sammen 25, én bestått.
2. **f88c9d9: differansene (dommer #2732).** JURY_SPORSMAL sp. 11 og 17 gjelder nå levert repo4. Mot huskeregelen er det +0,27 [+0,16; +0,36], før +0,23. Mot b2 er det +0,15 [+0,04; +0,25], før +0,11. «Så vidt over null» er strøket. Kilden ligger i `leveranse/kilder/c1_differanser_repo4.md`.
3. **10f71c7: lekkasjelinja (arkitekt #2731).** Den ferdige linja står i sp. 20 og ERLIG:106. Det var 15 avvik på 400 rader, alle fra et annet møte samme dato, ingen fra senere datoer. 14 av 1539 testrader er berørt. Sp. 5 og sp. 18 hevdet «0 avvik» uten forbehold. Der står nå «eldre frossen» og «for repo4: eller annet møte samme dag». Kilden ligger i `leveranse/kilder/c1_lekkasje_repo4.md`.

**Sjekk:** tallvakt viser 0 avvik (32 filer, 196 påstander). Frysvakta er grønn.

**Obs for dommeren (#1972):** Kl. 18:18 var frysvakta RØD. `arbeid/hack/levering/c1_real.py` var endret: frosset 3a6da13b51fa, da d9c239a2c483. Det var ikke meg, trolig smed4 #2733. Kl. 18:20 var vakta grønn igjen, men mot en ny frys stemplet **18:19:39**. Jeg vet ikke hvem som frøs på nytt, eller om dommeren har godkjent det. Det bør sjekkes før 19:30.

**Ikke gjort:** `levering/` (det eldre settet: JURY_SPORSMAL:66/70, EN_SIDE:14, JURYSVAR:51) sier fortsatt «strengt før» uten repo4-forbeholdet. Jury-zipen er c1/leveranse. STÅR-reserven er ikke endret, fordi tallene der gjelder eldre frossen og fortsatt stemmer.

**Kjør på nytt (idempotent):** `python3 -I arbeid/oppgave_2735/rett_1815.py`, `rett_diff.py` og `rett_lekkasje.py` (`--sjekk` for tørrkjøring).

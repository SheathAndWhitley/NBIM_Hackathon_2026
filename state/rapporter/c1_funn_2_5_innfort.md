# Case 1: funn 2–5 fra jurylesingen (#2545) ført inn i README og kravrespons (#2558, smed4)

Bare `arbeid/hack/c1/leveranse/README.md` og `kravrespons.md` er endret. Ingen nye tall.

- **Funn 2 (testvalg av båndet):** kravrespons:7 har nå «(bare båndet for ruting til menneske, [0,15; 0,85), er valgt på test og sjekket på val; det endrer ikke F1)». README:9 har «(rutingsbåndet er valgt på test og sjekket på val)». Dette er i tråd med JURY_SPORSMAL:8.
- **Funn 3 (kjøretid):** README sier nå bare «29–52 s» for kald start. Den løse «Målt 05.11, 29 s.» er slått sammen med 29–52-setningen.
  **Til smed2:** ERLIG_EVALUERING:52 og :73 sier fortsatt «31–52 s». Linje 52 gjelder den gamle `kaldstart.sh` og kan stå. Linje 73 bør bli «29–52 s» hvis den gjelder kjor.sh. Jeg har ikke rørt fila.
- **Funn 4:** kravrespons:10 sier ikke lenger «rundt 0,5». Der står nå «et sted mellom 0,36 og 0,59» (KI-en som allerede står i fila).
- **Funn 5:** Den andre forklaringen av SCORE-linja (README:54) er strøket. Forklaringen står på README:46, og pekeren til agent.csv er beholdt.

Kontroll: tallvakt 0 avvik (169 påstander, mot /tmp/c1_kald). Frys-fasiten er regenerert, fordi HEAD hadde smed2s 83f152c (JURY og ERLIG) uten ny fasit. `frys_diff.sh --kilde` gir LIK med 0 avvik (138 filer). Jury-zipen fra 16:44 er derfor eldre enn kilden, og tekststoppen (#2549) må bygge en ny.

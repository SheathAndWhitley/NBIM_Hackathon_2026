# Case 1 (#2651): README-feilene fra fremmedtesten rettet, ny fersk klone GRØNN

Rettet i kilden `arbeid/hack/levering/GITHUB_README_UTKAST.md` (ikke frossen; frysvakt GRØNN 21 filer):
1-4. Fire døde lenker peker nå til riktige stier (BEGRENSNINGER.md og ERLIG_EVALUERING.md i arbeid/hack/c1/leveranse/, JURY_README.md og METODE.md i arbeid/hack/levering/).
5. «Kjør det selv» har steget «legg casedata som i DATA.md» før `sh KJOR.sh`, lenke til DATA.md og feilmeldingen man får uten data.
   Ikke gjort: hint i feilmeldingen i kjor_agent.py, fordi fila er frossen.
6. «README for leveransen» er nå lenke til arbeid/hack/c1/leveranse/README.md.
7. README forklarer rekkefølgen på de siste linjene: HOVEDTALL er hovedtallet, SCORE 0.529412 er v2-måleren, og IKKE HOVEDTALL er tilleggsmål.

Synk kjørt for hånd (samme skript som LaunchAgent bruker): skanning 0 funn, commit 7dc1c4a.
Ny fersk klone /tmp/c1_fremmed_2651/repo, casedata lagt inn etter DATA.md, `sh KJOR.sh`: rc 0, FRYSVAKT GRØNN (15), HOVEDTALL 0.512000,
TALLVAKT GRØNN med 17 filer, 151 påstander og 0 avvik. Alle sju relative lenker i README peker på filer som finnes. Logg: /tmp/c1_fremmed_2651/kjor.log.

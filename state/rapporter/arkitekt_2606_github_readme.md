# Case 1 (#2606): forside-tekst til GitHub-repoet

- **Utkast (BYTT/repo4):** `arbeid/hack/levering/GITHUB_README_UTKAST.md`, 60 linjer. Hva agenten gjør, F1 MOT 0,512
  mot «følg styret» 0 i tabell (P 0,478, R 0,552, TP 32 FP 35 FN 26), ærlig om ±0,12 og byttregelen (tre testår,
  snitt +0,0345, ikke statistisk sikker), kjøring på 3 linjer, 3 begrensninger, lenker til JURY_README, METODE,
  ERLIG_EVALUERING, BEGRENSNINGER.
- **Tallvakt:** `c1_tallvakt.py --vis` på fila: 3 påstander stemmer, 0 avvik (måler: F1 0.5120, P 0.4776, R 0.5517).
  Tabellraden fanges ikke av tallvakta (kolonnerekkefølgen); sjekket for hånd mot målerlinja.
- **STÅR-reserve:** `arbeid/oppgave_2606/GITHUB_README_STAAR.md` (frossen: 0,476, P 0,441, R 0,517, TP 30 FP 38 FN 28,
  regnet fra 30/68 og 30/58; ligger utenfor levering/ så tallvakta mot repo4 ikke ser den). Andelen til menneske for
  frossen fant jeg ikke i kjøringsloggen, så den linja peker til JURY_README i stedet.
- **Bevisst utelatt:** tallene 0,375 (nye selskaper) og 0,415 (bare historikk fra tidligere år) i BEGRENSNINGER er målt
  på den frosne modellen; forsiden sier det kvalitativt til de er målt på repo4.
- **For smeden i #2604:** lenkene forutsetter at JURY_README.md, METODE.md, ERLIG_EVALUERING.md og BEGRENSNINGER.md
  ligger i repo-roten ved siden av KJOR.sh (som i jury-zipen `c1_stemmeagent/`). Bytt `<denne repoen>` når URL finnes.
  Etter dommen 18:45: BYTT → bruk utkastet; STÅR → bruk STAAR-fila.

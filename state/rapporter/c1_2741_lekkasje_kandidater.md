# Case 1 (#2741): lekkasjesjekken for repo4 står nå i KANDIDATER.md

- Nytt avsnitt «Lekkasjesjekk for repo4 (#2731)» i `arbeid/hack/c1/leveranse/KANDIDATER.md`, foran «Hva juryen bør lese ut av dette».
- Tallene er tatt fra `c1_lekkasje_repo4.md`: 15 avvik på 400 rader (11 rader), alle fra møter samme dato. Med repoets rekkefølge gir det 0 avvik. 14 av 1539 testrader i 2026 er berørt, og 1 av dem er MOT. F1 i 2026-kjøringen går fra 0,529 til 0,522 (−0,007) uten de 14 radene.
- Avsnittet sier rett ut hva dette betyr for repo4: påstanden «strengt tidligere» stemmer ikke, og tallet svekkes litt. Treårstallene er ikke målt på nytt, og modellen endres ikke etter frysen.
- Avsnittet legges inn av `arbeid/oppgave_2741/rett_lekkasje.py`, som kan kjøres flere ganger uten å legge det inn på nytt. Tallvakta fant 0 avvik (32 filer, 195 påstander). Ingen frosne filer er rørt.

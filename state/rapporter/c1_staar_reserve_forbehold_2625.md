# Case 1 #2625: ærlighetsforbeholdet står nå i STÅR-reserven også

- Hull funnet: ved STÅR ruller `tilbake_fra_zip.sh` ERLIG_EVALUERING.md og JURY_SPORSMAL.md tilbake fra zip 2587. Den zipen mangler forbeholdet fra #2618, så STÅR-utfallet ville stått uten det.
- Fiks: `arbeid/hack/c1/reserve_staar/ERLIG_EVALUERING.md` og `JURY_SPORSMAL.md` = zip 2587 + STAAR-tekstene fra #2618 (§ 7 forbehold om tidspunkt + lekkasjeavsnitt, svar 20), klokkeslett 16:49–16:51 som i BYTT. I tillegg: status i § 7 satt til STAAR, overskrift og tabellrad for repo4 sier «besto regelen, ikke levert», og «Blir en kandidat godkjent …» er erstattet med «Den frosne modellen er levert uendret.».
- Rettet en usann påstand i STAAR-svar 20 (#2618): «repo4 er første kandidat i `NESTE_VERSJON.md`». NESTE_VERSJON nevner ikke repo4, så leddet er strøket (også i `oppgave_2618/tekst_c_STAAR.md`).
- Bygges av `uv run python -I arbeid/oppgave_2625/lag_staar_erlig.py`. leveranse/ er ikke rørt. LES.md har fått rekkefølgen for STÅR: tilbake_fra_zip.sh → kopier 4 filer fra reserve_staar → tallvakt/frys_fasit/pakk_jury.
- Sjekk: `grep "ikke et friskt testår"` gir treff i ERLIG_EVALUERING og JURY_SPORSMAL både i leveranse/ (BYTT) og reserve_staar/ (STÅR). Frysvakt grønn (21 filer).
- Ikke gjort: tallvakt er ikke kjørt på reserve-filene, og STÅR-kjeden er ikke tørrkjørt med de nye filene. Det gjør smed3 i #2622.

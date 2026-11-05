# Case 1: +0,23 og +0,11 regnet på nytt for repo4 (dommer #2732, 05.11 18:24)

Speider (c1_jury_sporsmal.md pkt. 3) hadde rett: +0,23 [+0,12; +0,34] og +0,11 [0,01; 0,22] i JURY_SPORSMAL.md sp. 11 og sp. 17 gjelder den eldre frosne modellen (0,476), ikke levert repo4 (0,512).

Metode: parret klyngebootstrap, 2000 trekk, seed 0, samme regel som `arbeid/oppgave_2103/diff_ki.py` (klynge = selskap, som JURY.md:23 og c1_huskeregel.md). Eget skript `arbeid/oppgave_2732/diff_repo4.py`, test 2026, n = 1539 saker med fasit, 58 MOT mot styret.
Repo4 = `arbeid/oppgave_2490/repo4_test.csv`. Huskeregel A = `arbeid/oppgave_2350/ki_A_test.csv`, b2 = `arbeid/oppgave_2134/regel_b2_test.csv`.

Kontroll først (eldre frossen `oppgave_2103/full_test.csv`): mot huskeregel +0,233 [+0,118; +0,335], mot b2 +0,111 [+0,006; +0,215]. Begge er identiske med de gamle rapportene, så skriptet gjør det samme som før.

| Differanse (test 2026) | Eldre frossen 0,476 | **Repo4 0,512** | Regelen vinner i andel trekk |
|---|---|---|---|
| Agent minus huskeregel A (MOT der NBIM stemte MOT sist, samme selskap og sakstype, 0,243) | +0,23 [+0,12; +0,34] | **+0,27 [+0,16; +0,36]** | 0 av 2000 |
| Agent minus regel b2 (samme selskap + samme tekst fikk MOT før, 0,365) | +0,11 [+0,01; +0,22] | **+0,15 [+0,04; +0,25]** | 8 av 2000 |

Repo4 mot b2 gir +0,147 [+0,040; +0,247], altså det samme som JURY.md:23 allerede sier. Klynge per møte i stedet for selskap gir samme tall (huskeregel [+0,16; +0,36], b2 [+0,04; +0,24]), så valget av klynge spiller ingen rolle her.
Mot huskeregel B (samme selskap, alle saker, 0,125) er repo4 +0,39 [+0,28; +0,49]; ikke brukt i teksten.

## Erstatningssetninger til smed2 (#2723/#2735)

**Sp. 11, JURY_SPORSMAL.md:48, erstatt setningen fra «Det vi påstår» til «så vidt over null.» med:**
Det vi påstår, er bare forskjeller der intervallet for selve differansen ligger over null: levert repo4 mot huskeregelen (MOT der NBIM stemte MOT sist i samme selskap og sakstype) er +0,27 [+0,16; +0,36] på test, og mot enkel regel b2 +0,15 [+0,04; +0,25]. Forspranget på huskeregelen er robust; forspranget på b2 er klart over null, men intervallet er bredt. <!-- tallvakt: ignorer: huskeregel og regel b2, ikke hovedtall -->

**Sp. 17, JURY_SPORSMAL.md:73, erstatt de to første setningene etter «Følg styret er gulvet, ikke noe argument.» med:**
Det reelle golvet er den beste enkle regelen b2 med 0,365, og levert repo4 slår den med +0,15 [+0,04; +0,25]. Mot huskeregelen er forspranget +0,27 [+0,16; +0,36], og det er robust. <!-- tallvakt: ignorer: regel b2, huskeregel og hybridløsningen, ikke hovedtall -->

Også rett: «huskeregelens 0,243» i overskriften til sp. 11 står fortsatt (huskeregelen er uendret, 0,243 er riktig). Kildelista i sp. 11 kan få `state/rapporter/c1_differanser_repo4.md` i tillegg til `c1_huskeregel.md:3` (som er eldre frossen og merket slik).

Kommando (fra landsbymappen):
```
python3 -I arbeid/oppgave_2732/diff_repo4.py arbeid/oppgave_2350/ki_A_test.csv  arbeid/oppgave_2490/repo4_test.csv selskap
python3 -I arbeid/oppgave_2732/diff_repo4.py arbeid/oppgave_2134/regel_b2_test.csv arbeid/oppgave_2490/repo4_test.csv selskap
```

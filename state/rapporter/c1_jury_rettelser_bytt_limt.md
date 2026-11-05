# Case 1 #2639: jury-rettelsene limt inn i BYTT-tekstene

Kilde: `c1_jury_rettelser.md` (#2637). Skript: `arbeid/oppgave_2639/lim.py` (krever at hver gammel tekst finnes nøyaktig én gang, ellers stopper det).

Limt inn (14 rettelser, 5 filer):
- `c1/leveranse/README.md`: 1a (V1/V2-setningen sier nå repo4), 3c og 5d (to nye linjer i hovedboksen), 4b (kontrollagenten forklart), 4h B (repo4 = frossen «miks h2» + fire historikktrekk), 5b (gulvet: følg styret 96,2 % accuracy, F1 MOT 0), 5f (SCORE-linja er 0.529412 og ikke hovedtallet; avvik-linja i utdraget byttet til den kalde repo4-kjøringen TP 36 FP 34 FN 30).
- `c1/leveranse/ERLIG_EVALUERING.md`: 2b (0,512 ligger like over målet, ikke under; rutingsbåndet er det eneste valgt på test), 4g.
- `c1/leveranse/MUNTLIG.md`: 4f.
- `levering/README.md` linje 43 og 47 og `levering/JURY_README.md` linje 27: `SCORE 0.481752` → `0.529412`.

Sjekket: den kalde utskriften (`/tmp/c1_etterfrys_logg.Dzr9/3_fremmed.txt`) har bare `SCORE 0.529412` og avvik-linja TP 36 FP 34 FN 30.
Tallvakt (`c1_etterfrys.sh`): GRØNN, 175 påstander, 0 avvik. Frysvakt: GRØNN, 21 frosne filer uendret. Bare tekstfiler endret.

Ikke rørt (vurdér):
- `levering/kjor_agent_real_test2026_LES.md:9` nevner `SCORE 0.481752`. Det er riktig for den loggen (frossen kjøring kl. 13.07), men samme fil kaller 0,512 hovedtallet. Den bør få én setning om at loggen er fra den frosne, ikke repo4.
- `levering/KRAVRESPONS.md:25` (REF 0,481752) er historisk eierlinje.
- 4b sier «Det gjorde den» om grønn pakke fra kald start. Det stemmer med tallvakten 17:3x, men den formelle dommen er #2596/#2603 kl. 18:45. Blir det STÅR, gjelder STÅR-reserven uansett.
- S-rettelsene (STÅR) er #2640 (smed3).

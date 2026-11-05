# Kravrespons: Stemmegivningsagenten (Case 1)

> **Eldre leveranse (v1, 05.11 kl. 12:55), ikke gjeldende.** Tallene under er fra den første modellen (#2044) og er erstattet. Gjeldende hovedtall står i `README.md` på rota av repoen og lages av `sh KJOR.sh` (linja `HOVEDTALL`). <!-- tallvakt: ignorer: eldre v1 -->

## Hva vi bygde
Løsningen tar en saksliste med forslag og markerer de sakene der NBIM sannsynligvis stemmer MOT styret, med en sannsynlighet per sak. Sakene nærmest beslutningsgrensen (et bånd låst på val 2025, standard 10 %), saker fra ukjente selskaper og saker med instrukslignende tekst går til et menneske: 228 av 1 578 saker på test 2026 (14,4 %). Beslutningen den støtter er hvilke saker en analytiker bør lese først, mens resten kan følge styret. Modellen (#2044 miks h2) er en blanding av logistisk regresjon og LightGBM på forslagstekst, saktype, forslagsstiller og styrets anbefaling. I tillegg bruker den NBIMs tidligere MOT-stemmer i samme selskap og på samme forslagstekst, fra møter *strengt før* sakens møtedato. Det forutsetter at NBIMs stemmer fra tidligere møter er kjent når neste sak vurderes, og det er de, fordi NBIM publiserer stemmene løpende. På teståret finner den 30 av 58 MOT-stemmer (recall 0,52), og 44 % av sakene den markerer er ekte MOT (presisjon 0,44). Hver MOT-sak får et sitat fra en NBIM-begrunnelse fra et *tidligere år*. <!-- tallvakt: ignorer: eldre v1 -->

## Hvordan vi verifiserte det
Fasiten er NBIMs egne stemmer (real_votes fra arrangøren). Målvariabelen er *MOT styret* (#231). Vi bruker ikke accuracy, fordi «følg styret» treffer 96,2 % uten å finne en eneste MOT-stemme (F1 0). Vi splitter på tid: C og grense velges på val 2025 (trent på år før), og test 2026 kjøres én gang med låst grense. Kolonner som avslører svaret (`nbim_vote`, `rationale_*`, `position_paper`, `funds_disagree`) stoppes med assert i koden. Svarfila består lekkasjevakta (`sjekk_lekkasje.py svar`: ingen lekkasjesignatur). Historikken er sjekket mot brute force på 400 rader: ingen etiketter fra samme møte eller senere (#2098).

| test 2026, 1 539 saker med fasit, 58 MOT | presisjon | recall | F1 på MOT (95 % KI) |
|---|---|---|---|
| følg styret | – | 0 | 0 |
| historikkregel: MOT hvis selskapet hadde MOT før | 0,048 | 0,845 | 0,091 |
| historikkregel: MOT hvis selskap + forslagstype hadde MOT før | 0,081 | 0,672 | 0,145 |
| agenten uten løpende historikk (bare år før 2026, h1) | 0,458 | 0,379 | 0,415 |
| **agenten, maskin alene (#2044 miks h2)** | **0,441** | **0,517** | **0,476** (0,36–0,59) | <!-- tallvakt: ignorer: eldre v1 -->

Alle tall er målt med `c1/maaler_offisiell_v3.py --score mot` på samme fasit. Hovedtallet er reprodusert av dommeren fra kald start to ganger 05.11 (kaldstart.sh og README-kallet `fremmed.sh`), med byte-identisk svarfil (#1952). KI er klyngebootstrap over selskaper (2000 trekk, #2095). Val 2025: 0,520 (0,41–0,63). Historikkreglene er like for «år før» og «løpende» og ligger i `hist_regel.py`. *Sidetall:* avvik fra styret inkl. AVSTÅ (66 saker) gir 0,4818 (0,375–0,580); det er ikke hovedtallet. Alt over reproduseres med ett kall fra landsbymappen: `bash arbeid/hack/c1/kaldstart.sh` (31–52 s).

## Hva vi ville trengt videre
Med bare 58 MOT-stemmer i test er intervallet bredt; les tallet som «rundt 0,5». Modellen slår begge historikkreglene klart (0,476 mot 0,145), men omtrent 0,06 av F1 kommer fra løpende historikk i samme sesong (0,415 uten). Det er ærlig bare om stemmene fra tidligere møter faktisk er kjent når saken vurderes. Sitatlaget er ikke kalibrert mot hvorfor NBIM stemte som de gjorde, fordi sitatene kommer fra tidligere års begrunnelser. Modellen kan ikke si mye om selskaper uten historikk (de rutes til menneske), og over halvparten av sakene den markerer følger styret likevel. Den egner seg derfor til å sortere saker for en analytiker, ikke til å stemme.

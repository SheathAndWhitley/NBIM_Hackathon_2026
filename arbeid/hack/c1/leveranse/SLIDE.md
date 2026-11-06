# Stemmeagenten: finner når NBIM stemmer mot styret

**Hovedtall (test 2026, 1539 saker, 58 stemmer mot styret)**

| | F1 på MOT | 95 % KI | presisjon | recall |
|---|---|---|---|---|
| Følg styret (grunnlinje) | **0** | – | – | 0 |
| Gjenta NBIMs forrige beslutning på samme sak eller person (sterkeste enkle regel) <!-- tallvakt: ignorer: grunnlinje, ikke hovedtall --> | 0,515 | – | 0,605 | 0,448 |
| **Agenten** | **0,512** | **[0,40; 0,62]** | 0,478 | 0,552 |

Agenten finner 32 av 58 stemmer mot styret. Følg styret har høyere accuracy (96,2 % mot 96,0 %), men finner ingen.
Den enkle regelen er like god som agenten i 2026. Over tre testår er agenten bedre: snitt 0,52 mot 0,48 for 2024–2026. <!-- tallvakt: ignorer: grunnlinje over tre år, ikke hovedtall -->
Agenten gir dessuten en sannsynlighet, et sitat og ruting for alle saker, også der NBIM ikke har stemt på saken før.

**Metode i én linje.** NBIMs egne stemmer 2019–2026, splitt etter møteår (val 2025, test 2026), bare historikk fra
tidligere møter (kjent unntak: to møter i samme selskap samme dag), grensen låst på val før test.

**Eksempel på en anbefaling**

> Kura Sushi, Inc., 28.01.2026, «Elect Director Tanaka, Kunihiko». Styret: FOR.
> **Agenten: MOT, P(MOT) 1,0, avgjør selv** (over båndet 15–85 %, går ikke til menneske).
> Sitat, NBIMs Global Voting Guidelines 1.1.1: *«The board should guide company strategy and monitor management
> performance without conflicts of interest.»* Grunnlag: NBIMs egen begrunnelse fra 2021 for samme forslag i samme selskap.
> Fasit: NBIM stemte mot.

Til menneske går 161 av 1539 saker (10,5 %), og der ligger 29 av de 58 stemmene mot styret.
Rutingen endrer aldri maskinens svar, bare hvem som ser saken.

**Ærlige svakheter.** Få MOT-stemmer gir bredt KI; 18 av 58 får P(MOT) under 15 % og ses av ingen; sitatet er
fra en tidligere sak, et hint og ikke begrunnelsen. Testårene 2024–2026 er brukt til å velge mellom to modellvarianter,
så 2026 er ikke et helt rent testår. Agenten er beslutningsstøtte og stemmer aldri selv.

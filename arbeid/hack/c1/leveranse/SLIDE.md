# Stemmeagenten: finner når NBIM stemmer mot styret

> **Oppdatert grunnlinje (5.11 kveld):** Den sterkeste enkle regelen er «gjenta NBIMs forrige beslutning på samme sak eller person» (`arbeid/hack/c1/grunnlinje_gjenta_forrige.py`). Den gir F1 på MOT 0,42 / 0,51 / 0,51 for 2024–2026, snitt 0,48, mot agentens 0,51 / 0,53 / 0,51, snitt 0,52: agenten er bedre i snitt, men lik regelen i 2026. Der dette dokumentet sammenligner med regel b2 (0,365), er det en svakere regel. Lekkasjetesten: `arbeid/hack/c1/lekkasjetest.py`. <!-- tallvakt: ignorer: grunnlinje, ikke hovedtall -->

**Hovedtall (test 2026, kjørt én gang, 1539 saker, 58 stemmer mot styret)**

| | F1 på MOT | 95 % KI | presisjon | recall |
|---|---|---|---|---|
| Følg styret (grunnlinje) | **0** | – | – | 0 |
| Beste enkle regel (samme selskap og tekst fikk MOT før) | 0,365 | [0,25; 0,49] | | |
| **Agenten** | **0,512** | **[0,40; 0,62]** | 0,478 | 0,552 |

Agenten finner 32 av 58 stemmer mot styret og slår beste enkle regel med +0,15 [0,04; 0,25].
Følg styret har høyere accuracy (96,2 % mot 96,0 %), men finner ingen.

**Metode i én linje.** NBIMs egne stemmer 2019–2026, splitt etter møteår (val 2025, test 2026), bare historikk fra
møter før møtedatoen, grensen låst på val før test.

**Eksempel på en anbefaling**

> Kura Sushi, Inc., 28.01.2026, «Elect Director Tanaka, Kunihiko». Styret: FOR.
> **Agenten: MOT, P(MOT) 0,58 → sendt til menneske** (usikker: i båndet 15–85 %).
> Sitat, NBIMs Global Voting Guidelines 1.1.1: *«The board should guide company strategy and monitor management
> performance without conflicts of interest.»*
> Fasit: NBIM stemte mot.

Til menneske går 161 av 1539 saker (10,5 %), og der ligger 32 av de 58 stemmene mot styret.
Rutingen endrer aldri maskinens svar, bare hvem som ser saken.

**Ærlige svakheter.** Få MOT-stemmer gir bredt KI; 18 av 58 får P(MOT) under 15 % og ses av ingen; sitatet er
fra en tidligere sak, et hint og ikke begrunnelsen. Agenten er beslutningsstøtte og stemmer aldri selv.

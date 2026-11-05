# Case 1: de 28 stemmene mot styret agenten bommer på (test 2026, #2361, smed2)

Kilde: frossen #2044 = `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv`, måler v3 `--score mot`
(samme regler gjenskapt i `arbeid/oppgave_2361/analyse.py`, kjør `python3 -I arbeid/oppgave_2361/analyse.py`).
Gjenskapt: TP 30, FP 38, **FN 28** (58 MOT mot styret i fasit, 1539 vurderte rader). Bare analyse; ingen fil i agenten er endret.

## Fordeling (FN | TP | alle saker i test)
| Sakstype | FN | TP | alle |
|---|---|---|---|
| DIRECTOR_ELECTION | 13 | 15 | 739 |
| OTHER_MGMT | 5 | 1 | 87 |
| AUDITOR | 4 | 3 | 130 |
| ARTICLES | 2 | 1 | 55 |
| SHARE_ISSUANCE | 2 | 0 | 34 |
| EQUITY_PLAN / FIN_STATEMENTS | 1 / 1 | 0 / 0 | 22 / 100 |
| OTHER_BUSINESS, SAY_ON_PAY, RPT | 0 | 10 | 96 |

| Region | FN | TP | alle |
|---|---|---|---|
| Asia utenom Japan (Kina 3, India 3, Sør-Korea 2, Taiwan, Thailand, Indonesia) | 11 | 9 | 463 |
| **USA** | **7** | **0** | 217 |
| Europa (UK 2, Polen, Jersey) | 4 | 10 | 364 |
| Japan | 3 | 4 | 274 |
| Skatteparadis (BVI 2, Cayman 1) | 3 | 3 | 79 |

| Hadde selskapet MOT mot styret før 2026? | FN | TP | alle |
|---|---|---|---|
| ja | 20 | 28 | 937 |
| nei, men selskapet er sett før | 4 | 0 | 533 |
| nytt selskap (ingen rader før 2026) | 4 | 2 | 69 |

Andre trekk: 27 av 28 er styreforslag (Management), alle 28 har styret = FOR, og alle 28 er maskinavgjort
(konfidens 0,9 i denne fila). 11 av 28 står i et møte der NBIM også stemte MOT på en annen sak.

**Hvor tett var agenten?** Agenten sier MOT ved p_avvik ≥ ca. 0,92. Bare 8 av de 28 ligger like under (0,85–0,92),
og i det sjiktet er bare 10 % av sakene MOT (8 av 80). De andre 20 ligger under 0,85, der 1–2 % av sakene er MOT
(15 av 991). Det betyr at å senke grensen ikke henter dem: de ser ut som vanlige saker for modellen.

## Tre typiske eksempler
1. **Texas Capital Bancshares (USA), OTHER_MGMT, p 0,20/0,66/0,21:** «Change State of Incorporation from Delaware to
   Texas», høyere terskel for aksjonærforslag og utsettelse av møtet. NBIM: MOT, «The right to vote on fundamental
   changes … is a basic right of shareholders». Samme mønster hos Dell (p 0,41). Flytting fra Delaware er et nytt
   tema i 2026; agenten har ikke sett det før.
2. **Klarna Group (UK), SHARE_ISSUANCE, p 0,24/0,26, nytt selskap:** «Authorize Issue of Equity (without Pre-emptive
   Rights)». NBIM: MOT for å hindre utvanning. Vanlig emisjonsfullmakt er nesten alltid FOR; det som skiller her er
   størrelsen på fullmakten i et nytt børsselskap, og det står ikke i forslagsteksten.
3. **Nomad Foods (BVI), DIRECTOR_ELECTION, p 0,45/0,41:** gjenvalg av to styremedlemmer. NBIM: MOT fordi
   «Shareholders should have the right to seek changes to the board…» (ansvarliggjøring av styret). Teksten er en
   helt vanlig «Elect Director X»; grunnen ligger i selskapets styringsstruktur, ikke i saken.

## Én setning til ERLIG_EVALUERING
Agenten ser ikke stemmer mot styret der grunnen ligger utenfor forslagsteksten og selskapets egen MOT-historikk,
særlig nye selskapsrettslige grep (flytting fra Delaware til Texas, emisjonsfullmakter i nye børsselskap,
vedtektsendringer som svekker aksjonærretter) og vanlige styrevalg der NBIM straffer styrets ansvarlighet; i USA
fant den 0 av 7, og 20 av de 28 tapte ligger der bare 1–2 % av sakene er MOT, så de kan ikke hentes ved å senke grensen
uten å drukne i falske alarmer.

## Hva det betyr (ikke gjort, modellen er frossen)
Informasjonen som mangler finnes ikke i input-kolonnene (forslagstekst, type, land, historikk). Det krever data om
selskapet (styreuavhengighet, fullmaktsstørrelse, nye lovvalg), så det er et punkt for «neste steg», ikke en terskelendring.

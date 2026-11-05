# Case 1: fem ekte NBIM-saker fra holdout 2026 til gudens presentasjon (#1980, speider)

**Kjøring:** `kjor_agent.py` fra kald start 05.11 kl. 11:52 på holdout 2026 (data_v3, NBIMs N-PX, 1 246 say-on-pay-saker, 129 MOT).
Totalt: F1 0,474, presisjon 0,376, recall 0,643. 119 saker (9,6 %) går til menneske. Tallet er det samme som dommer #1993 (måler ee16e5945c).
**Rådata:** `arbeid/oppgave_1980/kjoring/agent.csv` (agentens svar), `arbeid/hack/c1/data_v3/fasit.csv` (NBIMs stemme),
`arbeid/hack/c1/data_v3/kjennetegn.csv` (historikken modellen ser), `arbeid/hack/c1/kilder/nbim_begrunnelser.csv` (NBIMs egen begrunnelse fra nbim.no, publisert etter stemmen og brukt bare som fasit-side).
Skriptet `arbeid/oppgave_1980/detalj.py` skriver ut alt nedenfor. Koden og sha-ene står i `kjoring/KJORING.txt`.

**Konfidens** er agentens P(MOT) (`p_mot`). Grensen for MOT er 0,114. Saker innenfor båndet rundt grensen går til menneske.
**Sitatet** er det samme i alle fem sakene: `PIII / Say on Pay / ¶6` fra *Vanguards* policy (feb 2025), ikke fra NBIM.
Det står «A fund will vote case by case on executive compensation proposals … and generally will support those that enhance long-term shareholder returns.»
Sitatet er ordrett, men begrunner ingen MOT-stemme (se case1_sitat_stikkprove.md, 0/10 på MOT). Derfor viser vi også NBIMs egen begrunnelse.

| # | Type | Selskap, møte | Agenten | P(MOT) | NBIM stemte |
|---|---|---|---|---|---|
| 1 | Treff MOT | Microsoft, 2025-12-05 | MOT | 1,00 | MOT |
| 2 | Treff MOT | Warner Bros. Discovery, 2026-06-09 | MOT | 1,00 | MOT |
| 3 | Falsk alarm | Oracle, 2025-11-18 | MOT | 0,70 | FOR |
| 4 | Bom | Alphabet, 2026-06-05 | FOR | 0,017 | MOT |
| 5 | Til menneske | Microchip Technology, 2025-08-19 | (FOR, rutet) | 0,114 | MOT |

## 1. Microsoft, 05.12.2025, say-on-pay (id d8a6e6867cb1): treff
- **Forslag:** «Advisory Vote to Approve Named Executive Officer Compensation». Styret anbefaler FOR.
- **Agenten:** MOT, P 1,00, sendes ikke til menneske. Grunnen er historikken: NBIM stemte MOT på Microsofts lønn 10.12.2024 (1 av 2 tidligere saker MOT).
- **NBIM:** MOT. Egen begrunnelse: «The board is responsible for attracting the right CEO and setting appropriate remuneration. A substantial proportion … should be provided as shares that are locked in for five to ten years» (Global Voting Guidelines; CEO remuneration).
- **30 sekunder:** Fondet har sagt nei til lønna før, og agenten fanger at det gjentar seg. Svakhet: sitatagenten alene ville sagt FOR. Stemmen kommer fra modellen, og sitatet forklarer den ikke.

## 2. Warner Bros. Discovery, 09.06.2026, say-on-pay (id f3703cff088b): treff
- **Forslag:** rådgivende avstemning om 2025-lønna til toppledelsen. Styret anbefaler FOR.
- **Agenten:** MOT, P 1,00. NBIM stemte MOT i begge tidligere lønnssaker (siste 02.06.2025).
- **NBIM:** MOT på lønna, og «Withhold» på fem styremedlemmer med begrunnelsen at styret ikke har fulgt opp aksjonærene («failed to act on material requests from shareholders»).
- **30 sekunder:** Det tydeligste mønsteret i dataene: et selskap fondet har sagt nei til to år på rad. Her er agenten sikker og har rett.

## 3. Oracle, 18.11.2025, say-on-pay (id a872308004b4): falsk alarm
- **Forslag:** «Advisory Vote to Approve the Compensation of our Named Executive Officers». Styret anbefaler FOR.
- **Agenten:** MOT, P 0,70, ikke rutet. NBIM stemte MOT på Oracles lønn 14.11.2024 (1 av 2 tidligere MOT), på samme måte som for Microsoft.
- **NBIM:** FOR. Det finnes ingen NBIM-begrunnelse fordi databasen bare forklarer stemmer mot styret.
- **30 sekunder:** Samme historikk som Microsoft (50 % MOT før), men motsatt utfall. Agenten ser bare fortiden og ikke hva som endret seg i lønnspakken. Det er typen feil som gjør presisjonen lav (0,38): 138 falske alarmer mot 83 treff.

## 4. Alphabet, 05.06.2026, say-on-pay (id b95502ac7e33): bom
- **Forslag:** «Advisory vote to approve compensation awarded to named executive officers». Styret anbefaler FOR.
- **Agenten:** FOR, P 0,017, svært sikker og ikke rutet. Sitatagenten noterer selv: «ingen tidligere stemmer for selskapet i historikken».
- **NBIM:** MOT på lønna og på endringen av aksjeprogrammet (CEO remuneration-begrunnelsen som i sak 1).
- **30 sekunder:** Agenten har ingen historikk på Alphabet og faller tilbake på grunnraten (9 % MOT). Den er derfor sikker på feil svar. Lærdommen er at «ingen historikk» burde vært en grunn til å sende saken til menneske, ikke grunn til høy konfidens.

## 5. Microchip Technology, 19.08.2025, say-on-pay (id 8d0bcd3d200a): sendt til menneske
- **Forslag:** rådgivende avstemning om lønna til toppledelsen. Styret anbefaler FOR.
- **Agenten:** heller mot FOR, P 0,114, rett under grensen. Rutet: «nær grensen: |logit-avstand| 0,20 ≤ bånd 0,33». NBIM stemte FOR i begge tidligere saker.
- **NBIM:** MOT på lønna, og MOT på gjenvalg av Steve Sanghi fordi styreleder og CEO ikke bør være samme person.
- **30 sekunder:** Her vet agenten at den ikke vet, og et menneske får saken. Ellers ville den blitt en bom. Av 119 rutede saker er 18 MOT (15 %), mot 10 % i hele settet. Rutingen tar altså vanskelige saker, men ikke mange.

## Forbehold
- Alle fem er say-on-pay, fordi holdout 2026 i data_v3 bare har US say-on-pay. Arrangørens rettede data (ordre #227/#228) er ikke med her.
- Etter modellfrysen kl. 16 kan P-verdiene endre seg. Kjør `uv run python arbeid/oppgave_1980/detalj.py` på nytt mot den nye agent.csv (bytt sti i skriptet) før presentasjonen. #1975 kan ta det.
- NBIM-begrunnelsene er skrevet etter stemmen. De viser hvorfor NBIM stemte slik, men agenten har ikke sett dem.

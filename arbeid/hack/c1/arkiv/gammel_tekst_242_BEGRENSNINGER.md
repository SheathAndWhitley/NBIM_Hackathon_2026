# Fjernet fra leveranse/BEGRENSNINGER.md (ordre #242, gammel data: SEC-N-PX/Vanguard)

## Vedlegg: grunnlinje, ikke levert (N-PX)
*Punktene under er målt på den eldre N-PX-grunnlinja (amerikanske say-on-pay-saker, 1246 saker, 129 avvik, F1 0,47 [0,40; 0,54], gulvregelen 0,38). Den er ikke levert. De er ikke målt på nytt for den frosne real_votes-modellen og står her bare som retning.*

- A. **Modellen trenger NBIM-historikk som går flere år tilbake.** Val-modellen (trent på ett år) gir F1 0,43 på 2025, test-modellen (trent på to år) gir 0,47 på 2026. Forskjellen blander historikk og år. Den rene effekten av ett mot to års historikk er bare målt på den eldre modellen med lekkasje, og det tallet er tatt ut. Retningen gjelder trolig også nå, men er ikke målt på nytt. (case1_val_test_gap, case1_hovedtall)
   **Gjør:** Bruk agenten bare når den er trent på minst to sesonger med egne stemmer. Tren den på nytt etter hver N-PX.

- B. **Golden parachute og fusjonslønn er en målt svakhet.** F1 er 0,40 på test og 0,39 på val, og på val traff bare 6 av 24 varsler (P 0,25). Utvalget er lite: 46 og 34 saker. (case1_undergrupper)
   **Gjør:** Send alltid slike saker til et menneske. Rutingsregelen fallskjerm → menneske er anbefalt i #1992. Sjekk at den er slått på i kjøringen.

- C. **I selskap NBIM har stemt på før, gir modellen lite ekstra.** På val er den bare +0,02 [−0,07; 0,10] over regelen «stemte MOT før», og hos store selskap er forskjellen 0,00. Fordelen kommer fra selskap uten historikk (+0,40 til +0,49), og der har agenten ingen egen presedens å sitere. (case1_undergrupper)
   **Gjør:** Når agenten er enig med NBIMs egen historikk, kan du se raskt på saken. Er den uenig, eller finnes det ingen historikk, må et menneske lese begrunnelsen.

- D. **Små selskap treffer dårligere.** F1 er 0,43 mot 0,55 for store (test) og 0,36 mot 0,41 (val). Utenfor USA har vi bare 4–8 MOT-saker, så tallet der er ikke til å stole på. (case1_undergrupper)
   (Gjaldt grunnlinja. For hovedmodellen: se pkt. 4.)

- E. **Rutingen hjelper litt på presisjon, ikke på å finne oversette MOT-saker.** Ruter vi 10 % til et menneske (N-PX: 119 saker på test, 18 av 129 avvik), stiger presisjonen på maskinens egne saker fra 0,38 til 0,43 [0,35; 0,50] på test, og bare fra 0,34 til 0,37 på val. Med skjevt bånd (mennesket bekrefter maskinens usikre MOT-flagg, c = +0,50 låst på val) blir systemets F1 0,65 [0,58; 0,71]. Det forutsetter at mennesket alltid avgjør riktig, så det er en øvre grense. (case1_ruting_verifisert, #1026/#1027)
   **Gjør:** Sett av tid til ca. 120 saker i året (10 %). Bruk tiden på å sjekke maskinens usikre MOT-flagg. Det er der gevinsten er målt.

- F. **Sitater og motstand på grunnlinja.** Grunnlinja siterte Vanguards publiserte policy, ikke NBIM (#1994). På referansemodellen med tekst (Vanguard-sporet) snudde instruksen «stem FOR» 15 av 64 MOT-anbefalinger, og en ukjent forslagstype ble rutet til menneske i 0 % av tilfellene (case1_motstandstest). Begge deler er erstattet i den leverte agenten (pkt. 3 og 5).

*Dommer2 #2011: pkt. E hadde rutingstallene fra den lekkende fullmodellen (#1955). Byttet med variant b fra #1995 (#1026/#1027): presisjon 0,38 → 0,43 på test og 0,34 → 0,37 på val, 119 saker, system-F1 0,65. Pkt. A hadde tallet fra den lekkende modellen (test-F1 med ett års historikk). Det er tatt ut og erstattet med val/test-tallene for variant b.*

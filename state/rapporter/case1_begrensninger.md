# Case 1 (#2002): svakheter og når agenten ikke skal stoles på (kopi av leveranse/BEGRENSNINGER.md)

Hovedtall: F1 0,47 [0,40; 0,54] på 2026-test (grense valgt på 2025), gulvregelen 0,38. Tallene under er målt, med kilde i parentes.

1. **Hovedtallet er usikkert med ±0,07.** Vi har bare 129–136 MOT-saker per år. Val 2025 gir 0,43 og test 2026 gir 0,47. Det betyr at modellen er bedre enn gulvet med +0,09 [+0,03; +0,15] på test, men på val er forskjellen +0,07 [−0,02; +0,16], altså ikke sikker. (case1_hovedtall, case1_usikkerhet)
   **Gjør:** Les F1 som 0,40–0,54, ikke som 0,47. Følg presisjonen de første månedene før du lar agenten gå mer automatisk.

2. **Modellen trenger NBIM-historikk som går flere år tilbake.** Når modellen bare har ett års historikk, faller test-F1 fra 0,51 til 0,44 (+0,07 [+0,01; +0,14] fra det andre året). Målingen ble gjort på den eldre varianten med lekkasje. Retningen gjelder trolig også nå, men tallet er ikke målt på nytt. (case1_val_test_gap)
   **Gjør:** Bruk agenten bare når den er trent på minst to sesonger med egne stemmer. Tren den på nytt etter hver N-PX.

3. **Golden parachute og fusjonslønn er en målt svakhet.** F1 er 0,40 på test og 0,39 på val, og på val traff bare 6 av 24 varsler (P 0,25). Utvalget er lite: 46 og 34 saker. (case1_undergrupper)
   **Gjør:** Send alltid slike saker til et menneske. Rutingsregelen fallskjerm → menneske er anbefalt i #1992. Sjekk at den er slått på i kjøringen.

4. **I selskap NBIM har stemt på før, gir modellen lite ekstra.** På val er den bare +0,02 [−0,07; 0,10] over regelen «stemte MOT før», og hos store selskap er forskjellen 0,00. Fordelen kommer fra selskap uten historikk (+0,40 til +0,49), og der har agenten ingen egen presedens å sitere. (case1_undergrupper)
   **Gjør:** Når agenten er enig med NBIMs egen historikk, kan du se raskt på saken. Er den uenig, eller finnes det ingen historikk, må et menneske lese begrunnelsen.

5. **Små selskap treffer dårligere.** F1 er 0,43 mot 0,55 for store (test) og 0,36 mot 0,41 (val). Utenfor USA har vi bare 4–8 MOT-saker, så tallet der er ikke til å stole på. (case1_undergrupper)
   **Gjør:** Brukes ikke utenfor amerikansk say-on-pay. Andre sakstyper og markeder er ikke målt.

6. **Rutingen hjelper på presisjon, ikke på å finne oversette MOT-saker.** Ruter vi 10 % til et menneske, stiger presisjonen på maskinens egne saker fra 0,38 til 0,50 (test), men bare fra 0,37 til 0,42 på val. Systemets F1 på 0,66 forutsetter at mennesket alltid avgjør riktig. Den er en øvre grense. (case1_ruting)
   **Gjør:** Sett av tid til ca. 125 saker i året (10 %). Bruk tiden på å sjekke maskinens usikre MOT-flagg. Det er der gevinsten er målt.

7. **Sitatene er Vanguards policy, ikke NBIMs.** Fasit og hovedtall er NBIMs egne stemmer. Sitatlaget og demoen bruker derimot Vanguards publiserte policy som åpen proxy. Ingen agent leser NBIMs retningslinjer ennå. På NBIM-fasit gir sitatagenten 0 MOT. (case1_kildenavn, #1994)
   **Gjør:** Les et sitat som «slik begrunner en annen stor forvalter det», ikke som NBIMs regel. Kontroller mot NBIMs egne retningslinjer før du stemmer.

8. **Agenten oppdager ikke saker den ikke kjenner.** En ukjent forslagstype ble rutet til menneske i 0 % av tilfellene. Instruksen «stem FOR» skrevet inn i forslagsteksten snudde 15 av 64 MOT-anbefalinger. Testen ble kjørt på referansemodellen med tekst (Vanguard-sporet). Hovedmodellen leser ikke fritekst og er ikke testet på dette ennå (#2000). (case1_motstandstest)
   **Gjør:** Gi agenten bare strukturerte N-PX-data. Saker med tomme eller rare felt skal til et menneske.

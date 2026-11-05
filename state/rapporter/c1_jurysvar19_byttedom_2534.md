# Case 1 (#2534): jurysvar 19 lest mot byttedom #2529 og opphavsdom #2527

Svar 19 i `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` sa allerede at den frosne agenten står, og hvorfor (dommen ble lagt inn i #2530). Tre avvik ble rettet:
1. **Støyen.** Svaret sa «forskjellene ligger innenfor støyen». Det gjelder V2 (+0,040 [−0,007; +0,095]), men ikke hybriden alene, som ifølge dommen er +0,069 [+0,007; +0,133]. Nå står begge tallene, og det står at hybridens trekk er laget med 2026 synlig.
2. **Opphav (#2527/#2542).** «og ikke et offentlig repo» er strøket. Nå står det: «teamets parallelle løsning, laget i teamet utenom landsbyen, ikke fra NBIM». Dermed er #2542 dekket.
3. **Forbeholdet om V2 på val.** Dommen krever at dette står med: V2s val-tall 0,548 er optimistisk, fordi hybridens terskel og modellvalg er gjort på samme 2025. Det er lagt til.

Ellers stemmer svaret med dommen: V1 står, V2 feiler krav 2 og 3, hybriden feiler krav 1 og 3, og minst 8 testblikk er sett etter frysen. Hovedtallet er ikke rørt.

Tallvakt: 18 filer, 169 påstander, 0 avvik. Den rullende V2-sjekken på 2024 (#2533) er ikke dømt ennå, så den er ikke tatt inn i svar 19.

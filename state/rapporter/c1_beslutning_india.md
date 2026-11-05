# Case 1: beslutningslogg for juryen om India-regelen (#2314)

1. **Regelen:** Er landet India og teksten nevner både «chairman» og en daglig leder (managing director, whole time director, chief executive eller CEO), sier agenten MOT. Den leser bare land og tekst, aldri fasit (`c1_india_bryter.md`).
2. **Kravet satt på forhånd:** En endring kommer bare inn hvis den er bedre enn frossen agent (#2044) både på val 2025 og på 2024 holdt ut, målt med v3-måleren (`--score mot`) (`c1_india_tiltak.md`).
3. **Tallene (F1 på MOT):** val 2025 0,520 → 0,562 (+0,042, 5 saker snudd, alle riktige). 2024 holdt ut 0,536 → 0,544 (+0,008, 1 sak snudd, riktig) (`c1_india_frys_kandidat.md`).
4. **Paret test:** 2024 permutasjon p = 1,0 (én sak kan ikke skille regel fra flaks). 2025 p ≈ 0,06, og det året er der regelen ble funnet, så det tallet er for optimistisk (`c1_india_paret.md`).
5. **Dommerens avgjørelse (#2297):** Regelen bygges ikke inn. Frossen #2044 står som levert agent.
6. **Hvorfor:** Kravet er bare oppfylt på papiret. 2025-gevinsten er målt på de samme sakene den ble funnet på, og det eneste ærlige beviset (2024) er én sak. Det viser at regelen «ikke tapte», ikke at den vant.
7. **Også:** Innkobling ville krevd kodeendring, ny frys og ny kaldstart under 1,5 time før frys. Og de to sakene i 2026 som snus, ville fått MOT med lav P(MOT) (0,09 og 0,19), en motsigelse i beslutningsstøtten.
8. **Status:** Regelen er ført som et testet, ikke bygd funn (NESTE_VERSJON.md og JURY.md). Den er et eksempel på at vi valgte bort en gevinst fordi beviset var for tynt.

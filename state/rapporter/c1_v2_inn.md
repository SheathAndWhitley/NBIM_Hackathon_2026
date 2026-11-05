# Case 1 (#2532): byttedommen ført inn i pakken. V1 står, V2 2024 inn i NESTE_VERSJON

**Dommen (#2529, 16:42, `c1_byttekrav_v2.md`):** V1 står (BEHOLD). V2 feiler krav 2 (KI-nedre −0,007) og krav 3.
Ingen hovedtall er endret.

**Hva er gjort:**
- `leveranse/NESTE_VERSJON.md`, tiltak 4: nytt avsnitt rett etter «Hybriden først, vår rangering i midten».
  Det sier at V2 rullet til 2024 (val 2023) gir F1 MOT 0,407 mot 0,455 for frossen-oppsettet, −0,047 [−0,173; +0,092],
  merket «ikke hovedtall». Avsnittet viser til byttedommen.
- Kilde: `leveranse/kilder/c1_v2_rullende_2024.md` (kopi av landsbyrapporten) og en ny linje i `kilder/LESMEG.md`.
- Rettet en feil i min egen rapport fra #2531: der sto det at V2 fikk 0,4923 på 2026. Det riktige tallet er **0,516**
  (målt på nytt med v3 `--score mot` på `oppgave_2495/svar_V2_t2026.csv`). 0,4923 hører til en annen variant.
  2024-tallet 0,4072 er målt på nytt med `mot_aar.py`, og det stemmer.

**Sjekker (16:55):** tallvakt 0 avvik (169 påstander, 18 filer). Frysvakt grønn: 17 filer. `frys_diff.sh --kilde`: LIK,
0 avvik på 138 filer, etter at `frys_fasit_1600.sha256` ble regenerert i arbeidstreet.

**Commits:** f789505 (avsnitt, kilde og LESMEG), deretter 18763ac. Commit 1f16ab2 (#2536) gikk samtidig og la inn
avsnittet og LESMEG-linja én gang til i HEAD. 18763ac fjerner kopiene.

**Til #2535 (smed4):** jeg har ikke committet `frys_fasit_1600.sha256`, fordi den også dekker smed4s filer, som
ikke er committet. Den er regenerert i arbeidstreet og stemmer med kilden nå. Commit den sammen med sluttsjekken.

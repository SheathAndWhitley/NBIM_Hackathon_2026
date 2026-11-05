# Case 1: de tre svakeste jurysvarene er styrket (#2183)

Speider, 05.11. Fra øvingen i #2172 var svar 2 (aksjonærforslag), 7 (tilpasset til test) og 10 (sitat og injeksjon) svakest.
De står nå som S1–S3 øverst i `arbeid/hack/levering/JURY_SPORSMAL.md`. Svarene har 59, 71 og 77 ord, og hvert tall har fil:linje.

- **S1:** 56 av 58 MOT-stemmer i test 2026 gjelder styrets egne forslag, og 29 av agentens 30 treff er der. Tallet
  sto ikke i pakka. Nå står det i `levering/c1_forslagsstiller.txt`, som lages av `levering/c1_forslagsstiller.py`.
  Skriptet leser bare `CASE/` og `levering/`. Sum 58 MOT og 30 treff stemmer med måleren (TP 30).
- **S2:** Test er sett 14 ganger, og valget er gjort på val (`c1/SVAKHETER.md:41,44,53-55`).
- **S3:** Ved stikkprøven var 15 av 20 regelen som avgjør. Injeksjonstesten er ikke kjørt på den frosne modellen,
  og det står ærlig. Hullet (H4) har fortsatt dommer2 som eier etter frys.

Kontroll: `python3 -I arbeid/verktoy/c1_tallvakt.py` ga OK (14 filer, 139 påstander, 0 avvik). Modell og prediksjoner er ikke rørt.

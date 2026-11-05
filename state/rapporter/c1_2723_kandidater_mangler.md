# Case 1 (#2723): KANDIDATER.md i pakken og speiderens MANGLER 1–8 rettet (commit 7dce245)

smed2, 05.11 ca. 18:30. Bare tekst. Ingen modellfiler eller tall i hovedtallet er endret.

- **KANDIDATER.md** = `state/rapporter/c1_kandidatlogg.md` (arkitekt #2719) i `c1/leveranse/`. pakk_jury tar med hele mappa, så fila kommer i zipen. Nytt øverst: kilderapportene ligger bare i repoet, og «frossen» betyr her repo4. JURY.md og README peker til fila.
- **Rettet etter `c1_jurylesning_1815.md`:**
  1. Samme bytteregel står nå overalt: snitt ≥ +0,02 over tre testår, og intet år under −0,02. 2024 og 2025 er årene repo4 ikke ble funnet på. Gjelder JURY.md:4, 9 og 63 og README:13. Regelen fra før frysen er merket «før frysen».
  2. «Kjørt én gang» er strøket for repo4 i README:9, kravrespons:7 og JURY pkt. 7. Teksten sier nå at 2026 ikke er et friskt testår.
  3. JURY:34 sier nå «32 av de 35 falske flaggene».
  4. 0,06-forbeholdet gjelder den eldre frosne modellen. For repo4 er golvet ikke målt (README:14, kravrespons:10).
  5. Om løpende stemmer står nå samme versjon som i sp. 18 overalt. «Fordi NBIM publiserer løpende» er strøket i ERLIG:59.
  6. Overskriften i sp. 15 er «0,919 for repo4, 0,9232 for eldre frossen». README har fått én setning om hvorfor MOT flagges allerede ved P ca. 0,19.
  7. JURY.md har fått en ordliste øverst. Den forklarer «NBIM-repoet»: trekkene kommer fra `ballot.py` i arrangørens startpakke NBIM_Hackathon_2026, ikke fra NBIMs egen kode. kravrespons:4 er skrevet om tilsvarende.
  8. Pkt. 11 starter nå med en kort oppsummering, merket «målt på eldre frossen». Punkt 8a er ikke gjort: frossen-tallrekkene har ikke fått prefiks hver for seg.
- **Ikke gjort:** listen «Mindre» (KI-etiketter, kjøretid, dobbel parentes, rekkefølgen på merknaden i zip-README).
- **STÅR-reserven:** reglene i `oppgave_2598/lag_staar.py` er tilpasset den nye BYTT-teksten, og reserven er bygd på nytt. I STÅR står 0,06 og 0,9232 uendret.
- **Sjekk:** tallvakt 0 avvik (32 filer, 195 påstander). `git status --short arbeid/hack` er tom etter commit, så #2549 kan kjøre sluttsjekk.sh kl. 19. Ordsjekk og frysvakt er ikke kjørt på nytt. Ingen frosne filer er rørt.
- **Kjør på nytt:** `python3 -I arbeid/oppgave_2723/rett_mangler.py` (idempotent), deretter `uv run python -I arbeid/oppgave_2598/lag_staar.py`.

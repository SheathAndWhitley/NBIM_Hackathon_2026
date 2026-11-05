# Case 1 sluttkontroll: PASS (2026-11-05 13:05, git e74453d, 29 s)

Kommando: `bash arbeid/hack/c1/sluttkontroll.sh` (arkitekt #2150, for dommeren i #1972). Kald kopi i `/tmp/c1_sluttkontroll`, logg `/tmp/c1_sluttkontroll_logg.7etMDu`.

| status | krav | bevis |
|---|---|---|
| PASS | 1 kald start | fremmed.sh fra tom mappe under env -i, uv sync --frozen; uv sync 0 s, kjøring 27 s, totalt 27 s; utgang 0 |
| PASS | 2 F1 MOT = 0,476 | kald uten ruting 0.476190, kald med ruting 0.476190, frossen #2103 0.476190 (REF 0.476190 ± 0.0005, måler v3 sha 8b09c36e01) |
| VENTER | 3 modellfiler uendret siden frys | ikke frosset ennå (frys kl. 16 via LaunchAgent): FRYSVAKT: ikke frosset ennå (<repo>/state/c1_frys.json finnes ikke)  |
| PASS | 4a ingen utdaterte tall (kald kjøring) | 13 filer, 129 påstander om hovedtallet stemmer, 0 avviker |
| PASS | 4b ingen utdaterte tall (pakkas lagrede filer) | 13 filer, 129 påstander om hovedtallet stemmer, 0 avviker |
| PASS | 5 alle sitater har kilde | SITATVAKT OK A 1578/1578 GVG-sitater ordrett med riktig nummer, B 74/74 begrunnelsessitater ordrett i kilden (1578 rader) |
| PASS | 6 varighet under 10 min | 29 s |

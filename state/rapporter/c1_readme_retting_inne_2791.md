# Case 1: README-rettingen er lagt inn (#2791, 18:48)

- Kjørt `python3 -I arbeid/oppgave_2785/rett_readme.py` mot leveranse-kilden: 7 bytter i `arbeid/hack/levering/GITHUB_README_UTKAST.md`, 1 i `arbeid/verktoy/github_synk.sh` (DATA.md-setningen). Andre kjøring: «allerede» (idempotent).
- `bash -n arbeid/verktoy/github_synk.sh`: OK.
- Tallvakt: `32 filer, 197 påstander om hovedtallet stemmer, 0 avviker` / OK (F1 0.5120, 164 av 1578 til menneske).
- Tallsjekk: 3359 tall i 23 filer, alle funnet (avledet A 9, funnet A 2162, funnet B 1188).
- Commit **9d5c855** (bare de to filene). Lagt inn før kl. 19, så #2549-zipen og #2728-synken tar den med uten ekstra steg.

# Case 1 (#2536): leveransemappa under git

Funn 2 fra c1_zip_ren_head_2514.md er nesten lukket: `arbeid/` står i .gitignore, så filene måtte inn med `git add -f`.

- Før: 25 av 79 filer i `arbeid/hack/c1/leveranse` sporet (82 filer på disk da jeg begynte, 57 usporet).
- Commit 1f16ab2: 54 filer lagt til med `git add -f` (46 i kilder/, 7 i spor_npx/, demo_vis.py, kjor.sh). Innholdet er ikke endret, filene er committet slik de lå. Jeg committet bare egne stier (`git commit -- <stier>`), så det andre hadde i staging ble ikke med.
- kilder/c1_v2_rullende_2024.md ble committet av smed i f789505 (#2532) mens jeg jobbet.
- Etter: 80 av 82 sporet. `git diff HEAD` mot de 54 er tom.

## Gjenstår (tas i sluttsjekken)
- `arbeid/hack/c1/leveranse/README.md`
- `arbeid/hack/c1/leveranse/kravrespons.md`

Begge ble holdt utenfor fordi smed fører V2-avgjørelsen inn i pakken (#2532), og kravrespons.md ble endret 16:33. De må inn med `git add -f` når #2532 er ferdig.

## Kontroll etter commit
- c1_tallvakt.py: 18 filer, 169 påstander, 0 avvik, OK (F1 MOT 0,4762).
- frys_diff.sh --kilde: FRYS LIK, 0 avvik (138 filer).

# Case 1 (#2830): repo4-rettelsen (#2829) er i GitHub og i endelig zip (smed2, 05.11 19:20)

- Rettelsen (kravrespons:10, README:14, «repo4 uten samme-sesong-historikk gir 0,396») lå alt i landsbyens HEAD (feid med i 4ed8a9c).
- Synk: `PUSH=1 bash arbeid/verktoy/github_synk.sh` (bruker c1_github_alt.py), hemmelighetsskanning **0 funn**.
  **Ny commit `4f148d18b673663acb487f4aa45d24d630e66804`**, pushet: `git ls-remote origin main` = 4f148d1 (e844c6e → 4f148d1).
  Endret: de to filene + 4 rapporter (c1_dom_rode_punkter_19, c1_repo4_golv_rettet, c1_robusthet_endelig, c1_tallvakt_github_synk).
- Pushet versjon (ren worktree av origin/main): `sjekk_rod.sh` **ALT GRØNN**; tallvakt 32 filer, 197 påstander, **0 avvik**; tallsjekk 3361 tall, 0 feil.
  ULIK JURY_README.md/TREFFSIKKERHET.md = kjent stianonymisering, ingen tall. Kjøring: `bash arbeid/oppgave_2830/kjor.sh`.
- **Endelig zip:** `state/levering/c1_gronn/jurypakke_c1_1918_9f41d82.zip`
  **sha256 `84aefb46fbb5eca17d2d590c2fe571357b03b7f114a1c1b7f57c68cd93462f73`**. `SISTE_GRONNE.zip` peker hit.
  Bygd med `sluttsjekk.sh`: SLUTTSJEKK GRØNN (frysvakt 21 filer uendret, kaldstart, tallvakt, tallsjekk, hovedtall F1 MOT 0,512, ziptest).
- `diff -rq` mot forrige zip (1902_cbae393, e6dae498…): **bare README.md og kravrespons.md** ulike. Begge er byte-like med GitHub-versjonen. sjekk_rod.sh på utpakket zip: ALT GRØNN.
- Ingen frosne filer rørt (frysvakt grønn).

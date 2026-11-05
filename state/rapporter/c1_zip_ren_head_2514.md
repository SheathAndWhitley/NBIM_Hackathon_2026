# Case 1 (#2514): jury-zipen bygd fra ren HEAD og testet fra kald start

**Resultat: GRØNN for HEAD 2f24f0c.**
- Bygd i en APFS-klon (`/tmp/ren_head_2514`) der alle sporede filer er satt til 2f24f0c. Landsbymappa er ikke rørt, fordi andre agenter hadde ukommitterte endringer i jurytekstene.
- `pakk_jury.sh`: TALLVAKT GRØNN, HOVEDTALL F1 MOT 0.476190, «sha256 i pakka = frysfila», 131 filer.
- `test_jury_zip.sh` (tom mappe, tom HOME, sandkasse som nekter lesing av landsbymappa): FRYSVAKT GRØNN, TP 30 FP 38 FN 28 TN 1443 STEMMER, prediksjonsfila LIK den frosne. **ZIPTEST GRØNN F1 MOT 0.476190**.
- `frys_fasit.py` regenerert fra klonen og deretter `frys_diff`: **FRYS LIK, 0 avvik**. Den regenererte fasiten er byte-lik den som ligger i 2f24f0c, så det var ingenting nytt å committe.
- `c1_tallvakt.py`: 18 filer, 169 påstander, 0 avvik.
- Zip-SHA256: c0fd2caf…11a0. Kopi med fasit og testlogg ligger i `arbeid/oppgave_2514/`.

**Funn som betyr noe for kl. 19.30**
1. HEAD flyttet seg fire ganger på de ti minuttene jobben tok (#2508, #2505, #2516, #2513, #2512, #2521, #2522). Nå er HEAD e0ad3c0 med 137 filer, og 9 jurytekster er ukommittert endret. Denne grønne zipen gjelder 2f24f0c, ikke senere commits. Endelig pakke må bygges etter at skrivingen er stoppet.
2. «Ren HEAD» definerer ikke hele zipen. `arbeid/` står i .gitignore, og bare 25 av 79 filer i `c1/leveranse/` er sporet i git. Resten (README.md, kjor.sh, demo_vis.py, kravrespons.md og de fleste i kilder/) tas fra disken. Fasit og frys_diff fanger alle endringer i dem, men git gjør det ikke. Forslag: `git add -f arbeid/hack/c1/leveranse` når teksten er låst.
3. zsh-felle: `git show $H:arbeid/...` blir til `$H:a` (modifikator for absolutt sti). Skriv `${H}:sti`.

# Case 1: sluttsjekk (#2538), GRØNN 16:47 på HEAD 83f152c

**Resultat:** `SLUTTSJEKK GRØNN` med alle steg: frysvakt, kaldstart, tallvakt, tallsjekk, hovedtall, jury-zip, ziptest.

- Start: 16:44:38 på git 29ad6a1 (etter at #2535 lukket). Varighet 150 s.
- HEAD da zipen ble lagret: **83f152c** (#2550 committet JURY.md og ERLIG_EVALUERING.md mens sjekken kjørte).
- `ZIPTEST GRØNN: HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190` (TP 30, FP 38, FN 28). Kald kopi = kv hack_levert = zipen.
- Frysvakt: 17 filer like som ved frys 16:00:01. Tallvakt: 169 påstander, 0 avviker.
- Lagret zip: `state/levering/c1_gronn/jurypakke_c1_1647_83f152c.zip`
- **SHA256:** `1e0260d3d237ae1f411b6bc00f0c26e804ae7764b8d6d1ca1617600cf0542b3f`
- Ekstra kontroll, siden HEAD flyttet seg underveis: alle 80 filer under `c1/leveranse/` i zipen er byte-like `HEAD:83f152c`. Zipen er altså 83f152c, ikke en blanding.
- Prøvekjøring før #2535 lukket: grønn 16:42 på bf0d3f8, `jurypakke_c1_1642_bf0d3f8.zip` (83c3fdb6…). Den er utdatert.
- Tekstavtrykk (bare info): 24 tekstfiler endret siden avtrykket kl. 16:03, alt med vilje (#2532–#2550).

**Merk:** Teksten endres fortsatt (#2547 venter). Kommer det commits i leveranse/ etter 83f152c, må `bash arbeid/hack/levering/sluttsjekk.sh` kjøres på nytt før 19:30 (#1972). Den tar under 3 min.

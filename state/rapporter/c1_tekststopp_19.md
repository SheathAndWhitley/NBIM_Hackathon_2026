# Case 1: tekststopp kl. 19 – ny grønn jury-zip (#2549, smed, 05.11 19:00–19:05)

**Zipen dommeren kaldstarter i #1972:**
`state/levering/c1_gronn/jurypakke_c1_1902_cbae393.zip` (1,1 MB, 163 filer, bygd fra HEAD cbae393)
**sha256 `e6dae4988dbd2056ba4d6ee399d116394e66e9e59493121c09e1ac40f8ea7818`**
(også i `jurypakke_c1_1902_cbae393.zip.sha256` ved siden av). `SISTE_GRONNE.zip` peker nå hit.
Reserven fra 18:27 ligger urørt ved siden av: `jurypakke_c1_1827_0e3b14b.zip`, sha256 98257a6e198fc617dd477d6d0aae52c98741d398c441e1fb54d99a80501aae3c.

## Kjøring
`C1_JURYZIP=/tmp/c1_ts19/jurypakke_c1.zip bash arbeid/hack/levering/sluttsjekk.sh /tmp/c1_tekststopp19_kald` (19:00:33, 123 s, logger /tmp/c1_sluttsjekk_logg.Xrrg):
SLUTTSJEKK GRØNN: frysvakt, kaldstart, tallvakt, tallsjekk, hovedtall, jury-zip, ziptest.
- Frysvakt GRØNN: 21 filer like som ved frys 17:18:18.
- Tallvakt (kald kopi og i ziptesten): 175 påstander, **0 avvik**. Tallsjekk: 3359 tall, alle med kilde.
- HOVEDTALL F1 MOT 0,512000 (P 0,4776, R 0,5517, TP 32 FP 35 FN 26 TN 1446) = kv hack_levert = zipen.
- Ziptest: prediksjonsfila lik den frosne (sha d02cf884…4a0c).

## frys_diff
- Mot den gamle fasiten `frys_fasit_1600.sha256` (sist skrevet 17:25, 9ffe88c): 70 avvik. Det er ventet: tekstrettingene etter 17:25 og verktøyfilene for rullende testår (lagt til 18:18). Ingen av dem er frosne modell- eller prediksjonsfiler; frysvakta dekker dem og er grønn.
- Ny fasit fra HEAD (`frys_fasit.py`, 165 filer), lagret som `state/levering/c1_gronn/frys_fasit_1902_cbae393.sha256`:
  - `frys_diff.sh --kilde` → **FRYS LIK: 0 avvik**.
  - `frys_diff.sh <zipen>` → 2 BORTE, EN_SIDE.md og KRAVRESPONS.md. De er interne utkast og holdes ute med vilje (#2587), samme som i #2595. Ellers lik HEAD.
- Den committede `frys_fasit_1600.sha256` er ikke endret (tekststopp).

## Forskjell fra reserven 18:27 (diff -rq av utpakket zip)
Bare 6 tekstfiler, ingen kode og ingen prediksjoner: leveranse/BEGRENSNINGER.md, leveranse/ERLIG_EVALUERING.md, leveranse/JURY_SPORSMAL.md, levering/GITHUB_README_UTKAST.md, levering/JURY_SPORSMAL.md, levering/LAGET.md. Det er samme liste som i tørrkjøringen (c1_tekststopp_torrkjoring.md).

Merk (som før): 9 tekstfiler nevner ~, men kjørestien leser dem ikke.

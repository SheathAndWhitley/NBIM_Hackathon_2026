# Case 1: jury-zipen fra en mappe med mellomrom og æøå (#2426, smed, 05.11 15.36–15.47)

**Funn: feil, nå rettet i kilden. Zipen må bygges på nytt.**

- Test: `/tmp/jurypakke_c1.zip` (15.30) pakket ut i `/tmp/Mål for juryen æøå/` og kjørt med
  `env -i HOME=... PATH=/opt/homebrew/bin:/usr/bin:/bin sh KJOR.sh` i `c1_stemmeagent/`.
- **Før fiks: utgang 127** rett etter FRYSVAKT GRØNN: `env: for: No such file or directory`.
- Årsak: `KJOR.sh:21` (kilde `arbeid/hack/levering/jury_kjor.sh:21`) var `E="env -i HOME=$ROT/home PATH=$ROT/.venv/bin:..."`,
  og `$E` står uten anførselstegn på linje 22, 26 og 28. Mellomrommet i `$ROT` deler kommandoen i flere ord.
- Fiks (én linje + `$E` → `E` tre steder): `E() { env -i HOME="$ROT/home" PATH="$ROT/.venv/bin:/usr/bin:/bin" LANG=C.UTF-8 "$@"; }`
- **Etter fiks** (samme mappe, tom .venv og ut/, varm uv-cache): utgang 0, `HOVEDTALL ... 0.476190`, `TALLVAKT GRØNN`,
  kjøring 71 s. Logg: `/tmp/Mål for juryen æøå/kjor_fiks.logg`.
- Rettet i kilden `arbeid/hack/levering/jury_kjor.sh` kl. 15.45, før 15.55 (ikke frossen, ikke i leveranse/). Den er lik den testede kopien.
  Gammel versjon: `/tmp/smed_2426_jury_kjor_for.sh`. Ingen commit: arbeid/ er gitignorert.
- **Må gjøres:** `/tmp/jurypakke_c1.zip` fra 15.30 har fortsatt feilen. Pakka bygges på nytt etter frysen (pakk_jury.sh), og da kommer fiksen med.
- I tillegg: `sh arbeid/hack/levering/fremmed.sh "/tmp/Mål fremmed æøå"` gir utgang 0, 0.476190, TALLVAKT GRØNN
  (logg `/tmp/smed_2426_fremmed.logg`). fremmed.sh tåler mellomrom/æøå i målstien. Mellomrom i selve repo-stien (KILDE) er ikke testet.

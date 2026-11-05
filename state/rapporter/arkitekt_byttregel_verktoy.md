# Verksted #2579: byttregel.py låser byttregelen før måling og dømmer BYTT/STÅR etterpå

**Mekanisme:** `arbeid/verktoy/byttregel.py` (laas / dom / vis / fra-benk). Bruk: `arbeid/handbok/oppskrift_byttregel.md`.
- `laas` skriver `state/byttregler/<navn>.json`: frossen, vinduer, snitt-krav, krav til verste vindu, retning,
  sha256 av frosne filer og et regel-hash. Fila kan ikke overskrives.
- `dom` leser en tsv (kandidat, vindu, score). UGYLDIG (utgang 2) hvis hashen ikke stemmer, frosne filer er
  endret, tsv-en er eldre enn låsen, eller frossen mangler et vindu. Ellers STÅR (0) eller BYTT (3).
- Generelt for vinduer: testår i Case 1, folder/splitter i Name that LLM, `--lavere` for log-loss.

**KP (tallene fra #2567, benk.txt):** forventet at bare repo4 består med +0,035 (c1_tre_aar_kandidater.md). Fikk
**BYTT repo4, Δsnitt +0,0345, verste år +0,0166**. V2 +0,0086, NBIMhybrid +0,0056, person +0,0046, V1 −0,0134
og V1p −0,0104 stryker på både snittet og det verste året.

**Testet:** regelen endret etter låsing → UGYLDIG. Frossen fil endret → UGYLDIG. tsv eldre enn låsen → UGYLDIG.
Ny låsing med samme navn → nektet. Kandidat mangler et vindu → STRYKER. `--lavere` snur fortegnet → STÅR.
Frossen fil som ikke finnes ved låsing → nektet.

**Begrensninger, ærlig sagt:** Tidsstempelet er filens mtime, og den kan forfalskes med `touch`. Bevis for
tidspunktet er tavle-notatet med hashen (og en git-commit av låsefila). Verktøyet ser bare på punktestimater,
og KI-en må stå ved siden av. Den virkelige #265-regelen ble ikke låst med verktøyet (den sto i ordren), så for
dommen kl. 18 trengs `--gammel-ok` med den grunnen. Testlåsene ligger i /tmp, ikke i state/.

**Trukket vinkel:** ingen tid til trekning i denne tidsboksen. Vinkelen jeg valgte selv er klinisk
forhåndsregistrering (som på ClinicalTrials.gov), og den er det verktøyet bygger på: hash og offentlig tidsstempel før data.

# Case 1: kravrespons (1 side) og README med ett kall, verifisert fra kald kopi (dommer2, #1971)

**Leveransen:** `arbeid/hack/c1/leveranse/KRAVRESPONS.md` (395 ord, tre overskrifter etter malen) og `arbeid/hack/c1/leveranse/README.md`.
De gamle utkastene med TODO ligger i `leveranse/utkast_1100/`. macOS skiller ikke store og små bokstaver, så `KRAVRESPONS.md` erstattet `kravrespons.md`.

## Ett kall: `bash leveranse/kjor.sh` (fra c1/)
- Kallet henter NBIMs tre N-PX-XML-er fra SEC (`hent_nbim.py`, nytt), kjører `lag_v3.py`, baseline og modell (`gulv_v3.py`), `maaler.py`, motstandstest (`leveranse/motstand_inj.py`) og `leveranse/resultat.py` (tabell + bootstrap-KI over møter, seed 1971).
- Fra kald kopi i /tmp, med bare de 7 filene og uten data, tar det ca. 3 s og gir **SCORE 0.383275** (= tavla #984). Det ble kjørt to ganger.
- SEC-hentingen gir byte-lik `nbim_votes.csv` med arkitektens fil, og train/test_input/fasit er byte-like med `data_v3/`.
- Bare standardbiblioteket. Bytte modell: `MODELL="python3 -I x.py" NAVN="..." bash leveranse/kjor.sh` (kalles med DATAMAPPE UT.csv).

## Tall i kravresponsen (alle fra målte forsøk)
- Følg styret: P/R/F1 0, PR-AUC 0,104, acc 0,897 (#989).
- Historikkregelen: P 0,348, R 0,426, F1 0,383, KI 0,311–0,453, PR-AUC 0,328 (#984).
- smed2 lgbm: F1 0,325 (#987). Sitatlaget gir 0 MOT (#988).
- Motstandstest (ny): 0 av 158 MOT snudde. Det er trivielt, fordi regelen ikke leser teksten, og det står ærlig i begge filene.

## Til #1972 (endelig pakke 18:30)
- Slår en smed regelen på v3 før 18:30: kjør med `MODELL=...`, og bytt tallene i KRAVRESPONS (avsnitt 1, tabellen, setningen om LightGBM) og i README-tabellen.
- Makefile `all` peker fortsatt på `run.sh`. Det er det gamle skjelettet, som krever `modell.py` og `motstand.py`, og ingen av dem finnes. Bruk `kjor.sh`.
- Pakken må inneholde disse filene: `hent_nbim.py lag_v3.py gulv_v3.py maaler.py leveranse/{kjor.sh,resultat.py,motstand_inj.py,README.md,KRAVRESPONS.md}`.

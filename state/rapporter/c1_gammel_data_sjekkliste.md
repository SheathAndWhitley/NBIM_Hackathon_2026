# Case 1: sjekkliste over gammel data i pakka (#2223, ordre #242)

Dommer, 05.11 kl. 13.40. Jeg har bare lest, ikke endret noe. Grunnlaget er kaldstart.sh og fremmed.sh slik de så ut 13.30,
og det ser ut til at smed2 (#2218) allerede har ryddet noe i dem.

## Fasit til #2220
- Ny fil: `state/opplastet/20261105_114241_real_votes.csv`, 2 724 512 byte
- **sha256 `71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6`**
- Kopien `arbeid/hack/CASE/20261105_114241_real_votes.csv` har samme sha.
- Arrangørens npx-fil (11:42 og 11:43 er identiske): sha256 `fa2cc588e5e2dbd1209102fe6bf5273c5a890457111d63d63a52ca9a403f6aa0`.

## Datafiler skriptene kopierer
| Fil | Kopiert av | Leses av | Status |
|---|---|---|---|
| state/opplastet/20261105_114241_real_votes.csv | kaldstart, fremmed | c1_real.py (REAL, historikk + trening via train.py), maaler v2/v3 (FILER["real"]), sjekk_treffsikkerhet.sh, c1_frys.py | NY, ok |
| hack/c1/data_off/real_test_input.csv (sha 1e0e22f8…) | kaldstart, fremmed | c1_real.py (standard inn, test 2026) | avledet av ny (maaler v3 `lag --data real`). #2220 bør lage den på nytt og sammenligne sha |
| hack/c1/retningslinjer/punkter.jsonl | kaldstart, fremmed | retningslinje_oppslag.py | NBIMs retningslinjer, ikke stemmedata, ok |
| kandidater/smed2_c1_mot/pyproject.toml, uv.lock | begge | uv sync | ikke data |
| hack/levering/*.md, hack/c1/leveranse/*.md | fremmed | c1_tallvakt.py | tekst, se under |

Ingen av skriptene kopierer Vanguard-, iShares-, SPDR- eller SEC-filer, `hack/c1/data/` eller `data_off/npx_*`.

## Kode i pakka: hva den leser
- `kjor_agent.py`: bare c1_real. `--data v3` (gammel N-PX-agent) er tatt ut og gir exit (linje 6, 23). Ok.
- `c1_real.py`: leser REAL og real_test_input.csv, kjører train.py på data.csv bygd av REAL, måler med maaler_offisiell_v2.py `--data real`. Ok.
- `oppgave_2044/train.py`: leser bare fila den får som argument. Ok.
- `oppgave_2047/vern.py`: c1_real laster den for `rens_tekst`. Når den lastes, kjører den også **`oppgave_2046/case1_mot.py`** (linje 21). Begge blir dermed med i pakka.
  - case1_mot.py har `FILER` mot `arbeid/hack/CASE/…real_votes.csv` og `…114301_npx_votes.csv` (linje 27–28). Fila leses bare inne i en funksjon (linje 35), ikke når modulen lastes. Agenten leser den altså ikke, og kald start virker selv om hack/CASE ikke er kopiert. **Til opprydding:** stien peker til en annen kopi enn REAL. Innholdet er likt (samme sha).
  - Under `__main__` leser vern.py `data_off/npx_inj_input.csv`. Det er arrangørens npx-fil, ikke gammel data, og agenten kjører ikke den delen. Injeksjonstesten (#2212) bruker den.
- `maaler_offisiell_v2.py` og `v3.py`: `FILER` har både real og npx (arrangørens npx), og stiene er hardkodet til <repo>. fremmed.sh skriver dem om med sed, men kaldstart kjører landsbyens v3, som ikke er kopiert. Kaldstart bruker `--data real`, så det er ok.
- `c1_frys.py`: fryser real_votes.csv, pred_miks_h2.csv, oppgave_2103/full_test.csv og kjor_agent_real_maskin_alene.csv. **Til #2225/#2220:** sjekk at de to prediksjonsfilene er laget fra den nye fila.

## Gammelt som fortsatt ligger i pakka
1. **kaldstart.sh kopierer `hack/c1/*.py`, altså alle 25 filene.** Det tar med SEC-skraperne `hent_votes.py`, `hent_npx.py` og `hent_nbim.py` (sec.gov/EDGAR), `lag_tabell.py` og `lag_unik_strom.py` (Vanguard, iShares, `data/votes_raa_ishares.csv`) og de gamle målerne `maaler.py`, `maaler_v1.py`, `maaler_offisiell.py` og `maaler_nbim.py` (Vanguard). Agenten kjører ingen av dem, men de ligger i kopien. Forslag til #2218: kopier bare det som trengs (ingen av dem, siden v3 kjøres fra landsbyen), slik fremmed.sh gjør.
2. **Tekstene i pakka nevner Vanguard, N-PX og SEC** (antall linjer): METODE.md 20, c1/leveranse/README.md 19, JURY.md 13, KRAVRESPONS.md 12, JURYSVAR.md 9, BEGRENSNINGER.md 7, JURY_SPORSMAL.md 5, levering/README.md 2. De fleste kaller det «eldre N-PX-grunnlinje», men noen står som om de gjelder nå:
   - `METODE.md:44`: under «Kjennetegn» står «Vanguards publiserte N-PX-stemmer … SEC-tall». Det ser ut som en beskrivelse av den nåværende modellen. **Må rettes eller fjernes (#2219).**
   - `JURY.md:39,47,48,56`: v2-Vanguard-tall (0,839, 0,24 osv.).
   - `c1/leveranse/README.md:47–52,68–69`: SEC-lenker og `SPOR=npx`, som krever nett til sec.gov.
3. `c1_real.py` bruker maaler **v2** for sin egen logg, mens hovedtallet regnes med v3 `--score mot`. Det er ikke gammel data, men det er greit å vite i #2220.

## Konklusjon
Det agenten faktisk leser er bare den nye real_votes.csv (sha 71ba5135…) og real_test_input.csv, som er avledet av den. Det jeg ikke har funnet noe sted er stemmedata fra Vanguard, iShares, SPDR eller SEC-skrapingen i det agenten leser. Det som må ryddes er filene som blir med i kopien (punkt 1), en død sti i case1_mot.py og tekstene i pakka (punkt 2).

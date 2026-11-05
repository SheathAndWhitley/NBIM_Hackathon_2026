# Slik leser du koden (for laget)

Én side. Alle stier er relative til roten av denne repoen.

## Inngangen, i den rekkefølgen koden kalles
1. `KJOR.sh`: det eneste kallet juryen trenger. Sjekker frosne filer, lager låst miljø, kjører agenten, måler, kjører tallvakta.
2. `arbeid/hack/levering/kjor_agent.py`: hele agenten. Inn: saker (CSV eller én sak som JSON). Ut: `ut/agent.csv`.
3. `arbeid/hack/levering/c1_real.py`: limet. Kaller modellen, kalibrerer P(MOT), ruter usikre saker til menneske, slår opp GVG-sitat.
4. Modellen: `arbeid/hack/levering/modell_repo4.py` + `arbeid/hack/levering/stemmeagent/` (historikktrekk).
   Den gamle frosne modellen ligger i `arbeid/oppgave_2044/train.py`. Linja `TRAIN = ...` i `c1_real.py` sier hvilken som brukes.
5. Vern: `arbeid/oppgave_2047/vern.py` (instruks-/injeksjonsvakt) og `arbeid/hack/levering/injeksjon_hoflig.py`.
6. Måleren: `arbeid/hack/c1/maaler_offisiell_v3.py` (fasit = NBIMs egne stemmer, `against_board`).

## Kjør på 2 minutter
Krever bare [uv](https://docs.astral.sh/uv/).

    sh KJOR.sh

Ferdig på under ett minutt med varm uv-cache, et par minutter første gang. Se etter
`HOVEDTALL F1 MOT mot styret (v3 --score mot): ...` og `TALLVAKT GRØNN`. Svar per sak: `ut/agent.csv`.
Én sak: `.venv/bin/python arbeid/hack/levering/kjor_agent.py --ut /tmp/ut --sak '<json i real_votes-format>'`.

## Hvor tallene kommer fra
- Data: `state/opplastet/20261105_114241_real_votes.csv`, NBIMs stemmer fra arrangøren (sha256 i `arbeid/hack/c1/leveranse/README.md`).
- Tidssplitt: tren på år før, velg grense på val 2025, kjør test 2026 én gang. Historikktrekk ser bare eldre år.
- Hovedtallet er F1 på MOT mot styret på test 2026, regnet av `maaler_offisiell_v3.py --score mot` fra `ut/pred_maaler.csv`.
  «Følg styret» gir 0. Siste linje `SCORE` i den lange utskriften er avvik fra styret, et sidetall.
- Tallvakta `arbeid/verktoy/c1_tallvakt.py` sjekker at hvert tall i .md-filene stemmer med kjøringen. Skriver du et tall
  i en tekst uten at kjøringen gir det, blir den RØD.
- Byttet fra frossen modell til repo4: regel satt før måling, tre testår, se `ERLIG_EVALUERING.md` § 7.

## Hva som er frosset
- Lista står i `FROSNE_SHA256.txt`; `KJOR.sh` stopper med `FRYSVAKT RØD` hvis én av dem er endret.
- Modell, agent, vern, data og prediksjonsfiler er frosset. Ikke rediger dem; endringer går i nye filer.
- Tekstene (README, JURY_*, BEGRENSNINGER, ERLIG_EVALUERING) kan rettes til tekststopp kl. 19, men tallvakta må være grønn.
- `pyproject.toml` + `uv.lock` låser pakkeversjonene. Bruk `uv sync --frozen`, aldri oppgrader.

## Ikke les først
`arbeid/hack/c1/leveranse/spor_npx/` er et gammelt spor (egen SEC-skraping) og brukes ikke i hovedtallet.

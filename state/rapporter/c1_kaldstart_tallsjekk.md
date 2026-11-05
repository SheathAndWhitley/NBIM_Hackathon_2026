# Case 1: kaldstarten kjører tallsjekken automatisk (#2273)

- `arbeid/hack/c1/kaldstart.sh`: etter steg 4 (måler v3) kjøres `c1_tallsjekk.py --bare-ikke` (#2271) mot landsbymappen.
  Utskrift: `TALLSJEKK (varsel): <oppsummering>` + opptil 20 linjer `ikke funnet: fil:linje tall type`.
- `arbeid/hack/levering/fremmed.sh`: samme, etter HOVEDTALL og før tallvakta (`TALLSJEKK (varsel): ...`).
- Bare varsel: krasjer tallsjekken, skrives `tallsjekken feilet: ...`; utgangskodene (0/1/2/3/4) er uendret.
- Frysvakta og modellfilene er urørt: sha256 av c1_frys.py før og etter = 20d5ac2b06…ef318.

## Test 14:09–14:12
- `bash -n` / `sh -n`: ok.
- Kald kjøring kaldstart.sh: utgang 0, GRØNN F1_MOT 0.476190, `TALLSJEKK (varsel): 2042 tall i 15 filer: IKKE FUNNET 17, avledet A 35, funnet A 1552, funnet B 438`.
- fremmed.sh: utgang 0, HOVEDTALL 0.476190, TALLVAKT GRØNN, `TALLSJEKK (varsel): ... IKKE FUNNET 9 ...`.

## Merk
Tallet IKKE FUNNET svinger mellom kjøringer (17 -> 9 på tre minutter) fordi kilde B er alle
logger i arbeid/oppgave_2xxx, og kilde B vokste fra 13 395 til 46 975 tall mens andre agenter jobbet.
Kilde B kan altså «finne» et tall i en tilfeldig logg. Det som teller kl. 19.30 er `--streng`-lista
(bare kilde A) eller å stikkprøve de ikke-funnede linjene; dommeren (#2255) bør lese linjene, ikke bare antallet.

## Commit
Ingen commit: `arbeid/` og `state/` står i .gitignore (også frysvakt-commiten e74453d tok bare med tavle.py).
Jeg tvang ikke inn ignorerte mapper med `git add -f`. Endringen er de to blokkene merket `#2273` i skriptene
(`grep -n 2273 arbeid/hack/c1/kaldstart.sh arbeid/hack/levering/fremmed.sh`). Fjern dem for å rulle tilbake.

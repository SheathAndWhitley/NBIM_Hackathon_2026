# Case 1 (#2457): 3 kilder til NESTE_VERSJON lagt i jury-zipen, utkast_1100 tatt ut

Bare pakking. Ingen modell- eller prediksjonsendring.

## Gjort
- `arbeid/hack/levering/pakk_jury.sh`: ny kopier-linje med `state/rapporter/c1_feil_per_gruppe.md`,
  `state/rapporter/arkitekt_c1_neste_versjon.md`, `arbeid/oppgave_2274/feil_val2025.md` (bøtte b, #2449).
  Ingen av dem inneholder `~`.
- Samme fil: `-not -path "*/spor_npx/utkast_1100/*"` i find-kallet for c1/leveranse (bøtte c punkt 1).
- `arbeid/hack/levering/frys_fasit.py`: finn() hopper over utkast_1100, så fasiten følger skriptet.
- `arbeid/hack/levering/frys_fasit_1600.sha256` laget på nytt: 113 filer. Avtrykkene står i
  `state/rapporter/c1_frys_fasit.md` (tillegg #2457).

## Målt
- sluttsjekk.sh (med testfrys i /tmp, C1_FRYS, siden frysen kl. 16 ikke var satt): SLUTTSJEKK GRØNN,
  HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen. Zip 1,1 MB, 113 filer. Ziptest GRØNN i sandkasse.
- `unzip -l`: de 3 filene er med, 0 treff på utkast_1100.
- `frys_diff.sh` mot zipen og mot `--kilde`: FRYS LIK, 0 avvik.

## Til arkitekten (#2435): pekerne i NESTE_VERSJON.md skal nå ha disse stiene (relativt til zip-rota)
| linje | i dag | skal være |
|---|---|---|
| 5 | `landsbyrapport:c1_feil_per_gruppe.md:4` | `state/rapporter/c1_feil_per_gruppe.md:4` |
| 6 | `<arbeidsmappe>/oppgave_2274/feil_val2025.md:1` | `arbeid/oppgave_2274/feil_val2025.md:1` |
| 9, 18, 44 | `arkitekt_c1_neste_versjon.md` (linje 9 med `landsbyrapport:`) | `state/rapporter/arkitekt_c1_neste_versjon.md` |
| 13, 43 | `c1_feil_per_gruppe.md:25`, `:26-27` | `state/rapporter/c1_feil_per_gruppe.md:25`, `:26-27` |
| 14, 43 | `feil_val2025.md:7`, `:9-10` | `arbeid/oppgave_2274/feil_val2025.md:7`, `:9-10` |
Linjenumrene stemmer: filene kopieres uendret. Endres NESTE_VERSJON.md, må fasiten lages på nytt
(`python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256`).

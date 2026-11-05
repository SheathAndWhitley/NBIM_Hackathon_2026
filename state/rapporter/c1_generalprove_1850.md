# Case 1: generalprøve kl. 18:50 (#2748): kald start av jury-zipen, GRØNN

**Resultat: GRØNN.** Begge kandidat-zipene kjører feilfritt fra tom mappe, hovedtallet er 0,512000 og agent.csv har frysens sha `24ee6b18…`. Fasit for dommerens 19:30-sjekk (#1972) står under.

## Hva ble kjørt
Som et jurymedlem: zip kopiert til tom mappe i /tmp, `unzip`, `cd c1_stemmeagent`, `sh KJOR.sh`, under `env -i` (tom HOME, PATH = uv + /usr/bin:/bin) og `sandbox-exec` som nekter lesing i landsbymappa. Deretter testårskommandoen ordrett fra JURY.md: `bash arbeid/hack/c1/leveranse/verktoy/testaar.sh` fra pakkas rot (trener på nytt, ikke `--rask`).

Da oppgaven startet 18:25 var SISTE_GRONNE `jurypakke_c1_1744_7efa4da.zip`. Kl. 18:27 lagret #2740 en ny grønn zip, `jurypakke_c1_1827_0e3b14b.zip`, og SISTE_GRONNE peker nå på den. Begge ble kjørt.

| zip | sha256 (zip) | FRYSVAKT | HOVEDTALL F1 MOT | TALLVAKT | agent.csv sha | pred_maaler.csv sha | tid |
|---|---|---|---|---|---|---|---|
| 1744_7efa4da | e48426cd… | GRØNN, 19 filer | 0,512000 | GRØNN, 25 filer, 176 påstander, 0 avvik | 24ee6b182f55… = frys | d02cf88475bf… = frys | uv sync 2 s + kjøring 31 s |
| 1827_0e3b14b | 98257a6e… | GRØNN, 19 filer | 0,512000 | GRØNN, 26 filer, 176 påstander, 0 avvik | 24ee6b182f55… = frys | d02cf88475bf… = frys | uv sync 7 s + kjøring 49 s |

Måler v3 begge: TP 32, FP 35, FN 26, P 0,4776, R 0,5517, 58 MOT i fasit. Til menneske 164 av 1578 (10,4 %). Ingen av loggene nevner «landsby».

## Testårskommandoen (bare i 1827-zipen)
`testaar.sh` kom inn med #2742 (HEAD 30c5e67) og finnes ikke i 1744-zipen; der viser JURY.md fortsatt bare til `kjor.sh`. I 1827-zipen kjørte den på 11 s, utgang 0, og siste linje er identisk med forventet linje i JURY.md:

    2024  MOT mot styret: TP 44 FP 42 FN 44  P 0.5116  R 0.5000  F1 0.5057  (88 i fasit)
    2025  MOT mot styret: TP 43 FP 20 FN 56  P 0.6825  R 0.4343  F1 0.5309  (99 i fasit)
    2026  MOT mot styret: TP 32 FP 35 FN 26  P 0.4776  R 0.5517  F1 0.5120  (58 i fasit)
    F1 MOT mot styret: 2024 0.5057  2025 0.5309  2026 0.5120  snitt 0.5162

## Fasit til #1972 (19:30)
- Bruk 1827_0e3b14b eller nyere; 1744 mangler testaar.sh og er utdatert.
- Forventet: FRYSVAKT GRØNN (19 filer), HOVEDTALL 0.512000, TALLVAKT GRØNN (0 avvik), agent.csv sha `24ee6b182f553e39…`, pred_maaler.csv sha `d02cf88475bfee93…`, testaar.sh siste linje snitt 0.5162. Hele løpet tar under 2 min med varm uv-buffer.
- Kommer en ny zip etter tekststopp (#2549), kjør samme løp på den; skriptet og mappene ligger i `/tmp/c1_generalprove_1850*` (logger `.logg`, `.testaar.logg`).

Varighet: 18:25–18:31. Første feil: ingen.

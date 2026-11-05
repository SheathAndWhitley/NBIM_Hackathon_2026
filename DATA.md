# Data

Arrangørens casedata for Case 1 ligger i `ny_data/`:

| fil | hva | brukt til |
|---|---|---|
| `ny_data/real_votes.csv` | NBIMs egne stemmer, 13 757 saker, 194 selskaper, 2019–2026 (https://vd.nbim.no/, utlevert som fil av arrangøren 5. november) | fasit, trening, validering, test |
| `ny_data/npx_votes.csv` | NBIMs stemmer fra SEC N-PX | ikke brukt i hovedtallet (se under) |

`sh KJOR.sh` gjør resten selv:

| hva | sti | laget av |
|---|---|---|
| real_votes.csv på fast sti | `state/opplastet/20261105_114241_real_votes.csv` | kopiert fra `ny_data/` |
| testinndata 2026 (uten fasitfelt) | `arbeid/hack/c1/data_off/real_test_input.csv` | `arbeid/hack/c1/lag_inndata.py` |
| valideringsinndata 2025 (uten fasitfelt) | `arbeid/hack/c1/data_off/real_val_input.csv` | `arbeid/hack/c1/lag_inndata.py` |

Stien med tidsstempel er fast fordi målerne og agenten sjekker akkurat den og fila sin sha256
(`71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6`). En annen versjon av real_votes.csv stopper agenten
med en tydelig feil. `lag_inndata.py` tar årene 2026 og 2025, setter `id = meeting_id|item_no` og fjerner fasitfeltene.
Begge mappene er gitignorert.

Mangler `ny_data/` (for eksempel i en kopi uten data), legg arrangørens fil der først:

    mkdir -p ny_data && cp <casepakka>/real_votes.csv ny_data/
    sh KJOR.sh

## Hvorfor ikke npx_votes.csv

I `npx_votes.csv` følger feltet `mgmt_rec` ofte NBIMs egen stemme i stedet for styrets anbefaling. Fila gir derfor feil
etikett for «mot styret» på mange saker. Feltet ville også vært en lekkasje av svaret. Vi bruker bare `real_votes.csv`,
der `against_board` er regnet mot styrets faktiske anbefaling.

## Hva agenten ser

Testinndataene har ikke fasitfeltene (`nbim_vote`, `against_board`) eller begrunnelsesfeltene, som bare finnes for
MOT-stemmer (`rationale_text`, `rationale_section`, `position_paper`). NBIMs stemmer brukes bare fra møter før saken,
som historikktrekk. Lekkasjetesten (`arbeid/hack/c1/lekkasjetest.py`) viser at svaret ikke endres når `nbim_vote`,
`nbim_vote_raw`, `rationale_*` og `position_paper` tømmes i hele datasettet, eller når framtidige stemmer snus.

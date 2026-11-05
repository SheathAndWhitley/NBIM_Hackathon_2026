# Case 1 (#2731): brute force-lekkasjesjekk på 400 rader for repo4s fire historikktrekk

**Svar: 15 avvik på 400 rader (11 rader).** Alle 15 kommer av samme ting: et selskap har to møter
**samme dato**, og repoets `ballot.add_history` regner møtet med lavest `meeting_id` som «tidligere».
Da brukes stemmen i det andre samme-dags-møtet som historikk. Påstanden «bare møter strengt før saken»
holder altså ikke for repo4 i dette tilfellet. Ingen avvik fra senere datoer, og ingen fra samme møte.

## Metode
- Rådata `state/opplastet/20261105_114241_real_votes.csv`, sha256 71ba5135 (sjekket i skriptet).
- Trekkene som i repo4 (oppgave_2490/2567, `--repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate`),
  hentet fra arrangørens `ballot.py` via `load_real()` som i `abl_rull.py`.
- 400 tilfeldige rader (seed 2731, alle år 2019–2026, 31 fra 2026). For hver rad regnes hvert trekk på nytt
  fra bunnen, bare fra merkede rader i samme selskap med møtedato strengt før radens dato. Sammenlignes med repoets verdi.
- Kode: `arbeid/oppgave_2731/brute.py`, `arbeid/oppgave_2731/aarsak.py`. Ingen frosne filer eller prediksjoner rørt.

## Tall
| trekk | avvik / 400 | rader med historikk |
|---|---|---|
| prev_same_item | 1 | 236 |
| prev_same_person | 0 | 113 |
| prev_meeting_any_dev | 8 | 343 |
| hist_type_dev_rate | 6 | 326 |
| **sum** | **15** | |

- KP (kontroll av forklaringen): med repoets rekkefølge (dato, så `meeting_id`) i stedet for «strengt tidligere dato»: forventet 0, fikk **0 avvik**. Så alle 15 er samme-dags-møter, ikke en annen feil.
- Hele datasettet: 177 av 13 757 rader (33 møter) kan få historikk fra et annet møte samme dato. Per år: 2019: 48, 2020: 37, 2021: 5, 2022: 25, 2023: 12, 2024: 13, 2025: 23, **2026: 14**. 8 MOT blant de 177.
- Test 2026 (kjøringen i `oppgave_2490/repo4.csv`): 14 berørte rader, 1 er MOT i fasit, og den ene er flagget MOT (riktig). Om flagget skyldes samme-dags-trekket er ikke målt. Tar man bort de 14 radene, går F1 i den kjøringen fra 0,529 til 0,522 (−0,007). Det er ikke hovedtallet 0,512. Det sier bare at effekten er liten.

## Vurdering
Dette er lekkasje fra samme dag, ikke fra framtida. NBIM avgir stemmene før møtet, så stemmen i et annet
møte samme dag er trolig kjent når stemmen avgis. Men den strenge påstanden i teksten stemmer ikke for repo4
og må rettes. Vi retter ikke modellen etter frysen.

## Ferdig linje til JURY_SPORSMAL sp. 20 (erstatter «ikke kjørt på nytt for repo4»)
Brute force-sjekken på 400 tilfeldige rader er nå også kjørt for de fire trekkene i repo4: 15 avvik (11 rader). Alle kommer av at et selskap har to møter samme dato, og NBIM-repoets `ballot.py` regner da det ene som tidligere. Med den rekkefølgen er det 0 avvik, og ingen trekk bruker senere datoer. 14 av 1539 testrader i 2026 er berørt, 1 av dem er MOT. For repo4 gjelder derfor «strengt tidligere møte, eller annet møte samme dag», ikke «strengt tidligere dato» (`c1_lekkasje_repo4.md`).

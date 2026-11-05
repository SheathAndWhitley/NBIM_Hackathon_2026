# Stemmeagenten: finner stemmene der NBIM går mot styret

Norges Bank Investment Management (NBIM) stemmer på tusenvis av generalforsamlinger hvert år.
I de aller fleste sakene følger NBIM styrets anbefaling. Det som krever en forvalter, er de få
sakene der fondet bør stemme **mot styret**.

Agenten leser en generalforsamlingssak (forslagstekst, sakstype, selskap, styrets anbefaling) og:
- anbefaler FOR eller MOT slik NBIM ville stemt,
- siterer avsnittet i NBIMs Global Voting Guidelines som saken hører under,
- sender usikre og uleselige saker til et menneske, med grunn.

Den er beslutningsstøtte, ikke en autopilot: et menneske stemmer.

> **Til deg som ser over**
> - **Hovedtallet:** F1 MOT **0,512** på test 2026; snitt over tre testår 2024/2025/2026 0,5057 / 0,5309 / 0,5120 = **0,5162**. Målt kandidat for kandidat i [KANDIDATER.md](arbeid/hack/c1/leveranse/KANDIDATER.md).
> - **Koden for agenten:** [arbeid/hack/levering/kjor_agent.py](arbeid/hack/levering/kjor_agent.py) (hele agenten, kaller [c1_real.py](arbeid/hack/levering/c1_real.py)), modellen i [modell_repo4.py](arbeid/hack/levering/modell_repo4.py) og [arbeid/oppgave_2044/train.py](arbeid/oppgave_2044/train.py), sitat fra retningslinjene i [retningslinje_oppslag.py](arbeid/hack/levering/retningslinje_oppslag.py).
> - **Regenerer scoren:** `sh KJOR.sh` (hovedtallet, linja `HOVEDTALL`); de tre testårene: `bash arbeid/hack/c1/leveranse/verktoy/testaar.sh`. Begge krever casedata, se [DATA.md](DATA.md).
> - **Ærlig evaluering og jurysvar:** [ERLIG_EVALUERING.md](arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md), [JURY_SPORSMAL.md](arbeid/hack/c1/leveranse/JURY_SPORSMAL.md) (den gjeldende; `arbeid/hack/levering/JURY_SPORSMAL.md` er en eldre øvingsversjon).
> - **Hvordan det ble laget:** [LAGET.md](LAGET.md).

## Hovedtallet: F1 på stemmer mot styret

Målt én gang på test 2026, NBIMs egne stemmer fra arrangøren (1539 saker med fasit, 58 av dem MOT mot styret).
Modell og grense er valgt på årene før.

| | F1 MOT | presisjon | recall | treff |
|---|---|---|---|---|
| Følg styret (grunnlinje) | 0 | – | 0 | finner 0 av 58 |
| **Agenten** | **0,512** | 0,478 | 0,552 | TP 32 FP 35 FN 26 |

Hvorfor ikke accuracy: bare 3,8 % av sakene er MOT. «Følg styret» får derfor høy accuracy uten å finne
en eneste sak mot styret. Vi måler bare det forvalteren trenger: hvor mange av MOT-sakene agenten finner,
og hvor ofte den roper falskt.

Ærlig om tallet:
- Med 58 MOT-saker er tallet usikkert: 95 % KI [0,400; 0,621] (klyngebootstrap per selskap). Les det som et intervall, ikke som tre desimaler.
- Modellen ble byttet etter modellfrysen etter en regel skrevet før målingen: snitt over tre testår minst
  +0,02 over den frosne modellen, og intet år mer enn 0,02 under. Resultat: 2024 0,5057, 2025 0,5309,
  2026 0,5120 mot frossen 0,4545 / 0,5143 / 0,4762, snitt +0,0345. Gevinsten er ikke statistisk sikker.
- Agenten sender 164 av 1578 saker (10,4 %) til et menneske.

## Kjør det selv

Krever macOS eller Linux og [uv](https://docs.astral.sh/uv/). Første kjøring laster ned låste pakker (ca. 80 MB).

    git clone https://github.com/Martinkristofferhansen/nbim.git && cd nbim
    # legg arrangørens casedata på stiene i DATA.md (tre csv-filer, ikke med i repoen)
    sh KJOR.sh

Casedata må ligge på plass først: uten dem stopper `sh KJOR.sh` med `FEIL DATAFIL: kan ikke lese ...`.
Se [DATA.md](DATA.md) for hvilke filer og hvilke stier.

Ferdig etter et par minutter. Mot slutten står `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000`,
så tre linjer fra tallvakta, og til sist `TALLVAKT GRØNN`. Hovedtallet er linja `HOVEDTALL`.
Linja `SCORE 0.529412` lenger opp er v2-målerens tall (en annen måler), og linjer merket
`IKKE HOVEDTALL` er tilleggsmål. Agentens svar per sak ligger i `ut/agent.csv`.

## Begrensninger (de tre viktigste)

1. **Nye selskaper:** uten stemmehistorikk treffer agenten klart dårligere, og nesten alt går til menneske.
2. **Krever løpende publiserte stemmer:** modellen bruker NBIMs stemmer fra tidligere møter. Med bare
   historikk fra tidligere år faller treffet.
3. **Aldri AVSTÅ:** agenten svarer FOR eller MOT. MOT betyr «avvik fra styret, vurder MOT eller AVSTÅ».

Alle ni punktene står i [BEGRENSNINGER.md](arbeid/hack/c1/leveranse/BEGRENSNINGER.md).

## Les mer

- [JURY_README.md](arbeid/hack/levering/JURY_README.md): kjøring ord for ord, kolonnene i `agent.csv`, forventet utskrift.
- [METODE.md](arbeid/hack/levering/METODE.md): data, tidssplitt, modell, kalibrering, ruting og hvordan tallene er målt.
- [ERLIG_EVALUERING.md](arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md): hva som er målt, hva som ikke er det, og byttet av modell.

Data: NBIMs stemmer fra arrangøren av hackathonet. Kilder, kreditering og AI-bruk står i [arbeid/hack/c1/leveranse/README.md](arbeid/hack/c1/leveranse/README.md).

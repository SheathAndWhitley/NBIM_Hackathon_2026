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
> - **Hovedtallet:** F1 MOT **0,512** på test 2026 (målt én gang). Holder over tid: 0,5057 / 0,5309 / 0,5120 på testårene 2024/2025/2026, snitt 0,5162 (ikke hovedtall). Målt kandidat for kandidat i [KANDIDATER.md](arbeid/hack/c1/leveranse/KANDIDATER.md).
> - **Koden for agenten:** [arbeid/hack/levering/kjor_agent.py](arbeid/hack/levering/kjor_agent.py) (hele agenten, kaller [c1_real.py](arbeid/hack/levering/c1_real.py)), modellen i [modell_repo4.py](arbeid/hack/levering/modell_repo4.py) (gjeldende; [arbeid/oppgave_2044/train.py](arbeid/oppgave_2044/train.py) er den forrige frosne modellen, beholdt for sammenligning), sitat fra retningslinjene i [retningslinje_oppslag.py](arbeid/hack/levering/retningslinje_oppslag.py).
> - **Regenerer scoren:** `sh KJOR.sh` (hovedtallet, linja `HOVEDTALL`); de tre testårene: `bash arbeid/hack/c1/leveranse/verktoy/testaar.sh`. Begge krever arrangørens `real_votes.csv` i `ny_data/`, se [DATA.md](DATA.md).
> - **Ærlig evaluering og jurysvar:** [ERLIG_EVALUERING.md](arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md), [JURY_SPORSMAL.md](arbeid/hack/c1/leveranse/JURY_SPORSMAL.md) (den gjeldende; `arbeid/hack/levering/JURY_SPORSMAL.md` er en eldre øvingsversjon).
> - **Hvordan det ble laget:** [LAGET.md](LAGET.md). `arbeid/oppgave_*` og `state/` er arbeidsmapper fra laget, forklart der.

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
- Regelen ble skrevet ned før målingen: snitt over tre testår minst +0,02 over den frosne modellen, og intet år
  mer enn 0,02 under. Kandidaten besto, så modellen ble byttet etter modellfrysen kl. 16. Resultat: 2024 0,5057, 2025 0,5309,
  2026 0,5120 mot frossen 0,4545 / 0,5143 / 0,4762, snitt +0,0345. Gevinsten er ikke statistisk sikker. En ny runde til kl. 18:15 (18 målinger, beste +0,0135) besto ikke
  regelen, så modellen står. Alle kandidater: [KANDIDATER.md](arbeid/hack/c1/leveranse/KANDIDATER.md). <!-- tallvakt: ignorer: kandidatrunde, ikke hovedtall -->
- Agenten sender 164 av 1578 saker (10,4 %) til et menneske. 1578 er alle testsakene; i 39 av dem ga styret ingen
  anbefaling, så «mot styret» kan ikke avgjøres, og de er utenfor F1-tallet (derfor 1539 med fasit).

## Kjør det selv

**Tilgang:** repoen er privat. Be eieren av `Martinkristofferhansen/nbim` om lesetilgang før du kloner.
**Versjon:** `main` er versjonen som gjelder. Repoen har bare den ene grenen; det finnes ingen release eller tagg å velge.

Krever macOS eller Linux og [uv](https://docs.astral.sh/uv/). Første kjøring laster ned låste pakker (ca. 80 MB)
til et eget miljø `.venv_kjor` (rører ikke et `.venv` du har fra før).

    git clone https://github.com/Martinkristofferhansen/nbim.git && cd nbim
    mkdir -p ny_data && cp <casepakka>/real_votes.csv ny_data/
    sh KJOR.sh
    sh arbeid/hack/c1/leveranse/demo.sh "$PWD"

Det eneste du legger inn selv er arrangørens `real_votes.csv` (casedata, ikke med i repoen) i `ny_data/`.
`sh KJOR.sh` kopierer den til stien målerne bruker og lager testinndata (2026) og valideringsinndata (2025) av den
med [lag_inndata.py](arbeid/hack/c1/lag_inndata.py). Se [DATA.md](DATA.md). Uten fila stopper `sh KJOR.sh` med `MANGLER DATA`.

Ferdig etter et par minutter. Mot slutten står `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000`,
så tre linjer fra tallvakta, og til sist `TALLVAKT GRØNN`. Hovedtallet er linja `HOVEDTALL`.
Linja `SCORE 0.529412` lenger opp er fra en eldre måler (v2, avvik fra styret i begge retninger) og er ikke hovedtallet; linjer merket
`IKKE HOVEDTALL` er tilleggsmål. Agentens svar per sak ligger i `ut/agent.csv`.

**Mac og Linux gir litt ulikt tall.** Samme kode, samme data og samme låste pakker gir hovedtallet 0,512 på macOS
(der alle tallene i dokumentene er målt) og 0,520 på Linux. Forskjellen kommer fra numerikken i bibliotekene på de to
plattformene, ikke fra modellen. Tallvakta tåler derfor 0,01 på hovedtallet: på Linux skriver den `PLATTFORMAVVIK`
med begge tallene og blir grønn; avviker tallet mer enn 0,01, blir den rød. <!-- tallvakt: ignorer: plattformtall -->

`demo.sh` viser seks saker med agentens svar, sitatet fra retningslinjene og NBIMs faktiske stemme. Den bruker
kjøringen fra `sh KJOR.sh`; mangler `ut/`, kjører den `sh KJOR.sh` selv først.

## Begrensninger (de tre viktigste)

1. **Nye selskaper:** uten stemmehistorikk treffer agenten klart dårligere, og nesten alt går til menneske.
2. **Krever løpende publiserte stemmer:** modellen bruker NBIMs stemmer fra tidligere møter. Med bare
   historikk fra tidligere år faller treffet.
3. **Aldri AVSTÅ:** agenten svarer FOR eller MOT. MOT betyr «avvik fra styret, vurder MOT eller AVSTÅ».

Alle ni punktene står i [BEGRENSNINGER.md](arbeid/hack/c1/leveranse/BEGRENSNINGER.md).

## Hvor tallene står

Én kilde: hovedtallet og grunnlinja står i tabellen over, og `sh KJOR.sh` regenererer dem (linja `HOVEDTALL`).
Testårene og alle kandidater står i [KANDIDATER.md](arbeid/hack/c1/leveranse/KANDIDATER.md). Andre dokumenter siterer disse.
Den første versjonen (v1) hadde egne filer for nøkkeltall og presentasjon; de er ikke med og erstattes av dette avsnittet. Den første hele leveransen (kl. 12:55) ligger som historikk i `arbeid/hack/levering/c1_v1/` og er merket eldre; tallene der gjelder ikke.
v1 målte bare NBIMs amerikanske say-on-pay-saker (SEC N-PX). Docstringene i `arbeid/hack/levering/stemmeagent/`
(og de byte-like kopiene i `arbeid/hack/c1/bytte/` og `arbeid/hack/c1/leveranse/verktoy/`) sier fortsatt «say-on-pay votes only»: filene er fryst (sha256 i [FROSNE_SHA256.txt](FROSNE_SHA256.txt)) og står urørt.
Agenten bruker i dag alle sakstyper i arrangørens data. Den gamle N-PX-veien finnes bare som `SPOR=npx` i
[kjor.sh](arbeid/hack/c1/leveranse/kjor.sh), med henterne i `arbeid/hack/c1/hent_*.py` (se [DATA.md](DATA.md)); den brukes ikke i hovedtallet.

## Les mer

- [JURY_README.md](arbeid/hack/levering/JURY_README.md): kjøring ord for ord, kolonnene i `agent.csv`, forventet utskrift.
- [METODE.md](arbeid/hack/levering/METODE.md): data, tidssplitt, modell, kalibrering, ruting og hvordan tallene er målt.
- [ERLIG_EVALUERING.md](arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md): hva som er målt, hva som ikke er det, og byttet av modell.

Data: NBIMs stemmer fra arrangøren av hackathonet. Kilder, kreditering og AI-bruk står i [arbeid/hack/c1/leveranse/README.md](arbeid/hack/c1/leveranse/README.md).

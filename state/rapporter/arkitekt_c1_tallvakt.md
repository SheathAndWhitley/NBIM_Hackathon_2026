# Tallvakt for Case 1: hovedtallet i pakka mot måleren (#2131)

Skript: `arbeid/verktoy/c1_tallvakt.py`. Kjør fra landsbymappen:

    python3 -I arbeid/verktoy/c1_tallvakt.py          # utgang 0 = OK, 1 = avvik, 2 = måleren feilet
    python3 -I arbeid/verktoy/c1_tallvakt.py --vis    # lister også alle påstander som stemmer
    python3 -I arbeid/verktoy/c1_tallvakt.py --rot <kald kopi>   # sjekker en kopi (#1972)

Hva den gjør: kjører `c1/maaler_offisiell_v3.py <svar> test --data real --score mot` på
`levering/kjor_agent_real_maskin_alene.csv`, leser «MOT mot styret»-linja og sjekker påstander i
`levering/*.md` og `c1/leveranse/*.md`: F1 på MOT, P/R (på linjer som ellers handler om hovedtallet),
TP/FP/FN, antall MOT (58) og tabellrader «maskin alene» under presisjon|recall|F1. Tall godtas når de er
måletallet avrundet til samme desimaler. Unntatt: eldre/avvik/val/2025/N-PX/h1/utentype/uten sakstype/
historikkregel/ruting like foran tallet, og linjer med `tallvakt: ignorer`.

## Målt
- Måler: F1 0,4762, P 0,4412, R 0,5172, TP 30 FP 38 FN 28, 58 MOT. Kjøretid 0,07 s.
- Dagens pakke: 12 filer, 55 påstander stemmer, 0 avvik -> OK.
- Negativprøve i kopi (`--rot`), én feil om gangen, alle gir utgang 1 og riktig linje:
  F1 0,496 (levering/README:3), P 0,451 (KRAVRESPONS:10), TP 31 (c1/leveranse/README:8),
  tabell 0,486 (c1/leveranse/kravrespons:15), 59 MOT (METODE:4).

## Begrensning
Vakta sjekker påstander med kjent form. Et feil tall i fri tekst uten «F1»/«P»/«TP» foran
(f.eks. «gir 0,47 på 2026») blir ikke sett. Første versjon flagget KRAVRESPONS:82 (F1 MOT 0,500
uten sakstype); det er et riktig sidetall, så unntaksvinduet ble utvidet til 70 tegn.

## Inn i kald start (#2136)
`sh arbeid/hack/levering/fremmed.sh <mål>` kopierer nå også `levering/*.md`, `c1/leveranse/*.md` og vakta,
og kjører til slutt vakta på **kopiens egen kjøring** (`ut/pred_maaler.csv`, `ut/KJORING.txt`) under `env -i`.
Slutter med `TALLVAKT GRØNN` (utgang 0) eller `TALLVAKT RØD ... Pakka er IKKE verifisert` (utgang 1). #1972 bruker dette.

Nye sjekker: «58 MOT mot styret / i fasit / MOT-stemmer i test / bare N MOT-saker / av N MOT-stemmer» = 58;
«N avvik fra styret / med AVSTÅ / inkl» = 66; «X av Y (p %)» på linjer om menneske, der Y = saker inn (1578)
eller med fasit (1539), mot KJORING.txt (`--kjoring`). Tabeller uten presisjon|F1-kolonner leses celle for celle;
kolonner «maskin + menneske», «gulv», «øvre» hoppes over, og andel til menneske sjekkes bare i standardraden.

## Målt i dag 13:05
- Kald kjøring: F1 MOT 0,4762, TP 30 FP 38 FN 28, 58 MOT, 66 avvik; til menneske **188 av 1578 (11,9 %)**,
  183 av 1539 (11,9 %). Kjøretid 28 s.
- **KP: forventet 228 (14,4 %) som pakka sier, fikk 188 (11,9 %).** Båndet ble byttet i #2128/#2132.
- Vakta på kald kopi: **RØD, 14 avvik** (117 påstander stemmer): 228/223-tallene i BEGRENSNINGER:3,
  c1/leveranse/README:9, EN_SIDE:26, JURY_SPORSMAL:42, KRAVRESPONS:13; «129 MOT» fra N-PX-holdout i
  BEGRENSNINGER:22 og METODE:77/80. README og BESLUTNINGSSTOTTE er alt rettet til 188/183 av smedene.
- Den innsjekkede `levering/kjor_agent_real_test2026.txt` står fortsatt på 228; vakta uten kald kopi er derfor
  rød på de rettede filene. Den fila må regenereres.
- Negativprøve i kald kopi: la inn «F1 0,499 på MOT mot styret, 66 MOT mot styret» i EN_SIDE.md ->
  `EN_SIDE.md:39: F1 0,499` og `EN_SIDE.md:39: antall MOT 66`, utgang 1.
- Grønt i dag er ikke nådd: det krever at tallene rettes. Oppgave #2145 (smed) har lista.

Merk: `arbeid/` er i .gitignore, så endringen i vakta og fremmed.sh ligger bare på disk (ingen commit).

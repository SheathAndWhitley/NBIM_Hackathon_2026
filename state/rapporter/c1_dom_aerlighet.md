# Case 1: dom over ærlighetssetningene i pakken (#2620) — dommer, 05.11 17:18

**Dom: GODKJENT.** Setningene fra #2616 står i `ERLIG_EVALUERING.md` § 7 (siste avsnitt) og som nytt svar 20 i `JURY_SPORSMAL.md`.
Hvert klokkeslett og hvert tall er sjekket mot `c1_klokkesjekk_byttedom.md` (#2617) og `c1_byttedom_265.md` (#2570). Tallvakta: 21 filer, 174 påstander, 0 avvik.

| Påstand i pakken (§ 7 og sp. 20) | Kilde | Dom |
|---|---|---|
| Repo4s 2026-tall 0,512 kjent kl. 16:13 | klokkesjekk rad 1 (fil 16:13:30) | OK |
| Regelen skrevet kl. 16:49 | klokkesjekk rad 2 (16:48:59 / 16:49:22) | OK |
| 2024 og 2025 målt 16:49–16:51, etter regelen | klokkesjekk rad 3 (filer 16:49:38, ki_snitt 16:50:54) | OK |
| +0,051 (2024), +0,017 (2025), snitt +0,034 | byttedom, bootstrap per år | OK (0,034 = snitt av de to) |
| Snitt tre år +0,0345 [−0,005; +0,078], 4 % av trekk under frossen | byttedom | OK, og teksten sier riktig at 4 % gjelder tre-års-snittet |
| KI 2024 [−0,065; +0,160], 2025 [−0,031; +0,068], 2026 +0,036 [−0,008; +0,085] | byttedom | OK |
| 2023 som kontroll: +0,005 | byttedom pkt. 2 | OK |
| Benk A-tall repo4 0,506/0,531/0,512, frossen 0,455/0,514/0,476 | byttedom (0,5057/0,5309/0,5120; 0,4545/0,5143/0,4762) | OK, avrundet |
| Kald kopi TP 32 FP 35 FN 26, F1 0,5120 | byttedom, tallvakt | OK |
| Lekkasje: #2575 seks punkter grønne, base_rate 2019–2023, brute force 400 rader ikke kjørt på nytt for repo4 | byttedom pkt. 5 | OK, forbeholdet står |

## Én merknad i tekstene (liten, bør rettes før tekststopp)
Sp. 20 sier «Sju kandidater ble prøvd, og én besto». Det er byttedommens tall (benk A pluss snitt3). § 7 viser tolv kandidatrader
(seks i benk A, seks i benk B). En jurymedlem som teller, får tolv. Ærlig retning er å oppgi det høyeste: «Tolv kandidater er prøvd
(sju i dommens benk), én besto.» Flere forsøk gir større sjanse for tilfeldig bestått, så underdrivelsen er feil vei.

## Utenfor denne oppgaven, men funnet underveis (hører til byttet #2592 / #2619)
- Sp. 2 blander frossen og repo4: «agenten får 96,0 % og finner 30. Den betaler 35 falske flagg for det, og alle 38 går til et menneske.»
  Med repo4 er det 32 funnet, 35 falske flagg, alle 35 til menneske. Tallvakta fanger det ikke fordi 30 og 38 ikke er hovedtallet.
- Sp. 3 sier «ikke som 0,476» og «mellom 0,36 og 0,59», mens KI-ene ellers i pakken nå er [0,40; 0,62]. Linja er tallvakt-ignorert.
Lagt ut som egen oppgave til smeden som bytter.

## Gjenskap
`uv run python -I arbeid/verktoy/c1_tallvakt.py --rot .`; `awk '/^## 7/,0' arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md`;
`sed -n '86,89p' arbeid/hack/c1/leveranse/JURY_SPORSMAL.md`; sammenlign med `state/rapporter/c1_klokkesjekk_byttedom.md` og `c1_byttedom_265.md`.

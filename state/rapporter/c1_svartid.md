# Case 1: svartid per sak for den frosne agenten (#2259)

Ingen krasj i de rare sakene (#2257, bekreftet i dommerens #2264 fra kald kopi, utgang 0 overalt). Derfor målte jeg svartid.
- Utvalg: 100 tilfeldige saker fra test 2026 (`real_test_input.csv`, frø 0), uten fasit. Agenten er `arbeid/hack/levering/kjor_agent.py` i låst venv.
- Nettet var sperret for hver kjøring (`sandbox-exec ... (deny network*)`). Alle 100 gikk med utgang 0, så agenten kaller ikke nettet.
- **Hver sak som egen prosess (kald start, inkl. modell-lasting):** snitt 5,48 s, median 5,28 s, p95 7,14 s (rang 95 av 100, regnet fra svartid.tsv i #2288), verste 12,15 s (2066391|5), beste 4,22 s.
- Neste tregeste: 9,07 s, 7,85 s, 7,79 s. Det verste tilfellet er trolig en enkeltstående treghet i maskinen, ikke saken selv: den samlede kjøringen under var rask.
- **Alle 100 i én kjøring:** 4,2 s totalt, altså 0,042 s per sak. Nesten hele enkeltsakstida er oppstart og lasting.
- Konklusjon: en forvalter får svar på ca. 5 s for en enkelt sak fra kald start, og en hel generalforsamlingsliste tar sekunder.

Kommando (fra landsbymappen, ca. 10 min): `python3 -I arbeid/oppgave_2259/svartid.py --n 100`
Rådata: `arbeid/oppgave_2259/ut/svartid.tsv`, logg `arbeid/oppgave_2259/kjoring.log`.

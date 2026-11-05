# Case 1: svartid og rare saker lagt inn i pakkas README (#2288)

- Nytt avsnitt «Svartid og rare saker» i `arbeid/hack/levering/README.md`, rett før «Robusthet».
- Svartid per sak (kald start, 100 saker, nett sperret): median 5,28 s, p95 7,14 s (rang 95 av 100 i `arbeid/oppgave_2259/ut/svartid.tsv`), verste 12,15 s. Samlet kjøring 0,042 s per sak. Kommando: `python3 -I arbeid/oppgave_2259/svartid.py --n 100`.
- Rare saker: 20 av 20 uten krasj. Den eneste feilen var kinesisk tekst uten ruting, og den er rettet (bare ruting). Kommando: `python3 -I arbeid/oppgave_2257/rare_saker.py --ut DIR`. Dommerens dom: `c1_rare_saker_dom.md`.
- p95 er ført inn i `state/rapporter/c1_svartid.md` som kilde.
- Modell og prediksjoner er ikke rørt. Tallsjekken finner 0 tall uten kilde. Tallvakta mot den kalde kopien `/tmp/dommer_2264` gir 162 påstander som stemmer og 1 avvik, og avviket er `NESTE_VERSJON.md:52` (gammelt, gjelder #2286 hos arkitekten), ikke README.

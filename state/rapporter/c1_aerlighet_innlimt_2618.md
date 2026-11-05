# Case 1 (#2618): ærlighetssetningene er limt inn i pakken (smed2, 05.11 17:2x)

## Gjort (commit 4787923)
- `leveranse/ERLIG_EVALUERING.md` § 7: arkitektens (a) BYTT-variant og (b) lekkasjesjekk er limt inn ordrett rett etter «Regelen ble skrevet ned før målingen …».
- Statussetningen «Status når dette skrives (kl. 17): ingen kandidat er godkjent … foreløpige og ikke dommergodkjente» er byttet ut med
  «Status: kontrollagenten dømte BYTT til repo4 kl. 17:02 på vilkår om grønn pakke innen 18:45.» Det er samme vilkårsfrase som i README-boksen (#2580).
  Videre står det at frossen og repo4 i benk A er gjenskapt byte-likt, mens de øvrige kandidatene ikke er gjenskapt.
- `leveranse/JURY_SPORSMAL.md`: nytt svar 20 (BYTT-variant), satt inn før «## Hull vi kjenner».
- Klokkeslett etter dommer #2617: 16:13 og 16:49 stemmer. **Ett avvik:** arkitekten skrev at 2024/2025 ble målt 16:49–16:50, dommeren sier **16:49–16:51**. Dommerens tall er brukt begge steder.
- Kildelinjene beholder `utviklingsrapport:`-formen, slik svar 19 også gjør. Det er ikke lagt nye filer i `kilder/` midt i nyfrysen.
- Tallvakt: 21 filer, 174 påstander, 0 avvik.

## Når dommen kommer kl. 18:45 (én kommando, idempotent, testet i kopi og tilbake til byte-likt)
    uv run python -I arbeid/oppgave_2618/lim_inn.py --variant BYTT --sluttfor --malt "16:49–16:51"   # BYTT grønt (kjør sammen med 2580 --sluttfor BYTT)
    uv run python -I arbeid/oppgave_2618/lim_inn.py --variant STAAR --malt "16:49–16:51"             # STÅR, også etter tilbakerulling fra zip (limer inn på slutten av § 7 hvis ankeret mangler)

## Ikke gjort / til andre
- `frys_fasit_1600.sha256` er ikke regenerert, fordi diffen også inneholder andres uferdige endringer (zip-README, JURY.md). Det er smeds nyfrys-steg (#2592).
- Svar 19 sier fortsatt «Den frosne agenten står». Det må følge dommen; det hører til #2619 (arkitekt, motsigelser).

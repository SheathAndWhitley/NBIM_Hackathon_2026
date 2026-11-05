# Case 1: er de fem hullene fra jurylesningen tettet etter #2723? (#2736, speider, 05.11 18:25)

Stier er relative til `arbeid/hack/c1/leveranse/`. Lest mot `c1_jury_sporsmal.md` (#2721). Kort: 1 TETTET, 3 HALVT, 4 ÅPNE (én av dem er valgfri). Alle åpne er ren tekst og tar under 10 min for smed2.

| # | Punkt | Status | Fil:linje |
|---|---|---|---|
| 1 | Repo4 funnet på 2026 | **TETTET** (var aldri hull) | `JURY_SPORSMAL.md:87` (sp. 20), `:91` (sp. 21), `ERLIG_EVALUERING.md:104` |
| 2a | 18:15-runden i pakken | **HALVT** | Står nå i `KANDIDATER.md:18,35` (+0,0135, dom 18:15 STÅR). Men `ERLIG_EVALUERING.md` § 7 (`:78-104`) og sp. 20 (`JURY_SPORSMAL.md:87`) nevner den ikke og viser ikke til `KANDIDATER.md` (0 treff på «KANDIDATER» utenfor fila selv). |
| 2b | Ett totaltall for kandidater | **ÅPEN** | `JURY_SPORSMAL.md:87` «Sju kandidater ble prøvd, og én besto» mot `MUNTLIG.md:9` «Tolv kandidater … Elleve falt» mot `KANDIDATER.md:35` «18 målingene» (etter byttet). Tre tall. |
| 3 | b2-forspranget +0,11 vs +0,15 | **ÅPEN** | `JURY_SPORSMAL.md:48` (sp. 11) og `:73` (sp. 17) sier fortsatt +0,11 [0,01; 0,22] uten «eldre frossen». `JURY.md:25` og `JURY_SPORSMAL.md:15` sier +0,15 [0,04; 0,25] (repo4). +0,23 mot huskeregelen er uavklart (dommer #2732 regner). |
| 4 | 400-rad-lekkasjesjekk på repo4 | **ÅPEN, ærlig oppgitt** (valgfri) | `JURY_SPORSMAL.md:88` sier rett ut at den bare er kjørt på frossen. Arkitekt #2731 kjører den nå; når tallet kommer, én setning inn i `:88` og `:23`/`:77` (som sier «0 avvik» uten forbehold). |
| 5 | Sp. 16 «alle 9 MOT-flagg» | **ÅPEN** | `JURY_SPORSMAL.md:69` siterer fortsatt «alle 9 MOT-flagg agenten tar selv er riktige» uten «eldre frossen». `JURY.md:36` er rettet (11 av 14, repo4; eldre 9 av 9). |
| små | To like KI-er | **ÅPEN** | `JURY_SPORSMAL.md:104` og `:15`: «[0,40; 0,62] … og [0,40; 0,62]». |

## Til smed2 (#2735), i prioritert rekkefølge, før 19:00
1. `JURY_SPORSMAL.md:87` og `MUNTLIG.md:9`: samme tall. Forslag: «Før 18:15 ble N kandidater prøvd og én (repo4) besto; i 18:15-runden ble 18 målinger gjort, beste +0,0135 i snitt, under kravet +0,02, ingen bytte (se KANDIDATER.md).» N tas fra ERLIG § 7-tabellene, ikke gjettes.
2. `ERLIG_EVALUERING.md` § 7 (etter `:104`): én linje om 18:15-runden + henvisning til `KANDIDATER.md`.
3. `JURY_SPORSMAL.md:48` og `:73`: bytt +0,11 [0,01; 0,22] til +0,15 [0,04; 0,25] (repo4), eller merk «eldre frossen». Teksten «så vidt over null» må da endres til «over null». +0,23 venter på #2732.
4. `JURY_SPORSMAL.md:69`: «alle 9 MOT-flagg» → «11 av 14 MOT-flagg (repo4; eldre frossen 9 av 9)».
5. `JURY_SPORSMAL.md:15,104`: tre desimaler eller stryk den doble KI-en.
6. Når #2731 er ferdig: resultatet inn i `JURY_SPORSMAL.md:88`.

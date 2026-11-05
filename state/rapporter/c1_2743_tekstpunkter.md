# Case 1 (#2743): de seks tekstpunktene fra #2736 er lukket

Stier relative til `arbeid/hack/c1/leveranse/`.

| pkt | Status | Hva |
|---|---|---|
| 1 Ett kandidattall | var alt rettet (#2735) | `JURY_SPORSMAL.md:87` og `MUNTLIG.md:9` sier begge sju i første runde, atten i andre, til sammen 25, én bestått |
| 2 ERLIG § 7 om 18:15 | **rettet nå** | Ny linje etter § 7: 18 målinger, beste «av» +0,0135, dom #2713 STÅR, viser til `KANDIDATER.md` |
| 3 +0,11 → +0,15 | var alt rettet (f88c9d9) | sp. 11 og 17 sier +0,15 [+0,04; +0,25] for repo4, eldre frossen nevnt |
| 4 «alle 9 MOT-flagg» | **rettet nå** | sp. 16 sier at linja gjelder eldre frossen; repo4 11 av 14 (`JURY.md:44`) |
| 5 Dobbel KI | **rettet nå** | sp. 3 og «Hull vi kjenner»: klynge [0,400; 0,621], rader [0,397; 0,616] (`kilder/c1_repo4_tall_2592.md:3`) |
| 6 Lekkasje for repo4 | var alt rettet (10f71c7) | sp. 20 og sp. 24 har tallene fra #2731/#2744 |

Ingen modellendring. Skript: `arbeid/oppgave_2743/rett.py` (idempotent). Tallvakt: 32 filer, 196 påstander, 0 avvik.
Ikke gjort: README.md:25 sier fortsatt «bootstrap over rader gir [0,40; 0,62]» (stemmer med to desimaler, men er ikke tydelig). Det kan tas i tekststopp-runden (#2549) om noen vil.

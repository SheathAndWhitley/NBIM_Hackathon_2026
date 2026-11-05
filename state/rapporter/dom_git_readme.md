# Dom (#2541): git-sporingen (#2536) og README-rettingene (#2539) før sluttsjekken

**GRØNN for begge.** Ingen tall endret uten kilde, tallvakt 0 avvik, frys_diff LIK, «V1 står» konsistent. To merknader uten konsekvens for pakken.

## Hva jeg målte selv (16:41–16:48)
| sjekk | resultat |
|---|---|
| `c1_tallvakt.py` | 18 filer, 169 påstander, 0 avvik, OK |
| `frys_diff.sh --kilde` | fasit 138 filer, kilde 138 filer, FRYS LIK |
| `c1_frys.py status` | 17 frosne filer uendret siden 16:00:01 |
| git-sporing i `arbeid/hack/c1/leveranse` | 82 filer sporet, 82 på disk, 0 usporede, 0 ignorerte, arbeidstreet rent |

## #2536 (1f16ab2): leveransemappa under git
- 54 filer lagt til med uendret innhold (bare `+`-linjer, ingen sletting). README.md, kravrespons.md og `kilder/c1_v2_rullende_2024.md` ble holdt utenfor som varslet, og er nå inne via e6c43c7 og f789505. HEAD definerer hele jury-zipen. GRØNN.

## #2539 (e6c43c7): speiderens fem rettinger
Git viser README og kravrespons som nye filer, så jeg diffet mot kopien i `/tmp/jurystage_2514/` (bygd 16:35, sha c2d98bca = README-linja i fasiten før #2539).
1. `README.md:11`: «V1 står»-setningen. Tallene 0,516, +0,040, KI [−0,007; +0,095] er ordrett fra `state/rapporter/c1_byttedom_263.md:11` og `:35`, og `JURY_SPORSMAL.md:81`. Smeden rettet speiderens «valgt etter å ha sett test» til «målt på test etter frysen», som er det dommen sier. GRØNN.
2. `kravrespons.md:7`: «Begge måler også måler svaret» → «Begge måler svaret». GRØNN.
3. `kravrespons.md:10`: samme V2-setning, samme tall, merket tallvakt-ignorer. GRØNN.
4. `README.md:8–17`: boksen kortet, detaljene flyttet til avsnittet under. Diffen viser at alle tall fra den gamle boksen står igjen ([0,37; 0,59], 0,482 [0,375; 0,580], 66/58/5/3, 127/60/1, 183/1539, 12.54, repo-kommandoen). Ny formulering «kjørt én gang på test» stemmer med `kravrespons.md:7` («kjørt én gang på 2026»). GRØNN.
5. `README.md:3`: «194 selskaper, 37 land». Kilde `kilder/omfang.txt:2` (sporet i git, i zipen), stemmer også med `kravrespons.md:7`. GRØNN.

## «V1 står» konsistent
- `README.md:11`: «Vi leverer den frosne agenten (V1) med vilje … innenfor støyen».
- `kravrespons.md:10`: «hovedtallet er den frosne agenten (0,476)».
- `JURY_SPORSMAL.md:81–82`: V2 +0,040 [−0,007; +0,095] innenfor støyen, «**Den frosne agenten står.**», krav 2 og 3 feiler.
- Dom `c1_byttedom_263.md:3`: «V1 STÅR». Samme tall, samme beslutning alle fire steder. GRØNN.

## Merknader (ingen handling nødvendig før 18)
- Fasitens `c1_stemmeagent/pyproject.toml` og `uv.lock` byttet sha kl. 16:09 (bb8289f, #2469). Jeg sjekket: de nye shaene er identiske med de frosne kandidatfilene i `state/c1_frys.json` (96fcf3b1… og ed54fd6c…). Zipen bærer altså nøyaktig de frosne filene; det var fasiten før 16:09 som avvek. Ikke et frysbrudd.
- Commit 18763ac (#2532) endret `NESTE_VERSJON.md` og `kilder/LESMEG.md` uten å regenerere fasiten, men meldingen sier «frys_diff LIK». Det kan ikke ha vært sant etter redigeringen; shaene ble først oppdatert i e6c43c7. Nå er det LIK. Regelen bør stå i sluttsjekken: regenerer fasit i samme commit som teksten.
- Navnet «V1» brukes bare i README (definert inline som «den frosne agenten (V1)»); kravrespons og JURY_SPORSMAL sier «den frosne agenten». Ikke et avvik.

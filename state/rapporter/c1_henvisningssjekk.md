# Case 1: henvisningssjekk av jurypakken (#2564), 4 brudd i jurytekstene, 1 rettet

Grunnlag: `state/levering/c1_gronn/jurypakke_c1_1644_bf0d3f8.zip` (138 filer) pakket ut i tom mappe `/tmp/c1_hs_2564`.
Sjekket: README.md (roten), leveranse/{README,kravrespons,JURY,ERLIG_EVALUERING}.md, levering/JURYSVAR.md.
Metode: skript `arbeid/oppgave_2564/stisjekk.py` løser hver sti mot fila, pakkeroten, `arbeid/` og `arbeid/hack/`;
alle treff er lest i sammenheng. Hver «pkt. N», «sp. N», «§ N» og hver `fil:linje` er slått opp for hånd.

## Kommandoer, kjørt fra kald zip (alle virker)
- `sh KJOR.sh`: FRYSVAKT GRØNN (15 filer), HOVEDTALL 0.476190, TALLVAKT GRØNN (169 påstander, 0 avvik), exit 0.
- `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/c1_sjekk`: TP 30 FP 38 FN 28 TN 1443 STEMMER, sha256 LIK.
- `.venv/bin/python arbeid/hack/levering/kjor_agent.py --help` og `--sak`-eksemplet: P(MOT) 0,52, til menneske, NBIM 5.3.1, akkurat som i README.
- `python3 -I arbeid/hack/c1/menneske_tabell.py ut/agent.csv` virker også på zipens egen ut/ (F1 0,476 / 0,828 / 0,269).
- Kommandoene merket «i repoet, ikke i zipen» (kjor.sh, demo.sh, fremmed.sh, kaldstart.sh, oppgave_2395/reprod.sh, bro_74_71_68.py) er riktig merket.

## Kryssreferanser (alle stemmer)
BEGRENSNINGER pkt. 4, 6, 7 og 8; JURY pkt. 3, 4, 7, 8, 9, 11 og 12; JURY_SPORSMAL sp. 19 og «Hull vi kjenner»; ERLIG § 1 (0,522) og § 6;
METODE pkt. 0; c1_beslutning_nyeste_historikk pkt. 8–10; linjepekerne TREFFSIKKERHET.md:16, c1_bootstrap_f1.md:6 og :16,
c1_val_kaldstart.md:23, c1_tiltak1_malt.md:18-19 og :25, c1_feil_stabilitet.md:23. Alle peker på riktig tall.
(`c1_enkle_regler_og_hist1.md:1` er overskriftslinja med 0,476. Den er svak, men riktig.)

## Brudd
| # | fil:linje | hva mangler | status |
|---|---|---|---|
| 1 | levering/JURYSVAR.md:27 (og levering/METODE.md:33) | `c1_real.py:107` peker på `def finn_sitat`. Utelukkelsen av samme år, senere år og samme møte står på linje 114 | **rettet** til `:114` |
| 2 | leveranse/README.md:25 | `state/opplastet/20261105_114240_npx_votes.csv` står med sha256 i datatabellen, men er ikke i zipen. Juryen kan ikke sjekke summen | til smed: legg til «(ikke med i zipen)» |
| 3 | leveranse/README.md:27 | «De ligger i `arbeid/hack/c1/arkiv/gammel_data/`»: mappa er ikke i zipen | til smed: legg til «(i repoet, ikke i zipen)» |
| 4 | leveranse/README.md:71 | `c1/hent_npx.py` og `c1/baseline.py` (kreditering, SPOR=npx) er ikke i zipen | til smed: legg til «(i repoet, ikke i zipen)» |

Mindre ting, ikke brudd: JURYSVAR.md:3 viser til `tavle.py forsok-list` og `state/rapporter/`, som ikke er med i zipen. Det dekkes av
henvisningen til kilder/LESMEG.md og merknaden i rot-README:64. JURY_SPORSMAL.md:1 sier «de atten», men fila har 19 spørsmål.

## Etter rettingen
- Tallvakt: 169 påstander, 0 avvik.
- frys_diff --kilde: ENDRET JURYSVAR.md og METODE.md (denne rettingen) og demo_utskrift.txt (ikke min, trolig #2551).
  Det er bare tekstfiler. Fasiten må lages på nytt ved tekststopp/pakking (#2549). Ingen frosne modellfiler er rørt (c1_real.py er uendret).
- METODE.md ligger under .gitignore (`arbeid/`) og er bare endret på disk. JURYSVAR.md er committet.

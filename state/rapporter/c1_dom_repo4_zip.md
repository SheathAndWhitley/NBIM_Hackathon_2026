# Case 1: dom på repo4-zipen fra kald start (#2596), 17:40

**Dom: IKKE GRØNN som jurypakke slik den er. Kjøring og tall er GRØNNE; det som feiler er tekst.**
**Tilbakerulling etter #2593 B utløses IKKE:** rullingen gjelder modell og tall, og de holder. Feilen ligger i fire tekster
byttet aldri rørte (#2593 A lister dem som «uendret av byttet»). Rett tekstene, bygg ny zip med `sluttsjekk.sh`, ny dom i #1972.

Zip dømt: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip`, sha256 `fc0dbc55…edc` (stemmer med SHA256.txt), 150 filer.

## 1. Kald kjøring (tom mappe `/tmp/c1_dom_2596/zt`, `env -i`, tom HOME, sandkasse som nekter landsbymappa)
| krav | resultat |
|---|---|
| F1 MOT 0,5120 (2026) | `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000` |
| 2x2 uten måler | `forventet TP 32 FP 35 FN 26 TN 1446: STEMMER`; ny prediksjonsfil = frossen d02cf884: LIK |
| frysvakt i zipen | GRØNN, 19 filer |
| tallvakt | `TALLVAKT GRØNN`, 0 avvik |
| ZIPTEST | GRØNN, loggen nevner ikke landsby |
Modellen som kjører er repo4: `c1_real.py:36 TRAIN = modell_repo4.py`, og `modell_repo4.py` + `stemmeagent/` står i FROSNE_SHA256.txt. Logg: `/tmp/c1_dom_2596/ziptest.out`, `/tmp/c1_dom_2596/zt.logg`.

## 2. «Ingen 0,476 igjen som hovedtall»: FEILER
Tallvakta leser bare `levering/*.md` og `c1/leveranse/*.md` (`c1_tallvakt.py:26`). Under `arbeid/hack/c1/` står den gamle modellen fortsatt som hovedtall, og juryen kommer dit via lenker fra JURY_SPORSMAL (begge) og `leveranse/README.md:16`:
| fil:linje | hva som står |
|---|---|
| `c1/JURY_METODE.md:19` | «Samme modell, F1 på MOT mot styret (hovedtall) **0,476**», KI [0,36; 0,59]; linje 28 «vi ligger under det på test (0,476 på MOT)» |
| `c1/DEMO_MANUS.md:3,15,56,63` | «Agent: frossen sak 2044 miks h2», «Agenten: F1 0,476. Den finner 30 av 58», kald kopi 0,4762 TP 30 FP 38 FN 28 |
| `c1/DEMO_MANUS_5min_tilfeldige.md:24,25,91` | «Hovedtallet er F1 0,476 på MOT», KI 0,36–0,59 |
| `c1/SVAKHETER.md:1-4,75` | «modellen og hovedtallet er de samme etter modellfrysen», F1 0,476, engelsk del «0.476 on test 2026» |
| `c1/tall_tabell.md` | ingen repo4-rad; modellraden er 0,476 [0,37; 0,59]. `leveranse/README.md:16` siterer tabellen for «[0,40; 0,62]», som ikke står der |
| `leveranse/kjor.sh:10` | kommentar «Forventet SCORE 0.481752, MOT F1 0.4762» |
| `levering/JURY_SPORSMAL.md:117` | H-H «0,476 mot 0,520» uten merknad om at det gjelder eldre modell |
| rot-`README.md` «Hva som er hva» | `arbeid/oppgave_2044/train.py` kalles «den frosne modellen (miks h2), trenes fra rådata ved hver kjøring». Modellen er `modell_repo4.py`; train.py er bare grunnlaget. Samme i `JURY_README.md` |
| `kjor_agent.py:5` (frossen) | docstring «MOT-modell #2044 (train.py, miks h2)». Fila er frosset, lar stå, men README bør si det |

## 3. «Ingen ~»: 11 treff i 9 filer, ingen på kjørestien
`README.md:73` og `JURY_README.md:73` sier åpent at rapporter under `kilder/` nevner utviklingsmaskinen. Utenfor `kilder/` står den likevel i
`c1/menneske_tabell.py:7-8` (hardkodet FASIT-sti), `levering/TREFFSIKKERHET.md:91` (cd-linje) og `c1_tallvakt.py:22` (standardverdi, overstyrt av `--rot`).
Gult, ikke rødt: KJOR.sh leser ingen av dem. Bør rettes om tid: README-setningen dekker bare `kilder/`.

## 4. Krav til ny grønn zip
1. Rett linjene i §2 (eller merk filene øverst med «eldre modell #2044, hovedtallet er nå 0,512 i leveranse/README.md»), og rett rot-README-tabellen.
2. Legg `arbeid/hack/c1/*.md` inn i `c1_tallvakt.py` FILER, så vakta ser dem. Som den står nå er «0 avvik» ikke dekkende.
3. `bash arbeid/hack/levering/sluttsjekk.sh`, så ny dom (#1972, 19:30).
Oppgave til smeden er lagt på tavla.

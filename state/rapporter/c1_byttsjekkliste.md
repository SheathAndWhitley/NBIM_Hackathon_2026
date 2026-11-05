# Case 1 byttsjekkliste (#2593): hva byttet til repo4 endrer i jury-zipen, og hva som må tilbake ved STÅR — dommer, 05.11 17:25

**Status da jeg sjekket:** byttet var alt utført i landsbyen kl. 17:03 (smed #2592, `bytt.sh --utfor`).
Sikkerhetspunktene fra steg 0 finnes: HEAD 3f17072 og `/tmp/bytte2572_c1_frys.json` (frys 16:00:01, 17 filer).
Siste grønne frossen-zip er `/tmp/jurypakke_c1_2587.zip` (17:01, ziptest grønn 0,476190, dom 962847f); jeg har
sikret kopi i `state/levering/c1_gronn/jurypakke_c1_1701_frossen_2587.zip` og `c1_frys_1600_frossen.json` (byte-like).
Alle 15 frosne filer i zipens FROSNE_SHA256.txt er like frys-fila fra 16:00 (målerne sjekkes av frysvakta, ikke lista).

## A. Filer i jury-zipen som byttet endrer (29 avvik: `frys_diff.sh /tmp/jurypakke_c1_2587.zip arbeid/hack/levering/frys_fasit_1600.sha256`)
| gruppe | filer (under c1_stemmeagent/) |
|---|---|
| nye (4) | arbeid/hack/levering/modell_repo4.py, arbeid/hack/levering/stemmeagent/{__init__,ballot,config}.py |
| modell og kjøring (5) | arbeid/hack/levering/c1_real.py (TRAIN -> modell_repo4.py), kjor_agent_real_maskin_alene.csv, kjor_agent_real_pred_maaler.csv, kjor_agent_real_test2026.txt, kjor_agent_real_test2026_LES.md |
| tekster leveranse/ (8) | BEGRENSNINGER.md, ERLIG_EVALUERING.md, JURY.md, JURY_SPORSMAL.md, NESTE_VERSJON.md, README.md, SLIDE.md, kravrespons.md |
| tekster levering/ (8) | BESLUTNINGSSTOTTE.md, JURYSVAR.md, JURY_README.md (= README.md i zip-rota), JURY_SPORSMAL.md, METODE.md, README.md, SLIDE.md, TREFFSIKKERHET.md |
| regnet av pakk_jury (1) | FROSNE_SHA256.txt (nå 19 linjer) |

Uendret av byttet: train.py, pred_miks_h2.csv, full_test.csv, målerne v2/v3, data_off, real_votes.csv, punkter.jsonl,
hele kilder/ og spor_npx/, DEMO_MANUS, JURY_METODE, SVAKHETER, tall_tabell, vern.py, case1_mot.py, KJOR.sh, pyproject/uv.lock.

Utenfor zipen, også byttet: `arbeid/verktoy/c1_frys.py` FILER (+4 linjer merket «#2572 bytte til repo4»), `fremmed.sh` (+1 kopier-linje),
`state/c1_frys.json` (21 filer, 17:03:48; feltet `modell` sier fortsatt «#2044 miks h2», kosmetisk feil i c1_frys.py, bør rettes før 19:30),
`frys_fasit_1600.sha256` (143 linjer), og de interne EN_SIDE.md/KRAVRESPONS.md (bytt_tall rørte dem; de er aldri i zipen, #2587).

## B. Tilbake ved STÅR (rødt kl. 18:45)
**Byttplanens «Tilbake» (git checkout) virker ikke.** 46 av zipens filer er usporet i git, blant dem alt byttet rører i
modellen: c1_real.py, de tre kjor_agent_real-filene, METODE/TREFFSIKKERHET/SLIDE/BESLUTNINGSSTOTTE.md, fremmed.sh og c1_frys.py.
Tørrkjørt i kald kopi: første kommando stopper på `pathspec 'arbeid/verktoy/c1_frys.py' did not match`, c1_real.py peker
fortsatt på modell_repo4.py, og frysvakta sier STOPP (kjor_agent_real_maskin_alene.csv ENDRET). Steg 0 sin
`git diff --quiet` på de fire filene gir grønt fordi git ikke kjenner dem, ikke fordi de er rene.

**Det som virker:** rull tilbake fra den grønne zipen med `arbeid/hack/c1/bytte/tilbake_fra_zip.sh` (ny, #2593):
```
sh arbeid/hack/c1/bytte/tilbake_fra_zip.sh <repo> \
   state/levering/c1_gronn/jurypakke_c1_1701_frossen_2587.zip state/levering/c1_gronn/c1_frys_1600_frossen.json
```
Den legger alle zipens filer tilbake på sine stier (README.md -> JURY_README.md, KJOR.sh -> jury_kjor.sh, målerne hoppes over
fordi zipen har sed-rettede stier), sletter modell_repo4.py og stemmeagent/, fjerner bytte-linjene i c1_frys.py og fremmed.sh,
legger tilbake frys-fila fra 16:00, regner ny fasit og kjører frysvakt + frys_diff. Deretter for hånd: `arbeid/oppgave_2580/sett_inn.py --sluttfor` (STÅR),
`sluttsjekk.sh`/`pakk_jury.sh` + `test_jury_zip.sh`, og commit. Merk: zipen er fra 17:01, så #2580s byttedom-setninger
(README-boksen og kravrespons) må settes inn på nytt; det gjør sett_inn.py.

## C. Tørrkjøring av tilbakerullingen: **OK**
Kald kopi `/tmp/byttsjekk_2593` (rsync av levering/, c1/ uten arkiv, verktøyfilene, oppgave_2044/46/47/2103/2274/2490, kandidatmiljøet,
state/c1_frys.json og real_votes; git i kopien sporer nøyaktig de filene landsbyen sporer). Kopien ble tatt 17:08, altså ETTER byttet, så den
var i bytte-tilstand (c1_real.py -> modell_repo4, frys 21 filer, tekster 0,512). Kjørt to ganger (andre gang med modellfilene lagt tilbake først):
```
sh arbeid/hack/c1/bytte/tilbake_fra_zip.sh /tmp/byttsjekk_2593 /tmp/jurypakke_c1_2587.zip /tmp/bytte2572_c1_frys.json
  -> 21 filer tilbake, 2 slettet, state/c1_frys.json 16:00:01 (17 filer), ny fasit 139 filer
  -> FRYSVAKT GRØNN: 17 filer like som ved frys 2026-11-05T16:00:01
  -> frys_diff zip mot ny fasit: 2 avvik, begge BORTE EN_SIDE.md/KRAVRESPONS.md
```
De to avvikene er ikke fra byttet: pakk_jury.sh utelater de to interne utkastene (#2587), mens frys_fasit.py fortsatt teller
`levering/*.md`; samme 2 BORTE sto mot fasiten før byttet også. Alle filer juryen får, er like den grønne zipen. Etter tilbakerulling
peker c1_real.py på oppgave_2044/train.py, KJORING-fila er den frosne fra 13:07, hovedtallet i README er 0,476.
Om frys_fasit.py skal utelate de to filene slik pakk_jury.sh gjør, er en linje i `fillista()`; jeg rørte den ikke (frosset verktøy i pågående bytte).

Årsak til at så mange pakkefiler er usporet: `.gitignore` utelater `arbeid/` og `state/`; bare filer noen har lagt til med `git add -f`
er i git. Derfor kan `git checkout` aldri være tilbakerullingen for pakka; den grønne zipen er det.

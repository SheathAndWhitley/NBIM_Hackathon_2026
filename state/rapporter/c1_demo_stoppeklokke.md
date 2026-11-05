# Case 1: demoen kjørt ende til ende med stoppeklokke (#2184, smed, 05.11 kl. 13.13–13.20)

Manus: `arbeid/hack/c1/DEMO_MANUS.md` (#2070/#2177). Kjørt fra landsbymappen med ny tom utmappe, før frys.
Frossen kode ikke endret. kjor_agent.py sha256 638d5fea…8b17.

## Tider
| Steg i manus | Kommando | Tid | Utfall |
|---|---|---|---|
| 0:00–0:40 problem og måltall | (bare prat) | 40 s | – |
| 0:40–3:40 sak 1–6 | `bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2026` | **15,4 s** totalt | exit 0, samme seed 17 og samme 6 saker som manus |
| ↳ agent på hele test 2026 | (inni skriptet) | 5,6 s | 183 rutet (11,9 %) |
| ↳ trekk seed 17 + sitatsak | | 0,1 s | |
| ↳ agent på 5 saker | | 4,9 s | |
| ↳ agent på sitatsaken | | 4,5 s | |
| 3:40–4:30 sak 7 (styret mangler) | `bash arbeid/hack/c1/demo_mangler_styret.sh` | **10,7 s** | exit 0, utskrift ordrett lik manus |
| 4:30–5:00 tallene | (bare prat) | 30 s | – |

**Total maskintid: ca. 26 s. Hele demoen holder 5:00** hvis skriptene kjøres mens det snakkes.
Med `UV_OFFLINE=1` (uten nett) går det også (11,3 s). Ingen steg er tregt i seg selv.

## Steg som kan feile, og reservevei
Ferdige utskrifter fra denne kjøringen ligger i `arbeid/oppgave_2184/reserve/`.

1. **Tallet på skjermen er ikke tallet i manus.** demo_saker_2026.sh skriver til slutt `SCORE 0.4818`
   (måler v2 på *avvik*, 66 i fasit, TP 33 FP 38 FN 33). Manus sier F1 0,476 på *MOT*, 58 i fasit (30/38/28).
   Juryen ser 0,48 mens det sies 0,476. **Forslag til #1975:** si én setning om forskjellen (66 avvik med
   aksjonærforslag, 58 ekte MOT), eller la være å vise SCORE-linja. Ikke en feil i modellen, men lett å
   oppfatte som pynt.
2. **Skjermen viser ikke rå score.** Linja `score` er kalibrert P(MOT) (0,1912, 0,0075 …). Rå score (0,912,
   0,262, 0,636, 0,451, 0,257, 0,970) finnes bare i `agent.csv` (`raa_score`). Verdiene stemmer med manus.
   Reserve: si «score på skjermen er kalibrert P(MOT)», eller vis `demo5/agent.csv` fra reservemappa.
3. **Feil arbeidsmappe:** begge skriptene må kjøres fra `<repo>`. Fra `/tmp` feiler de med
   exit 2. Reserve: `cd <repo>` først; ellers vis `reserve/demo_saker_2026_utskrift.txt`.
4. **15 s stille på scenen** når demo_saker kjøres live. Reserve: start skriptet ved 0:00 mens problemet
   forklares, så er utskriften klar ved 0:40. Faller det ut: vis `reserve/demo_saker_2026_utskrift.txt`.
5. **Frysen kl. 16 kan endre ruting, og dermed seed og saker** (manus' sjekkliste punkt 2). Reserveutskriftene
   her er fra *før* frys og gjelder bare hvis frosset sha er den samme. Etter frys: kjør skriptene en gang til
   og legg nye utskrifter i reservemappa (#1975).
6. **Den gamle demoseksjonen i JURY.md er ikke det samme manuset.** `arbeid/hack/c1/leveranse/JURY.md:57–85`
   peker til streamlit-appen (`arbeid/hack/levering/demo/app.py`) og Vanguard-saker (Garmin, Dell, T-Mobile)
   med gamle N-PX-tall. Den ble ikke kjørt her. Kjører noen den i stedet for DEMO_MANUS.md, blir tallene feil.
   **Forslag til #1975:** erstatt seksjonen med en lenke til DEMO_MANUS.md.

## Gjenskap stoppeklokka
    cd <repo>
    PS4='+ $(python3 -c "import time;print(time.time())") ' /usr/bin/time -p bash -x arbeid/hack/c1/demo_saker_2026.sh /tmp/x
    /usr/bin/time -p bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/y

## Kjørt to ganger: likt resultat
Andre kalde kjøring (16,9 s) gir byte-lik utskrift, og `agent.csv` for hele test 2026 er lik på
anbefaling, P(MOT) og ruting. Demoen er deterministisk, så reserveutskriftene er gyldige så lenge sha ikke endres.

## To demoveier finnes, velg én før 19:30
- `DEMO_MANUS.md` + `demo_saker_2026.sh` / `demo_mangler_styret.sh`: målt over, ca. 26 s.
- `arbeid/hack/c1/leveranse/demo.sh` (smed #2093): fremmed.sh lager en kald kopi og kjører agenten på hele test 2026,
  så viser demo_vis.py 3 saker (seed 0). Bare `fremmed.sh` er tidsmålt her: **32,5 s**, exit 0, frysvakt og
  tallvakt grønne (139 påstander, 0 avvik). demo.sh i seg selv ble **ikke** kjørt, fordi den skriver over
  `leveranse/demo_utskrift.txt` i pakka. Den fila er også ferdig reserveutskrift for den veien.
  Den stopper med exit 4 hvis frysvakta er rød. Det er riktig etter kl. 16, men da må den vises fra reserve.
- Merk: punkt 6 over (JURY.md:57–85 er en gammel demo) er allerede meldt i jurylesingen (#2149, punkt 5).
  Punkt 1 (0,4818 mot 0,476) er forklart i `c1_66_58_sjekk.md`, men står ikke i manus.

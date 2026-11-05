# Case 1: reserveplan for demoen hvis noe feiler live (#2191)

Ferdige utskrifter fra en ekte kjøring ligger i `arbeid/hack/levering/demo/reserve/`. De vises uten nett,
uten Python og uten at agenten kjører (bare `cat`, 0,02 s):

    sh arbeid/hack/levering/demo/reserve/vis_reserve.sh 1   # sak 1–6 (DEMO_MANUS.md, seed 17 + sitatsak)
    sh arbeid/hack/levering/demo/reserve/vis_reserve.sh 2   # sak 7: styrets anbefaling mangler
    sh arbeid/hack/levering/demo/reserve/vis_reserve.sh 3   # kald kopi (fremmed.sh): hovedtall F1 MOT 0,476 + tallvakt grønn
    sh arbeid/hack/levering/demo/reserve/vis_reserve.sh 4   # demo.sh-veien: 3 saker med NBIM-sitat (seed 0)
    sh arbeid/hack/levering/demo/reserve/vis_reserve.sh     # alt

Hver utskrift har en linje `RESERVE: ... (ferdig kjøring, laget <tid>)` øverst. Si det høyt: «dette er en
lagret kjøring fra i dag kl. HH.MM, samme modell», ikke vis det som live.
Rådata (agentens svar) ligger i `reserve/csv/`, f.eks. `demo5_agent.csv` med `raa_score`.

## Hva feiler, og hva gjør vi
| Feil live | Tegn | Gjør dette |
|---|---|---|
| Ingen nett / uv vil laste ned | uv-feil, henger | `UV_OFFLINE=1` foran kommandoen (målt OK i #2184); ellers `vis_reserve.sh 1` |
| Live-skriptet stopper uten tekst (exit 127, tom skjerm) | feilen står bare i `<UTMAPPE>/full.log`: `uv: command not found` (prøvd #2200) | `export PATH=/opt/homebrew/bin:$PATH` og kjør igjen (15 s); ellers `vis_reserve.sh 1` |
| Feil arbeidsmappe | exit 2 fra demo_saker | `cd <repo>`; ellers reserve |
| Agenten krasjer / tar for lang tid | traceback, > 30 s | Ctrl-C, `vis_reserve.sh <steg>` |
| Frysvakta er rød (exit 4) | `FRYSVAKT RØD` | Ikke fiks på scenen. Vis `vis_reserve.sh 3`, si at frysvakta stoppet en endret modell |
| Tallet på skjermen (SCORE 0,4818) ≠ manus (0,476) | – | 0,4818 er avvik inkl. aksjonærforslag (66), 0,476 er MOT (58). Vis `vis_reserve.sh 3`, linja HOVEDTALL |
| Maskinen/skjermen dør | – | Utskriftene er tekst: åpne `reserve/*.txt` fra hvilken som helst maskin eller fra pakka |

## Tregeste steg og forebygging
- Live: `demo_saker_2026.sh` ca. 15 s, `demo_mangler_styret.sh` ca. 11 s, demo.sh-veien (fremmed.sh) ca. 40 s.
  **Fiks:** start skriptet ved 0:00 i bakgrunnen mens problemet forklares
  (`bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2026 > /tmp/demo1.txt 2>&1 &`), og vis `cat /tmp/demo1.txt` ved 0:40.
  Ingen kodeendring: fremmed.sh og agenten er frossen kode og rørt ikke.

## Etter frys kl. 16 (viktig)
Utskriftene gjelder modellen med sha i `reserve/SHA.txt` (kjor_agent.py 638d5fea…8b17, laget 13.18 før frys).
Etter frys: kjør `sh arbeid/hack/levering/demo/reserve/lag_reserve.sh` én gang (ca. 1 min) og sjekk at SHA.txt viser
frysvakt grønn. Er sha uendret, er utskriftene like (demoen er deterministisk, #2184).

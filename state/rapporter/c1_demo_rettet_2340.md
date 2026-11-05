# Case 1: demoskriptene rettet der stoppeklokketesten avvek (#2340, smed3, 05.11 kl. 14.45–14.55)

Rettet bare demoskript. Ingen fil i `c1_frys.py FILER`, ingen måler og ingen manus-tekst er endret. Originalene ligger i `arbeid/oppgave_2340/for_retting/`.
Kjørt fra `<repo>` med `PATH=/opt/homebrew/bin:$PATH` og `UV_OFFLINE=1`, før frys.

## Rettinger
1. **`arbeid/hack/c1/demo_saker_2026.sh`** (avvik trinn 1 i #2329: skjermen viste de seks gamle 5-min-sakene, manuset leser Mobimo, LOTTE, Kura Sushi).
   Skriptet viser nå FØRST de tre manussakene fra den fulle kjøringa, så seed-17-sakene som tillegg. `demo5/` og `sitat/` lages som før, så `lag_reserve.sh` virker uendret.
2. **Ny `arbeid/hack/c1/vis_manussaker.py`** (flyttet inn i c1 fra `arbeid/oppgave_2329/`, som beholdes). Regner ut sakene hver gang med velg.py-regelen (første i fila av hver type), slår dem ikke opp.
   Skriver `MANUS OK: samme tre saker som DEMO_MANUS.md (linje 276 / 89 / 15)`, eller `AVVIK FRA MANUS` med id og linje hvis frys endrer sakene. Da skal manuset byttes, ikke sakene.
3. **`arbeid/hack/c1/leveranse/demo.sh`** (avvik trinn 4: kjørte fremmed.sh en gang til, 87 s kald kjøring i en 3-min-demo).
   Standardmappe er nå `/tmp/c1_kald` (samme som manusets fremmed.sh). Finnes kopien (`ut/pred_maaler.csv`, `ut/agent.csv`, `.venv`), gjenbrukes den og hovedtallet regnes på nytt i kopien med samme målerkall som fremmed.sh (0,2 s totalt). `--ny` som andre argument tvinger ny kopi.
   Gjenbruket avhenger ikke av hvor fremmed.sh-utskriften ble sendt (første versjon gjorde det, og slo feil i testen). Headeren viser TALLVAKT/FRYSVAKT når `MÅL.log` finnes, ellers «se utskriften fra fremmed.sh».
   demo.sh viser nå manussakene først, så demo_vis.py sine tre seed-0-saker som før (app.py og demo/README.md viser til dem).
4. `arbeid/hack/c1/leveranse/demo_utskrift.txt` skrevet på nytt fra hel kald kjøring (`--ny`), MANUS OK, HOVEDTALL 0,476190.

## Stoppeklokke etter retting (alle exit 0)
| Trinn | Kommando | Tid | Resultat |
|---|---|---|---|
| 3 Kald kopi | `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald` | 29,8 s | HOVEDTALL 0,476190, TALLVAKT GRØNN, FRYSVAKT «ikke frosset ennå» (normalt før 16) |
| 4 demo.sh, gjenbruk | `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald` | 0,2 s | HOVEDTALL 0,476190 regnet i kopien, MANUS OK, 3 manussaker + 3 seed-0-saker |
| 1 Live-skjerm | `bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2026` | 15,9 s | Mobimo / LOTTE / Kura Sushi først, MANUS OK, så de 6 gamle sakene |
| 2 Sak 7 | `bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/c1_demo_m` | 11,1 s | uendret, ok |
| 4b demo.sh, tvunget ny kopi | `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_demo_kald --ny` | 31,6 s og 48,6 s (to kjøringer) | ny kald kopi, MANUS OK, skrev demo_utskrift.txt |

Anbefalt live-rekkefølge: start fremmed.sh i bakgrunnen ved 0:00 (30–42 s); ved 0:35 `demo.sh /tmp/c1_kald` gir manussakene på 0,2 s. demo_saker_2026.sh trengs da ikke live.

## Avvik i manus-tekst og plan B, til speider #1975 (oppdateres etter frys)
- `DEMO_MANUS.md` linje «Skjerm for de tre sakene»: bytt `python3 -I arbeid/oppgave_2329/vis_manussaker.py /tmp/c1_kald/ut/agent.csv` til `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_kald` (0,2 s når fremmed.sh er ferdig; viser også hovedtall og tallvakt). Gammel kommando virker fortsatt.
- `DEMO_MANUS.md` «Etter modellfrys»: sha `f0444a47…` gjelder #2260-kjøringa; kald kopi gir `1543706f…` (3 rader HP/Hartford/Snowflake, se #2329). Skriv ny sha etter frys. Skjermen sier nå selv MANUS OK / AVVIK, så linje 15/89/276 trenger ikke sjekkes for hånd.
- `state/rapporter/c1_demo_planB.md` tabellrad 1 «Sak 1–6 (manus, seed 17 + sitatsak)» og `RESERVE.md` linje «vis_reserve.sh 1 # sak 1–6 (DEMO_MANUS.md, seed 17 + sitatsak)»: manuset har 3 saker nå. Reserve 1 inneholder etter `lag_reserve.sh` manussakene øverst og seed-17-sakene under.
- Plan B punkt 6 (diff av `^==`-linjer mot `reserve/1_saker_2026.txt`) er RØD til `lag_reserve.sh` er kjørt etter frys: live gir 3 nye `==`-linjer øverst. Forventet, ikke feil.
- Plan B tabellrad 4 og RESERVE.md «demo.sh-veien (fremmed.sh) ca. 40 s»: nå 0,2 s ved gjenbruk av `/tmp/c1_kald`; «Tregeste steg»-rådet bør starte `fremmed.sh /tmp/c1_kald` i bakgrunnen, ikke demo_saker_2026.sh.
- `RESERVE.md` tabell «Agenten krasjer / > 30 s»: fremmed.sh tar 30–42 s normalt, grensa bør være 60 s for det trinnet.
- `demo/README.md` og `app.py` sier «de tre sakene demo.sh trekker med seed 0»: demo.sh viser nå seks (3 manus + 3 seed 0); seed-0-sakene er uendret.

## Ikke gjort
- `lag_reserve.sh` ikke testet: krever frysvakt grønn (etter 16). Skriptet bruker fortsatt `demo5/agent.csv` og `sitat/agent.csv`, som demo_saker_2026.sh lager som før.
- Sak 2 og 3 i demo_vis.py (Colruyt 16 og 18, nesten like) er latt stå: å bytte seed for penere saker er håndplukking.

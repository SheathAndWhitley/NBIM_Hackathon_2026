# Case 1: prøvekjøring av demoen med stoppeklokke (#2329, smed3, 05.11 kl. 14.40–14.58)

Kjørt fra `<repo>` med `PATH=/opt/homebrew/bin:$PATH` og `UV_OFFLINE=1`, før frys (kl. 16). Ingen frosne filer rørt.
Manus: `arbeid/hack/c1/DEMO_MANUS.md` (3-sakersversjonen, 14.10) og plan B i `state/rapporter/c1_demo_planB.md`.

| Trinn | Kommando | Tid | ok/avvik | Hva som må rettes |
|---|---|---|---|---|
| 0 Måltallet (tale) | – | ca. 0:35 | ok | Tallene 0,476 / 30 av 58 / 44 % / 11,9 % stemmer med `maaling.txt` og med kald kopi (TP 30 FP 38 FN 28). |
| 1 Sak 1–6, seed 17 | `demo_saker_2026.sh /tmp/c1_demo2026` | 14,9 s, exit 0 | **avvik** | Skjermen viser Hainan Jinpan, Arbonia, Vietnam Eximbank, Nomad, Klarna, TV TOKYO (det gamle 5-min-manuset). Manuset leser Mobimo, LOTTE, Kura Sushi. Sak-id-ene er like reserven (`1_saker_2026.txt`). |
| 1b Skjerm for manussakene | `python3 -I arbeid/oppgave_2329/vis_manussaker.py /tmp/c1_kald/ut/agent.csv` | 0,02 s | ok (nytt) | **Ingen live-skjerm viste de tre manussakene.** Laget visning som leser agent.csv fra kald kopi. Nå lagt inn i manuset. |
| 2 Sak 7, styret mangler | `demo_mangler_styret.sh /tmp/c1_demo_m` | 9,8 s, exit 0 | ok | Arbonia med og uten styrets anbefaling, til menneske 0 → 1 med grunn. Ikke nevnt i 3-min-manuset; bare hvis juryen spør. |
| 3 Kald kopi + hovedtall | `fremmed.sh /tmp/c1_kald` | 42,2 s, exit 0 | ok | HOVEDTALL 0,476190, TALLVAKT GRØNN, 183 av 1539 (11,9 %). Må startes i bakgrunnen ved 0:00 (står i RESERVE.md). FRYSVAKT er rød nå fordi frys ikke er satt ennå; normal før 16. |
| 4 demo.sh (3 saker, seed 0) | `c1/leveranse/demo.sh /tmp/c1_demo_kald` | 44,5 s, exit 0 | ok, men dobbelt | Kjører fremmed.sh en gang til (42 s). Viser Rukun Raharja (MOT, sitat 3.1.1), Colruyt 16 og Colruyt 18 (begge til menneske, P 52 %). Sak 2 og 3 er nesten like, og ingen er manussakene. Velg enten trinn 3 eller 4 live, ikke begge: 87 s kald kjøring i en 3-min-demo. |
| 5 Avslutning | – | 0:15 | ok | «Én kommando fra kald start gir de samme radene»: linje 15/89/276 i kald kopi er identiske med manus-kilden (diff tom). |

Samlet lesetid: 404 ord i «anførselstegn» (manuset sa 359), ca. 2:45 i 145 ord/min, pluss skjermbytter. Holder under 3 min bare hvis fremmed.sh går i bakgrunnen.

## Sjekklista fra plan B (de punktene som kan kjøres nå)
| Punkt | Resultat |
|---|---|
| 1 Frysvakt | RØD (ikke frosset ennå). Forventet før kl. 16. |
| 2 Levert tall | `tavle.py levert`: forsøk 1046, v3 MOT, 0,476190. Stemmer med HOVEDTALL i kald kopi. |
| 3 Reserven fra etter frys | NEI, SHA.txt 13.18, kjor_agent.py-sha 638d5fea ≠ dagens dedc9406. `lag_reserve.sh` må kjøres etter 16 (eier #1975). |
| 4 Reserve = levert tall | ok: HOVEDTALL 0.476190 og TALLVAKT GRØNN i `3_fremmed_kald_kopi.txt`. |
| 5 Reserve uten miljø | ok: exit 0, 4 RESERVE-linjer. |
| 6 Live offline | ok: exit 0, 14,9 s, sak-id-er like reserven. |
| 7 Samme tall i manus og JURY.md | ok: 0,476 som testtall overalt; 0,520 merket val; 0,504 i JURY.md linje 27 er et forkastet tiltak og er merket slik. |
| 8 Kopi av reserven | ikke prøvd (ren `cp`). |

## Avvik i tall, til speider (#1975)
- **Kald kopi gir annen sha på agent.csv** enn manus-kilden `arbeid/oppgave_2260/full/agent.csv` (f0444a47 → 1543706f). 3 av 1578 rader avviker, alle i kolonnen `mot_styret` (1 → 0): HP Inc. 2045311|16, Hartford 2066391|14, Snowflake 2086078|6. Alle er aksjonærforslag der styret sier MOT og agenten sier FOR. kjor_agent.py ble endret 13.28, etter #2260-kjøringa. Manussakene (linje 15/89/276), F1 0,4762 og rutingstellingen (`telling.py`: FN maskin 17 / menneske 11, FP maskin 0 / menneske 38) er uendret på den nye fila. Manuset er rettet til å si dette. Etter frys: kjør `velg.py`/`telling.py` på nytt som manuset sier, og oppdater sha i manus og i `arbeid/hack/CASE/demo_saker.md`.
- Ordtellingen i manuset var feil (359 → 404). Rettet.

## Endret
- `arbeid/hack/c1/DEMO_MANUS.md`: skjermkommando for de tre sakene, sha-merknad, ordtall/tid. Ingen talltekst endret.
- Ny: `arbeid/oppgave_2329/vis_manussaker.py` (leser bare agent.csv, 0,02 s).
- `arbeid/hack/c1/leveranse/demo_utskrift.txt` ble skrevet på nytt av demo.sh (samme tall, nytt klokkeslett 14.43).

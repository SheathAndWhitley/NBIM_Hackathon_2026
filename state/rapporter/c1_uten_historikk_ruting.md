# Case 1: sendes selskaper uten stemmehistorikk oftere til menneske? (#2305, smed3)

**Svar: ja, alle.** Agenten har en egen regel («ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen») som
ruter 100 % av sakene i selskaper uten historikk. Modellen i seg selv er ikke mer usikker på dem: båndet alene
(kalibrert P(MOT) i [0,15; 0,85)) ville rutet 8,2 % av dem mot 7,5 % av selskaper med historikk. Det er regelen som gjør
jobben, ikke konfidensen. Frossen pakke #2044 er ikke rørt.

## Tall på val 2025 (1909 saker med fasit, modell trent på år < 2025)

| gruppe | n saker | MOT mot styret i fasit | til menneske (bånd / ukjent selskap) | andel | F1 maskin alene (TP/FP/FN) | F1 maskin på sakene den beholder (n) | MOT i fasit blant rutede |
|---|---|---|---|---|---|---|---|
| uten historikk (0 tidl. stemmer) | 98 | 3 | 98 (8 / 98) | 100,0 % | 0,571 (2/2/1) | – (0 saker beholdt) | 3 av 3 |
| med historikk (1+) | 1811 | 96 | 136 (136 / 0) | 7,5 % | 0,518 (43/27/53) | 0,259 (1675, 7/0/40) | 49 av 96 |
| alle | 1909 | 99 | 234 (144 / 98) | 12,3 % | 0,520 (45/29/54) | 0,259 (1675, 7/0/40) | 52 av 99 |

- «Uten historikk» = ingen etiketterte NBIM-stemmer i selskapet med møtedato strengt før sakens møtedato (samme
  definisjon som #2302, gruppe «0»). Den stemmer id for id med agentens regel «ukjent selskap» (0 avvik på val-inndata;
  agenten merker 99 av 1970, den 99. saken har ikke fasit).
- F1 maskin alene = agentens MOT-flagg (rå score ≥ grense 0,91885 og styret ikke MOT) mot MOT mot styret i fasit, som
  måler v3 `--score mot`. I gruppen uten historikk er det bare 3 MOT i fasit, så 0,571 er 2 treff av 3 og sier lite.
- Båndet fanger nesten alle flaggene: kalibrert grense er 0,191, så alle flagg med P(MOT) < 0,85 går til menneske.
  Maskinen beholder 7 MOT-flagg selv, alle riktige, og mister 40 av 99 MOT (ikke flagget, ikke rutet). Det er
  likt for begge grupper, så rutingen i seg selv flytter ikke F1 mellom dem.
- Modellens snitt kalibrert P(MOT): 0,057 uten historikk, 0,054 med. MOT-andel i fasit: 3,1 % mot 5,3 %.
  Ukjente selskaper har altså *lavere* MOT-andel enn kjente på val 2025, ikke høyere.

## Forbehold
- Agentens egen kjøring på val-inndata (`--csv real_val_input.csv`) gir 287 av 1970 til menneske (14,6 %: 193 bånd +
  99 ukjent selskap), men agenten skriver selv «saker fra før 2026 (i treningen, ikke ærlig målt): 1970»: P(MOT)
  der er in-sample. Tabellen over bruker derfor ut-av-prøve P(MOT) for 2025 (train.py sin `pv`, modell trent < 2025)
  med samme isotoniske kalibrering og bånd som agenten. Regelrutingen (ukjent selskap) er lik i begge.
- 61 val-saker uten fasit (against_board tom) er ikke med i tabellen.

## Gjenskap
```
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --csv arbeid/hack/c1/data_off/real_val_input.csv --vindu val --ut arbeid/oppgave_2305/agent_val
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2305/analyse.py arbeid/oppgave_2305/agent_val/agent.csv
```
Utskrift: `arbeid/oppgave_2305/analyse_ut.txt`. Per sak: `arbeid/oppgave_2305/val_grupper.csv` (id, tidl, ukjent, pv, q, band, rut, flagg, ys).

## Test 2026 (#2323, smed3): samme tabell med frossen #2044, 1539 saker med fasit

**Svar på spørsmålet:** test har 58 MOT mot styret i fasit, hvorav 28 er FN (ikke flagget av maskinen). Av de 58 MOT
havner 32 hos menneske (26 via båndet, 6 via «ukjent selskap»). Av de 28 FN havner 11 hos menneske (7 bånd, 4 ukjent
selskap); de siste 17 beholder maskinen selv som FOR, det er de ekte tapene. Alle 38 FP går til menneske, så maskinen
beholder 9 flagg alene, alle riktige (9/0/17 på de 1356 sakene den beholder, F1 0,514).

| gruppe | n saker | MOT mot styret i fasit | til menneske (bånd / ukjent selskap) | andel | F1 maskin alene (TP/FP/FN) | F1 maskin på sakene den beholder (n) | MOT i fasit blant rutede | FN hos menneske |
|---|---|---|---|---|---|---|---|---|
| uten historikk (0 tidl. stemmer) | 69 | 6 | 69 (0 / 69) | 100,0 % | 0,444 (2/1/4) | – (0 saker beholdt) | 6 av 6 | 4 av 4 |
| med historikk (1+) | 1470 | 52 | 114 (114 / 0) | 7,8 % | 0,479 (28/37/24) | 0,514 (1356, 9/0/17) | 26 av 52 | 7 av 24 |
| alle | 1539 | 58 | 183 (114 / 69) | 11,9 % | 0,476 (30/38/28) | 0,514 (1356, 9/0/17) | 32 av 58 | 11 av 28 |

- Raden «alle» er målt med v3 `--score mot` på den leverte fila (`kjor_agent_real_maskin_alene.csv`): TP 30 FP 38 FN 28,
  F1 0,476190, identisk med skriptets tall. Gruppe-radene kan ikke måles med v3 direkte (måleren krever alle id i vinduet
  og nekter ellers), så de er regnet med samme formel i skriptet; summen av gruppene gir v3-tallet.
- P(MOT) på test er ærlig: agenten skriver selv «saker fra før 2026 (i treningen): 0». Agentkjøringen her
  (`arbeid/oppgave_2323/agent_test/pred_maaler.csv`) er byte for byte lik den leverte `kjor_agent_real_pred_maaler.csv`.
- Agentens «ukjent selskap» treffer 70 av 1578 inn (69 med fasit), 0 avvik mot tidl==0 regnet fra datafila.
- Motsatt av val: på test har ukjente selskaper *høyere* MOT-andel (8,7 % mot 3,5 %) og høyere snitt kalibrert P(MOT)
  (0,077 mot 0,058). Båndet alene ville rutet 9 av 69 ukjente (13,0 %) mot 7,8 % av kjente. Regelen gjør fortsatt jobben:
  60 av de 69 rutes bare på grunn av regelen, og 4 av dem er MOT i fasit som maskinen ellers hadde tapt.
- 39 test-saker uten fasit er ikke med i tabellen (1578 inn, 1539 målt).

Gjenskap:
```
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --csv arbeid/hack/c1/data_off/real_test_input.csv --vindu test --ut arbeid/oppgave_2323/agent_test
python3 -I arbeid/oppgave_2323/analyse_test.py
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real --score mot
```
Utskrift: `arbeid/oppgave_2323/analyse_ut.txt`. Per sak: `arbeid/oppgave_2323/test_grupper.csv`.

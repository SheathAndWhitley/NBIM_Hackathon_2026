# Case 1: klokkesjekk av byttedommens forbehold (#2617) — dommer, 05.11 17:16

Påstandene fra arkitektens #2614 (c1_tre_harde_sporsmal.md, pkt. 3) sjekket mot tavlas logg (state/tavle.db, tabell logg),
git og filtider på disk. Alle klokkeslett er lokal tid 05.11.2026.

| # | Påstand | Dom | Kilde |
|---|---|---|---|
| 1 | Repo4s 2026-tall (0,5120) var kjent kl. 16:13 | **OK** (fil 16:13:30, meldt 16:14) | `arbeid/oppgave_2490/repo4_test.csv` mtime 16:13:30; rapport `c1_repotrekk_neste_versjon.md` 16:14:10 (rad «alle fire repotrekk … 0,512»); tavla forsøk #1195 16:14:14 «fire repotrekk … 0.512». Fila er byte-lik `oppgave_2570/kald/repo4_2026_test.csv`, som gir 0,5120 (cmp LIK). |
| 2 | Regelen kom kl. 16:49 | **OK** (16:48:59 / 16:49:22) | Ordre #265 inn 16:46:54 (logg ordre_ny). Regelen første gang skrevet i oppgaveteksten til #2567 kl. 16:48:59 (oppgaver.opprettet), gjentatt i #2570 16:49:13, og i mission.md commit `c1e7cf8` 16:49:22. |
| 3 | 2024 og 2025 for repo4 ble målt 16:49–16:50, etter regelen | **OK** | smed4 tok #2567 16:49:00; `oppgave_2567/repo4_2024_test.csv` og `repo4_2025_test.csv` mtime 16:49:38; `benk.txt` 16:50:22, `ki_snitt.txt` 16:50:54; fremgang 16:50:04 «repo4 trener for 2024/2025», 16:50:58 «alle 7 kandidater x 3 år målt». Tavla forsøk #1205 (snitt 0,5162) 16:51:07. |
| 3b | Fantes repo4-tall for 2024/2025 noe sted før regelen? | **NEI, bekreftet** | Søk i arbeid/ etter repo4-/repotrekk-filer før 16:48:59 gir bare de fire 2490-filene (val 2025/test 2026). Ingen rapport eller logglinje før 16:48:59 nevner repo4 sammen med 2024 eller 2025. |
| 4 | (byttedommens tillegg) frossens tre år var kjent før regelen | **OK** | `c1_personnokkel_rullende.md` 16:19:03 og dom #2503 16:22:28 har frossen 0,4545/0,5143/0,4762. |

## Ærlig presisering som bør med
- Avstanden mellom regel og måling er kort: 39 sekunder fra oppgaveteksten (16:48:59) til de første repo4-filene for 2024/2025 (16:49:38),
  16 sekunder fra mission-committen. Det er likevel riktig rekkefølge: smed4 startet 16:49:00 og kjørte kandidatene på tur; repo4 2024/2025 fantes ikke før det.
- «16:13» for 2026-tallet er filtiden; tallet ble meldt på tavla og i rapport 16:14. Begge formuleringer er sanne. Skriv «kl. 16:13» eller «kl. 16:14», ikke «16:1x».
- Setningen i pakken kan stå slik: «Byttregelen ble skrevet kl. 16:49 (ordre #265 kl. 16:47). Repo4s 2026-tall (0,512) var kjent fra kl. 16:13.
  Tallene som avgjorde, 2024 (+0,051) og 2025 (+0,017), ble målt kl. 16:49–16:51, etter regelen.»

## Gjenskap
`sqlite3 state/tavle.db "select ts,agent,hendelse,substr(detalj,1,120) from logg where detalj like '%2490%' or detalj like '%2567%' or detalj like '%#265%' order by ts"`;
`ls -lT arbeid/oppgave_2490 arbeid/oppgave_2567`; `git show --format=%ci c1e7cf8 -- mission.md`.

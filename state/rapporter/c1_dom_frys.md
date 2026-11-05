# Case 1: dom over modellfrysen kl. 16 (#2440)

Dommer, 05.11 kl. 16:20. **Dom: GRØNN.** Modellen er uendret siden 14:32, frysvakta er grønn, og min egen kalde
kjøring av den frosne pakka gir hovedtallet på nytt. Alt som er endret etter 15:30 er tekst og pakking, og hver
endring har en kjent, godkjent oppgave bak seg. Ingen modell-, terskel- eller prediksjonsendring etter kl. 16.

## 1. Hovedtallet gjenfunnet (akseptkrav 1)
Egen kald start kl. 16:10 (`BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh`, logg `arbeid/oppgave_2440_kaldstart.log`):

| Hva | Mitt tall | Ventet |
|---|---|---|
| F1 på MOT, måler v3 `--score mot` (sha 418a937e57) | **0,476190** | 0,476190 |
| pred_maaler.csv sha256 | b113b545dd86b263bba7… | b113b545…3653 |
| agent.csv sha256 | 1543706f9d9436bfcc6e… | 1543706f (rettet i #2325) |
| utgang / tid | 0 / 72 s | 0 |

Kontrollens egen kaldstart kl. 16:01 (#2247) ga samme tall. Frysvakt: `c1_frys.py sjekk --krev` = GRØNN, 17 filer like
som ved frys 2026-11-05T16:00:01. Alle 17 frosne filer har mtime ≤ 14:32:22 (nyeste: c1_real.py 14:32, injeksjon_hoflig.py 14:27,
begge dømt i #2474). Kontrollens «AVVIK» var et foreldet referansesett fra 13:51 (dom #2474), ikke et pakkeavvik.

## 2. Hva er «den godkjente pakka»
Siste grønne sluttsjekk før frysen: #2457 (commit 14dcbec kl. 16:00, «sluttsjekk GRØNN F1 MOT 0.476190, frys_diff LIK»).
Fasiten slik den lå i den committen (113 filer) er referansen. Fasiten nå (117 filer, regenerert 16:08 av #2475) er LIK kilden
(`frys_diff.sh --kilde`: 0 avvik).

## 3. Filer endret etter 15:30 (akseptkrav 2)
Pakkediff: fasit 16:00 (14dcbec) mot fasit nå. 0 borte, 4 nye, 11 endrede. Ingen av dem er blant de 17 frosne.

| Fil i zipen | Endret | Oppgave | Ønsket? |
|---|---|---|---|
| kilder/c1_motstand_etter_frys.md (ny) | 16:06 | #2479 motstandstest etter frys inn i jurytekstene | ja |
| kilder/c1_nbim_repo_sammenligning.md, …_dom.md (nye) | 16:08 | #2480 smed2 (pågår), kilde til jurysvar 3 | ja, tekst |
| state/rapporter/speider_2399_recall_budsjett.md (ny) | 16:09 | #2469, dom #2455 (kilde for NESTE_VERSJON:58) | ja |
| README.md (= levering/JURY_README.md) | 15:40, 16:07 | #2430, #2434, #2439 (kolonnetabell), #2475 (zip-størrelse) | ja |
| DEMO_MANUS.md | 16:02 | #1975 demo sjekket mot frossen pakke (agent.csv-sha rettet) | ja |
| leveranse/ERLIG_EVALUERING.md | 15:54, 16:06 | #2454, #2479 | ja |
| leveranse/JURY.md | 15:53, 16:06 | #2435 (sjargong ut), #2479 pkt. 11 | ja |
| leveranse/JURY_SPORSMAL.md | 15:53, 16:07 | #2435; **ucommittet** #2480 (presedenssetning, dømmes i #2484) | ja, tekst |
| leveranse/NESTE_VERSJON.md | 15:53, 16:08 | #2435, #2469; **ucommittet** #2481 tiltak 4 (arkitekt, pågår) | ja, tekst |
| leveranse/kilder/LESMEG.md | 15:54, 16:08 | #2454, #2479; **ucommittet** #2480 | ja |
| levering/JURYSVAR.md | 16:07 | samme minutt som #2480; fila er git-ignorert, eier ikke bekreftet av meg | tekst, dekkes av #2484 |
| pyproject.toml, uv.lock i zip-rota | 16:04 | #2475: kandidatens frosne (96fcf3b1/ed54fd6c) i stedet for landsbyens | ja, dom #2476 venter |

Endret 15:30–16:00 i pakka, alle før frys og dekket av grønn sluttsjekk #2457: kilder/c1_robusthet_reprod.md 15:31 (#2395),
c1_beslutning_nyeste_historikk.md og c1_offline_kaldstart.md 15:41 (#2435), leveranse/README.md 15:41 (#2438, 12 s → 4,8 s),
demo_utskrift.txt 15:42 (#2450), levering/BESLUTNINGSSTOTTE.md 15:42 (#2439), jury_kjor.sh = KJOR.sh 15:43 (#2426 mellomrom i sti),
demo.sh 15:48 (#2442). Utenfor zipen: pakk_jury.sh (#2422–#2475), sluttsjekk.sh (#2443), frys_diff.sh/frys_fasit.py (#2445, #2475).

Rettingene oppgaven nevner (#2435, #2438, #2439) er alle inne, alle ren ordlyd, alle før 16:00.

## 4. Konsekvens og krav til sluttsjekken 19:30
- Modellen er låst. Ingen endringer i de 17 frosne filene skal skje; frysvakta står i sluttsjekk.sh steg 1.
- Fasiten (frys_fasit_1600.sha256) ble regenerert kl. 16:08 mens #2480/#2481 var midt i redigering. **Den må lages på nytt
  når #2480 og #2481 er lukket** (`python3 -I arbeid/hack/levering/frys_fasit.py > arbeid/hack/levering/frys_fasit_1600.sha256`),
  ellers blir frys_diff rød mot zipen 19:30 på ren tekst. Tas i #1972.
- Tekstendringer etter 16 er lov (bare ordlyd), men hvert nytt tall skal gjennom tallvakta (#2255, #2470) og presedenssetningen gjennom #2484.

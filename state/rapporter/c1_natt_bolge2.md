# Case 1 natt, bølge 2: dommermåling av v2, v2+av, sanntids-terskel og tidsvekt (dommer2 #2890, 2026-11-05 19:50)

Måler: `arbeid/c1_natt/mal_kandidat.sh` (F1 MOT mot styret, oppgave_2567/maaler_aar.py --score mot). Frossen repo4 ga de pinnede
tallene i alle fem kjøringer. Svarmappene er kopiert med `cp -p` til `arbeid/oppgave_2890/k*/`, så REGEL.md beholder smedens
tidsstempel; måleren bekreftet at REGEL.md er eldre enn csv-ene i alle fem. Bytteregel #265/#281: snitt 2024-26 >= +0,02 over
frossen OG intet år (2023 medregnet) < −0,02. Selve byttet skjer ikke her: det er 02:00-dommen (#2874) og `state/c1_BYTT`.

| kandidat | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | diff snitt | verste år | dom | forsøk | selvrapportert |
|---|---|---|---|---|---|---|---|---|---|---|
| frossen repo4 | 0,3535 | 0,5057 | 0,5309 | 0,5120 | 0,5162 | 0 | | referanse | #1243 | |
| #2882 v2 SVD-tekst i LGBM, k valgt på val 32/64/48 (smed) | 0,3592 | 0,5326 | 0,5436 | 0,5299 | 0,5354 | +0,0192 | 2023 +0,0057 | **STÅR** | #1258 | 0,5354 ✓ |
| **#2887 v2 + av-regel (smed)** | 0,3723 | 0,5731 | 0,5667 | 0,5391 | **0,5596** | **+0,0434** | 2023 +0,0188 | **BYTT-kandidat** | #1259 | 0,5596 ✓ |
| #2883 midt+av, sanntids løpende terskel S2 (smed2) | 0,3636 | 0,5028 | 0,5276 | 0,5289 | 0,5198 | +0,0036 | 2025 −0,0033 | **STÅR** | #1260 | 0,5198 ✓ |
| #2885 tidsvekt tv valgt på val + av (smed3) | 0,3966 | 0,4000 | 0,5244 | 0,5487 | 0,4910 | −0,0252 | 2024 −0,1057 | **STÅR** | #1262 | 0,4910 ✓ |
| #2885 kontroll tv=1,0 + av (= #2701) | 0,3736 | 0,5269 | 0,5375 | 0,5246 | 0,5297 | +0,0135 | 2025 +0,0066 | STÅR (kontroll) | #1263 | 0,5297 ✓ |

Alle selvrapporterte tall er reprodusert på fjerde desimal. Ingenting står som «ikke levert»: alle tre smedene leverte innen tidsboksen.

## Gransking av BYTT-kandidaten v2+av (#2887)
Første kandidat i natt som fyller regelen, og med god margin: alle tre testår over frossen (+0,067/+0,036/+0,027) og vakt-året +0,019.
Det jeg har kontrollert før jeg kaller den BYTT-kandidat:
- **Kode = frossen + én ting.** `diff oppgave_2567/abl_rull.py c1_natt/v2/v2_rull.py` viser bare `--k` og tre linjer i LGBM-halvdelen:
  tf-idf og TruncatedSVD(k, random_state=0) tilpasses på treningsradene `tr` og transformerer alle rader. Ingen etiketter inn i SVD,
  LR-halvdelen uendret. Lekkasjeverktøyet (`hack/c1/sjekk_lekkasje.py kode`) flagger de samme fire linjene som i frossen (docstring,
  mål og injeksjonsmaske), ingen nye.
- **Modellen er deterministisk.** Jeg kjørte v2_rull.py på nytt for T=2024 k=32 i `arbeid/oppgave_2890/repro_v2/`: val- og testfil
  byte-identiske med smedens (`cmp`), 7 s.
- **Etterbehandlingen er reproduserbar.** v2av.py kjørt på nytt i `arbeid/oppgave_2890/repro_v2av/`: alle fire svarfiler identiske.
  Valget ingen/av ble tatt på val T−1 (0,3592→0,3723, 0,5532→0,5943, 0,5581→0,5595), av vant alle år. av-regelen er #2701s kode
  uendret, historikk strengt før året som måles.
- **Rekkefølgen holder.** v2-filene er fra 19:44 (#2882), REGEL.md for v2+av 19:46:27, svarfilene 19:46:36. k ble låst i #2882 på val
  før noen så v2+av-tall.
- **Gevinsten henger ikke på k.** Måler av smedens spredningsfiler (av på alle k, ikke brukt til valg):

  | k | 2024 | 2025 | 2026 | snitt |
  |---|---|---|---|---|
  | 32 | 0,5731 | 0,5357 | 0,5470 | 0,5519 |
  | 48 | 0,5680 | 0,5537 | 0,5391 | 0,5536 |
  | 64 | 0,5475 | 0,5667 | 0,5565 | 0,5569 |

  Dårligste k gir fortsatt +0,036 i snitt, og dårligste enkeltår over alle k er 2025 k=32 (+0,005). Det val-valgte 32/64/48 ligger
  litt over alle faste k (0,5596 mot 0,552–0,557), så 0,003–0,008 av tallet er val-valg-flaks; resten er trekket.
- **Hvorfor det virker, kort:** v2 alene gir +0,019 og av alene +0,0135; sammen +0,043. De er ortogonale (tekst-trekk i treet mot
  regel på NBIMs siste stemme), og av-regelen fjerner nettopp de falske flaggene v2 legger til (FP 2024 faller 47→34 uten tap av TP).

## Det som gjenstår før et faktisk bytte (02:00, #2874)
1. Støytesten fra arkitekten (#2889): +0,043 er godt over alt vi har sett av frøspredning (±0,02–0,05 på enkeltår, men snittet over
   tre år er roligere), men dommen skal ha tallet.
2. Byttet må gjøres i pakka: v2_rull.py inn i repoens pipeline med k låst (32/64/48 er per år; for levering på 2026-data er k=48),
   av-regel etter, og `KJOR.sh`/`testaar.sh` grønne på kald kopi (c1_natt_push.sh krever det). Det er en smed-oppgave, ikke måling.
3. Ingen ny variant av v2+av måles i samme mapper (REGEL). Stabling med regimeskifte (#2881b) er en ny kandidat med ny REGEL før måling.

## De andre, kort
- **v2 alene (#2882):** +0,0192, alle fire år i pluss, 0,0008 under kravet. Står, men er fundamentet for BYTT-kandidaten.
- **S2 sanntids-terskel (#2883):** ærlighetstall, ikke kandidat. Sanntid koster midt+av 0,006; lederen #2701 er allerede sanntid.
  Jurysetningen i c1_natt_sanntid.md holder.
- **Tidsvekt (#2885):** val valgte tv=0,7 for 2024, som ga en stram grense (32 flagg, recall 0,27) og 2024 −0,106. Vakt-året 2023 er
  +0,043, altså in-sample-pynt. Kontrollen tv=1,0 gjenskaper #2701 eksakt, så koden er riktig; trekket er bare dårlig. Spor lukket.

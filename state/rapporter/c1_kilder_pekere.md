# Case 1 (#2509): pekere til kilder/ og døde stier i jurytekstene

Skript: `arbeid/oppgave_2509/kilder_pekere.py` (fillista er `frys_fasit_1600.sha256`, altså zipen). Utskrift: `arbeid/oppgave_2509/utskrift.txt`.
Jurytekster: JURYSVAR, begge JURY_SPORSMAL, ERLIG_EVALUERING, kilder/LESMEG, DEMO_MANUS (+ JURY.md/README.md som tillegg).

**Foreldreløse filer i kilder/: før 13 av 50, nå 0 av 52.** De 12 som bare ble nevnt i JURY.md/README.md, eller ikke i det hele tatt (`c1_robusthet_sjekk.md`), har fått én linje hver i `kilder/LESMEG.md`. LESMEG selv nevnes nå fra JURYSVAR linje 3. De to nye personnøkkel-filene (lagt inn av andre underveis) har allerede pekere.

**Døde stier:** retting
- Pekte til en kopi som allerede lå i kilder/: JURYSVAR (ki_mot.py, c1_enkle_regler_og_hist1, nbim_repo_sammenligning + dom), levering/JURY_SPORSMAL (enkle_regler), DEMO_MANUS (demo_saker.md). Stiene er skrevet om til `kilder/`.
- Fantes i repoet, men ikke i zipen. Er nå med i zipen (ny kopier-linje i pakk_jury.sh, frys_fasit speiler den): c1/JURY_METODE.md, c1/SVAKHETER.md, c1/DEMO_MANUS_5min_tilfeldige.md, levering/c1_forslagsstiller.py/.txt, state/rapporter/c1_injeksjon_frossen.md, c1_motstandstall_dom.md, c1_demo_etter_rydding.md.
- Repo-skript som ikke kan kjøres fra zipen (kaldstart.sh, fremmed.sh, oppgave_2395/reprod.sh og fem_nye.py, oppgave_2345/bro_74_71_68.py, oppgave_2132/agent.csv) er merket «i repoet, ikke i zipen» i teksten.
- Står igjen i utskriften, men er ikke døde: utdatafiler (`agent.csv`, `ut/…`, `pred_maaler.csv`), `landsbyrapport:<navn>` (LESMEG.md:7 sier at de er interne rapporter), navnene LESMEG.md:3 selv sier er interne, `tavle.py`, og DEMO_MANUS-linjer som allerede er merket «ikke i zipen». leveranse/README.md beskriver hvordan pakka bygges fra repoet (den er ikke blant de fem jurytekstene) og er ikke endret.
- Ærlig rest: skriptet matcher på filnavn, så en sti med feil mappe men riktig filnavn et annet sted i zipen telles som levende.

**Kontroll:** pakk_jury.sh bygget fra kald start: HOVEDTALL F1 MOT 0.476190, TALLVAKT GRØNN (18 filer, 169 påstander, 0 avvik), sha256 i pakka = frysfila. Zipen har 127 filer, og de er filene i frys_fasit med lik sha256 (SHA_LIK). frys_fasit_1600.sha256 er regenerert. Ingen modellendring.

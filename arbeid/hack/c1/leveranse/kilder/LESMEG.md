# Kildene pakka peker til (kopier, 05.11 kl. 14.15)

> **Rydding 05.11 kveld:** lagets arbeidsmapper (`arbeid/oppgave_*`, `state/rapporter/`, eldre utkast og reservepakker) er
> fjernet fra repoet. Står det `utviklingsrapport:<navn>.md`, `state/rapporter/...` eller `arbeid/oppgave_<nr>/...` i en tekst,
> finnes fila i git-historikken: `git show 7d968c8:state/rapporter/<navn>.md` eller `git checkout 7d968c8 -- <sti>`.

Filnavn uten sti i rapportene under (f.eks. `abl.py`, `val_pred.py`, `reprod.sh`, `gvg2024.txt`) viser til lagets interne arbeidsmapper og er ikke med i pakka. Alle tall i rapportene står likevel ferdig målt i teksten.

Kopier av måle- og kontrollrapportene som JURY.md, BEGRENSNINGER.md og ERLIG_EVALUERING.md viser til, så pakka står alene.
Innholdet og tallene er uendret. Bare stier er skrevet om:
- en rapport som også ligger her heter `kilder/<navn>.md`; andre interne rapporter står som `utviklingsrapport:<navn>.md` (i eldre kilder `landsbyrapport:<navn>.md`, samme betydning);
- interne arbeidsfiler står som `<arbeidsmappe>/oppgave_<nr>/...` (ikke med i pakka);
- skript og tabeller fra arbeidsmappene heter `oppgave_<nr>_<fil>`. I `oppgave_2134_regler.py` skrives utfila nå til gjeldende mappe,
  og bruksteksten i `oppgave_2095_ki_mot.py` peker på kopien. Ellers er koden lik originalen.
- `demo_saker.md` (kopi 05.11 kl. 14.20 av `arbeid/hack/CASE/demo_saker.md`, uendret): de tre demosakene ordrett fra agentens utfil, med Mobimo (treff, linje 276) og LOTTE Chemical (bom, linje 89). Kilde for jurysvar 7–8 og demo-manuset.
- `TREFFSIKKERHET.md`, `c1_rare_saker_dom.md` og `c1_menneske_terskel.md` er kopiert inn 05.11 kl. 14.35, så JURY.md, BEGRENSNINGER.md og ERLIG_EVALUERING.md ikke peker ut av pakka.

**Ord du møter i kildene.** «sak 2134» og «forsøk 1115» er løpenumre i lagets interne arbeidslogg. De viser hvor en måling ble gjort, og du trenger dem ikke for å lese tallet.
«smed», «dommer» og «speider» er AI-agentene i laget: smeden bygger og måler, dommeren kontrollerer på nytt fra kald kopi, og speideren utforsker data.
«miks h2» er den frosne modellen: et snitt av logistisk regresjon og LightGBM med løpende historikk.
«hovedmålet» er F1 på MOT mot styret. «Maskin alene» betyr agentens stemme før noe går til et menneske.

Lagt til 05.11 kl. 14.40: `c1_val_kaldstart.md` (val 2025 fra kald start: 0,520 på MOT, 0,522 på avvik), `c1_feil_stabilitet.md` (KI for val), `c1_sitatkilder.md`, `c1_sitat_verifisert.md`, `c1_retningslinje_sitat.md` (sitatpåstandene) og `tell_trening.py`/`tell_trening.txt` (11 785 treningssaker).

Lagt til 05.11 kl. 15.10 (#2345): `tell_aar.py`/`tell_aar.txt` (MOT mot styret per år 2019–2026; test 2026: 141 møter, 136 selskaper, 140/135 blant sakene med fasit).

Lagt til 05.11 kl. 15.05 (#2358, dommer2): `c1_titlecase_vakt.md` (tittelvakta fra kl. 14.28: alle 16 instrukser fanges, verste F1 0,457 under angrep, 6 av 16 nye tittel-instrukser slipper med 18–27 stemmer endret uten ruting). De 16 instruksene og de 16 nye er kjørt på nytt av dommeren på filene som fryses; tallene i `c1_injeksjon_hoflig.md` (15 av 16, F1 0,392) gjelder vakta slik den var kl. 13.50, før tittelvakta.

Lagt til 05.11 kl. 16.06: `c1_motstand_etter_frys.md` (de 16 kjente og de 16 nye instruksene kjørt på nytt etter modellfrysen kl. 16 på den frosne agenten fra en kald kopi: 16/16 fanget, 0 stille endringer, verste F1 0,457; 6 av 16 nye slipper; alle tall like dommerens kjøring kl. 15.01).

Lagt til 05.11 kl. 16.15: `c1_nbim_repo_sammenligning.md` og dommen `c1_nbim_repo_sammenligning_dom.md` (teamets parallelle hybridløsning (laget av andre i teamet, parallelt med agenten, ikke fra NBIM), kjørt uendret på vår måler og test 2026: presedensregelen 0,515, +0,04 [−0,05; +0,13] over vår frosne modell; hybriden 0,545 på vår splitt, +0,069 [+0,007; +0,133]; PR-AUC 0,525 for vår modell). Kilde for jurysvar 3. `<opplastet>/` er zipen med hybridløsningen. Rettet 05.11 (ordre #262): løsningen er laget av andre i teamet, parallelt med agenten, ikke fra NBIM; «nbim_repo» i filnavnene er historisk og beholdes så pekerne ikke brekker.

**Resten av mappa (#2509, 05.11 kl. 16.35).** Disse kopiene ble før bare nevnt fra `leveranse/JURY.md` eller `leveranse/README.md`, så de står her også:
- `c1_beslutning_nyeste_historikk.md`: beslutningsloggen for forsøket med nyeste historikk (sak 2363).
- `c1_falske_mot.md`: hvorfor agenten sier falsk MOT i USA og på styrevalg (#2357).
- `c1_injeksjon_etter_2205.md`: injeksjonstesten kjørt på nytt etter robusthetsfiksen (sak 2212).
- `c1_kjoretid.md`: kjøretid og minne for agenten (sak 2213).
- `c1_mennesket_arbeid.md`: hvor mye arbeid mennesket får, og hvor mange MOT det fanger (#2377).
- `c1_mot_sakstyper.md`: hva slags saker MOT-stemmene er (sak 2181).
- `c1_robusthet_sjekk.md`: dommerens uavhengige gjentakelse av robusthetstesten (sak 2154).
- `c1_seed_frossen.md`: seed-spredning på den frosne agenten (#2326).
- `c1_tiltak1_malt.md`: tiltak 1 (styrevalg-historikk som forfaller) målt; ikke bygd inn.
- `case1_hvilken_fasit.md`: hvilken fasit som teller, NPX-fila eller NBIMs API-stemmer (sak 2052).
- `oppgave_2216_tell.py`: teller TP/FP/FN på MOT per forslagskilde og ruting fra en kald kjøring.
- `oppgave_2234_baseline_real_test.txt`: måleutskriften for «følg styret» på real_votes test 2026.

Lagt til 05.11 kl. 16.30 (dom #2508): `c1_personnokkel_rullende.png`, figuren til `c1_personnokkel_rullende.md` (rullende F1 MOT per testår 2024–2026, frossen modell mot + personnøkkel, 95 % KI-strek, «følg styret» = 0; ikke hovedtall). Pekes på fra `leveranse/NESTE_VERSJON.md`. Dommen `dom_2497_figur.md` sier hvor hvert punkt står i tabellen.

Lagt til 05.11 kl. 16.40 (#2512): `c1_rare_inndata.md` (jury-zipen kjørt med 9 rare filer: tom fil, feil skilletegn, manglende kolonne, nytt år, tom eller manglende historikk; ingen krasj uten melding) og dommen `dom_2499_rare_inndata.md` (dommer2 gjentok to av filene fra kald start, fem svakheter godkjent). Kilde for `BEGRENSNINGER.md` pkt. 9 og siste avsnitt i `NESTE_VERSJON.md`.

Lagt til 05.11 kl. 16.45 (#2521, feilhenvisninger fra `c1_tallkontroll.md`): `omfang.txt` og `omfang.py` (194 selskaper, 37 land, 1161 møter og 24 sakstyper i real_votes; kilde for kravresponsen), og fire landsbyrapporter som før bare fantes i repoet: `c1_bootstrap_f1.md` (bootstrap-KI for F1 på avvik, val [0,403; 0,624], test 0,482), `c1_neste_steg.md`, `c1_valgt_bort.md` (t4e-raden og to-målere-merknaden) og `c1_huskeregel.md`. Pekes på fra `JURY.md`, `ERLIG_EVALUERING.md` § 6, `JURY_SPORSMAL.md` pkt. 11 og `NESTE_VERSJON.md`.

Lagt til 05.11 kl. 16.50 (#2532, etter byttedom #2529): `c1_v2_rullende_2024.md` (hybriden først, vår rangering i midten, rullet til test 2024 med val 2023; ikke hovedtall, −0,047 mot frossen-oppsettet). Pekes på fra `NESTE_VERSJON.md` tiltak 4.

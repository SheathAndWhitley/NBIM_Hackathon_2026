# Case 1: hvilke manglende filer må med i jury-zipen (speider #2446, 05.11 kl. 15.55)

Kjørt `/tmp/lenkesjekk2.py` på nyeste zip (`/tmp/jurypakke_c1.zip`, 15:45, med tall_tabell.md). Resultat: 690 pekere,
**79 unike filer finnes i repoet, men ikke i zipen** (≈ 180 pekere). I tillegg 202 «MANGLER» (bare navn som `agent.csv`, `train.py`,
rapportnavn uten sti). Dem har jeg ikke gått gjennom én for én. Rå utskrift: `/tmp/sp2446/ut.txt`.
`tall_tabell.md` er alt med (cc84f77). `DEMO_MANUS.md` er lagt inn i pakk_jury.sh etter 15:45 (#2442), sjekk det i neste zip.

## (1) Må med i zipen: 9 filer, ca. 400 KB, alle bare stdlib eller zipens .venv
Juryen trenger disse for å etterprøve et tall eller en påstand. Alle stiene er relative til repo-roten, slik `kopier` i pakk_jury.sh vil ha dem.
Importene er sjekket: de finner `maaler_offisiell_v2/v3.py` og `c1_real.py` på samme plass i zipen.
```sh
kopier arbeid/hack/levering/kjor_agent_real_pred_maaler.csv \
       arbeid/hack/levering/kjor_agent_real_test2026.txt \
       arbeid/hack/c1/sjekk_lekkasje.py \
       arbeid/hack/levering/treffsikkerhet.py \
       arbeid/hack/levering/treffsikkerhet_ki.py \
       arbeid/hack/c1/terskel_val_test.py \
       arbeid/hack/c1/menneske_tabell.py \
       arbeid/hack/c1/data_off/real_val_input.csv \
       arbeid/hack/c1/DEMO_MANUS.md
```
| fil | hvorfor | pekes fra |
|---|---|---|
| `levering/kjor_agent_real_pred_maaler.csv` (40 KB) | svarfila bak hovedtallet 0,476. **Lenkesjekken sa den var med, men den er IKKE i zipen 15:45** (bare `_maskin_alene.csv` og `_LES.md`) | TREFFSIKKERHET.md:93,96,98, c1_feil_stabilitet.md:53, c1_robusthet_kald_2380.md:10, c1_robusthet_reprod.md:11 |
| `levering/kjor_agent_real_test2026.txt` (2 KB) | kjøreloggen: FEATURES-lista og «FORBUDT og ikke brukt», altså beviset for at det ikke er lekkasje | JURY.md:9, c1_tall_likt.md:26 |
| `c1/sjekk_lekkasje.py` (5 KB) | lekkasjevakta som ERLIG_EVALUERING viser til. Kjører med `maaler_offisiell_v2` i samme mappe | ERLIG_EVALUERING.md:59 |
| `levering/treffsikkerhet.py`, `treffsikkerhet_ki.py` (6 KB) | lager 2x2-tabellen og KI i TREFFSIKKERHET.md. Importerer `../c1/maaler_offisiell_v3`, som er med | TREFFSIKKERHET.md:96,98 |
| `c1/terskel_val_test.py` (2 KB) | viser at terskelen ble valgt på val, ikke på test (JURY_SPORSMAL S2). Bruker `c1_real` og numpy fra zipens .venv | TREFFSIKKERHET.md:86,87 |
| `c1/menneske_tabell.py` (3 KB) | tabellen «send til menneske». **NB:** standardstiene er hardkodet til `<repo>/...` (linje 7-8), så den må kjøres med AGENT.csv som argument, og FASIT-stien trenger samme sed-retting som målerne i pakk_jury.sh steg 3 (eller la være og bare vise koden) | c1_menneske_terskel.md:3 |
| `c1/data_off/real_val_input.csv` (340 KB) | val-kjøringen (F1 0,7547 på val, ruting 14,6 %) i c1_val_kaldstart.md kan bare gjentas med den | c1_val_kaldstart.md:4 |
| `c1/DEMO_MANUS.md` (6 KB) | allerede i pakk_jury.sh (#2442); står her så #1975 ser at den må være i den frosne zipen | c1_sitatkilder.md:5,67 |

**Testet fra utpakket zip 15:45 (filene kopiert inn, `python3 -I`, ingen .venv):** `treffsikkerhet.py`, `treffsikkerhet_ki.py` (bootstrap-KI, recall 34,6 % [15,8–55,0]) og `sjekk_lekkasje.py svar … --data real` (OK, utgang 0) kjører alle på `kjor_agent_real_pred_maaler.csv`. Ikke testet: `terskel_val_test.py` (trenger zipens .venv etter `sh KJOR.sh`) og `menneske_tabell.py` (hardkodede stier).

## (2) Pekeren bør omskrives: intern, gir ingen mening i zipen
Ikke ta filene med. Én setning i ERLIG_EVALUERING.md § 5 og README («utviklingsspor, ligger i repoet, ikke i zipen; `KJOR.sh` er zip-veien»)
dekker det meste. Disse linjene bør likevel rettes eller merkes «(repo, ikke i zipen)»:

**a. Gjenskap-kommandoer som ikke virker fra zipen (viktigst, juryen prøver dem):**
- `fremmed.sh`: ERLIG_EVALUERING.md:41, :70; README.md:33, :36; kilder/c1_mennesket_arbeid.md:3, :24, :28; c1_offline_kaldstart.md:8, :34;
  c1_rare_saker_dom.md:4, :40; c1_retningslinje_sitat.md:91, :93; c1_robusthet_frossen.md:42; c1_robusthet_kald_2380.md:7, :55;
  c1_robusthet_reprod.md:4, :10, :29, :31; c1_injeksjon_hoflig.md:5; c1_titlecase_vakt.md:75
- `kaldstart.sh`: ERLIG_EVALUERING.md:70; c1_injeksjon_hoflig.md:26, :69; c1_kjoretid.md:7, :18, :23; c1_retningslinje_sitat.md:91, :94;
  c1_titlecase_vakt.md:33, :79, :86; c1_val_kaldstart.md:3, :20
- `oppgave_2395/reprod.sh`, `fem_nye.py`: ERLIG_EVALUERING.md:43; c1_robusthet_reprod.md:3, :16, :25, :33
- `arbeid/hack/maaler.sh`: README.md:33; c1_menneske_terskel.md:19
- `arbeid/hack/CASE/20261105_114241_real_votes.csv` → skal være `state/opplastet/20261105_114241_real_votes.csv` (samme fil, er i zipen):
  c1_enkle_regler_og_hist1.md:27; dommer_ablasjon_v2.md:25

**b. Oppgavemapper (arbeid/oppgave_NNNN/…), bare spor av hvordan tallet ble laget:**
- c1_robusthet_kald_2380.md:12, :14, :37, :53, :54, :55, :58; c1_robusthet_reprod.md:5, :12-16, :24, :25, :31 (2063, 2380, 2395)
- c1_retningslinje_sitat.md:17, :34, :64, :84, :85, :95, :96; c1_sitatkilder.md:5; c1_sitat_verifisert.md:3, :5 (2106, 2115, 2118, 2130, kandidater/FROSSEN.md)
- c1_feil_stabilitet.md:16, :17, :18, :33 (2274); c1_val_kaldstart.md:20, :26 (2282); c1_tiltak1_malt.md:6, :39, :40, :42, :43 (2283)
- c1_seed_frossen.md:3, :6 (2326); c1_praksis_mot_policy.md:5, c1_praksis_dom.md:6 (2331); c1_falske_mot.md:3, :4, :5 (2087, 2357)
- c1_mennesket_arbeid.md:25 (2377); c1_rare_saker_dom.md:19, :43 (2257); demo_saker.md:5 (2260); c1_enkle_regler_og_hist1.md:27 (2134)
- c1_injeksjon_hoflig.md:5 (`arbeid/verktoy/c1_frys.py`)

**c. state/rapporter-pekere til filer som alt ligger i `kilder/` (rett til bare filnavn):**
- c1_praksis_mot_policy.md:43 → `c1_praksis_dom.md`; c1_praksis_dom.md:3 → `c1_praksis_mot_policy.md`
- c1_feil_stabilitet.md:3 (`state/rapporter/c1_feil_per_gruppe.md`, ikke i kilder/): merk «(repo)»
- Resten av B i c1_lenkesjekk.md (NESTE_VERSJON.md 14 stk, JURY_SPORSMAL.md:49, :54, JURY.md:77) står der med linjer. JURY*.md rører jeg ikke (#2435).

**d. Interne dokumenter som ikke er jurytekst:** c1_bommene.md:36, :39 (`SVAKHETER.md`); c1_tall_likt.md:17 (`c1/JURY_METODE.md`), :27 (`levering/demo/README.md`);
c1_sitat_verifisert.md:4 (`arbeid/hack/retningslinjer/nbim_retningslinjer.jsonl`: rådata, 365 KB; agenten i zipen bruker `c1/retningslinjer/punkter.jsonl`, si det i stedet);
c1_injeksjon_etter_2205.md:30 (`motstandstest.py`, 17 KB: kan tas med hvis #2266 vil at juryen skal kjøre motstandstesten selv, ellers merk «repo»).

## (3) Uviktig: la stå
- `c1/baseline.py`, `hent_npx.py` (README.md:67, kilder/case1_hvilken_fasit.md:8): kreditering/historikk.
- `spor_npx/utkast_1100/README.md:21-34, :64` (`hent_votes.py`, `maaler.py`, `baseline.py`, `hent_npx.py`): gammelt utkast, merk hele mappa «historisk».
- `state/opplastet/20261105_114240_npx_votes.csv` (README.md:21): 12 MB NPX-rådata, ikke brukt av hovedtallet. Ikke ta med.
- `arbeid/hack/CASE/demo_saker.md` (LESMEG.md:9): bare omtale, kopien ligger i kilder/.

## Kort for #1975
1. Lim kopier-linja over inn i pakk_jury.sh (etter tall_tabell-linja). Størst gevinst: `kjor_agent_real_pred_maaler.csv` og `kjor_agent_real_test2026.txt`, som JURY.md:9 bygger på.
2. Bytt `arbeid/hack/CASE/…real_votes.csv` med `state/opplastet/…` på to linjer.
3. Én setning om «repo, ikke i zipen» for fremmed.sh/kaldstart.sh/oppgavemapper i stedet for å rette 80 linjer.

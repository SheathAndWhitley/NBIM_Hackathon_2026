# Case 1: de 202 pekerne uten sti i jurytekstene, sortert i tre bøtter (#2449)

Kilde: /tmp/sp2446/ut.txt (#2446), avsnittet MANGLER. Zip-innhold: /tmp/sp2446/z (109 filer). Sortert med `arbeid/oppgave_2449/sorter.py` og deretter gått gjennom for hånd. Jeg har ikke endret noen filer.

| Bøtte | Antall | Betydning |
|---|---|---|
| a | 108 | Ufarlig. Filnavnet finnes i zipen under en annen sti (f.eks. `train.py`, `punkter.jsonl`), eller det er en utfil eller eksempelsti som lages når noen kjører pakka (`agent.csv`, `ut/*`, `_pred_uten_ruting.csv`, `rv.csv`, `saker.csv` som plassholder) |
| b | 8 | Peker på en fil juryen trenger for å etterprøve et tall. Alle 8 står i `NESTE_VERSJON.md`, og de peker på 3 filer |
| c | 86 | Intern peker. 34 av dem står i `spor_npx/utkast_1100/README.md`, et gammelt utkast med TODO. Resten står mest i `kilder/*.md` og peker på rapporter, oppgavemapper og skript i landsbyen |

## Bøtte b: ferdige linjer til pakk_jury.sh

Legg dem etter blokka til #2448. Ingen av de 9 filene til smed2 går igjen her. Jeg har sjekket at ingen av de tre filene inneholder `~`.
```sh
# NESTE_VERSJON.md bygger tall på disse (#2449, bøtte b)
kopier state/rapporter/c1_feil_per_gruppe.md state/rapporter/arkitekt_c1_neste_versjon.md \
       arbeid/oppgave_2274/feil_val2025.md
```
Etter kopieringen må pekerne i `NESTE_VERSJON.md` få full sti: `state/rapporter/c1_feil_per_gruppe.md:4/25/26`, `state/rapporter/arkitekt_c1_neste_versjon.md` og `arbeid/oppgave_2274/feil_val2025.md:7/9`. Linjenumrene stemmer fordi filene kopieres uendret. Det samme må gjøres for `landsbyrapport:arkitekt_c1_neste_versjon.md` på linje 9. Filene kan inneholde interne #-numre. Arkitekten (#2435) bør ta en titt på dem før frysen.

## Forslag til bøtte c, samlet
1. **Ta `arbeid/hack/c1/leveranse/spor_npx/utkast_1100/` ut av zipen.** Mappa er et gammelt utkast med `TODO` og står for 34 av de 86 pekerne. Linja i pakk_jury.sh: legg `-not -path "*/spor_npx/utkast_1100/*"` til i find-kallet som henter `arbeid/hack/c1/leveranse`.
2. **`landsbyrapport:`-pekerne** i `NESTE_VERSJON.md` og `JURY_SPORSMAL.md:49` er allerede merket som interne. De kan stå, men det må stå én gang øverst i fila at «landsbyrapport: = intern rapport, ikke i pakka».
3. **Rapportpekere uten `landsbyrapport:`-prefiks** i `NESTE_VERSJON.md`, utenom bøtte b (linje 47 `opplastet_…real_votes.md:7`): sett prefikset på, så de blir like som de andre.
4. **`ERLIG_EVALUERING.md:48, 70` `hist_regel.py`:** skriptet ligger bare i `arbeid/hack/levering/c1_v1/`. Skriv «gammelt internt skript, ikke i pakka», eller vis heller til `kilder/c1_enkle_regler_og_hist1.md`, som allerede er i zipen.
5. **`kilder/*.md`** er arbeidslogger med pekere som `abl.py`, `val_pred.py`, `reprod.sh`, `fem_nye.py` og `gvg2024.txt` til oppgavemapper. Lav prioritet: legg én linje øverst i `kilder/LESMEG.md` om at filnavn uten sti i kilder/ viser til landsbyens interne arbeidsmapper og ikke er med i pakka. Det er raskere og tryggere enn å skrive om 50 linjer før frysen.

## Hele tabellen (202 rader)
`lev/` = `arbeid/hack/c1/leveranse/`.

| fil | linje | peker | bøtte | forslag |
|---|---|---|---|---|
| README.md | 15 | `jurypakke_c1.zip` | a | utfil/eksempelsti, lages ved kjøring |
| README.md | 27 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| README.md | 29 | `ut/agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| README.md | 58 | `ut_egen/agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/ERLIG_EVALUERING.md | 56 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/README.md | 37 | `real_votes.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/README.md | 53 | `saker.csv` | a | plassholder i kommandolinja (--csv saker.csv) |
| lev/README.md | 53 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/README.md | 59 | `real_votes.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/README.md | 61 | `npx_votes.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/TREFFSIKKERHET.md | 69 | `train.py:116` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 5 | `test2026.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 21 | `KORT.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 25 | `_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 27 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_enkle_regler_og_hist1.md | 30 | `_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 31 | `_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 33 | `kontroll_h2_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_enkle_regler_og_hist1.md | 39 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_falske_mot.md | 3 | `real_votes.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/c1_feil_stabilitet.md | 4 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_injeksjon_etter_2205.md | 6 | `inj.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_etter_2205.md | 6 | `inj2.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_etter_2205.md | 6 | `f1.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_etter_2205.md | 6 | `resultat.json` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_hoflig.md | 22 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_hoflig.md | 23 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_hoflig.md | 24 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_hoflig.md | 27 | `vern.py` | a | i zip: arbeid/oppgave_2047/vern.py |
| lev/kilder/c1_injeksjon_hoflig.md | 30 | `resultat.json` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_injeksjon_hoflig.md | 30 | `tabell.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_kjoretid.md | 20 | `tider.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_menneske_terskel.md | 8 | `baand_tabell.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_mennesket_arbeid.md | 5 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_mennesket_arbeid.md | 6 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_mennesket_arbeid.md | 26 | `15_0.85/ut/_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_mennesket_arbeid.md | 28 | `kjor_tomt.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_mot_sakstyper.md | 31 | `c1_tallvakt.py` | a | i zip: arbeid/verktoy/c1_tallvakt.py |
| lev/kilder/c1_offline_kaldstart.md | 21 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_offline_kaldstart.md | 36 | `ut/pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_offline_kaldstart.md | 36 | `ut/agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_rare_saker_dom.md | 22 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_rare_saker_dom.md | 22 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_rare_saker_dom.md | 23 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_retningslinje_sitat.md | 3 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_retningslinje_sitat.md | 7 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_retningslinje_sitat.md | 7 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_retningslinje_sitat.md | 93 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_frossen.md | 6 | `DIR/_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_frossen.md | 42 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_frossen.md | 42 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_frossen.md | 42 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 8 | `c1_frys.json` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 9 | `_pred_uten_ruting.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 9 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 13 | `real_test_input.csv` | a | i zip: arbeid/hack/c1/data_off/real_test_input.csv |
| lev/kilder/c1_robusthet_kald_2380.md | 54 | `tabell.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 54 | `resultat.json` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 54 | `pred_maaler_kald.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_kald_2380.md | 54 | `KJORING_kald.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 11 | `../pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `tabell.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `resultat.json` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `sammenlign.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `fremmed.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `robusthet.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 25 | `reprod_utskrift.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 34 | `sammenlign.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 35 | `ut/tabell.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_robusthet_reprod.md | 35 | `ut2/tabell.md` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_siste_mot_forsok.md | 22 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_sitatkilder.md | 3 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_sitatkilder.md | 3 | `punkter.jsonl` | a | i zip: arbeid/hack/c1/retningslinjer/punkter.jsonl |
| lev/kilder/c1_sitatkilder.md | 3 | `real_train.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/c1_sitatkilder.md | 5 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_sitatkilder.md | 33 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_sitatkilder.md | 33 | `punkter.jsonl` | a | i zip: arbeid/hack/c1/retningslinjer/punkter.jsonl |
| lev/kilder/c1_sitatkilder.md | 36 | `arbeid/hack/c1/data_nbim/real_train.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/c1_streng_mot.md | 6 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_streng_mot.md | 27 | `svar_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_tall_likt.md | 28 | `svar_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/c1_val_kaldstart.md | 23 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_val_kaldstart.md | 25 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_val_kaldstart.md | 26 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_val_kaldstart.md | 29 | `real_val_input.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/c1_val_kaldstart.md | 36 | `train.py` | a | i zip: arbeid/oppgave_2044/train.py |
| lev/kilder/c1_val_kaldstart.md | 39 | `maaler_v3_ut.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/case1_hvilken_fasit.md | 32 | `_votes.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 3 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 5 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 11 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 39 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 67 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 100 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/demo_saker.md | 100 | `pred_maaler.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_2090_streng_mot.md | 7 | `real_votes.csv` | a | data, ligger i zip under data_*/ eller lages av KJOR.sh |
| lev/kilder/dommer_2090_streng_mot.md | 9 | `svar_val.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_2090_streng_mot.md | 9 | `svar_test.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 25 | `K/rv.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 27 | `rv.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 27 | `full.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 27 | `full.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 28 | `rv.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 28 | `hist1.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 28 | `hist1.log` | a | utfil/eksempelsti, lages ved kjøring |
| lev/kilder/dommer_ablasjon_v2.md | 30 | `full_test.csv` | a | i zip: arbeid/oppgave_2103/full_test.csv |
| lev/spor_npx/LESMEG.md | 8 | `agent.csv` | a | utfil/eksempelsti, lages ved kjøring |
| lev/spor_npx/LESMEG.md | 8 | `KJORING.txt` | a | utfil/eksempelsti, lages ved kjøring |
| lev/NESTE_VERSJON.md | 5 | `c1_feil_per_gruppe.md:4` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 9 | `arkitekt_c1_neste_versjon.md` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 13 | `c1_feil_per_gruppe.md:25` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 14 | `feil_val2025.md:7` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 18 | `arkitekt_c1_neste_versjon.md` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 43 | `c1_feil_per_gruppe.md:26` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 43 | `feil_val2025.md:9` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/NESTE_VERSJON.md | 44 | `arkitekt_c1_neste_versjon.md` | b | tall i NESTE_VERSJON bygger på den; kopier til kilder/ (se kopier-linje) |
| lev/ERLIG_EVALUERING.md | 48 | `hist_regel.py` | c | gammelt skript (arbeid/hack/levering/c1_v1/hist_regel.py): skriv «gammelt internt skript, ikke i pakka» |
| lev/ERLIG_EVALUERING.md | 70 | `hist_regel.py` | c | gammelt skript (arbeid/hack/levering/c1_v1/hist_regel.py): skriv «gammelt internt skript, ikke i pakka» |
| lev/JURY_SPORSMAL.md | 49 | `c1_neste_steg.md` | c | intern rapport (state/rapporter/c1_neste_steg.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/JURY_SPORSMAL.md | 49 | `c1_valgt_bort.md` | c | intern rapport (state/rapporter/c1_valgt_bort.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/JURY_SPORSMAL.md | 49 | `c1_bootstrap_f1.md` | c | intern rapport (state/rapporter/c1_bootstrap_f1.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/JURY_SPORSMAL.md | 49 | `c1_huskeregel.md:3` | c | intern rapport (state/rapporter/c1_huskeregel.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 3 | `c1_neste_steg.md` | c | intern rapport (state/rapporter/c1_neste_steg.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 22 | `arkitekt_tiltak1_malt.md` | c | intern rapport (state/rapporter/arkitekt_tiltak1_malt.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 24 | `opplastet_20261105_114241_real_votes.md:7` | c | intern rapport (state/rapporter/opplastet_20261105_114241_real_votes.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 32 | `c1_india_paret.md` | c | intern rapport (state/rapporter/c1_india_paret.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 33 | `c1_india_seeds.md` | c | intern rapport (state/rapporter/c1_india_seeds.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 34 | `c1_bootstrap_f1.md` | c | intern rapport (state/rapporter/c1_bootstrap_f1.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 47 | `opplastet_20261105_114241_real_votes.md:7` | c | intern rapport (state/rapporter/opplastet_20261105_114241_real_votes.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 55 | `c1_valgt_bort.md` | c | intern rapport (state/rapporter/c1_valgt_bort.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 58 | `speider_2399_recall_budsjett.md` | c | intern rapport (state/rapporter/speider_2399_recall_budsjett.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/NESTE_VERSJON.md | 63 | `c1_neste_steg.md` | c | intern rapport (state/rapporter/c1_neste_steg.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 3 | `c1_nyeste_historikk.md` | c | intern rapport (state/rapporter/c1_nyeste_historikk.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 6 | `c1_lekkasje_2363.md` | c | intern rapport (state/rapporter/c1_lekkasje_2363.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 7 | `c1_nyeste_historikk.md` | c | intern rapport (state/rapporter/c1_nyeste_historikk.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 10 | `c1_nyeste_historikk.md` | c | intern rapport (state/rapporter/c1_nyeste_historikk.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_beslutning_nyeste_historikk.md | 12 | `c1_beslutning_india.md` | c | intern rapport (state/rapporter/c1_beslutning_india.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_enkle_regler_og_hist1.md | 33 | `til_id.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_enkle_regler_og_hist1.md | 47 | `regler.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_feil_stabilitet.md | 75 | `val_pred.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_feil_stabilitet.md | 75 | `feil_per_gruppe_aar.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_feil_stabilitet.md | 75 | `ruting_varianter.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_injeksjon_hoflig.md | 30 | `fraser.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_kjoretid.md | 20 | `saker.jsonl` | c | intern fil (arbeid/verktoy/mal/llm_agent/saker.jsonl): stryk eller merk «intern, ikke i pakka» |
| lev/kilder/c1_rare_saker_dom.md | 5 | `c1_real_foer.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_retningslinje_sitat.md | 64 | `selskap.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_robusthet_kald_2380.md | 48 | `c1_injeksjonsvakt_ablasjon.md` | c | intern rapport (state/rapporter/c1_injeksjonsvakt_ablasjon.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_robusthet_reprod.md | 10 | `reprod.sh` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_robusthet_reprod.md | 19 | `fem_nye.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_sitat_verifisert.md | 26 | `sjekk.py` | c | intern fil (arbeid/oppgave_1836/sjekk.py): stryk eller merk «intern, ikke i pakka» |
| lev/kilder/c1_sitatkilder.md | 5 | `gvg2024.txt` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_sitatkilder.md | 5 | `sjekk_begrunnelser.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_sitatkilder.md | 5 | `gvg2024.txt` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_sitatkilder.md | 69 | `lag_retningslinjer.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_tall_likt.md | 26 | `kjor_agent_holdout2026.txt` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_tiltak1_malt.md | 23 | `boot.py` | c | intern fil (arbeid/oppgave_1838/boot.py): stryk eller merk «intern, ikke i pakka» |
| lev/kilder/c1_tiltak1_malt.md | 39 | `val_t11_tau1.csv` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_titlecase_vakt.md | 3 | `c1_motstandstall_dom.md` | c | intern rapport (state/rapporter/c1_motstandstall_dom.md): omskriv til «intern rapport, ikke i pakka» eller kopier til kilder/ |
| lev/kilder/c1_titlecase_vakt.md | 7 | `c1_frys.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_val_kaldstart.md | 26 | `val_pred.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/c1_val_kaldstart.md | 39 | `val_pred.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_2090_streng_mot.md | 7 | `streng_mot.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_ablasjon_v2.md | 12 | `abl.py:105` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_ablasjon_v2.md | 19 | `abl.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_ablasjon_v2.md | 27 | `abl.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_ablasjon_v2.md | 28 | `abl.py` | c | finnes ikke i repo: stryk pekeren |
| lev/kilder/dommer_ablasjon_v2.md | 32 | `abl.py` | c | finnes ikke i repo: stryk pekeren |
| lev/spor_npx/utkast_1100/README.md | 11 | `leveranse/run.sh` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 14 | `requirements.txt` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 15 | `ut/RESULTAT.md` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 15 | `ut/kjoring.log` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 21 | `data/votes.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 22 | `votes.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 23 | `modell.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 23 | `ut/pred.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 23 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 24 | `pred.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 25 | `motstand.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 25 | `ut/motstand.json` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 26 | `leveranse/rapport.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 26 | `ut/RESULTAT.md` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 29 | `data/votes.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 29 | `data/train.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 30 | `data/test_input.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 30 | `data/fasit.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 30 | `data/split_info.txt` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 32 | `modell.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 32 | `ut/pred.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 32 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 32 | `pred.csv` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 39 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 39 | `leveranse/sporlogg.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 41 | `leveranse/sporlogg.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 42 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 43 | `ut/maal_baseline.txt` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 43 | `ut/maal_modell.txt` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 43 | `motstand.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 43 | `ut/motstand.json` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 44 | `leveranse/rapport.py` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 46 | `ut/RESULTAT.md` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/README.md | 81 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |
| lev/spor_npx/utkast_1100/kravrespons.md | 16 | `ut/anbefalinger.jsonl` | c | gammelt utkast med TODO: ta hele spor_npx/utkast_1100 ut av zipen |

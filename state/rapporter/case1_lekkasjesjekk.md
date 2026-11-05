# Case 1: lekkasjesjekk av smed2s v3-kjennetegn (dommer #1985)

Kode sjekket: `arbeid/kandidater/smed2_c1_mot/train_v3.py` + `sec_feats.py` (lgbm v3).
Spørsmål per kjennetegn: er verdien kjent FØR generalforsamlingen (møtedato D)?

## Dom per kjennetegn
| Kjennetegn | Kilde og regel i koden | Dom |
|---|---|---|
| nb_n, nb_mot, nb_sist, nb_rate | NBIMs egne say-on-pay-stemmer, bare train-rader med møte < D. NBIM publiserer stemmene dagen etter møtet. Testrader bruker bare train-historikk (ingen testfasit). | ok |
| v_sop/dir/ann/akh_*, v_sop_sist, v_uenige, v_moter, v_nfond, v_aksjer | Vanguard N-PX, filtrert på `innsendt < D`. Innsendt er 2024-08, 2025-08 og 2026-08. Alle 136 456 rader har innsendt etter sitt eget møte, så samme møte kan aldri komme med. Test (møter 07.2025–06.2026) ser bare N-PX 2024 og 2025, val (07.2024–06.2025) bare N-PX 2024. `mgmt_felt_LEKKER` brukes ikke. | ok |
| t_* (merger, golden ...), t_len, us, skatteparadis, mnd | Forslagsteksten og ISIN fra innkallingen, møtemåned | ok |
| s_lonn, s_lonnvekst, s_cap, s_cap_andel, s_tsr, s_tsr1aar, s_tsr_peer, s_lonn_vs_storr (PvP fra proxy) | Regnskapsår-slutt e1 < D−20 d. Innkallingen med PvP for året som endte e1 kommer tidligst ~60 d etter e1, og minst ~30–40 d før møtet, så sikker grense er ~D−100 d. | **svak lekkasje**: e1 ligger < 100 d før møtet i 11 testrader og 10 valrader, men bare 1 rad per sett har PvP-tall der. Resten er gaap-ender. |
| g_sbc, g_sbc_vs_float, g_tap (10-K: aksjelønn, resultat) | Samme e1 < D−20 d. 10-K kommer 60–90 d etter regnskapsår-slutt. | **svak lekkasje**, de samme ~11 radene |
| s_float (EntityPublicFloat) | Float-dato < D−60 d. Floaten står i 10-K, som kommer ~8–9 mnd etter float-datoen (midt i regnskapsåret). | **lekker**: float-dato < 270 d før møtet i 21 testrader og 33 valrader |
| s_mangler | Navnematch mot SEC | ok |

Felles forbehold for alle SEC-kjennetegn: frames-API-et gir verdien fra siste innsending (accn fra 2026), ikke fra første publisering. PvP-tall for tidligere år gjentas i senere innkallinger, og omarbeidede tall er sjeldne. Jeg regner det som lite, men ikke null, og har ikke målt det.

## F1 med rettet etterslep
Rettet kopi: `arbeid/oppgave_1985/train_v3_rettet.py`. Endringen er PvP/gaap e1 < D−100 d og float < D−270 d. Ellers er koden identisk. Én seed, fasit via `hack/c1/maaler.py`.

| Kjøring | Val 2025 F1 | Test 2026 F1 |
|---|---|---|
| original, andel-mot 1,25 (KORT.md-tallet) | 0,4175 | 0,5092 |
| rettet, andel-mot 1,25 | 0,4096 | 0,5111 |
| original, standardgrense | 0,3591 | 0,4455 |
| rettet, standardgrense | 0,3716 | 0,4914 |
| PR-AUC rettet (val / test) | 0,315 | 0,465 |

**Konklusjon:** lekkasjen er reell, men liten. Den forklarer ikke at modellen slår gulvet, og tallene står seg innenfor støyen. Den rettede versjonen bør likevel brukes i leveransen, så vi kan si «alt er kjent før møtet» uten forbehold.

## Andre funn (metode, ikke datalekkasje)
- Standardgrensen er ustabil: en liten endring i kjennetegnene flytter test-F1 fra 0,446 til 0,491. Grensen fra kalibreringsbiten er støyete, og bootstrap (#1986) bør dekke dette.
- Faktoren 1,25 × basisrate: jeg har ikke sett hvor den ble valgt. Ble den valgt på test, er 0,509 optimistisk. Den må velges på val og bare rapporteres på test.

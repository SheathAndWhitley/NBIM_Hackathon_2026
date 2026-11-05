# Case 1: kaldstart på den frosne pakka etter frys kl. 16 (#2285)

Kjørt av smed3 kl. 16:01 den 05.11.2026, git 14dcbec. Logg: `arbeid/oppgave_2285/kaldstart_etter_frys.log`.

## Resultat
- Frys: `state/c1_frys.json` skrevet kl. 16:00:01 av LaunchAgent (17 filer, modell #2044 miks h2).
- `bash arbeid/hack/c1/kaldstart.sh` (BEHOLD=1): **utgang 0, GRØNN**, 91 s fra tom tmp-mappe til tall.
  Frysvakt GRØNN, uv sync --frozen (lightgbm 4.7.0, sklearn 1.9.1, pandas 3.1.1), agent kjørt, måler v3.
- **F1 MOT test 2026 = 0,476190** (TP 30 FP 38 FN 28, 58 i fasit) på både `_pred_uten_ruting.csv` og `pred_maaler.csv`. REF 0,476190, avvik 0.
- Agenten: 1578 saker, 74 avvik fra styret (71 MOT, alle med NBIM-sitat), 188 til menneske (11,9 %).

## Sha-tabell: frys-sha mot landsbyen og mot kald kopi
| fil | frys-sha[:12] | landsby | kald kopi |
|---|---|---|---|
| arbeid/oppgave_2044/train.py | 772fb71500e3 | LIK | LIK |
| arbeid/oppgave_2044/pred_miks_h2.csv | 40afcc3e2fec | LIK | ikke kopiert* |
| arbeid/oppgave_2103/full_test.csv | 69702192d3a4 | LIK | ikke kopiert* |
| arbeid/hack/levering/kjor_agent.py | dedc94062cf4 | LIK | LIK |
| arbeid/hack/levering/c1_real.py | 439b49f74836 | LIK | LIK |
| arbeid/hack/levering/injeksjon_hoflig.py | 51cd0698342c | LIK | LIK |
| arbeid/hack/levering/kjor_agent_real_maskin_alene.csv | 22ac6717e128 | LIK | ikke kopiert* |
| arbeid/oppgave_2047/vern.py | 19c3629fa670 | LIK | LIK |
| arbeid/oppgave_2046/case1_mot.py | d403dd3c8f3b | LIK | LIK |
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba | LIK | LIK |
| arbeid/hack/levering/retningslinje_oppslag.py | 0a45c013471b | LIK | LIK |
| arbeid/hack/c1/retningslinjer/punkter.jsonl | 089ddbddb839 | LIK | LIK |
| arbeid/hack/c1/data_off/real_test_input.csv | 1e0e22f86bbf | LIK | LIK |
| arbeid/hack/c1/maaler_offisiell_v2.py | 1111f1afce04 | LIK | LIK |
| arbeid/hack/c1/maaler_offisiell_v3.py | 418a937e57e5 | LIK | LIK |
| arbeid/kandidater/smed2_c1_mot/pyproject.toml | 96fcf3b1c108 | LIK | LIK |
| arbeid/kandidater/smed2_c1_mot/uv.lock | ed54fd6c8f92 | LIK | LIK |

17 av 17 like i landsbyen. 14 av 14 kopierte like i kald kopi.
\* De tre prediksjonsfilene kopieres ikke av kaldstart.sh med vilje: de skal lages på nytt fra kald start. Derfor gir `c1_frys.py sjekk --rot <kopi>` RØD (MANGLER) på kopien; det er ventet, ikke et avvik.

## Prediksjonene fra kald start mot de frosne
| kald utdata | sha[:12] | frossen fil | sha[:12] | |
|---|---|---|---|---|
| ut/_pred_uten_ruting.csv | 22ac6717e128 | levering/kjor_agent_real_maskin_alene.csv | 22ac6717e128 | **bit-lik** |
| ut/pred_maaler.csv | b113b545dd86 | levering/kjor_agent_real_pred_maaler.csv | b113b545dd86 | **bit-lik** |
| ut/_pred_uten_ruting.csv | 22ac6717e128 | oppgave_2103/full_test.csv | 69702192d3a4 | ulik sha, samme innhold |

full_test.csv (#2103) har 3 kolonner og p_avvik med full presisjon; kaldstartens fil har 4 kolonner (konfidens i tillegg) og p_avvik rundet til 5 desimaler. 1578 av 1578 id felles, 0 ulike anbefalinger, maks |Δp_avvik| 5e-6 (ren avrunding). v3 gir 0,476190 på begge.

## Konklusjon
Den frosne pakka reproduserer hovedtallet 0,476190 fra kald start, med bit-like prediksjoner. Ingen avvik å melde.
Kopien står i /tmp/c1_kald.UdVwk6 (BEHOLD=1) til neste omstart; KJORING.txt kopiert til arbeid/oppgave_2285/.

# Case 1 (#2673): dom over usikkerhetssetningen om 0,512 — dommer, 05.11 17:46

**GODKJENT** — hvert tall i setningen (JURY.md pkt. 2, linje 72; ERLIG_EVALUERING.md § 3, linje 33, commit 530ffd7) er gjenskapt av meg fra prediksjonsfilene i `arbeid/oppgave_2612/kjor/` (byte-like pakkens, jf. #2612) med pakkens egne skript. Ingen tall i setningen mangler kilde i målingene.

| påstand i setningen | min kjøring | kilde | stemmer |
|---|---|---|---|
| 0,512, 58 MOT, TP 32 FP 35 FN 26 | 0,5120, TP 32 FP 35 FN 26, n 1539 | ki_mot.py på pakke_repo4_test.csv; c1_tallsjekk_repo4.md | ja |
| 95 % KI [0,40; 0,62], klyngebootstrap per selskap, 2000 trekk | [0,400; 0,621], 135 selskaper, 2000 trekk seed 0 | kilder/oppgave_2095_ki_mot.py | ja |
| tre testår 0,506–0,531 | 2024 0,5057 / 2025 0,5309 / 2026 0,5120 | ki_repo4.py per år; #2612-kontrollen | ja |
| eldre frossen 0,476 | 0,4762 (TP 30 FP 38 FN 28) | ki_mot.py på pakke_frossen_test.csv | ja |
| gevinst +0,036 [−0,008; +0,085] | +0,0358 [−0,008; +0,085], 17 ulike prediksjoner | oppgave_2103/diff_ki.py (parret klyngebootstrap) | ja |
| «like over målet 0,5, innenfor støy» | 0,512 > 0,5; KI dekker 0,5 og diff-KI dekker 0 | følger av radene over | ja |
| (JURY-kilder) val 2025 0,530 [0,417; 0,638] | 0,5301 [0,417; 0,638] | ki_mot.py val | ja |
| (JURY-kilder) seed 0,462–0,522 på eldre frossen, 5 seed | min 0,4615 / maks 0,5217 | kilder/c1_seed_frossen.md | ja |
| (JURY-kilder) bootstrap over rader [0,397; 0,616] | [0,396; 0,609] (seed 0), [0,400; 0,611] (seed 2) | arbeid/oppgave_2592/nye_tall.md; egen `arbeid/oppgave_2673/rad_boot.py` | ja, innenfor bootstrap-støy (øvre grense 0,005–0,007 lavere hos meg; sidetall, ikke i selve setningen) |

Merknader (ingen krever retting):
- «de tre testårene gir 0,506–0,531» er riktig som spenn, men 2026-tallet 0,512 er det leverte; § 7-tabellen sier det. Greit.
- Setningen tar forbehold som er sanne: KI-et [0,40; 0,62] dekker både målet 0,5 og den eldre frosne 0,476, og diff-KI-et dekker 0. «Innenfor støy» er dermed en ærlig formulering, ikke pynt.
- Setningen står uendret i begge filer per 17:46 (git status ren for leveranse/).

Gjenskap: `python3 -I arbeid/hack/c1/leveranse/kilder/oppgave_2095_ki_mot.py arbeid/oppgave_2612/kjor/pakke_repo4_test.csv test` og `python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2612/kjor/pakke_frossen_test.csv arbeid/oppgave_2612/kjor/pakke_repo4_test.csv test` (under 10 s til sammen).

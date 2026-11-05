# Case 1: tre tiltak fra bomanalysen, målt på val 2025 før modellfrys kl. 16 (arkitekt, #2072)

Grunnlag: `c1_feilanalyse_mot.md` (#2067). smed2s modell #2044 på val 2025: F1-MOT 0,5217, tp 48, fp 33, fn 55.
KP: forventet 0,5217, fikk 0,5217 (`arbeid/oppgave_2067/proto2.py`). Grensen er valgt på val, så alle løft er litt optimistiske. Test 2026 er ikke rørt.

| # | tiltak | type | retter bomgruppe | målt på val | forventet F1-MOT på val | kost | smed | før 16? |
|---|---|---|---|---|---|---|---|---|
| 1 | `duality`-trekk: regex styreleder + daglig leder/whole-time/CEO i samme person, inn i LR og LGBM i `train.py` | trekk | India (0/14), styrevalg | etterregel +0,1 på p: 0,5217 → 0,5543 (val n 4–5, alle MOT; train n 8, MOT-rate 0,375 mot 0,058) | **+0,02 til +0,03** (bred usikkerhet, n lite) | 25 min (bygg, velg grense på val, test én gang) | smed2 | ja |
| 2 | Ruting: alle forslag i **India** går til et menneske, i tillegg til dagens 10 %-ruting | ruting | India (14 av 55 fn) | 137 rader (7 %), MOT-rate 0,102 mot 0,054 snitt; fanger 14/55 fn | 0 (ruting endrer ikke F1, men øker MOT-funn hos mennesket) | 15 min (én regel i rutingen + grunn i svaret) | smed2 (sammen med #2057) | ja |
| 3 | Klyngesignal på styrenivå (hele styret straffes i ett møte, f.eks. Fluence 8 MOT, 0 truffet) | — | styrevalg-klynger (12 fn i 2 møter) | møte-maks/møtesnitt av p: 0,52 → 0,28–0,40 (forkastet i #2067) | negativ med p alene; trenger fakta om uavhengighet som ikke finnes i real_votes | > 2 timer + nye data | — | **nei: svakhet til juryen** |

## Strøket med tall
- «non-independent» i teksten: train n 104, MOT-rate 0,067 (≈ snitt 0,058); val 22 rader, 0 MOT. Løft gir 0,52 → 0,48. Ikke bygg.
- «executive/whole-time director»: train-rate 0,055 (under snitt). Val +0,01 ved ett løft, ellers ned. Ikke bygg, det er støy.
- Statseid/nominee i teksten: train n 2. For lite.
- Ruting av «selskap med bare FOR før»: 604 rader, MOT-rate 0,012 (under snitt), fanger 7 fn. Ruting er dårligere enn tilfeldig der. **Svakhet til juryen**: uten fakta utenfra kan ingen modell finne første MOT i et selskap med ren FOR-historikk.
- Styrevalg i møter der modellen alt flagget noe: 270 rader, MOT-rate 0,056, fanger 15 fn. Ikke bedre enn snitt, så ingen ruting.

## Plan for smed2 (rekkefølge)
1. Tiltak 1 i `train.py` (binær `duality` i begge modeller), grense på val, test én gang. Rapporter val og test ærlig, også om test faller.
2. Tiltak 2 i rutingen (#2057): `country == India` → menneske, grunn «MOT-rate i India doblet i 2025 (0,046 → 0,102), modellen fanget 0 av 14 på val». Mål andel rutede saker og MOT-funn blant dem på val.
3. Speider/JURY.md (#1975): tiltak 3 og «bare FOR før» står som kjente svakheter, med tallene over.

Kode: `arbeid/oppgave_2067/proto2.py` (kjør med `uv run --project ../oppgave_2023 python proto2.py ../../state/opplastet/20261105_114241_real_votes.csv`).

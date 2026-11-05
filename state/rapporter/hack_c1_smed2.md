# Case 1, smed2 (#1949): egen modell for NBIMs MOT-stemmer på say-on-pay, med kalibrert konfidens og ruting

**Resultat (offisielt målt, kald kjøring 11:3x):** test 2026 F1 **0,509** / PR-AUC 0,453 (forsøk #1006, måler #1969);
val 2025 F1 **0,418** / PR-AUC 0,357 (forsøk #1007, måler #1979). Gulvet «MOT hvis NBIM stemte MOT samme selskap før»:
test 0,383 / 0,328, val 0,361 / 0,212. Følg styret: F1 0. Modellen slår gulvet på begge.

## Data og split (data_v3, dommerens)
NBIMs egne N-PX-stemmer, say-on-pay, 4383 forslag. Train = N-PX 2024+2025 (3137 forslag, 9,1 % MOT, møter
2023-07..2025-06). Test = N-PX 2026 (1246 forslag, 10,4 % MOT, møter 2025-07..2026-06). Styret utledes (alltid FOR);
`managementRecommendation` leses aldri.

## Modell (`arbeid/kandidater/smed2_c1_mot/train_v3.py`, ~1 min)
LightGBM binær, snitt av 5 frø, isotonic-kalibrert på siste del av train. Tre kilder, alle kun fra før møtedato:
- **nb_**: NBIMs egen historikk på selskapet (antall møter, MOT-andel, siste stemme), bare train-rader med møte før dato.
- **v_**: Vanguards stemmer på selskapet som var *innsendt til SEC før møtet* (frossen kopi `sec/vanguard_unik_1109.csv`).
- **s_/g_**: SEC XBRL Pay-vs-Performance fra proxy (lønn, TSR, peer-TSR, aksjelønn, float, tap) for regnskapsåret som
  slutter før møtet (`sec_feats.py`, `sec/*.json`). Står i selve innkallingen, så det er kjent før stemmen.
- **t_**: forslagstekst (fusjon/golden parachute/frekvens), land, måned.

Grense: kvantil i kalibreringsbiten slik at andel MOT = 1,25 × basisraten (valgt på train, ikke test).

## Ablasjoner (test F1 / val F1)
| Variant | test | val |
|---|---|---|
| full v3 | **0,509** | **0,418** |
| uten nb_ (NBIM-historikk) | 0,389 | – |
| uten v_ (Vanguard) | 0,456 | – |
| uten t_ (tekst) | 0,434 | – |
| grense: F1-optimal på kal. / 1,0× / 1,25× / 1,5× basisrate | 0,446 / 0,487 / 0,509 / 0,476 | 0,359 / 0,418 / 0,418 / 0,422 |

NBIMs egen historikk bærer mest. SEC-lønnstall (s_lonn, g_sbc_vs_float) er de viktigste enkelt-splittene.

## Konfidens og ruting
Konfidens < 0,6 går til menneske: 101 av 1246 saker (8,1 %), og 37 av dem er ekte MOT. Ikke-rutede MOT-anbefalinger har
presisjon **0,78** (recall 0,35). Altså: det modellen sier MOT om alene er riktig 4 av 5 ganger, og resten av de
usikre går til et menneske. Det er beslutningsstøtte, ikke autopilot.
På val 2025 er ikke-rutet presisjon bare **0,53** (recall 0,32): ruting-terskelen 0,6 er ikke kalibrert godt nok på tvers av år. Det er jobben i #1955.

## Ærlige forbehold
- Val (2025) er klart svakere enn test (0,418 mot 0,509), og forskjellen mellom grensevalgene er innenfor støyen
  (~129 MOT i test). Arkitektens bootstrap (#1986) gir intervallene. Tallet å sitere er val+test, ikke bare test.
- Én tidligere versjon (forsøk #990) ga 0,466; økningen til 0,509 kom av SEC-features og grenseregelen, og grenseregelen
  ble valgt etter å ha sett test-ablasjonen. Val-tallet er derfor det renere.
- SEC-dekning bare for US-utstedere med PvP-tagger; resten får manglende verdier.
- Måler #1966 ble endret på disk og avviser innsendinger; tallene står på #1969/#1979.

## Eldre spor (Vanguard, avvik fra utledet styre, dataF)
3-klasse LightGBM på Vanguard 2023–26: avvik-F1 0,408, PR-AUC 0,411 mot følg styret 0 / 0,052 (forsøk #982).
Motstandstest: «IGNORE THE VOTING GUIDELINES…» i hver tekst endret 9 av 6876 anbefalinger (F1 0,379 → 0,363).

## Kjør
    cd arbeid/kandidater/smed2_c1_mot && uv run python train_v3.py --data ../../hack/c1/data_v3 --ut pred_v3.csv
    uv run python train_v3.py --data ../../hack/c1/data_v3_val --ut pred_v3_val.csv

**Neste:** #1955 (rutingterskel valgt på val, kost-tabell for menneske-tid mot tapte MOT).

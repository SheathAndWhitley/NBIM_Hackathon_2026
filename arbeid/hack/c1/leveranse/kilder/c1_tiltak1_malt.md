# Tiltak 1 (styrevalg-historikk forfaller) målt: +0,031 på val 2025, men −0,015 på holdt-ut 2024. Ikke bygg det inn.

Oppgave sak 2283. Pakka, frossen sak 2044, miks h2 og test 2026 er ikke rørt. Ingen test-2026-prediksjon er laget.

## Hva er bygd
`arbeid/oppgave_2283/train_t1.py` er en kopi av `arbeid/oppgave_2044/train.py` (miks, `--hist 2`, samme C-rutenett
og samme valg av grense på val). Testdelen er fjernet. `--t1 1` legger til 15 trekk, bare på DIRECTOR_ELECTION, og
bare fra år **før** radens år (aldri årets etiketter eller begrunnelser):
- forfalt MOT-andel på styrevalg i selskapet, vekt exp(−(år siden−1)/τ), år siden siste MOT, MOT-andel siste sesong,
  «MOT før, men bare FOR siste sesong»
- samme person (navnenøkkel fra sak 2044): sett før, siste stemme MOT, år siden siste MOT, «MOT før, FOR sist»
- forfalt MOT-andel per `rationale_section` fra tidligere år (GVG 1.1, 1.2, 1.3, 2.1, 2.3, 3.1, 3.2)

## Tall (måler v3 `maaler_offisiell_v3.py val --data real --score mot`, sha256 418a937e…)

| oppsett | val 2025 F1 MOT (v3) | P styrevalg | TP styrevalg | holdt-ut 2024 F1 (intern) |
|---|---:|---:|---:|---:|
| grunnlinje (t1=0, samme kjøring) | **0,520231** (= smed3 sak 2274, KP: forventet 0,520231, fikk 0,520231) | 0,56 | 28 | 0,5672 |
| t1, τ=1 (standardverdi, satt før kjøring) | **0,550898** | 0,63 | 29 | 0,5524 |
| t1, τ=0,5 (beste av 3 τ, valgt på val) | 0,555556 | 0,65 | 28 | 0,5524 |
| t1, τ=2 | 0,538922 | 0,64 | 28 | – |

Parvis klyngebootstrap over møter (2000 trekk, `boot.py`), τ=1 minus grunnlinje:
- val 2025: +0,026 (intern F1), 95 % KI [−0,013, 0,070], P(bedre) 0,89
- 2024: −0,015, 95 % KI [−0,043, 0,017], P(bedre) 0,19. PR-AUC faller 0,591 → 0,565.

Akseptkravet fra NESTE_VERSJON.md er nådd på val 2025: F1 > 0,520, presisjon på styrevalg 0,56 → 0,63, TP på
styrevalg 28 → 29. Men på 2024, som er et uavhengig år, gjør tiltaket det **verre**. Det samme mønsteret (bedre
ett år, verre et annet) har vi allerede sett med USA-ruting. Gevinsten følger året, ikke mekanismen.
Papirtaket var 0,596; målt er 0,551, og det holder ikke over to år.

## Anbefaling
Ikke bygg inn. Ikke rør test 2026 for å avgjøre det. Til juryen er dette et ærlig funn: et tiltak som klarer
akseptkravet på val og likevel stryker på kryssjekk mot 2024. Vil noen prøve videre: mål hver ny variant på
både 2024 og 2025 før valg. Trekkene for samme person (4–7) er den enkleste kandidaten for en ablasjon.

## Kommandoer
```
bash arbeid/oppgave_2283/kjor.sh 1 1        # val 2025, skriver val_t11_tau1.csv + v3-SCORE
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2283/train_t1.py \
  state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --t1 1 --tau 1 --vaar 2024 --ut /tmp/x.csv
uv run --project arbeid/kandidater/smed2_c1_mot python -I arbeid/oppgave_2283/boot.py 2025 \
  arbeid/oppgave_2283/val_t10_tau1.csv arbeid/oppgave_2283/val_t11_tau1.csv
```
Forsøk på tavla: sak 1151 (τ=1, 0,550898), sak 1152 (τ=0,5, 0,555556), sak 1153 (2024, 0,5524). Alle er selvrapportert
med v3-kommandoen i notatet. Automåling er slått av, så de ikke blir målt mot test.

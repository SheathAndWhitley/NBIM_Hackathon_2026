# Case 1, tiltak 3: India som egen gruppe, målt på 2025 og 2024 (#2294)

Oppsett: kopi av #2283 `train_t1.py` (miks, --hist 2, --t1 0) med nytt flagg `--india`, i
`arbeid/oppgave_2294/`. 2025 = val (trent <2025, v3-måler `--score mot`). 2024 = holdt-ut (trent <2024,
intern F1, samme kode). C og grense velges på året som måles, likt for grunnlinje og variant.
KI = parvis klyngebootstrap over møter (`boot.py`, 2000 trekk). Test 2026 og frossen #2044 er ikke rørt.

Grunnlinja er reprodusert: india=0 gir v3 **0,520231** (2025) og **0,5672** (2024).

| variant | val 2025 (v3) | Δ 2025, 95 % KI | 2024 | Δ 2024, 95 % KI | India-MOT funnet 2025 / 2024 | bedre begge år? |
|---|---|---|---|---|---|---|
| 0 grunnlinje | 0,520231 | – | 0,5672 | – | 0/14 / 1/5 | – |
| 1 land×type-gruppe (India\|type som kategori) | 0,525000 | +0,007 [−0,031, 0,043] | 0,5535 | −0,014 [−0,106, 0,076] | 0/14 / 0/5 | nei |
| 2 = 1 + India-trekk (India, leder+daglig leder samlet, India×styrevalg, India×OTHER_MGMT) | 0,517241 | −0,0005 [−0,031, 0,026] | 0,5595 | −0,008 [−0,089, 0,073] | 0/14 / 0/5 | nei |
| 3 bare India-trekkene | 0,520231 | 0,000 [−0,027, 0,027] | 0,5590 | −0,008 [−0,053, 0,034] | 1/14 / 1/5 | nei |
| R regel: India og «chairman» + MD/whole-time/CEO i teksten → MOT, oppå grunnlinja | 0,561798 | +0,039 [0,008, 0,080] | 0,5743 | +0,007 [0,000, 0,024] | 5/14 / 1/5 | ja, men se under |

Funn:
- Modellvariantene (1–3) finner nesten ingen India-MOT, 0–1 av 14. Endringene i F1 kommer fra at C og
  grense flytter seg, ikke fra India. Grunnen er at India hadde få MOT før 2025: 1–5 per år, 3–5 %,
  mot 14 av 137 (10 %) i 2025. Mønsteret skiftet i 2025, og det finnes for lite treningsdata til å lære det.
- Regel R er funnet ved å lese de 14 val-sakene, så +0,039 på 2025 er tilpasset og optimistisk. Det
  ærlige beviset er 2024: regelen traff 1 sak, og den var riktig (+0,007). Før 2025 var mønsteret MOT i 3
  av 8 saker. Det er over F1/2 ≈ 0,27, grensen der et ekstra flagg i snitt øker F1. Det er altså et
  forsvarlig argument, men bygd på 8 saker. Mønsteret er GVG 1.2 (styreleder og daglig leder i samme person).

Anbefaling: **ikke bygg** før frysen. Modellvariantene 1–3 er forkastet, fordi ingen er bedre begge år.
Regel R oppfyller formelt kravet om å være bedre begge år, men 2025 er funnet på val og 2024 er én
sak. Den føres som kandidat for neste versjon og må prøves på ferske data (sesongen etter 2026) før den
tas i bruk. Den skal ikke prøves på test 2026 nå.

Kommandoer: `bash arbeid/oppgave_2294/kjor.sh <0|1|2|3> <2025|2024>`; `python3 -I arbeid/oppgave_2294/regel.py <år>`;
`python3 -I arbeid/oppgave_2294/boot.py <år> pred_i0_<år>.csv pred_i<v>_<år>.csv` (kjøres fra mappa).

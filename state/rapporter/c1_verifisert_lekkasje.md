# Dommer2 #2107: lekkasje-ablasjonen (uten sakstype) BEKREFTET fra kald kopi; hovedtall rettet, rutingtall avviker fortsatt

## 1. Ablasjon uten sakstype, kald kopi
Kopi til `/tmp/kald2107`: bare `abl.py` (sha1 3504cb68, = oppgave_2089/2103), real_votes (sha1 f0d5db21, lik opplastet),
låst miljø fra `oppgave_2023` (`uv sync`), kjørt under `env -i`. Måler `maaler_offisiell_v3.py --data real --score mot` (sha256 8b09c36e01).

| Variant | Val 2025 F1 MOT (P/R) | Test 2026 F1 MOT (P/R) | TP/FP/FN test |
|---|---|---|---|
| Full (frosset, smed2s fil) | 0,5202 (0,61/0,45) | **0,4762** (0,44/0,52) | 30/38/28 |
| Uten sakstype, dommer kald | 0,5089 (0,61/0,43) | **0,5000** (0,50/0,50) | 29/29/29 |
| Smed2 #2103 rapporterer | 0,509 / 0,520 | 0,500 / 0,476 | samme |

- Kalde svarfiler (val og test) er **byte-like** med `arbeid/oppgave_2103/` og `oppgave_2089/`. Koden er deterministisk.
- Parret bootstrap (smed2s `diff_ki.py` på min kalde fil): test +0,024 [−0,012; +0,062], 14 ulike prediksjoner av 1539. Stemmer med rapporten.
- **Dom: bekreftet.** Sakstypen lekker ikke fasit: uten feltet faller val med 0,011 og test stiger 0,024, begge KI krysser 0.
  Riktig at modellen ikke byttes (val velger full). Forbudte kolonner er assert-sjekket i koden og ble ikke lest.

## 2. Grep etter gamle hovedtall i `arbeid/hack/levering` og `c1/leveranse`
Hovedtallet 0,476 [0,36; 0,59] på MOT står riktig i README, METODE, JURYSVAR, KRAVRESPONS, ERLIG_EVALUERING og JURY.
Alle gjenværende 0,4818/0,482 er merket som *avvik*-F1, og 0,474/0,383 er merket N-PX/ikke hovedtall. Ingen gamle tall står som hovedtall.

**Avvik (sendt tilbake på tavla):** rutingtallet er ikke likt i pakken.
- `levering/README.md` l.28: 228 saker (14,4 %) (#2094, kald kopi).
- `levering/KRAVRESPONS.md` l.13 og l.61: 176 av 1578 (11,2 %), 171 av 1539 (11,1 %).
- `levering/kjor_agent_real_test2026_LES.md` l.10: 176 / 171 (11,1 %).
- `c1_tall_likt.md` (#2095) har 176/1578. Ett tall må velges ved frys og stå overalt. 228/1578 = 14,45 %: «14,4» og «14,5» brukes om hverandre.
Mindre: `KRAVRESPONS.md` rad 7 sier fortsatt «HULL H2: virker ikke fra kald kopi», men #2094 lukket H2.
`c1/leveranse/JURY.md` l.24 («slår ingen modell en ettlinjes regel, 0,383») gjelder N-PX og er merket øverst i fila; skrives om i #1975.
Forslag: ERLIG_EVALUERING kan få ablasjonsraden på MOT (0,476 → 0,500 uten sakstype) fra denne rapporten.

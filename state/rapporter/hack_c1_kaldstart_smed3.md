# Case 1: kaldstart for selskaper uten historikk (smed3, #2065)

**Form:** en selskapsblind logistisk regresjon. Trekkene er hashede ord og bigram fra forslagsteksten (tall normalisert),
type, land, marked, proponent, type×land, type×marked og møteaggregat (antall saker, antall styrevalg, hvilke typer
møtet har, om det har aksjonærforslag). Ingen company_id. Variant B legger til et eget historikktrekk (glattet MOT-rate,
antall tidligere saker, ny-flagg). C=1 og grensen er valgt på VAL 2025 (trent ≤2024). Test 2026 er trent ≤2025 med samme p-grense.
Kode: `arbeid/hack/varianter/smed3_utf_kald/kald.py`.

| variant | VAL25 | TEST26 helhet | TEST26 uten hist | TEST26 med hist |
|---|---|---|---|---|
| A selskapsblind (#1044) | 0,508 | **0,471** | 0,364 (2 av 8 MOT, 1 FP) | 0,480 |
| B + historikktrekk (#1045) | 0,511 | **0,500** | 0,615 (4 av 8, 1 FP) | 0,488 |

Alle tall er fra dommerens måler (`maaler.sh … real_test`), F1 på avvik fra styret.

**Viktigst:**
1. Delmengden uten historikk er bitteliten: 69 forslag, 8 MOT og 7 selskaper i test, og 98 forslag med 3 MOT i VAL.
   95 %-KI fra bootstrap over selskaper er 0–0,55 for A og 0–0,91 for B. Den kan ikke rangere metoder,
   og en grense kan ikke velges på 3 MOT. Derfor er grensen valgt på hele VAL.
2. A ser aldri historikk, men faller likevel fra 0,48 (med hist) til 0,36 (uten hist). Det er samme fall som
   0,48 → 0,37 i oppgaven. Fallet forklares altså av hvilke selskaper delmengden består av (Vietnam, Canada, Japan, få MOT),
   ikke av at historikken mangler.
3. En selskapsblind modell gir 0,471 på helheten, nesten like mye som modeller med historikk. Historikken legger til omtrent 0,03.
   Til beslutningsstøtte betyr det at nye selskaper kan få samme modell. Usikkerheten for dem bør likevel rutes til menneske,
   fordi tallet ikke kan bekreftes på så få saker.

Ikke gjort (tidsboks): kNN-likhet mellom selskaper og en egen grense for nye selskaper. Det siste er umulig å velge ærlig med 3 MOT i VAL.

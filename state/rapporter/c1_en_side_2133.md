# Case 1: én side for juryen skrevet (#2133)

- Ny fil: `arbeid/hack/levering/EN_SIDE.md` (37 linjer): hva agenten gjør, metode (tidssplitt val 2025/test 2026, ingen lekkasje, følg styret F1 MOT 0), hovedtall, ruting til menneske, tre begrensninger.
- Tall kjørt på nytt med `maaler_offisiell_v3.py ... test --data real --score mot`: TP 30 FP 38 FN 28, P 0,4412 R 0,5172 F1 0,4762, 58 MOT. Stemmer med `c1_tallkonsistens.md` (KI [0,36; 0,59], avvik 0,4818 som sidetall).
- Rutingtallet 228 av 1578 (14,4 %) er hentet fra README (kald kjøring #2094), ikke fra c1_tallkonsistens.
- Lenket fra `levering/README.md` linje 9.

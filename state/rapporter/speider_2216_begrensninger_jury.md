# Case 1: Begrensninger-seksjon lagt i JURY.md (#2216)

Seksjonen «Begrensninger: hva agenten ikke kan» (10 punkter) står øverst i `arbeid/hack/c1/leveranse/JURY.md`.

Verifisert selv med måler v3 på kald kjøring `/tmp/c1_kald/ut/_pred_uten_ruting.csv` (05.11 12:29):
`MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762 (58 i fasit)`, SCORE avvik 0.481752.

Egen telling (`arbeid/oppgave_2216/tell.py`, agent.csv + data.csv):
- 18 aksjonærforslag av 1578 saker i test 2026; 56 av 58 MOT er på styrets forslag.
- Ikke-rutede MOT-flagg: 22 av 32 riktige (P 0,69). 31 av 41 flagg som ikke er MOT går til menneske.
- Ruting: 228 av 1578 (14,4 %): 175 nær grensen, 52 ukjent selskap, 1 injeksjon.

Avvik funnet: `BEGRENSNINGER.md` sier 188 av 1578 (11,9 %) til menneske. Siste kalde kjøring gir 228 (14,4 %), trolig etter vaktene i #2152. Bør rettes i #1975 etter frysen.

# Case 1 (#2530): jurysvar 19 «Hvorfor leverer dere ikke den beste varianten?»

Skrevet som svar 19 i `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` (5 linjer). Det kom ingen nye tall.
- Hovedtallet 0,476 er valgt uten å se test. V2 (0,516 på test, 0,548 på val) og repo-hybriden (0,545) er målt etter frysen. V2 mot frossen er +0,040 [−0,007; +0,095], med 58 MOT og KI ca. ±0,1.
- Å velge det beste av flere testblikk blåser opp tallet. t4e ga 0,529 på test, men tapte på val med 0,468 mot 0,522.
- I drift: den frosne agenten. V2 er neste versjon når den vinner på rullerende val 2022–2025. Hybriden kalles ikke NBIMs (ordre #262).
- Kilder: c1_hvorfor_ikke_bedre.md, c1_hybrid_pluss_rangering.md, NESTE_VERSJON.md:35-36, 89-96, 100-102.
- Tallvakt: 169 påstander, 0 avvik.
- Beslutningslinja er hentet fra dom #2529 (se under).

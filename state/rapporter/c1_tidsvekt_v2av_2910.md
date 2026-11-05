# Case 1 #2910: tidsvekt på v2+av gir IKKE bedre treff (målt, 3 frø, 4 år)

Regel skrevet før måling: arbeid/hack/varianter/smed3_utf_tidsvekt/REGEL.md (hovedkandidat tau=3 låst der).
Kode: v2tv_rull.py = pakkas v2_rull.py + radvekt w = 0.5^((siste treningsår - year)/tau) i LR og LGBM,
+ av_regel.py etterpå. tau=0 er byte-likt v2+av. Frø = LGBM random_state 0/1/2. kjor.sh T TAU SEED.

F1 MOT, snitt over 3 frø [min-maks]:

| tau | 2023 vakt | 2024 | 2025 | 2026 | snitt 24-26 (dårligste frø) |
|---|---|---|---|---|---|
| 0 (= v2+av) | 0,3571 [0,3429-0,3676] | 0,5588 [0,5509-0,5714] | 0,5605 [0,5574-0,5667] | 0,5622 [0,5565-0,5714] | 0,5605 (0,5598) |
| 1,5 (ref) | 0,3317 [0,3158-0,3478] | 0,5867 [0,5765-0,6038] | 0,5234 [0,5198-0,5276] | 0,5437 [0,5323-0,5517] | 0,5513 (0,5438) |
| 3 (kandidat) | 0,3462 [0,3388-0,3523] | 0,5638 [0,5604-0,5665] | 0,5304 [0,5085-0,5532] | 0,5425 [0,5333-0,5517] | 0,5455 (0,5341) |

Frossen repo4 (#2713): 0,3350 / 0,5057 / 0,5309 / 0,5120, snitt 0,5162. v2+av fasit (#2890, frø None): 0,5731 / 0,5667 / 0,5391, snitt 0,5596.

Dom etter regelen:
- Mot frossen: kandidaten tau=3 består (snitt 0,5455 >= 0,5362, intet år under frossen -0,02). Men det gjør v2+av også, med mer.
- Mot v2+av (det som faktisk ligger til dom kl. 02): tau=3 taper, snitt -0,015 og 2025 -0,030. Kortere tau (1,5) taper mer
  på 2025/2026/2023 og vinner bare 2024. Tidsvekt forskyver treffet mellom år, den løfter ikke snittet. NEI, med tall.
- Anbefaling: ikke legg tidsvekt på v2+av. Ingen bytte fra meg.

Sidefunn, viktig for dommen kl. 02: frøstøyen i v2+av er ±0,01-0,02 per år. Fasit-tallet 2026 0,5391 (frø None)
ligger under hele frøspennet 0,5565-0,5714 for frø 0/1/2, og 2024-fasit 0,5731 ligger over spennet 0,5509-0,5714.
Snittet over 3 år er stabilt (0,5596 fasit mot 0,5605 frøsnitt), så v2+av-dommen tåler frøene, men enkeltår bør
ikke leses på fjerde desimal. 2023 som vakt-år for v2+av: 0,3571 (frossen 0,3350), så vakta holder.

Filer: resultat.txt (36 kjøringer), oppsummering.txt, ut/*_maal.txt (målerutskrift per kjøring), REGEL.md, KORT.md.

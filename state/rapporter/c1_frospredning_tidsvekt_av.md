# Case 1 #2920: frø-spredning for tidsvekt+v2+av (tau=3), 5 frø på 2023-2026

Underlag for natt-dommen 02:00 (#2874). Kandidat fra #2910: pakkas v2_rull.py + radvekt 0.5^((siste treningsår - year)/3)
i LR og LGBM + av_regel.py. Frø = LGBM random_state 0-4 (0-2 fra #2910, 3-4 kjørt nå). Samme måler
(maaler_aar.py, F1 MOT, --data real), k 32/64/48 for 2024/25/26, k=48 for vakt-år 2023. Regel: REGEL.md i variantmappa, skrevet før #2910-målingen.
Referanse tau=0 (= v2+av byte-likt) kjørt med de samme 5 frøene.

F1 MOT, 5 frø, snitt (sd) [min-maks]:

| år | tau=3 kandidat | tau=0 = v2+av | frossen repo4 |
|---|---|---|---|
| 2023 vakt | 0,3490 (0,0107) [0,3388-0,3656] | 0,3582 (0,0100) [0,3429-0,3676] | 0,3350 |
| 2024 | 0,5594 (0,0065) [0,5514-0,5665] | 0,5591 (0,0079) [0,5509-0,5714] | 0,5057 |
| 2025 | 0,5295 (0,0167) [0,5085-0,5532] | 0,5530 (0,0122) [0,5340-0,5667] | 0,5309 |
| 2026 | 0,5443 (0,0096) [0,5333-0,5565] | 0,5593 (0,0082) [0,5487-0,5714] | 0,5120 |
| snitt 24-26 | 0,5444 (sd 0,0088 over frø) min frø 0,5341 | 0,5571 (sd 0,0047) min frø 0,5519 | 0,5162 |

Verste år for kandidaten: 2025, snitt 0,5295 mot frossen 0,5309 (-0,0014). Verste frø i 2025 er 0,5085, det er
-0,0224 under frossen og bryter vakta på -0,02 for det ene frøet. Snittet bryter ikke.

Er gevinsten over frossen større enn frøstøyen?
- Kandidat tau=3: gevinst på snitt 24-26 er +0,0282. Frøstøy på snittet er sd 0,0088, spenn 0,5341-0,5564. Ja,
  gevinsten er ca. 3 sd og alle 5 frø ligger over frossen (0,5162). Men bare 4 av 5 frø klarer terskelen 0,5362
  (frø 0 gir 0,5341). Og gevinsten er null i 2025 (-0,0014, sd 0,0167): der er det bare støy.
- v2+av (tau=0): gevinst +0,0409, sd 0,0047, alle 5 frø over terskelen med minst 0,0157 margin, intet år under
  frossen i noe frø. Mer gevinst, halve frøstøyen.
- Kandidat mot v2+av, parvis på samme frø (snitt 24-26): -0,0127, sd 0,0093, negativ for alle 5 frø
  (-0,0258 / -0,0034 / -0,0157 / -0,0042 / -0,0146). 2025 taper i alle 5 frø (snitt -0,0235), 2026 taper i 4 av 5,
  2024 er likt (+0,0003). Tidsvekta er altså systematisk dårligere enn v2+av, ikke bare støy.

Dom etter regelen: tidsvekt+v2+av består bytteregelen mot frossen på snitt, men med tynn margin i verste frø og et
vakt-brudd i ett frø for 2025. Mot v2+av, som er det som faktisk ligger til dom kl. 02, taper den i alle frø. Anbefaling
uendret fra #2910: ikke legg tidsvekt på v2+av. v2+av står seg: 5 frø, sd 0,0047 på snittet, gevinst +0,0409 over frossen.

Filer: arbeid/hack/varianter/smed3_utf_tidsvekt/resultat.txt (52 kjøringer), resultat_2920_tau3.txt, resultat_2920_tau0.txt,
ut/v2tv_<år>_tau<tau>_s<frø>_maal.txt (målerutskrift per kjøring).

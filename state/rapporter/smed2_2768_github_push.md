# Case 1 #2768: lenkefikser og 'Til deg som ser over'-boks pushet til GitHub (nbim)

- #2764 (lenkesjekk) var lukket. Kjørte `PUSH=1 bash arbeid/verktoy/github_synk.sh` to ganger, begge med 0 funn i hemmelighetsskanningen (mønstre + portvakt c1_hemmelig_skann.sh).
- Første push: c66408c (lenkefiksene). Arkitekten (#2767) la boksen inn i både synk-kilden og direkte i repoen (37fed69); en annen synk ga 13c3b4a. Andre kjøring: ingen nye endringer, pushet.
- origin/main = **13c3b4a** (over 37fed69 og c66408c). `git show origin/main:README.md` inneholder 'Til deg som ser over'-boksen.
- Ingen fasitfil: ingen real_votes/real_test_input/real_val_input/pred_miks_h2 i `git ls-files`; alle 6 csv-er har bare id,anbefaling,(konfidens),p_avvik. `kilder/case1_hvilken_fasit.md` er et metodenotat, ikke data.
- NB: boksen heter «Til deg som ser over», ikke «Start her».

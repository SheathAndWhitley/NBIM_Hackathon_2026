# Case 1: tabell over målte tall for JURY.md (#2064)

Én kommando: `python3 -I arbeid/hack/c1/lag_tall_tabell.py` skriver `arbeid/hack/c1/tall_tabell.md` (3 s).
Hver rad er en prediksjonsfil som kjøres gjennom `maaler_offisiell_v2.py` på real_votes. P, R, F1 og PR-AUC leses fra målerens utskrift. Bootstrap-KI regnes i skriptet, og det stopper hvis punkt-F1 avviker fra målerens.

- Funn: før dette var bare grunnlinja målt på real_votes. Beste modell og ablasjonen var selvrapportert. Nå er de målt, og tallene stemmer med selvrapportene. KP: forventet 0,482, fikk 0,482. Alle 11 ablasjonsrader er like.
- Hovedtall TEST 2026 (66 MOT): følg styret 0,000, smed2 miks 0,482 [0,38, 0,58], smed3 sitatvariant 0,481 [0,37, 0,58] (VAL 0,512). Uten selskapshistorikk 0,372 [0,29, 0,46], uten all historikk 0,282.
- Konvertering: smedenes `rad,p,mot_pred` blir til `id,anbefaling` med modellens egen val-valgte beslutning (målerens rad,p-modus bruker fast 0,5). 39 testrader uten fasit, som smedene dropper, fylles som «ikke avvik». Måleren teller dem ikke, og skriptet sjekker at de mangler fasit.
- Hull: smed2 (#2044/#2045) lagrer ikke VAL-prediksjoner, så VAL står som «ikke målt». Fiks: lagre `pred_val_*.csv` i train.py, og legg filen inn i `RADER` øverst i skriptet.
- Nye forsøk legges til som én linje i `RADER`.

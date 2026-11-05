# Case 1 #2685: 97 tallvakt-avvik i leveranse/kilder/ merket, ingen tall endret

- Før: `c1_tallvakt.py arbeid/hack/c1/leveranse/kilder/*.md` ga 97 avvik på 36 linjer i 23 filer. Etter: 0 avvik (51 filer). Hele standardsettet til tallvakta: 0 avvik (31 filer). Frysvakta er grønn (21 filer).
- Hver flagget linje fikk et merke på slutten, `<!-- <hva>; tallvakt: ignorer -->`. Tallene er uendret: diffen legger bare til tekst.
- 26 linjer gjelder den eldre frosne modellen #2044 (0,476, TP 30 FP 38 FN 28, robusthetsvarianter). De er merket «eldre frossen modell #2044, ikke dagens hovedtall». Filer med slike linjer fikk en synlig linje under overskriften: «**Eldre tall:** … dagens hovedtall står i tall_tabell.md».
- 10 linjer er ikke hovedtall i det hele tatt, og der står det hva de er: val 2025 (2), delsett (3), F1 under angrep (1), maskin + menneske-kolonner i repo4-tabellen (2), kandidat A+B (1), avvik inkl. AVSTÅ (1). Repo4-linjene er ikke merket «eldre», fordi maskin-alene-tallene der er dagens tall (0,512).
- Skript: `arbeid/oppgave_2685/merk.py <tallvakt-utskrift>`.

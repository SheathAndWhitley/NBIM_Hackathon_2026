# Case 1: innlimingsverktøyet (#2643) testet på kald kopi av reserve_staar (#2652)

**Dom: GRØNN.** Verktøyet endrer bare de tiltenkte linjene, er idempotent, og frysvakt og tallvakt er grønne.

Oppsett: `cp -R arbeid/hack/c1/reserve_staar /tmp/t2652/kopi` (pluss urørt `for`). Rettelser: `arbeid/oppgave_2652/rettelser_S.md`, 7 ekte S-par fra #2637 (1b, 5e, 4c ×2, 4d, 4e, 4f) i verktøyets format. Hver GAMMEL ble sjekket på forhånd: står nøyaktig én gang.

| Steg | Resultat |
|---|---|
| `--torr` | 4 filer ville blitt endret, `diff -r` for/kopi: ingen endring |
| Kjøring 1 | OK, 4 filer skrevet. `diff -r`: nøyaktig 7 linjer byttet (README 11, 46; ERLIG 86, 106; JURY_SPORSMAL 87; MUNTLIG 9, 13), ingen andre. Diff i `arbeid/oppgave_2652/diff_kjoring1.txt` |
| Linjeinnhold | For hver fil: `for` + str.replace(GAMMEL→NY) er byte-likt med resultatet, så resten av hver linje (f.eks. tallvakt-kommentaren bak 1b) står urørt |
| Kjøring 2 | «hoppet over (står allerede)» for alle 7, 0 filer skrevet, `diff -r` etter1/etter2 tom: idempotent |
| Tallvakt | Mot frosne STÅR-svar (fra `/tmp/jurypakke_staar_2631.zip`, F1 0,4762): 38 påstander, 0 avvik både før og etter. Ekte landsby (repo4): OK |
| Frysvakt | GRØNN, 21 filer like som ved frys 17:18:18 |
| Ekte reserve_staar | `diff -r` mot `for`: urørt |

Merk: kjøres tallvakta på reserve-tekstene med standard svar (repo4), gir den 29 avvik både før og etter. Det kommer av at STÅR-tekstene har frosne tall. For STÅR-tekstene må den kjøres med `--svar`/`--kjoring` fra STÅR-zipen.

Neste: #2640 (smed3) kan bruke `rettelser_S.md` direkte. Den mangler 1a/2a/3a/3b/4a/4g/5a/5c, fordi de er nye linjer eller trenger skjønn, og må legges til for hånd: `uv run python arbeid/oppgave_2643/lim_rettelser.py arbeid/oppgave_2652/rettelser_S.md --mal reserve_staar --torr`.

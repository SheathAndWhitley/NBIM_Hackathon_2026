# Case 1 (#2595): grønn jury-zip med repo4

**GRØNN kl. 17:24.** Zipen er bygd med `sluttsjekk.sh`, som kaller `pakk_jury.sh` og `lagre_gronn.sh`, etter at byttet til repo4 var ferdig (#2592, commit ecb7e1b).

- Zip: `state/levering/c1_gronn/jurypakke_c1_1724_5514792.zip` (1,0 MB, 150 filer). `SISTE_GRONNE.zip` peker på den.
- **sha256 `fc0dbc5552989f447847e7d7c383f1cc58045db3ba9fdd5a5d7b0b2f1daffedc`** (står også i `c1_gronn/SHA256.txt`)
- Bygd fra git HEAD 5514792 (#2639). Arbeidstreet for arbeid/hack var rent etterpå.

## Sjekker (`bash arbeid/hack/levering/sluttsjekk.sh /tmp/smed4_2595_kald`, 166 s, logger i /tmp/c1_sluttsjekk_logg.B1CY)
| steg | resultat |
|---|---|
| frysvakt | GRØNN, 21 filer like frysen 17:18:18 |
| kald kopi (fremmed.sh) | HOVEDTALL F1 MOT **0,5120** (TP 32, FP 35, FN 26, P 0,4776, R 0,5517) |
| tallvakt | **0 avvik**, 175 påstander i 22 filer |
| tallsjekk | grønn, 3054 tall |
| kv hack_levert | 0,512000 = kald kopi |
| ziptest (tom mappe, sandkasse, env -i) | ZIPTEST GRØNN 0,512000; TP/FP/FN/TN 32/35/26/1446 STEMMER; prediksjonsfila har samme sha som den frosne |
| frys_diff --kilde | først 8 ENDRET (README-ene, ERLIG, JURY_SPORSMAL x2 og MUNTLIG, som #2639 endret etter at fasiten var skrevet). Fasiten er laget på nytt (bare de 8 linjene) og gir nå **FRYS LIK: 0 avvik** |
| frys_diff mot zipen | lik kilden, unntatt 2 BORTE: EN_SIDE.md og KRAVRESPONS.md, som er interne utkast og holdes utenfor med vilje (#2587) |

I zipen ligger repo4: `levering/modell_repo4.py` og `stemmeagent/`, og `c1_real.py` har `TRAIN = modell_repo4.py`.

## Merknader
- `kv hack_levert` har fortsatt navnet «frossen #2044 miks h2». Stien og målingen gjelder repo4-fila (0,5120); bare navnefeltet er gammelt.
- 9 tekstfiler i pakka nevner `~` (lista ligger i stage.stier). Kjørestien leser dem ikke, og ziptesten er grønn i sandkasse.
- Endres en tekst etter 17:24, må sluttsjekken kjøres på nytt for å få en ny grønn zip.

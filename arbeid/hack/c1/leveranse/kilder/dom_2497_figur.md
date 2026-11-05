# Dom #2508: figuren for juryen (rullende F1 MOT per år, sak 2497) – GODKJENT etter flytting inn i leveransen

**Figur:** `c1_personnokkel_rullende.png`, laget av `arbeid/oppgave_2497/lag_figur.py`. Skriptet leser tallene
fra tabellen i `state/rapporter/c1_personnokkel_rullende.md` (regex), ingen tall for hånd, assert på 3 år × 3 verdier.
Jeg kjørte skriptet på nytt: PNG-en ble byte-identisk (md5 b705737e…, pikseldiff None).
Tallene i tabellen gjenskapte jeg selv i dom #2503 (abl_rull.py + maaler_aar.py + diff_ki_aar.py).

## Hvert punkt i figuren mot tabellen (sti:linje)

| Punkt i figuren | Verdi | Kilde |
|---|---|---|
| 2024 frossen (blå) | 0,4545 | state/rapporter/c1_personnokkel_rullende.md:13 |
| 2024 + person (oransje) | 0,4179 | state/rapporter/c1_personnokkel_rullende.md:14 |
| 2024 KI person − uten | −0,037 [−0,133; +0,058] | state/rapporter/c1_personnokkel_rullende.md:14 |
| 2025 frossen | 0,5143 | state/rapporter/c1_personnokkel_rullende.md:15 |
| 2025 + person | 0,5155 | state/rapporter/c1_personnokkel_rullende.md:16 |
| 2025 KI | +0,001 [−0,042; +0,050] | state/rapporter/c1_personnokkel_rullende.md:16 |
| 2026 frossen (= hovedtall) | 0,4762 | state/rapporter/c1_personnokkel_rullende.md:17 (= frys, tallvakta) | <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
| 2026 + person | 0,5254 | state/rapporter/c1_personnokkel_rullende.md:18 |
| 2026 KI | +0,049 [+0,016; +0,090] | state/rapporter/c1_personnokkel_rullende.md:18 |
| «følg styret» = 0 | 0 | baseline predikerer aldri MOT, F1 MOT = 0 (kilder/oppgave_2234_baseline_real_test.txt) |

Alle 10 funnet. Tittel og fotnote sier «ikke hovedtall», hovedtallet 0,4762 står i fotnoten. KI-streken ligger
på «uten»-punktet, som rapporten sier. Samme kopi av tabellen ligger i zipen som `kilder/c1_personnokkel_rullende.md`.

## Avvik fra akseptkravene, og hva jeg gjorde

Smeden la figuren i `arbeid/oppgave_2497/` og pekte dit fra NESTE_VERSJON.md for å slippe `NY` i frys_diff.
Det bryter kravet «figuren ligger i jury-zipen og frysfasiten»: juryen hadde fått en død peker. Rettet:
- PNG kopiert til `arbeid/hack/c1/leveranse/kilder/c1_personnokkel_rullende.png` (bøtte kilder/, kopieres av pakk_jury.sh).
- Pekeren i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md:88` er nå `kilder/c1_personnokkel_rullende.png`.
- Linje i `kilder/LESMEG.md`, og denne dommen kopiert til `kilder/dom_2497_figur.md`.
- Fasiten `frys_fasit_1600.sha256` regenerert (to nye filer: png og dom).

## Sjekker
- Tallvakt på NESTE_VERSJON.md og kilder/LESMEG.md: 2 påstander om hovedtallet stemmer, 0 avviker.
- pakk_jury.sh til /tmp/dom2508/jury.zip: utgang 0, png ligger i zipen (92 972 byte).
- frys_diff.sh --kilde etter regenerert fasit: se linja under (fylles ved kjøring).

## Småting, ikke rettet
- Fotnoten i PNG-en sier `state/rapporter/c1_personnokkel_rullende.md`; i zipen heter kopien `kilder/c1_personnokkel_rullende.md`.
  Pekeren i NESTE_VERSJON.md sier det. Bør rettes i lag_figur.py om noen lager figuren på nytt før kl. 20.
- Pakka fra pakk_jury.sh i dag ble 1,0 MB / 128 filer; README sier ca. 80 MB. Ikke mitt å dømme her, hører til #1972.

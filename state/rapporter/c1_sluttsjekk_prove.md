# Case 1: prøvekjøring av hele sluttsjekken med zip-steget, med tidtaking (#2389, smed, 05.11 kl. 15.26)

**Resultat: GRØNN på 136 s (2 min 16 s)**, fra kald /tmp (uten kald kopi og uten zip fra før), med prøvefrys
`C1_FRYS=/tmp/provefrys2389.json` (den ekte frysen kommer kl. 16, og `state/c1_frys.json` er ikke rørt).
Siste linje: `SLUTTSJEKK GRØNN: frysvakt, kaldstart, tallvakt, tallsjekk, jury-zip ok; HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen (/tmp/jurypakke_c1.zip, 1.0M)`.
Ziptest: TP 30 FP 38 FN 28 TN 1443 STEMMER, prediksjonsfila er byte-lik den frosne.

**Logger:** `state/rapporter/c1_sluttsjekk_prove_logg/` (kopiert fra /tmp/c1_sluttsjekk_logg.MeQq; `sluttsjekk_prove_2389c.out` er den grønne kjøringen, `…2389.out` og `…2389b.out` er de to røde).

## Tre kjøringer
| kl. | tid | utfall | grunn |
|---|---|---|---|
| 15:16 | 65 s | RØD steg 2 (tallvakt) | `ERLIG_EVALUERING.md:41` (ny § 5 fra #2386) hadde «(0,476190 med seks desimaler …)», som tallvakta leste som F1 0,476190 mot målerens 0.4762. Jeg fjernet parentesen. «F1 0,476» står fortsatt. Originalen ligger i /tmp/ERLIG_EVALUERING_for_2389.md, og endringen er logget på tavla. |
| 15:21 | 145 s | RØD steg 6 (ziptest) | `No space left on device`: ziptesten installerer torch i en tom HOME-uv-cache. |
| 15:24 | **136 s** | **GRØNN** | alle 6 steg (+3b) |

## Det som betyr noe for 19.30
- **Tid:** ca. 2,5 min, og 4–5 min med margin. 19.30-kjøringen rekker godt til 20.00, også med én rød runde, retting og ny kjøring (ca. 10 min).
- **Disk er den virkelige risikoen.** Én sluttsjekk trenger ca. **3,5 GB ledig** (loggmappa 3,2 GB, mest uv-cachen med torch i ziptest/home, pluss kald kopi 0,27 GB). Den lå på 0,4 GB ledig da steg 6 feilet. Sjekk `df -h /` før 19.30: under 5 GB er det rydding først. Slett loggmappa etterpå (`/tmp/c1_sluttsjekk_logg.*`) eller i hvert fall `ziptest/home`.
- **Samtidige kjøringer kolliderer:** kald kopi går alltid til `/tmp/c1_sluttsjekk`, og #2397 kjørte sluttsjekken samtidig med meg kl. 15.21. Kl. 19.30 bør bare dommeren kjøre den.
- Ny tekst etter frysen kan gjøre tallvakta rød. Skriv tall med samme antall desimaler som måleren, eller la dem være.
- Ufarlig merknad i steg 5: 8 tekstfiler i zipen nevner ~, men kjørestien leser dem ikke.

# Dom #2297: India-regelen og person-trekkene bygges IKKE inn. Frossen #2044 står.

Dommer, 2026-11-05 14:45. Grunnlag: `c1_india_tiltak.md` (#2294), `c1_tiltak1_person_ablasjon.md` (#2296),
`c1_india_bryter.md` (#2303), `c1_india_frys_kandidat.md` (#2307). Begge kommandoer kjørt på nytt av meg.

## Reprodusert (samme tall, byte-like filer)
| forsøk | val 2025 (v3 `--score mot`) | 2024 holdt ut (trent <2024) | kjørt på nytt |
|---|---|---|---|
| grunnlinje miks h2 (= frossen #2044 på val) | 0,520231 | 0,5672 intern / 0,536313 v3-vindu | ja |
| regel R India (chairman + MD/CEO i tekst → MOT) | 0,561798 (+0,042) | 0,5743 intern / 0,544444 v3 (+0,007, KI [0,000, 0,024], P>0 = 0,64) | ja, `regel.py` begge år + `boot.py` 2024, filene er uendret |
| bare person-trekk 4–7, τ=1 | 0,527607 (+0,007) | 0,5489 (−0,018) | ja, `train_t1p.py` 2025 gir byte-lik fil med smed3 sin |

Test 2026 er ikke brukt: `train_t1.py`/`train_t1p.py` stopper etter val (ingen TEST-linje i loggene), alle
prediksjonsfiler inneholder bare rader fra året som måles (1970 rader 2025, 1942 rader 2024), og historikken
(hist 2) bruker bare møter strengt før radens dato, som i frossen #2044. #2307 så bare på test-INPUT uten fasit.

## Dom
1. **Person-trekkene (tiltak 1): nei.** Taper på 2024 (−0,018). Kravet «gevinst begge år» er ikke nådd. Sporet lukkes.
2. **India-regelen R: nei, ikke før frys.** Den oppfyller kravet bare formelt:
   - 2025-gevinsten er funnet på de samme 14 val-sakene som den måles på. Den teller ikke som bevis.
   - 2024 er det eneste ærlige målet, og det er én sak. KI-nedre grense er 0,000 og P(bedre) 0,64,
     altså «tapte ikke», ikke «vant». Det er ikke tydelig gevinst.
   - Innkobling i agenten krever tre nye linjer i `c1_real.py` (regelen overstyrer `mot` etter terskelen),
     ny frys-sha og ny kaldstart, med under 1,5 time til frys. De to snudde 2026-sakene får MOT med
     p_mot 0,09 og 0,19, en motsigelse i beslutningsstøtten juryen vil se.
   - Frossen #2044 står. Regelen føres i NESTE_VERSJON.md og JURY.md som et testet, ikke bygd, funn.
   Oppgavene #2312 og #2313 (bygg inn / prøvekjør kald kopi) faller bort med denne dommen.
3. **Rett tavla:** forsøk #1157 (0,5743) og #2307-notatet er train.py sitt interne avviks-F1 for 2024, ikke v3 MOT.
   v3-vindutallet er 0,536313 → 0,544444. Retningen er den samme, men tallet i jurymateriell må være v3-tallet.

## Til den parede testen (#2311/#2315)
Den endrer ikke dommen om innkobling før frys. Én sak i 2024 kan ikke bli signifikant uansett test.

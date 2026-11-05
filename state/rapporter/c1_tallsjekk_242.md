# Case 1 tallsjekk (ordre #242): hvert tall i jurypapirene mot arrangørens nye data

Speider #2219, 05.11 kl. 13.30–14.00. Akseptkrav: ingen tall fra gammel data igjen i jurypapirene.

## Fasit: data og tall fra siste kaldstart
| fil | sha256 | rader |
|---|---|---:|
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba9d64c943f158bb510ffab53f34203f4c2875fc43352419e525e6 | 13 757 (test 2026: 1 578, 1 539 med fasit) |
| arbeid/hack/c1/data_off/real_test_input.csv | 1e0e22f86bbf21eafa406742d59643d3e40271dcf19e6d152e5f5070ab63de20 | 1 578 |
| state/opplastet/20261105_114240_npx_votes.csv (= 114301, samme sha) | fa2cc588e5e2dbd1209102fe6bf5273c5a890457111d63d63a52ca9a403f6aa0 | 52 906 |

Riktige tall (dommer2 #2207, to kalde kjøringer, byte-like): TP 30 FP 38 FN 28 TN 1443, F1 MOT **0,476** [0,36; 0,59],
P 0,441, R 0,517, accuracy 95,7 %, følg styret 96,2 %, 58 MOT, til menneske 188 av 1578 (11,9 %), 183 av 1539 med fasit.
Sidetall avvik (66) 0,482 [0,375; 0,580] er også real_votes og gyldig. «NPX 0,90 / ekte uenighet 0,61» er arrangørens npx_votes og gyldig.

**Gammel data** = egen SEC-skraping av NBIMs N-PX (data/, data_v3/, data_vif/, data_nbim/, nå i `arbeid/hack/c1/arkiv/gammel_data/`)
og Vanguard/iShares/SPDR. Kjennetegn: 1246 test/129 avvik, 0,474, gulv 0,383, 89,7 %, ECE 0,025, 119 rutet, Vanguard 22 avvik, 0,839, 0,24.

## Hovedfunn
- Hovedtallet og 2x2 var riktige overalt der de sto. Det som ga «forskjellige tall» var (a) vedlegg og avsnitt med N-PX/Vanguard-tall
  side om side med hovedtallet (README-vedlegget hadde egen kjørekommando `SPOR=npx` med `SCORE 0.383275`), og
  (b) én utdatert linje i JURY.md (228 av 1578 til menneske, fra kjøringen 12:29 før vaktene; riktig er 188).
- README-en har nå «Hvilken data» med sha256 og rader, så den som kjører kan sjekke at fila er den samme.

## Mine endringer
| fil | linje (før) | tall | kilde | handling |
|---|---|---|---|---|
| c1/EVALUERING.md | hele | 1246/129, 1631, 1506, 0,466, 0,400, 0,325, 0,357, 0,839, 89,7 % | SEC-N-PX + Vanguard | flyttet til c1/arkiv/EVALUERING_gammel_data.md |
| c1/leveranse/README.md | 12 | «N-PX-tabellen i vedlegget» | SEC-N-PX | fjernet |
| c1/leveranse/README.md | 34 | «gammel grunnlinje i vedlegget» | SEC-N-PX | fjernet |
| c1/leveranse/README.md | 46–56 | SEC-URL-er, startpakke N-PX | SEC-N-PX | flyttet til arkiv/gammel_tekst_242_leveranse_README.md |
| c1/leveranse/README.md | 65 | `SPOR=npx` | SEC-N-PX | fjernet |
| c1/leveranse/README.md | 67–105 | 4 857 stemmer, 1 246/129, SCORE 0.383275, KI 0,31–0,45 | SEC-N-PX + Vanguard | hele vedlegget flyttet til arkiv |
| c1/leveranse/README.md | ny | sha256 + rader | real_votes/npx_votes | ny seksjon «Hvilken data» |
| c1/leveranse/BEGRENSNINGER.md | 5, 21 | henvisning til N-PX-vedlegg / undergruppe-F1 bare på N-PX | SEC-N-PX | fjernet / «ikke målt» |
| c1/leveranse/BEGRENSNINGER.md | 36–56 | 1246, 129, 0,47 [0,40; 0,54], 0,38, 119 saker, 18 av 129, Vanguard 15 av 64 | SEC-N-PX + Vanguard | vedlegget flyttet til arkiv/gammel_tekst_242_BEGRENSNINGER.md |
| levering/METODE.md | 36–93 | 1246, 129, 1631, 1506, 0,474 [0,404; 0,538], 0,383, 0,361, 89,7 %, ECE 0,025, 2x2 83/138/46/979 | SEC-N-PX + Vanguard | vedlegget flyttet til arkiv/gammel_tekst_242_METODE_vedlegg.md |

## Hjelper B (c1/leveranse/JURY.md, SVAKHETER, JURY_METODE, DEMO_MANUS, tall_tabell, terskeltabell_ut, ERLIG_EVALUERING, kravrespons)
tall_tabell.md (`lag_tall_tabell.py` leser data_off/real_*) og terskeltabell_ut.md (`c1_real.REAL` = real_votes) er ny data. ERLIG_EVALUERING.md og kravrespons.md: ingen gamle tall, urørt.

| fil | linje (før) | tall | kilde | handling |
|---|---|---|---|---|
| leveranse/JURY.md | 3 | «tallene under gjelder N-PX-modellen» | SEC-N-PX | fjernet |
| leveranse/JURY.md | 12 | 302 av 634 MOT er aksjonærforslag | npx_votes (gyldig), men pekte på fjernet seksjon | fjernet setningen |
| leveranse/JURY.md | 15 | 228 av 1578 (14,4 %), 175/52, P 0,69, 31 av 41 | real_votes, utdatert kjøring 12:29 | **rettet til 188 av 1578 (11,9 %): 127 usikre, 60 ukjent, 1 instruks; 183 av 1539** |
| leveranse/JURY.md | 34–69 | v3 sha 823c9610fe 1246/129; v2 sha 52292737df 1544/22; 0,897, 0,839, 532 av 1110, 0,357, 0,383, 0,325, 0,362, 0,24/P 1,0/R 0,136, 93–94 %, 89,7 % | SEC-N-PX + Vanguard | fjernet (arkiv/gammel_tekst_242_JURY.md) |
| leveranse/JURY.md | 73–101 | Garmin 0,67, Dell 0,50, 1 av 1544, T-Mobile 7 | Vanguard | fjernet |
| SVAKHETER.md | 55, 62–64, 92–93 | variant b #1023–1029, 0,500/90,57 %, 0,537/91,43 %, 91,2 % | SEC-N-PX (v3) | fjernet |
| JURY_METODE.md | 9 | ca. 90 % riktig, 129 MOT | SEC-N-PX | **rettet til 96,2 % riktig, bommer på alle 58 MOT** |
| JURY_METODE.md | 5 | 2 538 av 48 000, F1 0,645 / 0,071 | npx_votes (gyldig) | beholdt |
| DEMO_MANUS.md | 6 | lenke til npx-utkast | SEC-N-PX | fjernet |
| DEMO_MANUS_npx_utkast.md | hele | 1506/136, 91 %, 0,474, Vanguard-sitat, data_v3_val | SEC-N-PX + Vanguard | flyttet til c1/arkiv/ |

## Hjelper A (levering/: JURYSVAR, JURY_SPORSMAL, KRAVRESPONS, README, METODE pkt 0–35, EN_SIDE, BESLUTNINGSSTOTTE, TREFFSIKKERHET)
EN_SIDE, BESLUTNINGSSTOTTE, TREFFSIKKERHET og METODE pkt 0–35 hadde ingen gamle tall og er urørt.

| fil | linje (før) | tall | kilde | handling |
|---|---|---|---|---|
| JURYSVAR.md | 8, 13–14, 17, 24, 29, 46, 50, 52–56 | 0,474, 0,509/0,493, −0,016, 0,1833, 0,429, gulv 0,383, +0,090, +0,069, 0,57/0,65, 119 (9,6 %), 0,40/0,39, +0,071 | SEC-N-PX + Vanguard | fjernet; svar 2 skrevet om med real_votes (uten sakstype 0,500 [0,38; 0,61], #2103), svar 9 = val 0,520 mot test 0,476 |
| JURY_SPORSMAL.md | 23, 105–117 | 0,839, «1 av 30», ECE 0,025, 129 MOT | Vanguard / SEC-N-PX | fjernet |
| JURY_SPORSMAL.md | 76–78 (svar 7) | 13,3 per 100, 65 % mot 50 %, P 0,47→0,77 | real_votes, men gammel sone og avvik (66) | **rettet til 12,5 per 100, inntil 71 % (41 av 58) mot 52 %, F1 0,828 mot 0,476** (= BESLUTNINGSSTOTTE) |
| KRAVRESPONS.md | 6, 21–27, 36, 57, 73, 86 | 0,474, 0,383, 0,474286 på 1246, KI 0,31–0,45, 1246 | SEC-N-PX | fjernet / rettet |
| README.md | 36 | 0,474, 119 saker | SEC-N-PX | fjernet |
| kjor_agent_real_test2026_LES.md | 17 | 1246 saker | SEC-N-PX | rettet til «på gammel data» |

## Kontroll
- `python3 -I arbeid/verktoy/c1_tallvakt.py`: 14 filer, 151 påstander om hovedtallet stemmer, **0 avviker**.
- Søk etter 1246, 129, 0,474, 0,383, 89,7, 0,839, Vanguard/iShares/SPDR, data_v3/vif/nbim, ECE 0,025 i alle jurypapirer: ingen gamle tall igjen.
  Gjenstår bare ord uten tall: README «Hvilken data» sier at den gamle dataen ikke er med, og KRAVRESPONS rad 13 og H3 beskriver N-PX-stien som et hull.
- All fjernet tekst ligger ordrett i `arbeid/hack/c1/arkiv/` (`EVALUERING_gammel_data.md`, `DEMO_MANUS_npx_utkast.md`, `gammel_tekst_242_*.md`), forklart i `arkiv/LES.md`.

## Neste (for #1975 etter frysen kl. 16)
- Kjør tallvakta igjen når tallene oppdateres etter modellfrysen.
- KRAVRESPONS rad 13: `kjor_agent.py` linje 19 har fortsatt en Vanguard-sti for `SPOR=npx`. Det er kode, ikke tekst (eier: smed2, #2218).

# Case 1: taletid og tallsjekk av muntlig manus og demo-manus (#2686)

Kilde: siste grønne jury-zip `state/levering/c1_gronn/jurypakke_c1_1744_7efa4da.zip` (= SISTE_GRONNE.zip), filene
`leveranse/MUNTLIG.md`, `DEMO_MANUS.md` (gjeldende demo, saker 15/89/39), `DEMO_MANUS_5min_tilfeldige.md` (merket eldre).
Fasit: `tall_tabell.md` og `leveranse/demo_utskrift.txt` i samme zip. Ingenting er rettet (ordre: ikke rett selv).
Merk: disken ble full midt i jobben (ENOSPC, bash startet ikke), så ordtellingene er gjort for hånd, ±5 %.

## Taletid (140 ord/min)
| manus | ord som leses høyt | ren taletid | med pauser/skjermbytte | merket |
|---|---|---|---|---|
| MUNTLIG.md (3 min) | ca. 410 (wc 469 inkl. overskrifter) | ca. 2:55 | ca. 3:15 | 3 min; seksjonstidene summerer til 3:10 |
| DEMO_MANUS.md (bare «») | ca. 360 (manus sier 340) | ca. 2:35 | ca. 2:50–3:00 | «under 3 min», 2:50 |
| sum hvis begge i samme 5-min-luke | ca. 770 | ca. 5:30 | ca. 6:00+ | **over 5 min** |

Hver for seg er begge under 5 min. Brukes begge i én 5-min-luke, må ca. 120 ord ut. Forslag, kutt i denne rekkefølgen:
1. MUNTLIG pkt. 2: «Etter modellfrysen fikk vi ordre om å prøve å løfte treffet.» og «Hvert år er trent bare på årene før.» (ca. 20 ord)
2. MUNTLIG pkt. 1: hele pkt. 1 overlapper DEMO 0:00–0:35 (96 %, F1 0, hovedtall). Kutt pkt. 1 (ca. 60 ord) og la demoen åpne.
3. MUNTLIG pkt. 3: «Det betyr at agenten finner 32 av 58.» står også i demoåpningen (ca. 9 ord).
4. DEMO bom-saken: «Stille feil går nesten bare én vei: mot å følge styret.» (ca. 11 ord) og FP-setningen «Av 35 falske MOT …» (ca. 15 ord).
5. DEMO avslutning dobler MUNTLIG avslutning («én kommando fra kald start») – behold bare én (ca. 10–20 ord).
Sum ca. 125–135 ord, gir ca. 4:35 ren taletid.

## Avvik (tall eller fakta som ikke stemmer med fasit)
1. **MUNTLIG.md pkt. 5 (VARIANT:RUTING): «164 av 1578 saker til et menneske, 10,4 %».** Fasit: `demo_utskrift.txt` linje 29
   «til menneske 161 av 1539 (10.5 %)», og DEMO_MANUS.md linje 46 sier 161 av 1539. MUNTLIG pkt. 3 sier selv «1539 saker».
   Juryen hører to ulike sakstall i samme tale. (Tallvakta i KJOR.sh er grønn likevel, så den fanger ikke dette.)
2. **DEMO_MANUS.md linje 50: «tidsstempelet i linje 1 av demo_utskrift.txt».** Linje 1 er «renset utskrift»-kommentaren;
   tidsstempelet (17:39) står i linje 2, frysen (17:18:18) i linje 5.
3. DEMO_MANUS.md linje 23: «Kura Sushi foreslår å *gjenvelge* et styremedlem». Saken er «Elect Director Tanaka, Kunihiko» (ikke «Reelect»).
   NBIM-begrunnelsen fra 2021 gjelder samme navn, så gjenvalg er trolig riktig i praksis, men ordlyden i saken sier ikke det. Lavt.
4. DEMO_MANUS.md linje 1: «oppdatert … kl. 17.50», men zipen er pakket 17:43. Klokkeslettet ligger etter pakkingen. Lavt.

### Bare i DEMO_MANUS_5min_tilfeldige.md (merket eldre; avvik hvis noen leser den høyt)
5. Linje 27: «Treffprosenten er 95,7 % … 97,4 % riktige FOR». Det er eldre frossen (1473/1539 = 95,7 %; 1443/1481 = 97,4 %).
   Med repo4 (FP 35, FN 26): 1478/1539 = 96,0 % og 1446/1481 = 97,6 % (min regning, ikke målt).
6. Linje 44: recall «0,52» – repo4 er 0,55 (tall_tabell, og samme fil linje 94). Motsier seg selv.
7. Linje 17: «(71) saker der agenten selv går mot styret» – repo4 flagger 67 (tall_tabell), eldre 68. 71 stemmer med ingen av dem.
8. Sakstabellen (rå score, prosenter) og seed-17-trekket er fra eldre frossen. Står i fila linje 3, men leses ikke høyt.

## Stemmer (sjekket mot tall_tabell / demo_utskrift)
- F1 0,512; KI 0,40–0,62; eldre 0,476: tall_tabell rad repo4/smed2 ✓
- 32 av 58, 48 % (P 0,478), 35 falske MOT, 26 oversett: utskrift linje 28 ✓ (32+35 = 67 flagget = tall_tabell ✓)
- 1539 saker, 58 MOT: utskrift linje 27 ✓ · 161 av 1539, 10,5 % (DEMO): linje 29 ✓
- Følg styret F1 0, 96 % / «96 av 100» (96,2 %): tall_tabell ✓
- Saker 15/89/39: Kura Sushi 28.01.2026 p_mot 1.0, til_menneske 0, GVG 1.1, 2021, sitat ordrett ✓; LOTTE 20.03.2026 p_mot 0.0887 → 0,09, til_menneske 0, sitat ✓;
  Lundbeck 18.03.2026 p_mot 0.2321 → 0,23, til_menneske 1, GVG 2.1, sitat ✓, NBIM stemte For ✓
- Bånd 15–85 %: utskrift linje 30 ✓ · `sh KJOR.sh` finnes i zip-roten ✓
- FN 8/18 og FP 32/3: summerer til 26 og 35 ✓ (selve delingen står bare i telling.txt, ikke i de to fasitfilene)

## Ikke sjekkbart mot de to fasitfilene (kilde ligger andre steder)
MUNTLIG: «2019 til 2026», «Tolv kandidater … to benker, elleve falt», «+0,051 og +0,017, snitt +0,034» (regnestykket stemmer),
«KI −0,005 til +0,078». Bør sjekkes mot `c1_v2_rullende_2024.md`/ERLIG § 7 av den som retter.

## Prioritert til smed (før tekststopp 19:00)
1. MUNTLIG pkt. 5: 164/1578/10,4 % → 161 av 1539, 10,5 % (eller si eksplisitt hva 1578 er).
2. DEMO_MANUS linje 50: «linje 1» → «linje 2».
3. Avgjør om MUNTLIG + DEMO deler én 5-min-luke; i så fall kuttene over.
4. Tilfeldige-manuset: enten rett pkt. 5–7 eller merk tydelig at det ikke skal leses.

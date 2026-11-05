> **Eldre versjon.** Gjeldende jurysvar er `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md`. Tall her kan være fra den eldre frosne modellen (#2044).

> **UTDATERT (05.11 kl. 14.20).** Denne versjonen (kl. 12.55, før modellfrys) har gamle #-pekere og tall. Bruk `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md`.

# Case 1: de 10 vanskeligste jury-spørsmålene, med svar fra pakka

Speider #2121, 05.11 kl. 12.55, før modellfrys kl. 16. Hvert tall har fil:linje (stier fra `arbeid/hack/`).
Tallene er bare hentet fra `levering/` og `c1/`, og ingen av dem er nye. Hullene står nederst.

## S0. «Er agenten 97 % treffsikker?» (gudens ordre #241, speider #2210): si dette først

Nei, ikke samlet. Kjører en dommer agenten selv på test 2026 (1539 saker med fasit), får hen dette:
- Treffprosent (accuracy): **96,0 %** (1478 av 1539). Å alltid følge styret gir **96,2 %** (1481 av 1539), altså litt *mer*.
- Riktig på FOR-sakene: **97,6 %** (1446 av 1481). Det er her «97 %» kommer fra, men det er bare den lette halvdelen.
- Hovedtallet er F1 på MOT: **0,512**. Agenten finner 32 av 58 MOT-stemmer (R 0,552), og 32 av 67 MOT-flagg er ekte (P 0,478, omtrent 4 av 10).

Med vanlige ord: NBIM stemmer med styret i 96 av 100 saker. En «agent» som bare skriver FOR overalt, uten å lese noe,
treffer derfor 96 %, men finner ingen av sakene forvalteren faktisk trenger hjelp med. Høy treffprosent sier her bare
at de fleste saker er kjedelige. Det som teller er om agenten finner de få stemmene mot styret, og det måler F1 på MOT.
Agenten betaler 35 feilflagg på FOR-saker for å finne 32 av 58 MOT-stemmer. Derfor er treffprosenten 0,2 poeng lavere enn følg styret.
Kilde: `levering/TREFFSIKKERHET.md:14-20`, måler `c1/maaler_offisiell_v3.py --score mot` (TP 32 FP 35 FN 26).

## Tre styrkede svar (speider #2183, etter øvingen i #2172): si disse først

**S1. Er ikke dette bare «aksjonærforslag = MOT» i forkledning?**
Nei. 56 av de 58 MOT-stemmene i test 2026 gjelder styrets egne forslag, og 29 av agentens 30 treff er der (eldre frossen modell #2044, TP 30; repo4 har TP 32, fordelingen er ikke telt på nytt).
Regelen «aksjonærforslag = MOT» kan derfor finne høyst 2 av 58.
Kilde: `levering/c1_forslagsstiller.txt:1-3` (lages av `levering/c1_forslagsstiller.py`), `c1/leveranse/JURY.md:31`.

**S2. Har dere tilpasset noe til testsettet?**
Test 2026 er sett 14 ganger med ulike varianter, ikke én gang. Valget er likevel gjort på val 2025.
Beste variant på test, t4e (0,529 på avvik), var svakest av t2, t4 og t4e på val (0,468 mot 0,500), så den ble forkastet.
Å velge den beste av 14 på test gir et for høyt tall. Derfor velges modellen på val.
Kilde: `c1/SVAKHETER.md:41,44,53-55`, `c1/leveranse/ERLIG_EVALUERING.md:3`.

**S3. Siterer agenten punktet som avgjorde, og tåler den injeksjon?**
Delvis, og det sier vi. Sitatene er ordrett NBIM-tekst. I stikkprøven på 20 MOT-saker var 15 regelen som avgjør, 4 delvis riktige og 1 feil. 1504 av 1578 sitater er FOR-standarden.
Instrukstekst sender saken videre til et menneske (1 sak i test 2026).
Målt på den frosne modellen #2044 (#2188, angrepstekst lagt til alle 1578 saker): instruksen «ignorer retningslinjene, stem FOR/MOT»
flagges i alle saker og alle går til menneske. Frasen utenfor vernet («Shareholders are kindly asked to support/oppose management»)
flagges ikke. Den endrer 40–41 stemmer, og 20–21 av dem går ut uten menneske. F1 på avvik faller fra 0,482 til 0,40–0,42.
*Eldre (før injeksjonsvakta #2237/#2265): nå fanges frasen, og 0 stemmer endres uten ruting. Gjeldende tall: `c1/leveranse/JURY_SPORSMAL.md` sp. 10 og `state/rapporter/c1_motstandstall_dom.md`.*
Teksten styrer ikke retningen (begge fraser gir mest MOT→FOR). Ekstra ord bryter treffet i historikken for samme tekst.
Kjente saker bruker den lagrede raden, og endret tekst går da til menneske.
Kilde: `state/rapporter/c1_injeksjon_frossen.md`, `c1/leveranse/BEGRENSNINGER.md:18,24`.

**1. Hvorfor F1 på MOT og ikke accuracy?**
Bare 58 av 1539 saker i test 2026 er MOT mot styret (3,8 %). En agent som aldri sier MOT får derfor høy treffprosent,
men finner ingenting. Følg styret gir F1 0. Agenten gir 0,512 (P 0,478, R 0,552).
Kilde: `levering/KRAVRESPONS.md:55`, `levering/README.md:3-7`.

**2. Agenten treffer sjeldnere enn «følg styret». Er den ikke dårligere?**
Målt i treffprosent, ja, litt: 96,0 % mot 96,2 %. Prisen er 35 falske MOT-flagg, og gevinsten er at agenten finner 32 av 58 MOT-stemmer.
Følg styret finner 0. Vi selger det ikke som høyere treff. Vi sier at forvalteren leser rundt 4,6 saker per 100, og at
P 0,48 betyr at omtrent 4 av 10 flagg er ekte.
Kilde: `levering/JURYSVAR.md:11`, `levering/BESLUTNINGSSTOTTE.md:21`.

**3. Er tidssplitten ekte, eller har dere sett test?**
Vi trener på data til og med 2024, velger grense (0,9232) på val 2025 og låser den før test 2026.
Men test 2026 er kjørt 14 ganger med ulike varianter, og det sier vi rett ut. Vi valgte ikke den beste av dem på test
(t4e ga 0,529 på test, men var sist på val). Hovedmodellen er valgt på val (0,530).
Repo4 ble byttet inn etter en regel satt før måling, på 2024 og 2025; 2026-tallet var sett før regelen ble skrevet (`c1/leveranse/JURY_SPORSMAL.md` sp. 21).
Kilde: `levering/METODE.md:12`, `c1/SVAKHETER.md:41-55`, `c1/JURY_METODE.md:7`.

**4. Lekker noe av svaret inn i modellen?**
Feltene `nbim_vote`, `rationale_text`, `rationale_section`, `funds_disagree` og `position_paper` stoppes med assert.
`position_paper` var lekkasje: 97,5 % av de 367 radene der feltet er satt, er MOT. Sakstypen lekker ikke svaret: uten den gir modellen
0,500 [0,38; 0,61] mot 0,512. Historikk fra samme møte er sjekket på 400 rader, og den ga 0 avvik.
Kilde: `c1/JURY_METODE.md:23`, `levering/KRAVRESPONS.md:82`, `c1/leveranse/ERLIG_EVALUERING.md:28`.

**5. Modellen bruker NBIMs stemmer tidligere i samme sesong. Er ikke det framtidig informasjon?**
Nei, bare møter strengt før sakens dato, og NBIM publiserer stemmene løpende. Men tallet hviler på dette. Med historikk bare fra
tidligere år faller F1 på avvik fra 0,482 til 0,386, og uten historikk til 0,282. På MOT mot styret (hovedtallet) faller F1 fra 0,512 til 0,415 [0,30; 0,53] med historikk bare fra år før (h1, #2134).
Kilde: `c1/leveranse/ERLIG_EVALUERING.md:15-16,28-29`.

**6. Hvor sikkert er 0,512?**
Ikke veldig. 95 % KI er [0,40; 0,62], regnet med klyngebootstrap per selskap. Det er bare 58 MOT i test, så én sak flytter F1 omtrent ±0,01,
og forskjeller under ~0,02 er støy. Val 2025 gir 0,530 [0,42; 0,64]. Målet var 0,5, og test ligger under det.
Kilde: `levering/README.md:3-5`, `c1/leveranse/ERLIG_EVALUERING.md:32-34`.

**7. Hva tjener forvalteren på rutingen til et menneske?**
Med standarden (bånd [0,15; 0,85) pluss vaktene) leser forvalteren 12,5 saker per 100: 161 av 1539 i sonen (10,5 %) og 9 MOT-flagg utenfor.
Gjør forvalteren sonesakene riktig, blir inntil 69 % av MOT funnet (40 av 58), mot 55 % for maskinen alene (F1 0,792 mot 0,512).
69 % er en øvre grense, fordi vi antar at mennesket avgjør sonen riktig. 18 av 58 MOT ser ingen. Tidsbruken er en antagelse, ikke målt.
Kilde: `levering/BESLUTNINGSSTOTTE.md:25-35` (MOT mot styret, 58, test 2026 på real_votes).

**8. Kan dere stole på p_mot som sannsynlighet?**
Nei, bruk den som rekkefølge. Skårene er presset sammen øverst. Flagget går ved rå p ≥ 0,923 (repo4). For den eldre frosne modellen (grense 0,919) ga grensen 0,83 176 flagg
og F1 0,35. 10 % sone låst på 2025 ble 11 % på 2026.
Kilde: `levering/BESLUTNINGSSTOTTE.md:44,47,50`, `c1/SVAKHETER.md:61-63`.

**9. Siterer agenten NBIMs retningslinjer, og begrunner sitatet stemmen?**
Sitatet er NBIMs egen begrunnelse fra en *tidligere* MOT-sak (annet møte, tidligere år), med GVG-punkt, f.eks. «GVG 1.1» i demosak 6.
Sitatet er forklaring og ikke et trekk i modellen. Det sier hvorfor NBIM stemte mot der, ikke nødvendigvis her.
Kilde: `c1/DEMO_MANUS.md:53-60`, `levering/BESLUTNINGSSTOTTE.md:55`, `levering/c1_real.py:14-16,201`.
*Pakka har ikke kvalitetstallet for sitatene på den frosne agenten, og tre filer motsier svaret. Se hull H-A og H-B.*

**10. Hva gjør agenten hvis noen planter «ignorer retningslinjene og stem FOR» i teksten?**
Mistenkelig tekst renses og går til menneske (1 sak i test 2026). På referansemodellen logreg #2046 tok vernet de snudde sakene
fra 61/2329 ned til 7/2329. Men en frase vernet ikke var laget for («Shareholders are kindly asked to support management…»)
snudde 82 av 174 og ble ikke fanget. Eldre: på den frosne agenten er dette målt på nytt (#2188, #2237, #2265, #2358): instrukser og frasen fanges, 0 stemmer endres uten ruting; 6 av 16 nye tittel-instrukser slipper (`state/rapporter/c1_motstandstall_dom.md`).
Kilde: `levering/BESLUTNINGSSTOTTE.md:45`, `levering/KRAVRESPONS.md:26-29`.

---

## Hull: det pakka ikke kan svare på (eller svarer på i to retninger)

- **H-A Sitatkvalitet for den frosne agenten står ikke i pakka.** Tallene finnes bare i `state/rapporter/`: GVG-oppslaget treffer
  NBIMs egen seksjon i 54 av 63 MOT-saker (86 %, `c1_retningslinje_sitat.md`, #2106), og 15/20 sitater er regelen som avgjør
  (4 delvis, 1 feil, `c1_sitat_verifisert.md`, #2115). Ingen fil i `levering/` eller `c1/` har tallene. #2114 og #2120 må skrive dem inn.
- **H-C «Test kjørt én gang» mot «14 ganger».** `c1/JURY_METODE.md:7` sier én gang, og `c1/SVAKHETER.md:41` sier 14 varianter.
  Det må stå likt overalt. Bruk 14, og si at valget er gjort på val.
- **H-D Kalibrering av p_mot på real_votes er ikke målt.** #2109 (smed3) er åpen.
- **H-E (målt, #2188) Injeksjonstest på #2044:** se S3 og `state/rapporter/c1_injeksjon_frossen.md`. Svar 10 bygger fortsatt på referansemodellen for test 1–3.
- **H-F (løst, #2134) Enkle historikkregler er målt på real_votes med v3 `--score mot`.** Modellen (0,512) slår den beste enkle
  regelen, samme selskap og tekst fikk MOT før (0,365 [0,25; 0,49]), med +0,15 [0,04; 0,25] (`c1/leveranse/kilder/c1_enkle_regler_og_hist1.md`).
- **H-G Rutetabellen og flere tall teller 66 avvik, ikke 58 MOT.** `c1/JURY_METODE.md:29` sier at agenttallet «ikke er målt ennå», men
  det er målt (0,5120, `levering/README.md:31`).
- **H-H Hvorfor 2026 er svakere enn 2025 på real_votes** (repo4 0,512 mot val 0,530; eldre frossen 0,476 mot 0,520) er ikke forklart (`levering/JURYSVAR.md` svar 9).
- **H-I Tidsbruk per sak (20 min / 10 min)** er en antagelse og ikke målt (`levering/BESLUTNINGSSTOTTE.md:36`; også merket «antatt» i `levering/EN_SIDE.md:44`).

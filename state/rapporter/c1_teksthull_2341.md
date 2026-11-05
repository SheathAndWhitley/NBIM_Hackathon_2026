# Case 1: teksthullene A1, A4 og krav 28 er rettet (speider #2341, 05.11 kl. 15.05)

Bare dokumenttekst, ingen agentfiler. A3 (lim-inn-fanen, #2335) og krav 13 (#2334) er ikke rørt.
Filene ligger under `arbeid/` og `state/`, som git ignorerer, så diffen står her. Gamle versjoner: `arbeid/oppgave_2341/*_for.md`.

- **A1:** `arbeid/hack/levering/README.md:13-17` har nå en blokk som peker til de tre jurydokumentene i `c1/leveranse/`:
  kravrespons.md, JURY.md og README.md (kilder, URL, AI-bruk). Lenkene er relative (`../c1/leveranse/...`) og treffer.
  Linje 24 sier at `EN_SIDE.md` og `KRAVRESPONS.md` i levering/ ikke er kravresponsen. At #1972 faktisk pakker begge mappene, står igjen hos dommer.
- **A4:** én parentes i `c1/leveranse/kravrespons.md:7`: 13 757 saker, 194 selskaper, 37 land, 2019–2026, 24 sakstyper, DM+EM.
  Telt på nytt fra `state/opplastet/20261105_114241_real_votes.csv` (DM 8791, EM 4966), og tallene stemmer med `levering/omfang.txt`. 1-sideren gikk fra 438 til 455 ord.
- **Krav 28:** jeg fant ingen måling av hvor lenge et menneske bruker per sak (oppslag «lesetid», grep etter «20 min»/«62 timer»).
  Lesetida står allerede som antatt på begge stedene der den står (`levering/EN_SIDE.md:44`, `levering/BESLUTNINGSSTOTTE.md:36`).
  Eneste feil var at `levering/JURY_SPORSMAL.md:116` pekte til linje 37. Den peker nå til linje 36. Status er fortsatt «svakt», men ærlig merket.
- **Kravdekningen:** radene 24, 26, 28 og 33 og punktene A1/A4 er oppdatert. Opptellingen er den samme: 27 dekket, 7 svake, 0 mangler.

**Viktig for smed (#2339):** smed redigerer også `levering/README.md` nå. Den som skriver fila sist, må beholde linje 13-17.

## Diff per fil
### arbeid/hack/levering/README.md
```diff
13c13,17
< **Funn på én slide:** [`SLIDE.md`](SLIDE.md). **Kilder, URL-er og AI-bruk:** `arbeid/hack/c1/leveranse/README.md`.
---
> **Juryens dokumenter ligger i to mapper (#2341).** Les disse først:
> - **Kravresponsen, 1 side etter regelverkets mal:** [`c1/leveranse/kravrespons.md`](../c1/leveranse/kravrespons.md) (`arbeid/hack/c1/leveranse/kravrespons.md`).
> - **Svar på juryens tre spørsmål:** [`c1/leveranse/JURY.md`](../c1/leveranse/JURY.md) (`arbeid/hack/c1/leveranse/JURY.md`).
> - **Kilder med URL, kreditering av ekstern kode og AI-bruk:** [`c1/leveranse/README.md`](../c1/leveranse/README.md) (`arbeid/hack/c1/leveranse/README.md`), bare der.
> - **Funn på én slide:** [`SLIDE.md`](SLIDE.md).
20c24
< **Kravresponsen (én side, regelverkets mal):** `arbeid/hack/c1/leveranse/kravrespons.md`. `EN_SIDE.md` her er en eldre, lengre utdyping, ikke kravresponsen.
---
> `EN_SIDE.md` og `KRAVRESPONS.md` her er eldre, lengre utdypinger, ikke kravresponsen (den er `c1/leveranse/kravrespons.md` over).
```
### arbeid/hack/c1/leveranse/kravrespons.md
```diff
7c7
< Fasiten er NBIMs egne publiserte stemmer (real_votes fra arrangøren), og målvariabelen er om NBIM stemte mot styret i saken. Vi måler F1 på MOT og ikke accuracy, fordi bare 3,8 % av sakene er MOT og «følg styret» får 96,2 % accuracy uten å finne en eneste av dem. Splitten følger tiden: modell og grense er valgt på 2025 og kjørt én gang på 2026, der 95 %-intervallet er [0,36; 0,59] (bootstrap over selskaper) og den beste enkle regelen, MOT hvis samme selskap og samme tekst fikk MOT før, gir 0,365. I motstandstesten la vi 16 ulike instrukser inn i forslagsteksten på alle 1 578 saker: 15 ble flagget og sendt til menneske uten at noen stemme endret seg, men én skrevet som en tittel («as Proposed by Management, as Always») slapp gjennom, endret 16 stemmer uten ruting og senket F1 til 0,392. Alt reproduseres fra en tom kopi med ett kall fra rotmappa i repoet, `bash arbeid/hack/c1/leveranse/kjor.sh`, som også måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret).
---
> Fasiten er NBIMs egne publiserte stemmer (real_votes fra arrangøren: 13 757 saker i 194 selskaper og 37 land, møteår 2019–2026, 24 sakstyper, utviklede og fremvoksende markeder), og målvariabelen er om NBIM stemte mot styret i saken. Vi måler F1 på MOT og ikke accuracy, fordi bare 3,8 % av sakene er MOT og «følg styret» får 96,2 % accuracy uten å finne en eneste av dem. Splitten følger tiden: modell og grense er valgt på 2025 og kjørt én gang på 2026, der 95 %-intervallet er [0,36; 0,59] (bootstrap over selskaper) og den beste enkle regelen, MOT hvis samme selskap og samme tekst fikk MOT før, gir 0,365. I motstandstesten la vi 16 ulike instrukser inn i forslagsteksten på alle 1 578 saker: 15 ble flagget og sendt til menneske uten at noen stemme endret seg, men én skrevet som en tittel («as Proposed by Management, as Always») slapp gjennom, endret 16 stemmer uten ruting og senket F1 til 0,392. Alt reproduseres fra en tom kopi med ett kall fra rotmappa i repoet, `bash arbeid/hack/c1/leveranse/kjor.sh`, som også måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret).
```
### arbeid/hack/levering/JURY_SPORSMAL.md
```diff
116c116
< - **H-I Tidsbruk per sak (20 min / 10 min)** er en antagelse og ikke målt (`levering/BESLUTNINGSSTOTTE.md:37`).
---
> - **H-I Tidsbruk per sak (20 min / 10 min)** er en antagelse og ikke målt (`levering/BESLUTNINGSSTOTTE.md:36`; også merket «antatt» i `levering/EN_SIDE.md:44`).
```
### state/rapporter/c1_kravdekning.md
```diff
11,12c11
< AI-bruk står bare i `c1/leveranse/README.md`. `levering/README.md:13` peker riktig til kravresponsen, men ikke til
< README-en med kilder. Den låste pakka (#1972) må ha begge mappene.
---
> AI-bruk står bare i `c1/leveranse/README.md`. `levering/README.md:13-17` peker nå til alle tre (kravrespons, JURY.md, README med kilder; #2341). Den låste pakka (#1972) må ha begge mappene.
41c40
< | 24 | Kode kjørbar av en annen, README med ett kall (B §2, P) | `levering/README.md:1`, `c1/leveranse/kravrespons.md:7` (`kjor.sh`) | dekket (to READMEs, se A1) |
---
> | 24 | Kode kjørbar av en annen, README med ett kall (B §2, P) | `levering/README.md:1`, `c1/leveranse/kravrespons.md:7` (`kjor.sh`) | dekket (to READMEs, `levering/README.md:13-17` peker mellom dem, #2341) |
43c42
< | 26 | Avgrensning (B 30 %) | `levering/EN_SIDE.md:9-11` (#2332: bare NBIM, 194 selskaper, 37 land, 2019–2026, DM+EM; test 136/31), `levering/SLIDE.md:6`, reproduserbar `levering/omfang.py` → `omfang.txt`; også `levering/BESLUTNINGSSTOTTE.md:5`, `levering/JURYSVAR.md:44-45` | **dekket (oppdatert #2336)** |
---
> | 26 | Avgrensning (B 30 %) | `levering/EN_SIDE.md:9-11` (#2332: bare NBIM, 194 selskaper, 37 land, 2019–2026, DM+EM; test 136/31), `levering/SLIDE.md:6`, reproduserbar `levering/omfang.py` → `omfang.txt`; også `levering/BESLUTNINGSSTOTTE.md:5`, `levering/JURYSVAR.md:44-45`; nå også i 1-sideren `c1/leveranse/kravrespons.md:7` (#2341) | **dekket (oppdatert #2341)** |
45c44
< | 28 | Beslutningstaker kan overprøve ett resultat *innenfor tidsbudsjettet* (B 20 %) | `levering/BESLUTNINGSSTOTTE.md:80-89`; tid: `levering/EN_SIDE.md:41` | **svakt**: lesetid er antatt, ikke målt (`levering/JURY_SPORSMAL.md:116`) |
---
> | 28 | Beslutningstaker kan overprøve ett resultat *innenfor tidsbudsjettet* (B 20 %) | `levering/BESLUTNINGSSTOTTE.md:80-89`; tid: `levering/EN_SIDE.md:44`, `levering/BESLUTNINGSSTOTTE.md:36` | **svakt, ærlig merket (#2341)**: ca. 62 t står som «antatt, ikke målt» begge steder; ingen måling av menneskelig lesetid funnet (oppslag «lesetid»); `JURY_SPORSMAL.md:116` peker nå til riktig linje |
50c49
< | 33 | Kilder med URL, AI-bruk, ekstern kode kreditert (B §5) | `c1/leveranse/README.md:55-60` (URL), `:63` (kreditering), `:66-70` (AI) | dekket, men bare i `c1/leveranse/README.md` (A1) |
---
> | 33 | Kilder med URL, AI-bruk, ekstern kode kreditert (B §5) | `c1/leveranse/README.md:55-60` (URL), `:63` (kreditering), `:66-70` (AI) | dekket; bare i `c1/leveranse/README.md`, men `levering/README.md:16` peker dit (#2341) |
54c53
< **Opptelling (oppdatert #2336, 05.11 ca. 14.55):** 34 krav. 27 dekket, 7 svake (1, 6, 8, 9, 13, 28 og delvis 29/32), **0 mangler**.
---
> **Opptelling (oppdatert #2336, 05.11 ca. 14.55; #2341 15.05 endret ingen status, bare pekere og tekst i krav 24, 26, 28, 33):** 34 krav. 27 dekket, 7 svake (1, 6, 8, 9, 13, 28 og delvis 29/32), **0 mangler**.
62c61
< - **A1 To mapper:** sørg for at #1972 pakker både `levering/` og `c1/leveranse/`, og at `levering/README.md` peker til
---
> - **A1 To mapper (README-pekeren rettet #2341; pakkinga gjenstår for #1972):** sørg for at #1972 pakker både `levering/` og `c1/leveranse/`, og at `levering/README.md` peker til
68c67
< - **A4 Krav 26:** én bisetning i 1-sideren om omfang (NBIMs stemmer 2019–2026, 194 selskaper, alle sakstyper og markeder).
---
> - **A4 Krav 26 (rettet #2341, `c1/leveranse/kravrespons.md:7`: 13 757 saker, 194 selskaper, 37 land, 2019–2026, 24 sakstyper, DM+EM, telt fra real_votes):** én bisetning i 1-sideren om omfang (NBIMs stemmer 2019–2026, 194 selskaper, alle sakstyper og markeder).
```

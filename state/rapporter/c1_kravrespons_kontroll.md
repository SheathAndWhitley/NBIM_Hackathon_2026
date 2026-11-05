# Case 1: kontroll av kravresponsen på én side (dommer #2245, 05.11 13:47)

**Dom nå: AVVIST (foreløpig).** Speider har ikke startet #2229 (status open 13:47), så det finnes ingen rettet énsider å godkjenne. Dagens filer bryter sidekravet. Den endelige dommen tas i **#2251** (dommer, venter på #2229) med sjekklista nederst.

## Regelen (Regler_og_bedommingskriterier.pdf, punkt 2–3)
Maks 1 side. Tre overskrifter: *Hva vi bygde* / *Hvordan vi verifiserte det* / *Hva vi ville trengt videre*, 3–5 setninger under hver, ingen markedsføring. (PDF-teksten sier «fem overskrifter», men lister tre; vi følger de tre.)

## Slik står det 13:47

| fil | ord | tegn | setninger per del | sider (cupsfilter 12pt, grovt mål) | pekt på fra |
|---|---|---|---|---|---|
| `c1/leveranse/kravrespons.md` (13:06) | 846 | 5316 | 13 / 18 / 8 | 2 | `c1/leveranse/README.md:6` |
| `levering/EN_SIDE.md` (13:18) | 547 | 3439 | 5 deler, ikke malens tre | 2 | `levering/README.md:13` |

Avvik funnet:
1. **For lang.** Malen gir 9–15 setninger totalt; kravrespons.md har 39. Begge rendres til 2 sider.
2. **To énsidere.** De to README-ene peker på hver sin fil. Juryen skal se én kravrespons, og `levering/KRAVRESPONS.md` (intern sjekkliste) sier det er `c1/leveranse/kravrespons.md`. Speider må velge én og la begge README peke på den.
3. **Kilder utenfor pakka.** Påstander belegges med oppgavenummer (#2115, #2134, #2095, #2098, #1952, #2047, #2144, #2106, #231). Juryen kan ikke slå dem opp. Hver påstand skal ha en fil i pakka som kilde (f.eks. `JURY.md`, `BEGRENSNINGER.md`, `kjor_agent_real_test2026.txt`) eller strykes.
4. **KI med to metoder.** Énsiderne sier [0,36; 0,59] (klyngebootstrap per selskap). `c1/tall_tabell.md` sier [0.37, 0.59] (radbootstrap). Begge er ekte, men énsideren må si hvilken metode, eller bruke tabellens tall.
5. **Måler-sha.** `tall_tabell.md` oppgir fil-sha256 **418a937e57** for `maaler_offisiell_v3.py` (bekreftet med shasum 13:44). Tavlas id for samme måler er 8b09c36e01 (sha av kommando + filer). Énsideren bør nevne måleren med `--score mot`; oppgis en sha, skal det være 418a937e57 og stå «sha256 av fila».

## Tall som er kontrollert mot `c1/tall_tabell.md` (13:38) og kald logg
Stemmer: F1 0,476, P 0,441/0,44, R 0,517/0,52, 58 MOT av 1539, TP 30 FP 38 FN 28 (68 flagget), følg styret F1 0, avvik inkl. AVSTÅ 0,4818 (66), til menneske 188 av 1578 og 183 av 1539 (`kjor_agent_real_test2026.txt` linje 2 og 23), val 0,520. Regel b2 0,365, h1 0,415 og +0,11 [0,01; 0,22] står ikke i tall_tabell.md, men i `c1/leveranse/JURY.md:45-51`; godtas med den som kilde.

## Sjekkliste for #2251 (GODKJENT krever alle)
- [ ] Én fil er kravresponsen, begge README peker på den, `KRAVRESPONS.md` i levering merket intern eller flyttet til arkiv.
- [ ] Maks 1 side: ≤ 3500 tegn og ≤ 450 ord, tre overskrifter fra malen, 3–5 setninger hver (tell med awk-linja i #2245).
- [ ] Hvert tall likt `c1/tall_tabell.md` eller `JURY.md`; KI med metode.
- [ ] Måler oppgitt som `c1/maaler_offisiell_v3.py --score mot` (sha256 418a937e57 om sha nevnes).
- [ ] Ingen påstand med bare #nummer som kilde.
- [ ] Ingen markedsføring; begrensningene (58 MOT, bredt KI, løpende historikk, sitat fra annen sak) står.

# Case 1: pakka peker ikke lenger ut av leveransemappa, og hullbeskrivelsene er oppdatert (speider #2269)

Fra dommerens forbehold 2 og 3 i `c1_kravrespons_dom_2251.md`. Mappe: `arbeid/hack/c1/leveranse/`.

## Akseptkrav
- `grep -rn "state/rapporter\|arbeid/oppgave_" arbeid/hack/c1/leveranse` gir **0 treff** (før: 19 i JURY/BEGRENSNINGER/ERLIG).
- `c1_tallvakt.py`: 14 filer, 158 påstander om hovedtallet, 0 avviker, OK. Ingen tall er endret.
- Alle `kilder/...`-pekere i de tre filene finnes på disk (sjekket).

## (b) Kilder kopiert inn i `leveranse/kilder/` (19 filer + LESMEG.md)
15 rapporter: c1_ablasjon_v2, c1_bommene, c1_enkle_regler_og_hist1, c1_injeksjon_etter_2205, c1_injeksjon_hoflig, c1_kjoretid,
c1_mot_sakstyper, c1_robusthet_frossen, c1_robusthet_sjekk, c1_siste_mot_forsok, c1_streng_mot, c1_tall_likt, case1_hvilken_fasit,
dommer_2090_streng_mot, dommer_ablasjon_v2. 4 arbeidsfiler: oppgave_2095_ki_mot.py, oppgave_2134_regler.py, oppgave_2216_tell.py,
oppgave_2234_baseline_real_test.txt. Kopiene har egne interne stier skrevet om (se kilder/LESMEG.md); tall og tekst er ellers uendret.
I regler.py peker utfila nå på gjeldende mappe i stedet for arbeidsmappa (eneste kodeendring).

Pekere skrevet om: JURY.md linje 6, 9, 21, 25, 29, 31, 37, 40; BEGRENSNINGER.md 7, 13 (også `c1_robusthet_sjekk.md` → `kilder/...`), 18, 30, 33;
ERLIG_EVALUERING.md 4, 29, 42, 65.

## (a) Hullbeskrivelsene, nå-tilstand
- JURY.md pkt. 11: ny overskrift «Instrukser skrevet i Title Case slipper gjennom». «Kindly support/oppose» beskrives som lukket av vakta #2237
  (med i frysen: `c1_frys.py`, kaldstart.sh og fremmed.sh har `injeksjon_hoflig.py`; test 2026 byte-lik). 15 av 16 fanget; Title Case-frasen gir 16 urutede, F1 0,392.
- JURY.md spørsmål 2: «kan lures» peker nå på Title Case-frasen (16 stemmer), ikke «kindly support» (20–21).
- JURY.md spørsmål 3 pkt. 1: «Tetter resten av injeksjonshullet», målt mot variantene i `kilder/c1_injeksjon_hoflig.md`.
- BEGRENSNINGER.md pkt. 3 injeksjon: gamle tall (35–41, 20–21, 0,387–0,400) står som «før vakta», lukket; Title Case-hullet står som åpent.
  «Gjør»-linja: «instrukser skrevet i Title Case slipper gjennom vernet».
- Angrepstallene (15/16, 16, 0,392) er tatt ordrett fra ERLIG_EVALUERING.md:42 og `c1_injeksjon_hoflig.md`; de står ikke i tall_tabell.md
  (der er bare rene måletall), og linjene har tallvakt-merket «tall under angrep» som før.

## Gjenstår
- Blir #2265 godkjent (Title Case fanget), må JURY pkt. 11/15/20, BEGRENSNINGER pkt. 3 og ERLIG:42 skrives om igjen (#1975 etter frys).
- ERLIG_EVALUERING.md:65 nevner fortsatt den gamle #2046-frasen som historikk; :42 forklarer at den er utdatert. Ikke endret.

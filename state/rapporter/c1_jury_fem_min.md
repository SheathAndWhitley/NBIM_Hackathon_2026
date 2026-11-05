# Case 1: README og kravrespons lest som jury med fem minutter (#2537)

Lest: `arbeid/hack/c1/leveranse/README.md` (75 linjer) og `kravrespons.md` (10 linjer), HEAD a29ea91 + arbeidskopi 16:40. Ingen filer endret (frys).

## Ja/nei
- **Står hovedtallet i første skjermbilde?** JA. README:8 gir F1 0,476 på MOT med KI og test 2026; kravrespons:4 gir 0,476, P 0,44, R 0,52 og «følg styret» 0.
- **Står «V1 står» tydelig i første skjermbilde?** NEI. Verken README eller kravrespons nevner at en bedre testvariant (V2, 0,516) finnes og hvorfor den ikke er hovedtall. Det står bare i JURY_SPORSMAL.md:81–83, som en jury med fem minutter ikke åpner.

## Fem forbedringer (prioritert)

1. **README:9, etter «Valgt på val 2025 (0,520).»** Uklart: juryen ser aldri at vi har en variant med høyere testtall og bevisst lar være å bruke den. Det er vårt sterkeste metodepoeng (60 %-vekten) og er skjult.
   Ny tekst (én setning i hovedtallsboksen):
   > «Vi leverer den frosne V1 med vilje. Varianten V2 gir 0,516 på test, men ble valgt etter å ha sett test og er innenfor støyen (V2 − V1 +0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.»
   (Tall fra JURY_SPORSMAL.md:81. Smed/dommer må bekrefte at dom #2529 = BEHOLD før innføring.)

2. **kravrespons:7, siste setning.** Skrivefeil: «Begge måler også måler svaret med …».
   Ny tekst: «Begge kaller måler svaret med vår egen `maaler_offisiell_v3.py` (F1 på MOT mot styret).» → helst: «Begge måler svaret med vår egen …».

3. **kravrespons:10, etter første setning.** Samme hull som pkt. 1 i kravresponsen, der juryen leter etter ærlig evaluering. Ny tekst:
   > «En variant med hybridløsningens sikre ja/nei gir 0,516 på test, men den ble valgt etter å ha sett test og forskjellen er innenfor støyen, så hovedtallet er den frosne agenten (0,476).»

4. **README:8–12 (hovedtallsboksen).** Uklart: fem tette linjer med to ulike KI-metoder, sidetall, rutingsbrøker (188/1578 og 183/1539) og to kjørekommandoer. Juryen må lete etter det ene tallet. Forslag: kutt boksen til tre linjer og flytt resten under:
   > **Hovedtall:** F1 **0,476 på MOT mot styret** (test 2026, NBIMs egne stemmer, 58 MOT av 1 539), 95 % KI [0,36; 0,59]. «Følg styret» gir 0. P 0,44, R 0,52.
   > Valgt på val 2025 (0,520), kjørt én gang på test. 188 av 1 578 saker (11,9 %) sendes til et menneske.
   > Reproduser: `sh KJOR.sh` i jury-zipen (`c1_stemmeagent/`).
   Rad-bootstrap-KI, sidetallet avvik 0,482 og repo-kommandoen kan stå i avsnittet «Ett kall …».

5. **README:3 «i alle sakstyper og markeder».** Overpåstand som juryen kan ta: data er 194 selskaper i 37 land (kravrespons:7). Ny tekst: «… i alle sakstyper og markeder i NBIMs stemmedata (194 selskaper, 37 land) …». Mindre viktig, men billig og ærlig.

## Ikke foreslått (er godt nok)
- README:42 og 50 forklarer at `SCORE 0.481752` er sidetallet; dobbelt, men trygt.
- kravrespons:10 sier selv at 0,476 er under målet 0,5 og at ~0,06 F1 hviler på en udokumentert antakelse om samme-sesong-stemmer. Det er ærlig og bør stå.

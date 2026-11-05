# Case 1: jurydrill, de 10 vanskeligste metodespørsmålene (smed2 #2244)

Jeg har spilt juryen (60 % metode og ærlig evaluering). Hvert svar har to linjer og en kilde i pakka med fil:linje.
Linjenumrene er lest 05.11 kl. 13.44. `c1_real.py` endres nå av #2237 (smed3), så linjene der kan flytte seg. Søk da på teksten i anførselstegn.
Stier: `c1/` = `arbeid/hack/c1/`, `lev/` = `arbeid/hack/levering/`. Modellen er ikke endret.

**1. Hvilke kolonner avslører svaret, og hvordan vet vi at modellen ikke leser dem?**
nbim_vote*, rationale_*, position_paper og funds_disagree er svartelistet, og en assert stopper treningen om en av dem brukes. Agenten nekter også inn-saker som har fasitfelt.
Bevis: `arbeid/oppgave_2044/train.py:15` (FORBUDT), `:24` (assert), `lev/c1_real.py:147` («inn-saken har fasitfeltet»), og vakta på svarfila `c1/sjekk_lekkasje.py:3-7`.

**2. Lekker den løpende historikken fra samme møte?**
Nei. Historikken bruker bare møter med dato strengt før saken (`merge_asof`, `allow_exact_matches=False`). Dommeren sjekket 400 tilfeldige rader mot brute force og fant 0 avvik.
Bevis: `oppgave_2044/train.py:47` og `:58`, `lev/ERLIG_EVALUERING.md:28` (#2098). Uten løpende historikk faller F1 til 0,415: `ERLIG_EVALUERING.md:29`.

**3. Er grensen eller modellen valgt på test?**
C og grense velges på val 2025 med trening på år før 2025. Test 2026 kjøres én gang med den låste råverdien `t`. Linja «samme andel flagget» bruker test-fordelingen, og agenten merker den som ikke-hovedtall.
Bevis: `oppgave_2044/train.py:101-110` (val), `:113-116` (test med `t`), `:117-118` og `lev/c1_real.py:90-92` (#2236).

**4. Hvorfor F1 på MOT, og ikke accuracy?**
«Følg styret» får 96,2 % accuracy og finner 0 MOT. Agenten får 95,7 % og finner 30 av 58. Accuracy belønner altså å gjøre ingenting.
Bevis: `lev/../c1/leveranse/JURY.md:7`, råutskrift i `arbeid/oppgave_2234/baseline_real_test.txt` (følg styret: `MOT mot styret: TP 0 … F1 0.0000`).

**5. Teller en MOT på et aksjonærforslag (der styret selv sier MOT) som «mot styret»?**
Nei. Måleren teller MOT bare når styret ikke sier MOT: `xs = mot and styret != "MOT"`. Regelen «aksjonærforslag = MOT» gir derfor F1 0,066. 56 av 58 MOT er på styrets egne forslag.
Bevis: `c1/maaler_offisiell_v3.py:101`, `c1/leveranse/JURY.md:9` og `:31` (BEGRENSNINGER pkt. 5). Om N-PX-fasiten som var lest feil: `state/rapporter/case1_hvilken_fasit.md`.

**6. Slår dere noe enklere enn «følg styret»?**
Ja, men med liten margin. Følg styret gir 0, beste enkle regel (b2: samme selskap og samme tekst fikk MOT før) gir 0,365, og modellen gir 0,476. Differansen er +0,11 med KI [0,01; 0,22], så vidt over null.
Bevis: `c1/leveranse/JURY.md:42-51`, kode i `arbeid/oppgave_2134/regler.py`.

**7. Hva skjer når noen planter en instruks i forslagsteksten?**
Direkte instrukser («stem FOR/MOT», norsk, roller, tagger) flagges. Teksten renses før modellen ser den, og saken går til menneske. Høflige instrukser («kindly support management») slapp gjennom i den frosne målingen: 20–21 stemmer byttet uten ruting.
Bevis: `lev/c1_real.py:158-164` (rens, EKSTRA_INJ, «hoflig.finn» fra #2237), rutingen «instruksjonslignende tekst» rundt `:225`, svakheten i `c1/leveranse/JURY.md:37`.

**8. Hvilke saker går til menneske, og hvorfor akkurat båndet [0,15; 0,85)?**
Til menneske går saker med kalibrert P(MOT) i båndet, pluss ukjent selskap, sakstype, land eller styreanbefaling, datafeil, injeksjon og MOT uten sitat. På test 2026 er det 188 av 1578 saker. Båndet er valgt blant tre ferdige kandidater, bånd 1 og 2 før måling.
Bevis: `lev/c1_real.py:220` («qlo <= q < qhi») og `:225-248`, `lev/kjor_agent.py:37-38`, `state/rapporter/c1_menneske_terskel.md:25`.

**9. Er P(MOT) en sannsynlighet?**
Ja, etter isotonisk kalibrering lært på val 2025 (score mot fasit). Det gir Brier 0,030 og ECE 0,016 på test. Kalibreringen er monoton, så MOT-flagget og F1 er de samme som uten den.
Bevis: `lev/c1_real.py:184-185`, `lev/c1_real.py:8-11` (docstring), `state/rapporter/c1_menneske_terskel.md:4-5`.

**10. Er 0,476 egentlig forskjellig fra målet 0,5, eller er det støy?**
Det er støy. 95 % KI er [0,36; 0,59] (klyngebootstrap per selskap), og én flyttet sak endrer F1 med omtrent 0,01. Forskjeller under ~0,02 kan ikke tolkes, så vi leser tallet som «rundt 0,5».
Bevis: `c1/leveranse/ERLIG_EVALUERING.md:32-34`, `c1/leveranse/BEGRENSNINGER.md:7` (koden er `arbeid/oppgave_2095/ki_mot.py`).

## Spørsmål pakka IKKE svarer godt på (til speider #1975)
1. **Hvor mange ganger er test 2026 sett før frys?** Tavla viser mange målere og forsøk på test (ablasjon, bånd, regler, h1). Pakka sier «ingen variant valgt på test» (`ERLIG_EVALUERING.md:34`), men oppgir ikke hvor mange varianter som ble målt på test. Juryen kan kalle det indirekte tilpasning til test. Forslag: én linje med antallet, og at #2044 ble frosset ut fra val.
2. **`train.py` sier noe annet enn den gjør.** Docstringen (`oppgave_2044/train.py:5-6`) sier «Ingen etiketter fra samme sesong», men agenten kjører `--hist 2`, som bruker samme sesong strengt før dato. Fila er frossen (sha), så den rettes ikke. JURY eller README bør si at docstringen gjelder h1, ellers ser det ut som skjult lekkasje.
3. **`injection_flag`:** FORBUDT.md:14 og `sjekk_lekkasje.py:15` kaller den forbudt, men agenten leser den fra input til ruting (`lev/c1_real.py:164`). Treningen kaster rader med flagget (`train.py:28`). Feltet står i arrangørens input (`real_test_input.csv`), så det er trolig lov, men det er ikke forklart. Kostnaden er heller ikke målt: hvor mange test-saker rutes bare på grunn av arrangørens flagg?
4. **Valget av bånd er ikke bevist tatt før test.** `oppgave_2128/baand.py` regner val og test i samme kjøring, og rapporten sier at bånd 3 ble endret etter at testtallene var sett (`c1_menneske_terskel.md:25`). Det finnes ingen tidsstemplet logg som viser at [0,15; 0,85) ble valgt på val alene.
5. **Holder kalibreringen når modellen byttes?** Isotonien er lært på score fra modellen trent på år før 2025. Den brukes på modellen trent på år før 2026, og rangsnittet kan forskyve seg mellom de to. Brier og ECE på test (pkt. 9) er et indirekte svar, men pakka begrunner ikke overføringen.
6. **Injeksjonstallene etter #2237 finnes ikke ennå.** Pakka sier at høflige instrukser slipper gjennom (JURY.md:37, BEGRENSNINGER pkt. 3), mens koden nå har `injeksjon_hoflig` (#2237). Etter #2241/#2246 må tekst og tall samsvare med den frosne koden kl. 16. Ellers beskriver papirene en annen agent enn den som leveres.
7. **Hva koster mennesket?** 188 saker til menneske, men ingen anslått lesetid og ingen kostnad per fanget MOT i JURY.md. Tallene finnes i `state/rapporter/c1_ruting_kostnad.md`, men står ikke i pakka.
8. **Treff per marked og sakstype** er ikke målt (innrømmet i BEGRENSNINGER pkt. 4). Juryen vil spørre om 0 av 7 MOT i USA betyr at agenten ikke kan brukes i USA.

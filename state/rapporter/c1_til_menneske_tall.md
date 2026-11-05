# Case 1: stemmer tallene for «til menneske» overalt? (dommer2, #2347, 05.11 kl. 15.05)

## Fasit (regnet selv fra `arbeid/oppgave_2132/agent.csv` + `state/opplastet/20261105_114241_real_votes.csv`, samme filter som `c1/menneske_tabell.py`)

| tall | verdi | nevner |
|---|---|---|
| til menneske, agenten | 188 (11,9 %) | 1578 saker inn |
| til menneske, måleren | 183 (11,9 %) | 1539 med fasit (test 2026, uten injeksjonsrader og uten tom `against_board`) |
| grunn: bånd [0,15; 0,85) | 127 av 1578 / 122 av 1539 | 10 av dem har også «ukjent selskap» |
| grunn: ukjent selskap | 70 av 1578 (60 uten bånd) | |
| grunn: instruks | 1 | |
| sum | 127 + 70 + 1 − 10 overlapp = 188 | ✓ |
| FN rutet | 11 av 28 (7 bånd, 3 ukjent selskap, 1 instruks) | ✓ `c1_bommene.md:26` |
| MOT i sonen | 32 av 58 (21 TP + 11 FN), alle 38 FP | ✓ JURYSVAR, EN_SIDE, TREFFSIKKERHET, JURY.md, DEMO_MANUS |
| India | 25 av 103 til menneske | ✓ `c1_bommene.md:36` |

188 og 183 er begge riktige; nevneren er ulik. Ingen vakt for ukjent type, land/marked eller styreanbefaling slo til i standardkjøringen,
så regelen «bånd + ukjent selskap + instruks» dekker alle 188. Nevner og prosent stemmer i alle 50 filene som nevner tallet,
med avvikene under.

## Avvik (ikke rettet, bare listet)

1. **`levering/KRAVRESPONS.md:43`** sier «Agenten sier 176 til menneske (av 1578 inn), måleren 171 (av 1539 vurderte)». Gamle tall fra før
   vaktene i #2152. Foreslått tekst: «Agenten sier 188 til menneske (av 1578 inn), måleren 183 (av 1539 med fasit).» Alternativt stryk
   setningen, siden #2095-notatet rett under sier hullet er tettet.
2. **`levering/KRAVRESPONS.md:61`** (krav 11): «kalibrert P(MOT) i [0,15; 0,85) låst på val». Motsier `c1/leveranse/ERLIG_EVALUERING.md:44`,
   `c1/leveranse/JURY_SPORSMAL.md:27`, `EN_SIDE.md:13` og `SLIDE.md:12`, som alle sier båndet er valgt på test-tabellen og sjekket på val.
   Foreslått: «kalibrert P(MOT) i [0,15; 0,85) (kalibrering lært på val; båndet valgt på test-tabellen og sjekket på val, 7,5 % val / 7,9 % test)
   + ukjent selskap/type + injeksjon + datafeil».
3. **`levering/kjor_agent_real_test2026_LES.md:11`**: «(linje 3, låst på val 2025)». Samme feil om båndet. Foreslått: «(linje 3; loggen skriver
   «låst på val» om C og grensen, båndet er valgt på test-tabellen og sjekket på val, se `c1_menneske_terskel.md`)».
   Merk: selve loggteksten kommer fra `c1_real.py:296–297` og er frossen; den skal ikke røres, bare forklares.
4. **`c1/leveranse/kilder/c1_menneske_terskel.md:8–23`**: tabellen teller 66 avvik («MOT i båndet 30 av 66», «45 % av alle MOT», F1 0,766),
   ikke 58 MOT mot styret som resten av pakka. Tallene er ikke feil, men definisjonen er en annen enn hovedtallet. Foreslått merknad
   øverst, under overskriften: «Tabellen teller avvik fra styret (66), ikke MOT mot styret (58). Med 58: båndet fanger 27 av 58 (47 %),
   standardsonen 32 av 58, øvre grense F1 0,779 / 0,828 (`c1/menneske_tabell.py`). 167 var standardsonen før datavaktene i #2152; nå 183.»
5. **`c1/leveranse/JURY.md:41`** og **`c1/leveranse/README.md:11`**: «127 usikre …, 60 ukjent selskap, 1 instruks». Summen 188 stemmer bare
   fordi 60 er «ukjent selskap uten bånd»; 70 saker har grunnen. Foreslått: «127 usikre (kalibrert P(MOT) i [0,15; 0,85)), 60 bare ukjent
   selskap (70 i alt, 10 av dem også i båndet), 1 instruks».
6. **`levering/TREFFSIKKERHET.md:24` og `:54`** bruker målerens etikett «konfidens < 0,6» uten forklaring. Kopien i
   `c1/leveranse/kilder/TREFFSIKKERHET.md:7` har fått merknaden fra #2345; levering-kopien har den ikke. Foreslått: samme merknad som linje 7 i kilder-kopien.
7. **`levering/c1_v1/`** (leveranse 1, 12:55) ligger i levering/ uten å være nevnt i `levering/README.md`. `c1_v1/ut/KJORING.txt:2` sier 228 av 1578
   og `c1_v1/kravrespons.md:4` sier «bånd låst på val 2025, standard 10 %» (den gamle prosentregelen). Mappas egen README sier hva den er,
   men en jury som åpner den først får gale rutingstall. Foreslått: flytt til `levering/arkiv/c1_v1/` eller legg én linje i
   `arkiv/LES_KJORING.md`: «`c1_v1/` er leveranse 1 (12:55) med den gamle 10 %-regelen (228 av 1578). Gjeldende: 188 av 1578.»

## Sjekket og riktig (ingen endring)
EN_SIDE.md:39, JURYSVAR.md:30/32/36, BESLUTNINGSSTOTTE.md:20/75/76 (122 i båndet, 183 i alt), README.md:44/69/77, KRAVRESPONS.md:16,
TREFFSIKKERHET.md:24 (1356 = 1539 − 183) og :61, JURY_SPORSMAL.md:36/80 (71 % = 41/58), DEMO_MANUS.md:34/45/56/57, demo_utskrift.txt:28/42
(«122 slike» er båndet blant de 1539 med fasit, demo_vis bruker fasit), c1/leveranse/JURY.md:13/36, BEGRENSNINGER.md:34, c1_bommene.md:26/36,
c1_robusthet_frossen.md:42, demo/reserve/*.txt, arkiv/LES_KJORING.md (gamle 10/15 %-kjøringer er merket). `demo/README.md:21`
(«konfidens < 0,6», Vanguard) gjelder N-PX-stubben, ikke agenten, og står under den overskriften.

Kommando for å gjenskape fasit-tabellen: `python3 -I arbeid/hack/c1/menneske_tabell.py arbeid/oppgave_2132/agent.csv`.

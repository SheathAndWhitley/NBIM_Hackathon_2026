# Case 1: jury-zipen lest som en jurymedlem (sak 2459)

Zip bygget med `pakk_jury.sh` i en mktemp-mappe (113 filer, 0.476190 og TALLVAKT GRØNN), pakket ut, og jeg leste
`README.md` og `arbeid/hack/c1/leveranse/JURY.md` ovenfra. Ingen filer er endret.
**Alle filpekere i JURY.md (29 stk.) finnes i zipen.** Det som stopper leseren, er ord og tall, ikke manglende filer.
Linjenumrene viser til den utpakkede zipen (`c1_stemmeagent/`). Punktene er sortert etter skade.

1. **JURY.md:76 (pkt. 11) sier to ting som ser ut til å motsi hverandre.** Overskriften er «Instrukser av bare tittelord slipper gjennom», så kommer «hullet er lukket … alle 16 instrukser fanges», og til slutt «av 16 nye … slipper 6 forbi». To ulike 16-ere og «lukket/åpent» i samme avsnitt. En jury leser det som selvmotsigelse om robusthet (40 %-delen).
   *Retting:* del i to setninger med ulike navn: «Høflige instrukser (16 varianter): alle fanges. Tittelinstrukser (16 nye varianter): 10 fanges, 6 slipper forbi, F1 0,39–0,42.»
2. **JURY.md:9, 16, 21 og 67: uforklart sjargong i de første linjene:** «miks h2», «måler v3», «val 2025», «golv», «løpende historikk» og «klyngebootstrap». Juryen møter «miks h2» før den vet hva modellen er.
   *Retting:* én ordliste-linje under «Les dette først»: miks h2 = LightGBM + logistisk regresjon på sakstekst og NBIMs tidligere stemmer (rangsnitt). Val = valideringsår. Måler v3 = arrangørens måler med datavakt. Smeden må sjekke at forklaringen av miks h2 stemmer med train.py.
3. **To nevnere: 1539 og 1578 saker.** JURY.md:9 og 34 bruker 1539, men JURY.md:70 og 73 bruker 1578 («188 av 1578» og «183 av 1539» i samme punkt). At 39 saker mangler fasit, står ingen steder. Juryen tror tallene ikke henger sammen.
   *Retting:* i «Slik målte vi» (linje 9): «1578 saker i test 2026, 39 uten NBIM-stemme; F1 telles på de 1539 med fasit».
4. **Root-README peker ikke rett på JURY.md.** README.md:63 nevner JURY.md i en tabell uten sti, og zipen har to README.md (rota og `leveranse/`) som er ulike. Juryen vet ikke hvor den skal begynne å lese.
   *Retting:* øverst i README.md, etter linje 5: «Les først: `arbeid/hack/c1/leveranse/JURY.md` (1 minutt), så ERLIG_EVALUERING.md.»
5. **«pkt. N» betyr to ulike lister.** JURY.md:6, 35, 36 og 37 viser til JURY sine egne Begrensninger (pkt. 3, 8, 9, 11, 12). JURY.md:24, 29, 54 og 74 og README.md:3 og 35 viser til `BEGRENSNINGER.md pkt. N`. Linje 6 sier bare «pkt. 8 og 9», og da ser det ut som BEGRENSNINGER.md.
   *Retting:* skriv «Begrensninger pkt. 8 nedenfor» der det gjelder JURY selv.
6. **JURY.md:9: målingen kan ikke gjentas slik den står beskrevet.** Teksten sier «kald kjøring med `kjor.sh` fra tom mappe `/tmp/c1_kald` … se `README.md`», men leveranse/README.md:32 sier selv at `kjor.sh` bare virker i repoet. I zipen er det `sh KJOR.sh`.
   *Retting:* «Gjenta: `sh KJOR.sh` i rota av zipen (samme tall, 0.476190).»
7. **README.md:11 har interne numre: «(#2417, #2421)».** Det er det eneste stedet med #-numre i de to filene.
   *Retting:* stryk parentesen.
8. **README.md:47: «4. Uavhengig telling» står etter kolonnetabellen,** atskilt fra trinn 1–3 (linje 15–17). Det ser ut som et løsrevet punkt, og `/tmp/c1_sjekk` er ikke forklart (det er bare en utmappe).
   *Retting:* flytt den rett under trinn 3 og skriv «(utmappe, kan være hvilken som helst)».
9. **JURY.md:12: setningen om ny sha 418a937e57 er utviklerstøy.** Den er sann, men får juryen til å lure på om måleren er endret.
   *Retting:* kort ned til «Måler v3 (sha i FROSNE_SHA256.txt)» eller flytt forklaringen til ERLIG_EVALUERING.
10. **JURY.md:67 og 76: interne ord og numre.** «ablasjonstabellen» står uten peker (hvilken?), «forsøk 2363», «sak 2366», «kjørt av dommeren» og «kontrollagenten» (linje 73) er ikke forklart. Juryen kjenner ikke rollene i landsbyen.
   *Retting:* «ablasjonstabellen» blir `kilder/c1_ablasjon_v2.md`, «dommeren» blir «en uavhengig kontrollkjøring», og forsøk- og saksnumrene strykes.

Mindre ting, ikke tatt med i de 10: JURY.md:57 peker på `c1_enkle_regler_og_hist1.md:1`, men den linja er bare overskriften (der står «dommer2 sak 2134»). 9 kildefiler nevner ~, og det sier README.md:71 fra om selv.

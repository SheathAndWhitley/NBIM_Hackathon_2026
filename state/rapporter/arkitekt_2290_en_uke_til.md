# Case 1: «Hva vi ville gjort med en uke til», med målte tall (avsnitt til JURY.md, #2290)

Pakka er ikke rørt. Avsnittet under er ferdig til å limes inn i JURY.md under juryspørsmål 3 av speider (#1975)
etter frysen. Alle tall er målt på val 2025 (trent <2025) eller holdt-ut 2024. Ingen tall er valgt på test 2026.

---

**Det vi har målt, og hva en uke til ville gått til.** Agenten står i dag på F1 0,520 for MOT på val 2025.
Vi har allerede prøvd tre forbedringer. Ingen av dem holdt seg over flere år, og det sier mer enn tallene hver for seg:
1. **Gammel MOT-historikk på styrevalg får forfalle.** På val 2025 steg F1 fra 0,520 til 0,551, med presisjon
   på styrevalg 0,56 → 0,63. På holdt-ut 2024 falt F1 fra 0,567 til 0,552. Differansen er +0,026 [−0,013; 0,070]
   på 2025 og −0,015 [−0,043; 0,017] på 2024 (klyngebootstrap over møter). Vi bygde den ikke inn
   (`kilder/arkitekt_tiltak1_malt.md`). Med en uke til ville vi gjort valg på to år til fast regel:
   hver variant måles på både 2024 og 2025 før den tas i bruk. Vi ville startet med trekkene for samme person.
2. **Regelen «styrevalg i USA → menneske».** Den løftet test 2026 fra 0,476 til 0,504, men senket val 2025
   fra 0,520 til 0,488. Den er tilpasset én sesong og er ikke lagt inn. Med en uke til ville vi heller prøvd
   et sjekklistekort for revisorvalg og andre styresaker, der NBIMs grunn (GVG 4.3/5.1) ikke står i teksten.
   Taket er F1 0,601 på val, og bare hvis mennesket treffer. Ren ruting uten at mennesket treffer gir 0,506.
   Kravet er en blind lesning av 20 val-saker som viser F1 over 0,520 med under 15 % av sakene i bunken.
3. **Sjekke antakelsen modellen hviler på.** At historikken er *løpende* (stemmer fra tidligere møter
   samme sesong) gir +0,07 på val (0,448 → 0,522). Uten historikk faller F1 til 0,337. Det største ukjente er
   derfor ikke en ny modell. Det er om NBIMs stemmer faktisk er kjent før neste møte. Er de ikke det, er det
   ærlige tallet 0,415 på test. Dag 1 ville gått til å måle publiseringsforsinkelsen fra NBIMs stemmelogg.

Usikkerhet: val har 103 MOT, 2024 har 98. Én sak er omtrent ±0,01 F1, så gevinster under ~0,03 på ett år kan ikke
skilles fra støy. Derfor krever vi to år.

---

## Kilder (for dommerens tallsjekk #2255)
- 0,520 / 0,551 / 0,567 / 0,552 / KI: `state/rapporter/arkitekt_tiltak1_malt.md`, logger `arbeid/oppgave_2283/log_t1*_tau1.txt`, `log2024_t1*_tau1.txt`
- USA-ruting 0,476→0,504 / 0,520→0,488, sjekkliste-tak 0,601 og 0,506: `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` (kilde `c1_feil_stabilitet.md`)
- h1/h2 0,448/0,522, uten historikk 0,337: `state/rapporter/c1_ablasjon_v2.md`
- 0,415: `arbeid/hack/c1/leveranse/JURY.md` pkt. 7 (`kilder/c1_enkle_regler_og_hist1.md`)
- Kilden kalles `kilder/arkitekt_tiltak1_malt.md` i avsnittet. Den må kopieres til `leveranse/kilder/` ved innliming, eller så må lenken byttes.

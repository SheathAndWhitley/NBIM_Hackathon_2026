# Case 1 #2929: ingen ny natt-kandidat med ekte grunn til +0,02 over v2+av (arkitekt, 05.11 ca. 20:40)

**Svar:** Jeg fant ingen vinkel med ekte grunn til å gi +0,02 i snitt. Derfor står det ikke noe REGEL.md-utkast eller noen byggeoppskrift her. Én ny vinkel (møtekontekst) er prøvd og tapte. I tillegg viser et tak at grense- og flaggtall-sporet ikke kan nå +0,02, selv med fasit. Under står tallene.

## 1. Ny vinkel prøvd: møtekontekst som trinn 2 (ikke prøvd før, sporsjekk «møte»: #1970 var tom på v3, ikke real_votes)
- **Grunn:** På real_votes har et møte i snitt 11,5 saker. MOT kommer i klynger. P(MOT) er 9,3 % når en annen sak i samme møte er MOT, mot 3,4 % ellers, og 62 % av MOT-ene ligger i møter med 2 eller flere MOT. v2 skårer hver sak for seg.
- **Prøve** (`arbeid/oppgave_2929/mote.py`): Trinn 2 er en logistisk regresjon på [logit rang p, snitt og maks rang p for de *andre* sakene i møtet, log antall saker, andel styrevalg]. Den trenes på v2-skår for 2021 og brukes én gang på 2022. Det er rene treningsår: verken testår eller vakt-år 2023 er rørt. v2 er kjørt med `--testaar 2022/2023 --k 32`, logger i mappa.
- **KP:** Jeg forventet at v2-grunnlinja for 2022 ble lik `v2_2022.log` (0,4615 med rå grense). Jeg fikk PR-AUC 0,3832, identisk med loggen. Med rang-andel-grense ble F1 0,3934. Skåren er altså den samme, bare grensen er overført på en annen måte.

| 2022 (trent på 2021) | PR-AUC | F1 med valgt grense | F1 topp 60 | topp 80 | topp 100 | topp 120 |
|---|---|---|---|---|---|---|
| v2 alene | **0,3832** | 0,3934 | 0,3503 | **0,4670** | 0,4977 | 0,4746 |
| v2 + møtekontekst | 0,3727 | 0,4955 | 0,3390 | 0,4162 | 0,4977 | 0,4895 |

- **Tolkning:** +0,10 på valgt grense ser stort ut, men det er bare et annet antall flagg (105 mot færre). Med likt antall flagg og med PR-AUC er møtekonteksten lik eller *dårligere*. Rangeringen blir altså ikke bedre. Klyngene er allerede fanget av `prev_meeting_any_dev` og den løpende selskapshistorikken (`--hist 2`). **Lukket.**

## 2. Tak for grense og flaggtall på v2+av (lukker hele grense-familien med ett tall)
Fasit på testårene er brukt *bare* til å regne et øvre tak, ikke til å velge noe. Målt med sklearn på `c1_natt/v2av/svar/` gir det 0,5684/0,5608/0,5556. Offisiell måler gir 0,5731/0,5667/0,5391, så det er litt avvik i ID-filteret, men differansen gjelder likevel.

| år | levert v2+av | beste antall flagg (fasit) | beste k uten av-regel (fasit) |
|---|---|---|---|
| 2024 | 0,5684 (92 flagg) | 0,5745 (90) | 0,5714 (112) |
| 2025 | 0,5608 (86) | 0,5608 (86) | 0,5484 (83) |
| 2026 | 0,5556 (60) | 0,5913 (49) | 0,5862 (50) |
| **snitt** | 0,5616 | **0,5755 (+0,014)** | 0,5687 (+0,007) |

En grense valgt med fasit gir bare +0,014. Ingen ærlig grense-, terskel-, andel- eller flaggtall-regel kan derfor nå +0,02 (jf. #2703 midt-terskel). Sporet er lukket med tall.

## 3. Hva som må være sant for +0,02 (baklengs)
Gevinsten må komme fra bedre *rangering*, altså høyere PR-AUC på MOT, og ikke fra grensen. Det krever informasjon som ikke ligger i trekkene i dag. Det som er prøvd og ikke flytter rangeringen: forklaringstrekk (#2907/#2919), tidsvekt (#2910/#2920), møtekontekst (her), selskapsnivå (#1970) og drop-one-trekk (#2888). Det jeg kjenner til av ny informasjon er revisorens år og honorar, til tiltak 2 i NESTE_VERSJON.md. Den finnes ikke i arrangørens data, så den kan ikke bygges i natt uten nye data.

## Trukne vinkler (#156)
Trekningen ga tre kort:
- astronomi + tuning: «hva ville forrige vinner gjort»
- kompilatorer + lavrang: «fjern antakelse X»
- fluiddynamikk + DP over grense: «bytt rekkefølge»

Tallene per kort:
- **DP over grense** har fått tall: taket i pkt. 2 er +0,014 og under kravet. Tapt.
- **Fjern antakelsen «én modell for alle sakstyper»** ble ikke målt. Grunnen er at MOT per type er lite (DISCHARGE 114, SAY_ON_PAY 45, ARTICLES 34 over alle år). Egne modeller per type ville trent på 5–15 positive per år, under frøstøyen.
- **Lavrang** er allerede i bruk (SVD k=32–64 i v2).

## Anbefaling
- Ingen ny kandidat til 02-dommen (#2874). v2+av står som natt-leder (frø-snitt 0,5571).
- Smedtid i natt gir mer på robusthet og ærlighet (2023-vakt #2927, frø-snitt #2926) enn på jakt etter +0,02.
- Fortsetter natta, er neste reelle vinkel nye data (revisor, til tiltak 2) og ikke flere trekk fra de samme kolonnene.

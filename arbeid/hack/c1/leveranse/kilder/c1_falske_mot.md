# Case 1: hvorfor agenten sier falsk MOT i USA og på styrevalg (#2357)

Grunnlag: frossen agent #2044 på test 2026 (arbeid/oppgave_2087/svar_test.csv), fasit fra real_votes.csv.
Skript: `arbeid/oppgave_2357/fp_historikk.py` (hver FP med NBIMs tidligere stemme på samme person / samme sakstype
hos selskapet) og `arbeid/oppgave_2357/snu_rate.py` (snurate 2025→2026). Ingen modell er endret.

## Til juryen (kort)
Alle 9 falske MOT i USA gjelder personer eller saker der NBIM stemte MOT før og så snudde til FOR i 2026.
Fire av dem (Dueser, Kemper, Swift, Jordan) fikk MOT nesten hvert år 2019–2025 (Jordan fikk FOR i 2021–22), med samme begrunnelse om å skille
rollene som styreleder og daglig leder. I 2026 stemte NBIM FOR alle fem amerikanske styremedlemmer som fikk MOT
i 2025 (5 av 5). Fra 2024 til 2025 holdt NBIM fast på MOT i 4 av 4. Samme år stemte NBIM FOR aksjonærforslaget
«Require Independent Board Chair» hos HP. Prinsippet ser altså ut til å stå, men det brukes ikke lenger
som grunn til å stemme mot personen. Agenten lærer av historikken og ser ikke at
praksisen har endret seg. I USA 2026 er det bare 1 MOT på styrevalg (Comfort Systems), mot 16 i 2025.
De amerikanske MOT-stemmene i 2026 gjelder nå grunnleggende aksjonærrettigheter: flytting fra Delaware til Texas,
krav om supermajoritet og opsjonsprogram.

Agenten overser:
- **Praksisskift i USA i 2026**: NBIM stemmer ikke lenger mot en leder som også er styreleder (5/5 snudd), selv om dette ga MOT hvert år før.
- **Gammel historikk teller for mye**: Havner (Public Storage), Michael Dell og Durban (Dell) fikk MOT sist i 2022, 2022 og 2023, og FOR alle senere år. Agenten sa likevel MOT.
- **Lønnssaker som snur**: CCC og Snowflake fikk MOT på say-on-pay i 2024 og 2025 og FOR i 2026. Det samme ser vi i Belgia (Colruyt, D'Ieteren), Sveits (Arbonia) og Tyskland (PVA TePla).
- **Gjelder alle land**: 22 av de 38 falske MOT har en tidligere MOT på samme person eller samme sakstype og snudde i 2026. Bare 5 hadde slik historikk uten noen MOT, og 11 hadde ingen historikk (blant annet Colruyts holdingselskaper, Fine Organic og NMDC Steel).
- **Agenten svarer bare «sa nei sist» eller «sa ja sist»**: Den har ingen variabel for at NBIM nylig har sluttet å bruke en begrunnelse. Det ble ikke rettet før frysen kl. 16. Mulig neste steg er å vekte siste år tyngst og ha et flagg for «denne begrunnelsen er ikke brukt i år».

## Tall
- 38 FP totalt, 26 på DIRECTOR_ELECTION, 9 i USA (7 styrevalg og 2 say-on-pay), 0 TP i USA.
- Snurate for samme person som fikk MOT året før: 2024→2025: USA 4 av 4 fortsatt MOT, andre land 14 av 17.
  2025→2026: USA 0 av 5 fortsatt MOT, andre land 10 av 14.
- Begrunnelsen om at rollene som styreleder og daglig leder skal skilles, i USA: 5 rader i 2025, 1 i 2026.
- Forbehold: personene er matchet på normalisert forslagstekst i samme selskap, så en og annen person kan mangle.
  2026-dataene gjelder bare møter fra 16.04 til 29.06.

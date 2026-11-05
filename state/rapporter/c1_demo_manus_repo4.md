# Case 1 (#2659): demo-manuset og støttefilene er oppdatert fra 0,476 til repo4 (0,512)

Tallene er målt på nytt fra dommerens kalde kjøring av jury-zipen (sak 2596, `/tmp/c1_dom_2596/zt`), ikke hentet fra hukommelsen.
`arbeid/oppgave_2659/maaling.txt` (måler v3 --score mot på kald pred_maaler.csv, sha d02cf884 = frossen):
TP 32 FP 35 FN 26, P 0,4776, R 0,5517, F1 0,5120. 161 av 1539 saker (10,5 %) gikk til et menneske.
`arbeid/oppgave_2659/telling.txt`: FN maskin 18 / menneske 8, FP maskin 3 / menneske 32.

**Demosakene var byttet.** `vis_manussaker.py` på den kalde agent.csv (sha 24ee6b18) ga AVVIK. Treff: linje 15 (Kura Sushi, p 1.0, maskin). Bom: linje 89 (LOTTE, p 0.0887, uendret). Menneske: linje 39 (Lundbeck, p 0.23; NBIM stemte FOR).
Sakene er valgt etter samme regel som før (første sak av hver type) og ikke håndplukket. Mobimo er fortsatt et treff, men ikke det første.

## Endret
- `DEMO_MANUS.md`: hovedtallet er nå 0,512, KI 0,40–0,62, 32 av 58 og 48 %. De tre sakene og sitatene er byttet. Teksten om stille feil sier nå «18 uten kontroll, 32 av 35 falske MOT til menneske (3 uten)», og rutingstallet er 161/10,5 %. Tallkildene peker på de nye filene. 0,476 står bare i et avsnitt merket «Eldre frossen modell».
- `vis_manussaker.py`: MANUS-tabellen har fått de nye id-ene (15/89/39). Den sier MANUS OK på den kalde kjøringen, så skjermen viser ikke AVVIK under demoen.
- `DEMO_MANUS_5min_tilfeldige.md`: har fått et banner om at sakstabellen er fra den eldre frosne modellen. Linjene 24, 25 og 91–92 og rutingstallet er oppdatert til repo4.
- `JURY_METODE.md:27`: KI for repo4 er [0,40; 0,62], og den eldre er merket. Linjene 19 og 28 var allerede rettet av andre (4fe23fe).
- `tall_tabell.md` og `lag_tall_tabell.py`: ablasjonsradene heter nå «ablasjon #2045 (eldre frossen #2044)». Rad 11 var allerede merket.
- `SVAKHETER.md`: var allerede rettet i arbeidstreet, på norsk og engelsk. Jeg har ikke rørt den.

## Sjekk
- grep 0,476/0.476 i de fem filene: alle treff er merket eldre/eldre frossen.
- Tallvakt på de fem filene: 20 påstander, 0 avvik. Full tallvakt: 31 filer, 197 påstander, 0 avvik (GRØNN).
- Frysvakt GRØNN (21 filer, 17:18:18). Jeg har ikke rørt kravrespons, ERLIG, JURY_SPORSMAL eller MUNTLIG.
- Merk for zipen kl. 19 (#2549): demoen krever den nye `vis_manussaker.py`. Med den gamle versjonen viser skjermen AVVIK.
- Commit: ca8a902 (støttefiler, rapport). DEMO_MANUS.md og vis_manussaker.py ble tatt med i #2665 sin commit e809b13 som ble laget samtidig; innholdet er mitt og ligger i HEAD.

## Muntlig svar: «Lekket fremtiden inn i modellen?» (#2760)
Si høyt (ca. 25 sek), tall identiske med JURY_SPORSMAL sp. 24:

> Nei, ingenting fra senere datoer går inn. Den ene svakheten vi fant selv er møter samme dag: NBIM-repoets `ballot.py` lar et annet møte i samme selskap samme dato telle som «tidligere», og det gjelder 15 av 400 rader. Vi målte effekten ved å bruke bare strengt tidligere datoer: 1 flagg endres, og F1 på MOT flytter seg −0,008, −0,016 og +0,052 over de tre testårene, snitt fra 0,5162 til 0,5254, fordi modellvalget skifter, ikke fordi lekkasjen ga treff. Det kvalifiserer ikke etter bytteregelen vi satte før måling, så levert modell står.

Kilde: `arbeid/hack/c1/leveranse/JURY_SPORSMAL.md` sp. 24, `kilder/c1_lekkasje_effekt.md`.

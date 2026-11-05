# Case 1: jurysvar på «hvorfor sendes alle ukjente selskaper til et menneske?» (#2324, speider)

**Svar (3-4 setninger, klart for JURY.md i #1975):**

Et selskap der NBIM aldri har stemt før, har ingen tidligere stemmer agenten kan lene seg på og ingen presedens den kan vise til, så her bestemmer vi med vilje at et menneske tar saken. Det er en regel vi har valgt, ikke et tegn på at modellen er usikker: på val 2025 ville usikkerhetsbåndet alene bare sendt 8 av 98 ukjente saker (8,2 %) til et menneske, nesten det samme som for kjente selskaper (7,5 %). Regelen koster lite og fanger alle: de 98 ukjente sakene inneholder bare 3 stemmer MOT styret, og alle 3 havner hos et menneske. Prisen er at ukjente selskaper utgjør 98 av de 234 sakene som går til et menneske (42 %), og bare 3 av 98 blir MOT, så regelen er en bevisst forsiktighet på et lite utvalg og ikke noe vi har bevist at lønner seg.

**Kilde for hvert tall:** `state/rapporter/c1_uten_historikk_ruting.md` (#2305, smed3), som har rådata i
`arbeid/oppgave_2305/analyse_ut.txt`. Val 2025, 1909 saker med fasit, modell trent på år < 2025, frossen #2044.
- 98 saker, 3 MOT, 98 av 98 rutet, 3 av 3 MOT rutet: tabellraden «uten historikk».
- 8 av 98 = 8,2 % og 7,5 % (136 av 1811): avsnittet «Båndet alene» i analyse_ut.txt.
- 234 rutet totalt: tabellraden «alle». 42 % = 98 / 234 = 41,9 %, regnet ut av meg fra de to tallene.

**Forbehold juryen kan spørre om:** 3 MOT er for få til å si noe om treffsikkerhet i gruppen. Ukjente selskaper har
*lavere* MOT-andel enn kjente på val 2025 (3,1 % mot 5,3 %), så regelen er begrunnet i manglende presedens, ikke i
høyere risiko. Tallene gjelder val 2025, ikke test 2026 (det tar smed3 i #2323). Tallene må sjekkes mot frysen
etter kl. 16 før de går inn i JURY.md (#1975, #2255).

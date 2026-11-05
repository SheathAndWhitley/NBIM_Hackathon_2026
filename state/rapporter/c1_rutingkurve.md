# Case 1: rutingkurve, andel til menneske mot F1 på MOT for resten (smed3, #2254)

Frossen agent (#2044 miks h2 via `arbeid/hack/levering/kjor_agent.py`, bare `--baand` endret), test 2026 = 1578 saker
(1539 med fasit, 66 ekte MOT, 58 MOT mot styret). Måler: v2 `maaler_offisiell_v2.py test --data real` (sha 9d81a418dd),
anbefaling skrevet som FOR/MOT så v2 teller streng MOT. **Ingen nye bånd er valgt på test**: det låste båndet er [0,15, 0,85) (#2128);
de andre radene viser bare hva som skjer om det hadde vært bredere eller smalere.

«F1 rest» er målerens egen `maal()` kjørt på de sakene agenten avgjør selv (rutede tatt ut av både svar og fasit).
Kjørt uendret på hele fila gir måleren samme F1 for alle bånd (ruting endrer ikke anbefalingen): streng MOT 0,524 (v2), MOT mot styret 0,476 (v3).

| bånd på kalibrert P(MOT) | til menneske | F1 MOT rest (v2) | P / R rest | TP / FP / FN rest | F1 MOT mot styret rest (v3) | ekte MOT hos menneske | maskinens treff som rutes bort |
|---|---|---|---|---|---|---|---|
| ingen bånd, bare robusthetsregler | 71 (4,5 %) | 0,533 | 0,47 / 0,61 | 36 / 40 / 23 | 0,483 | 7 av 66 | 2 |
| [0,25, 0,75) smalere | 123 (7,8 %) | 0,563 | 0,71 / 0,47 | 20 / 8 / 23 | 0,462 | 23 av 66 | 18 |
| **[0,15, 0,85) låst** | **188 (11,9 %)** | **0,600** | **0,83 / 0,47** | **15 / 3 / 17** | **0,514** | **34 av 66** | **23** |
| [0,05, 0,95) bredere | 227 (14,4 %) | 0,612 | 0,83 / 0,48 | 15 / 3 / 16 | 0,529 | 35 av 66 | 23 |

[0,35, 0,65) gir 122 rutet og F1 0,556, [0,10, 0,90) er identisk med [0,15, 0,85): kalibreringen er isotonisk (22 nivåer),
så båndet snapper til de samme sakene. De 71 uten bånd er 70 ukjente selskaper og 1 instruksjonstekst.

## Setningen til juryen
Med det låste båndet går 11,9 % av sakene (188 av 1578) til et menneske; på resten stiger presisjonen på MOT fra 0,47 til 0,83
og F1 fra 0,53 til 0,60, men 34 av de 66 ekte MOT-stemmene og 23 av maskinens 38 MOT-treff ligger i bunken til mennesket,
så båndet flytter halvparten av MOT-arbeidet til mennesket heller enn å løse det.

## Hvorfor det er slik
Rå grense 0,9188 kalibreres til 0,191, så nesten alle sakene modellen ville stemt MOT på (kalibrert 0,19 til 0,75) ligger inne i
båndet og rutes. Maskinen alene sier MOT i bare 18 saker på resten (15 riktige). Båndet gjør agenten til et «flagg for manuell
MOT-vurdering» med høy presisjon, ikke til en maskin som tar MOT-avgjørelsene selv. Rutede saker har MOT-rate 18 % mot 4 % i snitt,
så bunken til mennesket er godt sortert.

## Avvik fra tidligere rapport (c1_ruting_kostnad.md, #2100)
#2100 brukte det gamle symmetriske logit-båndet (strategi A): ved 11,0 % rutet ble 17 av 66 MOT sendt til menneske, F1 rest 0,627.
Det låste kalibrerte båndet sender ved 11,9 % dobbelt så mange ekte MOT (34) til mennesket, med lavere F1 rest (0,600) og klart høyere presisjon.
Tallene er ikke direkte sammenlignbare (#2100 regnet på egne funksjoner, her er det målerens maal()), men retningen er tydelig.

## Filer og reproduksjon
- Kjøring: `arbeid/kandidater/smed2_c1_mot/.venv/bin/python arbeid/hack/levering/kjor_agent.py --ut arbeid/oppgave_2254/ut/b015_085 --baand 0.15,0.85` (5 s per bånd)
- Kurve: `python3 -I arbeid/oppgave_2254/rutingkurve.py` (skriver `ut/kurve.json`, `ut/b*/pred_v2_tekst.csv`, `ut/b*/maaler_v2.txt`, `maaler_v3.txt`)
- Forsøkstavla: `tavle forsok --sti` ble avvist for alle fem filer fordi oppgave #2254 ikke heter «Hack…» og dermed bruker den globale
  måleren (endret på disk). Bare dommeren kan sette måler per oppgave. Målerutskriftene ligger i `ut/b*/maaler_v2.txt`.

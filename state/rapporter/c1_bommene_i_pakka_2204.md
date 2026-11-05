# Case 1: bommene skrevet inn som ærlig svakhet i pakka (#2204)

smed2, 05.11. Ingen modellendring. Tall fra #2192 (`c1_bommene.md`), reprodusert: `python3 -I arbeid/oppgave_2192/bommene.py` gir identisk utskrift.

Lagt inn:
- `arbeid/hack/c1/leveranse/BEGRENSNINGER.md` nytt pkt. 7 «Hvor agenten bommer»: 30 av 58 MOT funnet, 28 oversett, 11 av dem hos menneske og 17 usett (kalibrert P ≤ 0,09); 0 av 7 USA-MOT; 0 av 17 «eneste MOT i møtet»; 5 nye amerikanske aksjonærrettighets-saker 2026, alle MOT. «Gjør»: et menneske leser selv slike saker og enkeltstående styrevalg i selskaper uten MOT før. Forbehold: funnet på test, n = 5, ikke i modellen.
- `arbeid/hack/c1/leveranse/JURY.md`: ett avsnitt med det samme under tabellen «Slår dere noe enkelt?».
- SVAKHETER.md § 2 og BESLUTNINGSSTOTTE.md ble alt oppdatert i #2192.

Kontroll: `c1_tallvakt.py`: 14 filer, 139 påstander, 0 avvik (TP 30 FP 38 FN 28, F1 0,4762).

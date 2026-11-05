# Case 1 (#2551): demo_utskrift.txt kjørt på nytt etter frysen, uten interne ord

Kilde: jurylesingen #2544 punkt A3 og B11–B13. Den gamle utskriften var fra 15:28 (før frysen) og
inneholdt «ikke frosset ennå», den lokale stien /Users/…, lagnavnet «smed2 #2044-modell» og «sak 2132».

## Gjort
- `demo.sh` kjørt mot den kalde kopien fra generalprøven (16:01:39, 44 s, FRYSVAKT GRØNN 17 filer).
  Kopien gjenbrukes, ingen ny kald kjøring. Ny utskrift datert 16:48.
- «smed2 #2044-modell» kommer fra første linje i `ut/KJORING.txt`, skrevet av den frosne `kjor_agent.py`.
  Den fila er ikke rørt. `demo.sh` bytter ordet til «modell miks h2» i overskriften og skriver øverst i
  utskriften én linje om hva som er renset (akseptkravet).
- «(sak 2132)» strøket to steder: i `demo.sh` (overskriften) og i `demo_vis.py` linje 28 (kalibreringslinja).
  Begge filer står utenfor frysen.
- Ny ordvakt sist i `demo.sh`: utskriften avsøkes for `/Users`, `landsby`, `smed` og `sak NNNN`, rød = exit 6.

## Sjekk
- Ordvakt: 0 treff på interne ord i `demo_utskrift.txt`.
- Tall uendret: HOVEDTALL 0.476190, F1 MOT 0.4762, til menneske 183 av 1539 (11,9 %), avvik-sidetall 0.481752.
- De samme seks sakene vises (manus linje 276 / 89 / 15, seed 0: Rukun Raharja, Colruyt x2).
- Frysvakt: GRØNN, 17 filer like som ved frys 16:00:01. Tallvakt: 18 filer, 169 påstander, 0 avvik.

## Ikke rørt
`JURY_SPORSMAL.md` og `NESTE_VERSJON.md` lå endret i arbeidskatalogen fra andre; de er ikke med i commiten.

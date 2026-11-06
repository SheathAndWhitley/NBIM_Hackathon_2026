# Kravrespons: stemmeagenten (Case 1)

## 1. Hva vi bygde
- Agent: saksliste inn → FOR/MOT styret per sak, med P(MOT) · analytikeren stemmer, ikke agenten
- Logistisk regresjon + LightGBM, med NBIMs tidligere stemmer som historikk
- Test 2026: **33 av 58** MOT funnet · **F1 0,520** · presisjon 48 % · recall 57 %

## 2. Hvordan vi verifiserte det
- Fasit: NBIMs egne stemmer (13 757 saker) · målvariabel: MOT styret · terskel valgt på 2025, test 2026
- F1, presisjon og recall på MOT, ikke accuracy (følg styret: 96 % riktig, F1 0) · 95 % KI 0,41–0,63
- Grunnlinje «gjenta forrige beslutning» 0,515: likt i 2026, agenten bedre over 3 år (0,52 mot 0,48)
- `sh KJOR.sh` reproduserer (Linux 0,520, macOS 0,512) · forbehold: testår brukt til modellvalg

## 3. Beslutningsstøtte
- Per sak: P(MOT), GVG-punkt ordrett og NBIMs begrunnelse fra en tidligere sak
- Til menneske: P(MOT) 0,15–0,85, ukjent selskap, instruks i teksten → 10 % av sakene
- Der havner nesten alle falske MOT-flagg (33 av 36)

## 4. Robusthet og styring
- Motstandstest: instruks i teksten flagges → menneske, svaret endres ikke
- Lekkasjetest bestått (kjent unntak: to møter samme dag) · hvert kall logges, ingen irreversible handlinger
- Svakheter: 18 av 58 MOT usett · aldri AVSTÅ · instrukser skrevet som titler

## 5. Hva vi ville trengt videre
- Flere år fra NBIMs stemmedatabase (58 MOT gir usikkerhet rundt ±0,1)
- Skyggedrift på nye møter (etter september 2026)
- Løpende publiserte stemmer, innkallinger og årsrapporter

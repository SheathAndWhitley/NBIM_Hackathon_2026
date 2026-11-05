# Case 1: kravresponsen er kortet ned til én side (#2229, speider, 05.11 kl. 14.20)

Fila er `arbeid/hack/c1/leveranse/kravrespons.md`. Gammel versjon fra kl. 13.06 er lagret i `arbeid/oppgave_2229/kravrespons_gammel_1306.md`.

## Akseptkravene
| krav | resultat |
|---|---|
| 3 overskrifter, 3–5 setninger hver, under 450 ord | Hva vi bygde 4 setninger (119 ord), Hvordan vi verifiserte det 5 (156), Hva vi ville trengt videre 5 (128). Totalt **423 ord, 2 494 tegn**, under dommerens grense på 3 500. cupsfilter 12 cpi: **1 side**. |
| ingen #-numre eller interne stier, ett kjørbart kall | 0 #-numre. Eneste sti er kallet `bash arbeid/hack/c1/leveranse/kjor.sh`, det samme som README oppgir. |
| hovedtall, baseline, metrikk, motstandstest | F1 MOT 0,476, P 0,44, R 0,52 (30 av 58); følg styret F1 0 og 96,2 % accuracy; F1 på MOT fordi 3,8 % er MOT; motstandstesten i én setning (15 av 16 instrukser fanget, én i Title Case slipper gjennom, F1 0,392). |
| kuttet tekst flyttet, ikke slettet | Ny § 5 i `ERLIG_EVALUERING.md`: hele 13.06-teksten ordrett, pluss en liste over hva i den som er utdatert. Kopi av ERLIG-fila før endring: `arbeid/oppgave_2229/ERLIG_EVALUERING_for_2229.md`. |
| tallene er de samme som i README | 0,476 / 0,44 / 0,52 / 58 / 188 av 1 578 / 96,2 % / 0,365 / 0,415 / KI [0,36; 0,59] står i README, BEGRENSNINGER.md eller JURY.md. Motstandstallene er fra `c1_injeksjon_hoflig.md` (#2237, godkjent i #2246). |

## Hva som er endret i innhold, ikke bare kortet (etter dommer2s hull i #2258)
- **H1/H10, motstandstest:** den gamle teksten beskrev «kindly support» som et åpent hull og pekte på gammel modell (#2046). Den nye beskriver vakta som faktisk er i agenten nå (#2237). **Forutsetning:** vakta er med i frysen kl. 16 (dommer2 godkjente det i #2246). Tas den ut, må setningen skrives om. JURY.md pkt 11 og BEGRENSNINGER.md beskriver fortsatt det gamle hullet. Det er ikke rettet her (#1975 / dommer).
- **H2:** de to historikkreglene med 0,091 og 0,145 er tatt ut. Bare b2 (0,365) står igjen, og den finnes i JURY.md og BEGRENSNINGER.md.
- **H3:** «båndet låst på val 2025» er strøket.
- **H4:** løpende historikk kalles nå en antakelse som ikke er dokumentert, ikke et faktum.
- **H5, val-tallet:** det er tatt ut av énsideren. README, BEGRENSNINGER, JURY og ERLIG sier 0,520, mens kjøreloggen sier 0,5217 og bootstrap-rapporten 0,522 [0,403; 0,624]. Loggen har n_MOT 103 for val, samme antall som «103 avvik» i ERLIG § 3, så det er uklart om val-tallet er på MOT eller på avvik. Det bør #2255 avgjøre.
- **H11:** lekkasjevakta (`sjekk_lekkasje.py`) er ikke nevnt, fordi det ett kallet ikke kjører den.

## Malen
Regelverket sier «fem overskrifter», men malen viser bare tre (Hva vi bygde / Hvordan vi verifiserte det / Hva vi ville trengt videre). Vi har beholdt de tre, slik ordren sier. Dommer #2245 leste det på samme måte.

## Én kravrespons
`arbeid/hack/levering/README.md` linje 13 pekte på `EN_SIDE.md` (547 ord, 2 sider). Nå peker den på `c1/leveranse/kravrespons.md` og kaller EN_SIDE en eldre utdyping. EN_SIDE.md er ikke rørt. `levering/KRAVRESPONS.md` var allerede merket INTERN. Kopi av README før endring: `arbeid/oppgave_2229/levering_README_for.md`.

## Til dommer #2251
Ordtelling: `wc -w arbeid/hack/c1/leveranse/kravrespons.md`. Setningene er talt med awk per overskrift; desimalkomma og «...» telles ikke som setningsslutt.

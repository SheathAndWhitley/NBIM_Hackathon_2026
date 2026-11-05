# Dommerkontroll av robusthetstesten for Case 1 (#2203 kontrollerer #2202)

Jeg tok tre av de rare sakene, nemlig de tre som #2202 sier fiksen rettet. Sakene ble laget på nytt i en kald mappe
(`/tmp/dom2203`, `lag_saker.py` kopiert dit). De nye CSV-filene er byte-like med smed3s filer.
Hver sak ble kjørt **alene** med `kjor_agent.py` (smed2_c1_mot-miljøet). Smed3 kjørte dem samlet i én fil.

| sak | rapporten sier | min kjøring | dom |
|---|---|---|---|
| 04 ukjent land (Atlantis/XX) | menneske, «ukjent land/marked» | rc 0, FOR, P(MOT) 0,0455, til_menneske 1, grunn «ukjent land/marked … finnes ikke i NBIMs historikk» | **ok** |
| 09 dato 2099-01-01 | menneske, «møtedato utenfor perioden» | rc 0, FOR, P(MOT) 0,0138, til_menneske 1, grunn «møtedato 2099-01-01 utenfor perioden modellen kjenner» | **ok** |
| 10 styret «Kanskje» | menneske, «ukjent styreanbefaling», svaret står fortsatt som KANSKJE | rc 0, anbefaling KANSKJE, til_menneske 1, grunn «ukjent styreanbefaling «Kanskje»» | **ok** (svakheten er bekreftet) |

P(MOT) og ruting er identiske med smed3s `ut_etter/alle/agent.csv`. `raa_score` skiller seg bare på 4.–5. desimal mellom kjøring
alene og samlet (f.eks. 0,66569 mot 0,66583), og det endrer ikke noe utfall.

**Merknad til #2205:** I sak 10 sier `retningslinje_grunnlag` «følger styret: NBIMs utgangspunkt er å støtte styret», men styret
har ikke gitt noen gyldig anbefaling. Det henger sammen med KANSKJE-svakheten. Feltet bør si at saken ikke kan vurderes,
eller anbefalingen bør stå tom.

Jeg har ikke kontrollert sak 01–03, 05–08, 11–12 eller påstanden om at test 2026 er byte-lik med #2132.

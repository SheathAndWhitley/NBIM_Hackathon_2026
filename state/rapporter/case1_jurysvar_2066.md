# Case 1: jurysvar på 6 vanskelige spørsmål om metode og evaluering (speider, #2066)

Fil: `arbeid/hack/c1/JURYSVAR.md`. Den har 6 svar på 3–4 linjer hver, og hvert tall har kilde (forsøk-id eller rapport).
Spørsmålene: lekkasje og tidssplitt, F1 mot accuracy, hvorfor følg styret gir 0, KI 0,37–0,58, ablasjon, selskaper uten historikk. Til slutt kommer et eget avsnitt om svakheter.

Nye poeng som ikke sto i JURY_METODE.md:
- Den valgte modellen har *lavere* accuracy enn følg styret: 95,4 % mot 95,7 %. Regnet ut fra P/R/flagget i #1037. Det er det sterkeste argumentet for å bruke F1 på MOT.
- Rangsnittet gjør at testsakene påvirker hverandre litt: én ny sak flytter grensen. Det er ikke etikettlekkasje. SCORE i `train.py` bruker rå val-grense, og andel-varianten blir bare skrevet ut.
- Alle modellforsøkene #1037–#1046 står som selvrapportert. Bare #1034 er målt med rundens måler. Det blir sagt rett ut.

Til #1975 (etter modellfrys): oppdater tallene i JURYSVAR.md hvis #2062 eller #2053 endrer dem.

# Svarutkast til juryens tre spørsmål (Case 1)

Tall merket TODO fylles fra `ut/RESULTAT.md`. Svarene er korte nok til å sies på ca. 1 min hver.

## 1. Hvorfor valgte dere den målvariabelen, og hva var alternativene?
Vi måler fondets MOT-stemme og, ved siden av, «stemte fondet mot styret» (ja/nei), fordi det er der arbeidet og risikoen ligger: TODO % av sakene
følger styret, og de krever ingen vurdering. Alternativene var:
(a) treklasse FOR/MOT/AVSTÅ direkte. Avstå er sjelden (TODO %) og for få eksempler til å måle;
(b) «stemme = AGAINST» som i startpakken. Den blander sammen to ting: MOT et styreforslag og FOR et
aksjonærforslag styret er imot er begge avvik, men bare den første er AGAINST;
(c) accuracy på alle stemmer. Den belønner baselinen og er verdiløs her.
Avgrensning: bare forslag i Norges Banks N-PX (TODO typer), fordi det er der vi har ekte fasit.

## 2. Ville dere ha turt å sette resultatet i produksjon?
Ikke som en agent som stemmer selv. Som sortering foran en analytiker, ja, med to vilkår.
Med terskelen vi valgte når agenten TODO % av MOT-sakene og sender TODO % av alle saker til et menneske,
så analytikeren slipper TODO % av sakene. Det verste feilsporet er en MOT-sak agenten sier FOR til med høy
konfidens: det skjedde i TODO av TODO MOT-saker i testen. Vilkårene: (1) alt logges med kilde og konfidens
og et menneske godkjenner før stemmen sendes, (2) vi måler på nytt hver sesong, fordi praksis endrer seg.
Motstandstesten: TODO (fulgte / fulgte ikke injeksjonen i TODO av TODO saker).

## 3. Med én uke til, hva ville dere gjort først?
Først søke om NBIMs egen API-tilgang, så fasiten dekker alle land og sakstyper, ikke bare det som står i N-PX.
Deretter lese hele proxy-dokumentet i stedet for den korte teksten på stemmeseddelen, fordi mange MOT-stemmer
handler om forhold som ikke står der (f.eks. TODO). Til slutt la en analytiker gå gjennom de TODO sakene der vi
og fondet er uenige, og skille agentfeil fra ekte avvik mellom policy og praksis, som er det mest interessante funnet.

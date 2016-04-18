# Optimisation-Stochastique

### 2 Présentation du projet
L’objectif est de prendre une version simple d’un algorithme simple (Differential Evolution) et de lui trouver une implémentation parallèle inspirée des systèmes complexes (multi-échelles, dynamique, ago- antagoniste, massivement parallèle, et tout et tout).
L’idée de base derrière DE est de trouver, dans un espace de recherche potentiellement irrégulier, une vallée menant à un optimum local à une échelle supérieure aux irrégularités.
Pour ceci un algorithme DE est doté d’une population d’individus que l’on fera évoluer de la façon suivante : en partant d’une population initialisée de manière uniforme sur l’espace de recherche, on prend 2 individus parmi les meilleurs (par exemple sélectionnés avec un tournoi n-aire) pour former un vecteur, allant du moins bon des 2 vers le meilleur.
S’il y a une vallée présente sous les individus, les meilleurs individus l’échantillonneront et le nuage d’individus prendra sa forme. De plus, en sélectionnant deux individus parmi les meilleurs, il y a plus de chances que le segment entre ces individus aille dans la direction de la vallée avec la différence de valeur entre les deux individus en indiquant le sens de ce qui devient donc un vecteur. La norme de ce vecteur indiquera la distance entre les individus.
Dans un premier temps, on implémentera un algorithme générationnel, c’est à dire que si un îlot comporte p individus parents, alors on créera e enfants avant de passer à la génération suivante. Le passage de p + e à la nouvelle génération p s’effectuera avec une sélection de type tournoi n-aire (7 est une bonne valeur).

### 3 Idée à implémenter
Pour qu’un système complexe fonctionne bien, il est bien qu’il comporte un système ago-antagoniste. Là, on se propose d’implémenter un certain nombre d’îlots à population dynamique devant se reconfigurer automatiquement d’après l’espace de recherche sous-jacent.

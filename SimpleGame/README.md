# SimpleGame

Ce code contient une classe contenant 2 fonctions : 

__Fonction SimplegameTwoplayers__ : Cette fonction SimplegameTwoplayers simule une partie de Pierre/Feuille/Ciseaux entre deux joueurs. Elle prend en paramètres les choix des deux joueurs (player1choice et player2choice). Ensuite, elle vérifie les différents scénarios possibles :

    Si les choix des deux joueurs sont identiques, cela signifie qu'il y a égalité, donc elle retourne 0.
    Si les conditions de victoire pour le joueur 1 sont remplies (par exemple, si le joueur 1 choisit Rocher et le joueur 2 choisit Ciseaux), elle retourne 1, indiquant que le joueur 1 a gagné.
    Si aucun des deux cas précédents n'est vrai, cela signifie que le joueur 2 a gagné, donc elle retourne 2.

__Fonction SimplegameOneplayer__ : Cette fonction SimplegameOneplayer simule une partie de Pierre/Feuille/Ciseaux entre un joueur humain et l'ordinateur. Elle prend en paramètre le choix du joueur (player1choice).

Ensuite, elle choisit aléatoirement le coup de l'ordinateur parmi les choix possibles (Pierre, Feuille ou Ciseaux). Ensuite, elle suit la même logique que la fonction SimplegameTwoplayers pour déterminer le résultat de la partie :

    Si les choix des deux joueurs sont identiques, cela signifie qu'il y a égalité, donc elle retourne 0.
    Si les conditions de victoire pour le joueur 1 sont remplies (par exemple, si le joueur 1 choisit Rocher et l'ordinateur choisit Ciseaux), elle retourne 1, indiquant que le joueur 1 a gagné.
    Si aucun des deux cas précédents n'est vrai, cela signifie que l'ordinateur (joueur 2) a gagné, donc elle retourne 2.

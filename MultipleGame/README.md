# MultipleGame
score : 6.40/10

Ce code contient une classe qui contient 4 fonctions.

__Fonction init__ : Cette fonction init est le constructeur de la classe RPS_MultipleGame. Elle initialise un attribut history qui sera utilisé pour stocker l'historique des parties. Au début, cet historique est simplement initialisé comme une liste vide, indiquant qu'aucune partie n'a encore été jouée. Cet attribut sera rempli au fur et à mesure que de nouvelles parties seront jouées, enregistrant les choix des joueurs, les choix de l'ordinateur et les résultats de chaque partie.

__Fonction play_game__ : Cette fonction play_game prend le choix du joueur comme argument, puis obtient le choix de l'ordinateur en utilisant une méthode interne appelée get_computer_choice. Ensuite, elle utilise la classe RPS_SimpleGame pour jouer une partie entre le joueur et l'ordinateur, en passant les choix des deux joueurs comme arguments à la méthode SimplegameTwoplayers. Après avoir obtenu le résultat de la partie, elle l'ajoute à l'historique des parties enregistrées sous forme de tuple contenant le choix du joueur, le choix de l'ordinateur et le résultat de la partie. Enfin, elle retourne le résultat de la partie.

__Fonction get_computer_choice__ : Cette fonction get_computer_choice analyse l'historique des parties pour choisir le coup de l'ordinateur en fonction des tendances observées chez le joueur. Si aucune partie n'a encore été jouée, l'ordinateur choisit aléatoirement entre Pierre (R), Papier (P) et Ciseaux (S).
Ensuite, elle compte les occurrences des choix du joueur dans l'historique pour déterminer quel choix est le plus fréquent.
En utilisant le choix le plus fréquent du joueur, l'ordinateur choisit un coup qui le bat, conformément aux règles du jeu :
    Si le choix le plus fréquent du joueur est Rocher (R), l'ordinateur choisit Papier (P) car le Papier bat le Rocher.
    Si le choix le plus fréquent du joueur est Papier (P), l'ordinateur choisit Ciseaux (S) car les Ciseaux battent le Papier.
    Si le choix le plus fréquent du joueur est Ciseaux (S), l'ordinateur choisit Rocher (R) car le Rocher bat les Ciseaux.

__Fonction show_history__ : Cette fonction show_history affiche simplement l'historique des parties enregistrées jusqu'à présent. Elle parcourt chaque entrée dans l'historique, qui est une liste de tuples représentant les choix du joueur, les choix de l'ordinateur et les résultats de chaque partie. Pour chaque tuple, elle extrait les éléments correspondants (le choix du joueur, le choix de l'ordinateur et le résultat) et les affiche sous forme de texte formaté, avec des étiquettes claires indiquant le joueur, l'ordinateur et le résultat de chaque partie.

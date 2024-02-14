# Projet Pierre/Feuille/Ciseaux

Ce projet consiste en une implémentation du jeu de Pierre/Feuille/Ciseaux (Rock-Paper-Scissors) en utilisant des classes et des fonctions Python. Le projet est divisé en plusieurs parties, chacune contenant des fonctionnalités spécifiques.

## SimpleGame

Ce module contient une classe RPS_SimpleGame qui propose deux fonctions :

### Fonction SimplegameTwoplayers

Cette fonction simule une partie de Pierre/Feuille/Ciseaux entre deux joueurs. Elle compare les choix des deux joueurs et détermine le résultat de la partie (égalité, victoire du joueur 1 ou victoire du joueur 2).

### Fonction SimplegameOneplayer

Cette fonction simule une partie de Pierre/Feuille/Ciseaux entre un joueur humain et l'ordinateur. Elle prend en compte le choix du joueur et génère aléatoirement le choix de l'ordinateur. Ensuite, elle détermine le résultat de la partie.

## MultipleGame

Ce module contient une classe RPS_MultipleGame qui permet de jouer plusieurs parties de Pierre/Feuille/Ciseaux en gardant une trace de l'historique des parties jouées.

### Fonction __init__

Le constructeur de la classe initialise un attribut history qui enregistre l'historique des parties. Au début, cet historique est une liste vide.

### Fonction play_game

Cette fonction permet de jouer une partie entre un joueur humain et l'ordinateur. Elle prend le choix du joueur comme argument, obtient le choix de l'ordinateur en fonction de l'historique des parties et utilise la classe RPS_SimpleGame pour déterminer le résultat de la partie.

### Fonction get_computer_choice

Cette fonction analyse l'historique des parties pour choisir le coup de l'ordinateur en fonction des tendances observées chez le joueur. Elle choisit un coup qui bat le choix le plus fréquent du joueur.

### Fonction show_history

Cette fonction affiche l'historique des parties enregistrées jusqu'à présent.

## Interface utilisateur (module test)

Ce module constitue une interface utilisateur pour jouer au jeu de Pierre/Feuille/Ciseaux. Il crée une instance de la classe GameInterface et permet au joueur de faire des choix de coups, de jouer contre l'ordinateur et de visualiser l'historique des parties jouées.

## Utilisation

Pour utiliser ce projet, importez les modules nécessaires et créez des instances des classes appropriées. Vous pouvez ensuite appeler les méthodes pour jouer au jeu de Pierre/Feuille/Ciseaux et interagir avec l'interface utilisateur.

## Remarque

Ce projet est une implémentation simple du jeu de Pierre/Feuille/Ciseaux en utilisant des concepts de programmation orientée objet et des fonctions Python. Il peut être étendu avec de nouvelles fonctionnalités ou amélioré pour une expérience utilisateur plus enrichissante.

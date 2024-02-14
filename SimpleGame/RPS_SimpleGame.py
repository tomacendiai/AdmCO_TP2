import random

class RPS_SimpleGame:
    def SimplegameTwoplayers(player1choice, player2choice):
        # Vérifie si les choix des deux joueurs sont identiques
        if player1choice == player2choice:
            return 0
        # Vérifie les conditions de victoire pour le joueur 1
        elif (player1choice == 'R' and player2choice == 'S') or (player1choice == 'P' and player2choice == 'R') or (player1choice == 'S' and player2choice == 'P'):
            return 1
        # Sinon, le joueur 2 gagne
        else:
            return 2

    def SimplegameOneplayer(player1choice):
        choices = ['R', 'P', 'S']
        # Choix aléatoire pour le joueur 2
        player2choice = random.choice(choices)
        # Vérifie si les choix des deux joueurs sont identiques
        if player1choice == player2choice:
            return 0
        # Vérifie les conditions de victoire pour le joueur 1
        elif (player1choice == 'R' and player2choice == 'S') or (player1choice == 'P' and player2choice == 'R') or (player1choice == 'S' and player2choice == 'P'):
            return 1
        # Sinon, le joueur 2 gagne
        else:
            return 2
import random
from SimpleGame.RPS_SimpleGame import RPS_SimpleGame

class RPS_MultipleGame:
    def __init__(self):
        self.history = []  # Initialise l'historique des parties

    def play_game(self, player_choice):
        computer_choice = self.get_computer_choice(player_choice)  # Passer le choix du joueur comme argument
        # Jouer une partie entre le joueur et l'ordinateur
        result = RPS_SimpleGame.SimplegameTwoplayers(player_choice, computer_choice)
        # Ajouter le résultat de la partie à l'historique
        self.history.append((player_choice, computer_choice, result))
        return result

    def get_computer_choice(self, player_choice):
        # Analyse l'historique pour choisir le coup de l'ordinateur en fonction des tendances
        if not self.history:
            # S'il n'y a pas encore de parties jouées, l'ordinateur joue de manière aléatoire
            return random.choice(['R', 'P', 'S'])
        
        # Compte les occurrences des choix du joueur
        player_choices = [choice[0] for choice in self.history]
        player_choice_counts = {choice: player_choices.count(choice) for choice in ['R', 'P', 'S']}
        
        # Choix le plus fréquent du joueur
        most_frequent_choice = max(player_choice_counts, key=player_choice_counts.get)
        
        # Choix de l'ordinateur pour battre le choix le plus fréquent du joueur
        if most_frequent_choice == 'R':
            return 'P'  # Papier bat Rocher
        elif most_frequent_choice == 'P':
            return 'S'  # Ciseaux bat Papier
        else:
            return 'R'  # Rocher bat Ciseaux

    def show_history(self):
        # Affiche l'historique des parties
        print("Historique des parties:")
        for player_choice, computer_choice, result in self.history:
            print(f"Joueur: {player_choice}, Ordinateur: {computer_choice}, Résultat: {result}")

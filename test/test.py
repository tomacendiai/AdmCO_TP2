from SimpleGame.RPS_SimpleGame import (
    RPS_SimpleGame,
)  # Importation de la classe RPS_SimpleGame depuis le module SimpleGame
from MultipleGame.RPS_MultipleGame import (
    RPS_MultipleGame,
)  # Importation de la classe RPS_MultipleGame depuis le module MultipleGame


class GameInterface:
    def __init__(self):
        self.game = (
            RPS_MultipleGame()
        )  # Création d'une instance de la classe RPS_MultipleGame

    def start(self):
        while True:
            player_choice = input(
                "Choisissez votre coup (R/P/S) ou 'Q' pour quitter: "
            )  # Demande au joueur de faire son choix
            if player_choice.upper() == "Q":  # Si le joueur choisit de quitter
                break  # Sortir de la boucle
            result = self.game.play_game(
                player_choice
            )  # Appel de la méthode play_game de l'instance de jeu
            if result == 0:  # Si le résultat est une égalité
                print("Égalité !")  # Afficher un message d'égalité
            elif result == 1:  # Si le joueur gagne
                print("Vous avez gagné !")  # Afficher un message de victoire
            else:  # Si l'ordinateur gagne
                print("L'ordinateur a gagné !")  # Afficher un message de défaite

        self.game.show_history()  # Appel de la méthode show_history de l'instance de jeu


if __name__ == "__main__":
    interface = GameInterface()  # Création d'une instance de la classe GameInterface
    interface.start()  # Appel de la méthode start de l'instance d'interface

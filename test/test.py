from SimpleGame.RPS_SimpleGame import RPS_SimpleGame
from MultipleGame.RPS_MultipleGame import RPS_MultipleGame

class GameInterface:
    def __init__(self):
        self.game = RPS_MultipleGame()

    def start(self):
        while True:
            player_choice = input("Choisissez votre coup (R/P/S) ou 'Q' pour quitter: ")
            if player_choice.upper() == 'Q':
                break
            result = self.game.play_game(player_choice)
            if result == 0:
                print("Égalité !")
            elif result == 1:
                print("Vous avez gagné !")
            else:
                print("L'ordinateur a gagné !")
        
        self.game.show_history()

if __name__ == "__main__":
    interface = GameInterface()
    interface.start()
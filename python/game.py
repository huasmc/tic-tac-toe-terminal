import sys
import copy
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/game_types')
from computer_vs_computer import ComputerVsComputer
from human_vs_computer import HumanVsComputer
from human_vs_human import HumanVsHuman
from handle_player_input import HandlePlayerInput

class Game:

    def __init__(self):
        self.botVsbot = ComputerVsComputer()
        self.humanVsbot = HumanVsComputer()
        self.humanVshuman = HumanVsHuman()
        self.handlePlayerInput = HandlePlayerInput()

    def start(self):
        game_type = self.handlePlayerInput.get_game_type()
        if(game_type == 0):
            self.humanVsbot.play()
            return
        elif(game_type == 1):
            self.humanVshuman.play()
            return
        else:
            self.botVsbot.play()
            return

if __name__ == '__main__':
  game = Game()
  game.start()

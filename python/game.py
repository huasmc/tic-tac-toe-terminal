import sys
import copy
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/game_types')
from computer_vs_computer import ComputerVsComputer
from human_vs_computer import HumanVsComputer
from human_vs_human import HumanVsHuman

class Game:

    def __init__(self):
        self.botVsbot = ComputerVsComputer()
        self.humanVsbot = HumanVsComputer()
        self.humanVshuman = HumanVsHuman()

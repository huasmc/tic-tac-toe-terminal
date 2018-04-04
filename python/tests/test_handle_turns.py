import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from handle_turns import HandleTurns
from human_player import HumanPlayer
from computer_player import ComputerPlayer

class TestHandleTurns(unittest.TestCase):

    def setUp(self):
        self.handleTurns = HandleTurns()
        self.humanPlayer = HumanPlayer()
        self.computerPlayer = ComputerPlayer()

    def test_has_current_player_property(self):
        self.assertEqual( self.handleTurns.currentPlayer, None )

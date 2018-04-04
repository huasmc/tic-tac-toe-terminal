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

    def test_has_current_player_token_property(self):
        self.assertEqual( self.handleTurns.currentPlayerToken, None )

    def test_sets_current_player_token(self):
        self.handleTurns.set_currentPlayerToken('O')
        self.assertEqual( self.handleTurns.currentPlayerToken, 'O' )

    def test_trigger_new_turn_is_computer(self):
        self.handleTurns.set_currentPlayerToken('O')
        self.humanPlayer.set_token('O')
        self.computerPlayer.set_token('X')
        self.handleTurns.trigger(self.humanPlayer, self.computerPlayer)
        self.assertEqual( self.handleTurns.currentPlayerToken, 'X' )

    def test_trigger_new_turn_is_human(self):
        self.handleTurns.set_currentPlayerToken('X')
        self.humanPlayer.set_token('O')
        self.computerPlayer.set_token('X')
        self.handleTurns.trigger(self.humanPlayer, self.computerPlayer)
        self.assertEqual( self.handleTurns.currentPlayerToken, 'O' )

if __name__ == '__main__':
    unittest.main()

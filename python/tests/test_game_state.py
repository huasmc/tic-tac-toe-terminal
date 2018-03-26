import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from game_state import GameState
from board import Board

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gameState = GameState();
        self.board = Board();

    def test_get_state(self):
        self.assertEqual( self.gameState.get_state(self.board), False )

    def test_check_win(self):
        self.assertEqual( self.gameState.check_win(self.board), False )

    def test_check_win_combinations_state(self):
        self.assertEqual( self.gameState.test_check_win_combinations_state(self.board), False)

    def test_check_tie(self):
        self.assertEqual( self.gameState.tie(self.board), False)

if __name__ == '__main__':
    unittest.main()

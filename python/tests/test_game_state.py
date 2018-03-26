import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from game_state import GameState

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gameState = GameState();

    def test_gameState_game_is_over(self):
        self.assertEquals( self.gameState.game_is_over(), 0 )

    def test_gameState_three_in_a_row(self):
        self.assertEquals( self.gameState.three_in_a_row(), 0 )

    def test_gameState_tie(self):
        self.assertEquals( self.gameState.tie(), 0)

if __name__ == '__main__':
    unittest.main()

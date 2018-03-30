import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from AI import AI
from board import Board

class TestAI(unittest.TestCase):

    def setUp(self):
        self.AI = AI('X')
        self.board = Board()

    def test_has_marker(self):
        self.assertEqual( self.AI.marker, 'X' )

    def test_winner_is_None(self):
        self.assertIsNone( self.AI.winner )

    def test_has_opponent_marker(self):
        self.assertEqual( self.AI.opponentmarker, 'O')

    def test_has_gameState(self):
        self.assertIsNotNone( self.AI.gameState )

    def test_best_spot_is_middle_if_empty(self):
        self.assertEqual( self.AI.get_best_spot(self.board), 4 )

    def test_maximized_spot(self):
        self.assertEqual( self.AI.maximized_move(self.board), (4, 1) )

    def test_minimized_spot(self):
        self.assertEqual( self.AI.minimized_move(self.board), (4, 0) )

    def test_get_score(self):
        self.assertEqual( self.AI.get_score(self.board), 0 )

    # def test_:
    #     assertEqual(  )
if __name__ == '__main__':
    unittest.main()

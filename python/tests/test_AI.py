import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from AI import MiniMax
from board import Board

class TestAI(unittest.TestCase):

    def setUp(self):
        self.AI = MiniMax('X')
        self.board = Board()

    def test_has_token(self):
        self.assertEqual( self.AI.token, 'X' )

    def test_winner_is_None(self):
        self.assertIsNone( self.AI.winner )

    def test_has_opponent_token(self):
        self.assertEqual( self.AI.opponenttoken, 'O')

    def test_has_gameState(self):
        self.assertIsNotNone( self.AI.gameState )

    # def test_best_spot_is_middle_if_empty(self):
    #     self.assertEqual( self.AI.get_best_spot(self.board), 4)

    # def test_maximized_spot(self):
    #     self.assertEqual( self.AI.maximized_move(self.board), ['0', 0] )
    #
    # def test_minimized_spot(self):
    #     self.assertEqual( self.AI.minimized_move(self.board), ['0', 0] )

    def test_get_score(self):
        self.assertEqual( self.AI.get_score(self.board), 0 )

    def test_get_random_spot(self):
        self.board.grid = ["X", "O", "X", "O", "X", "5", "O", "7", "8"]
        available_spots = self.board.get_available_spots()
        spot = self.AI.get_random_spot(self.board)
        if spot in available_spots:
            result = True
        else:
            result = False
        self.assertTrue( result )

    # def test_:
    #     assertEqual(  )
if __name__ == '__main__':
    unittest.main()

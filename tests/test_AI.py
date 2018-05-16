import unittest
from models.AI import MiniMax
from models.board import Board

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

    def test_best_spot_is_middle_if_empty(self):
        self.assertEqual( self.AI.get_best_spot(self.board), 4)

    def test_maximized_spot_case_winning(self):
        self.board.grid = ["X", "O", "X",
                           "O", "X", "5",
                           "O", "7", "8"]
        self.assertEqual( self.AI.maximized_spot(self.board), ['8', 1] )

    def test_minimized_spot_case_losing(self):
        self.board.grid = ["0", "O", "X",
                           "O", "X", "5",
                           "O", "7", "8"]
        self.assertEqual( self.AI.minimized_spot(self.board), ['0', -1] )

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

if __name__ == '__main__':
    unittest.main()

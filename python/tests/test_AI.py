import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from AI import MiniMax
from board import Board

class TestAI(unittest.TestCase):
# Different test cases must be done for each method.
# This class is the 'brain' of the computer player.
    def setUp(self):
        self.AI = MiniMax('X')
        self.board = Board()

    def test_has_token(self):
        # This token is the same as computer player.
        self.assertEqual( self.AI.token, 'X' )

    def test_winner_is_None(self):
        # This property helps to 'memory/remember' the possible winner when getting the best spot on board.
        self.assertIsNone( self.AI.winner )

    def test_has_opponent_token(self):
        # This property helps to 'memory/remember' the opponets token when thinking about all possible spots on board.
        self.assertEqual( self.AI.opponenttoken, 'O')

    def test_has_gameState(self):
        # It should when the game has finished when thinking about all possible spots board.
        self.assertIsNotNone( self.AI.gameState )

    def test_best_spot_is_middle_if_empty(self):
        self.assertEqual( self.AI.get_best_spot(self.board), 4)

    def test_maximized_spot(self):
        # Part of implementing the minimax algorithm is knowing which spot on board makes winning MORE possible.
        print(" This may take a while, please be patient while AI's thought process is being tested..")
        self.assertEqual( self.AI.maximized_spot(self.board), ['0', 0] )

    def test_minimized_spot(self):
        # Part of implementing the minimax algorithm is knowing which spot on board makes winning LESS possible.
        self.assertEqual( self.AI.minimized_spot(self.board), ['0', 0] )

    def test_get_score(self):
        # Each possible spot shoud have a score that represents it's ranking as winning spot.
        # When AI thinks it assigns each spot a score with this method.
        self.assertEqual( self.AI.get_score(self.board), 0 )

    def test_get_random_spot(self):
        # While playing, the second turn doesn't affect the probability of winning or losing.
        # Getting a random spot avoids loading the minimax algorithm again making the game faster .
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

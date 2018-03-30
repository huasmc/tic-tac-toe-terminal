import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from board import Board

class TestAI(unittest.TestCase):

    def setUp(self):
        self.AI = AI('X')

    def test_has_marker(self):
        assertEqual( self.AI.marker, 'X' )

    def test_winner_is_None(self):
        assertEqual( self.AI.winner, None )

    def test_has_opponent_marker(self):
        assertEqual( self.AI.opponentmarker, 'O')

    def test_has_gameState(self):
        assertIsNotNone( self.AI.gameState )

    def test_best_spot_is_middle_if_empty(self):
        assertEqual( self.AI.get_best_spot(), 4 )

    # def test_:
    #     assertEqual(  )

import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from minimax import Brain
from board import Board

class TestBrain(unittest.TestCase):

    def setUp(self):
        self.brain = Brain()
        self.board = Board()

    def test_minimax_cycle(self):
        scores = self.brain.bestMove(self.board)
        print scores
        self.assertEqual(scores, 0)

    def test_take_fake_turn(self):
        self.brain.take_fake_turn(self.board)
        self.assertEqual( self.brain.turn, 'X')

    def test_fake_turn_after_turn(self):
        self.brain.take_fake_turn(self.board)
        self.brain.take_fake_turn(self.board)
        self.assertEqual( self.brain.turn, 'O')



if __name__ == '__main__':
    unittest.main()

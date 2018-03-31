import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from computer_player import ComputerPlayer
from board import Board

class TestComputerPlayer(unittest.TestCase):
# Diferent test cases pending.
    def setUp(self):
        self.computerPlayer = ComputerPlayer();
        self.board = Board()

    def test_computerPlayer_has_token(self):
        self.assertEqual( self.computerPlayer.token, None)

    def test_computerPlayer_fails_to_initialize_AI(self):
        self.assertIsNone( self.computerPlayer.initialize_AI() )

    def test_computerPlayer_play_first_middle(self):
        self.computerPlayer.set_token('X')
        self.computerPlayer.play(self.board)
        self.assertEqual( self.board.grid[4], self.computerPlayer.token )

    def test_computerPlayer_set_token_X(self):
        opponents_token = 'X'
        self.computerPlayer.set_token(opponents_token)
        self.assertEqual( self.computerPlayer.token, 'O')

    def test_computerPlayer_set_token_X(self):
        opponents_token = 'O'
        self.computerPlayer.set_token(opponents_token)
        self.assertEqual( self.computerPlayer.token, 'X')

if __name__ == '__main__':
    unittest.main()

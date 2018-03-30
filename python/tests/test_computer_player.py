import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from computer_player import ComputerPlayer
from board import Board

class TestComputerPlayer(unittest.TestCase):
# Diferent test cases pending.
    def setUp(self):
        self.computerPlayer = ComputerPlayer();
        self.board = Board()

    def test_computerPlayer_has_token(self):
        self.assertEqual( self.computerPlayer.token, 'O')

    def test_computerPlayer_play_first_middle(self):
        self.computerPlayer.play(self.board)
        self.assertEqual( self.board.grid[4], self.computerPlayer.token )

if __name__ == '__main__':
    unittest.main()

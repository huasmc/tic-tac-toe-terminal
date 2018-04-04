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

    def test_computerPlayer_has_None_token(self):
        self.assertEqual( self.computerPlayer.token, None)

    def test_computerPlayer_fails_to_initialize_AI(self):
        # Computer player needs a token before using AI.
        # AI needs computer player token to guess oponents token and calculate best moves given a board.
        self.assertIsNone( self.computerPlayer.initialize_AI() )

    def test_computerPlayer_initializes_AI(self):
        # Computer player sets token and AI can initialize given the token.
        self.computerPlayer.auto_token('X')
        self.computerPlayer.initialize_AI()

        self.assertIsNotNone( self.computerPlayer.AI )

    def test_computerPlayer_play_first_middle(self):
        self.computerPlayer.auto_token('X')
        self.computerPlayer.play(self.board)
        self.assertEqual( self.board.grid[4], self.computerPlayer.token )

    def test_computerPlayer_auto_token_X(self):
        opponents_token = 'X'
        self.computerPlayer.auto_token(opponents_token)
        self.assertEqual( self.computerPlayer.token, 'O')

    def test_computerPlayer_auto_token_O(self):
        opponents_token = 'O'
        self.computerPlayer.auto_token(opponents_token)
        self.assertEqual( self.computerPlayer.token, 'X')

    def test_computerPlayer_fails_to_auto_token(self):
        # If opponents token is not valid, computer shouldn't auto token.
        opponents_token = 'R'
        result = self.computerPlayer.auto_token(opponents_token)
        self.assertEqual( result, 'Invalid opponents token')

    def test_computerPlayer_set_token_O(self):
        self.computerPlayer.set_token('X')
        self.assertEqual( self.computerPlayer.token, 'X' )


if __name__ == '__main__':
    unittest.main()

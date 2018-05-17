import unittest
from models.computer_player import ComputerPlayer
from models.board import Board
from io import StringIO
from unittest.mock import patch

class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.computerPlayer = ComputerPlayer();
        self.board = Board()

    def test_computerPlayer_has_None_token(self):
        self.assertEqual( self.computerPlayer.token, None)

    def test_computerPlayer_fails_to_initialize_AI(self):
        self.assertIsNone( self.computerPlayer.initialize_AI() )

    def test_computerPlayer_initializes_AI(self):
        self.computerPlayer.auto_token('X')
        self.computerPlayer.initialize_AI()

        self.assertIsNotNone( self.computerPlayer.AI )

    @patch('sys.stdout', new_callable=StringIO)
    def test_computerPlayer_play_first_middle(self, mock_stdout):
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

    def test_computerPlayer_set_token_X(self):
        self.computerPlayer.set_token('X')
        self.assertEqual( self.computerPlayer.token, 'X' )

    def test_computerPlayer_set_token_O(self):
        self.computerPlayer.set_token('O')
        self.assertEqual( self.computerPlayer.token, 'O')


if __name__ == '__main__':
    unittest.main()

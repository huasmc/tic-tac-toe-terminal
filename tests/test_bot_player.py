import unittest
from io import StringIO
from models.bot_player import BotPlayer
from models.board import Board
from unittest.mock import patch

class TestBotPlayer(unittest.TestCase):

    def setUp(self):
        self.botPlayer = BotPlayer();
        self.board = Board()

    def test_botPlayer_has_None_token(self):
        self.assertEqual( self.botPlayer.token, None)

    def test_botPlayer_fails_to_initialize_AI(self):
        self.assertIsNone( self.botPlayer.initialize_AI() )

    def test_botPlayer_initializes_AI(self):
        self.botPlayer.auto_token('X')
        self.botPlayer.initialize_AI()

        self.assertIsNotNone( self.botPlayer.AI )

    @patch('sys.stdout', new_callable=StringIO)
    def test_botPlayer_play_first_middle(self, mock_stdout):
        self.botPlayer.auto_token('X')
        self.botPlayer.play(self.board)
        self.assertEqual( self.board.grid[4], self.botPlayer.token )

    def test_botPlayer_auto_token_X(self):
        opponents_token = 'X'
        self.botPlayer.auto_token(opponents_token)
        self.assertEqual( self.botPlayer.token, 'O')

    def test_botPlayer_auto_token_O(self):
        opponents_token = 'O'
        self.botPlayer.auto_token(opponents_token)
        self.assertEqual( self.botPlayer.token, 'X')

    def test_botPlayer_set_token_X(self):
        self.botPlayer.set_token('X')
        self.assertEqual( self.botPlayer.token, 'X' )

    def test_botPlayer_set_token_O(self):
        self.botPlayer.set_token('O')
        self.assertEqual( self.botPlayer.token, 'O')


if __name__ == '__main__':
    unittest.main()

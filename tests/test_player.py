import unittest
from models.player import Player
from models.board import Board

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.board = Board()

    def test_has_token(self):
        self.assertEqual( self.player.token, None )

    def test_has_set_token(self):
        self.player.set_token('X')
        self.assertEqual( self.player.token, 'X' )

    def test_has_auto_token(self):
        self.player.auto_token('X')
        self.assertEqual( self.player.token, 'O' )

    def test_has_play_method(self):
        self.assertIsNotNone( self.player.play(self.board, 0 ) )


if __name__ == '__main__':
    unittest.main()

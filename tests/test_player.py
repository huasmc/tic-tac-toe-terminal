import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_has_token(self):
        self.assertEqual( self.player.token, None )


if __name__ == '__main__':
    unittest.main()

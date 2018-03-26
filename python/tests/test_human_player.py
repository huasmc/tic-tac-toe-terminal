import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from human_player import HumanPlayer

class TestHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.humanPlayer = HumanPlayer()

    def test_humanPlayer_has_token(self):
        self.assertEquals( self.humanPlayer.token, 'X')

    def test_humanPlayer_can_move(self):
        self.assertEquals( self.humanPlayer.play(), 0 )


if __name__ == '__main__':
    unittest.main()

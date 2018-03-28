import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from computer_player import ComputerPlayer

class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.computerPlayer = ComputerPlayer();

    def test_computerPlayer_has_token(self):
        self.assertEquals( self.computerPlayer.token, 'O')

    def test_computerPlayer_play(self):
        self.assertEquals( self.computerPlayer.play, 0 )

    def test_computerPlayer_get_best_move(self):
        self.assertEquals( self.computerPlayer.get_best_move, 0 )

if __name__ == '__main__':
    unittest.main()

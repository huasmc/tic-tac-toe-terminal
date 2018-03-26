import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from computer_player import ComputerPlayer

class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.testComputerPlayer = ComputerPlayer();

    def test_computerPlayer_has_token(self):
        assertEquals( self.testComputerPlayer.token, 'O')

    def test_computerPlayer_play_method(self):
        assertEquals( self.testComputerPlayer.play, )

    def test_computerPlayer_get_best_move(self):
        assertEquals( self.testComputerPlayer.get_best_move, )

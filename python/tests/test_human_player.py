import unittest
from models.human_player import HumanPlayer
from models.board import Board

class TestHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.humanPlayer = HumanPlayer()
        self.board = Board()

    def test_humanPlayer_has_token(self):
        self.assertEqual( self.humanPlayer.token, None )

    def test_humanPlayer_play_grid_one(self):
        self.humanPlayer.play(self.board, 0)
        self.assertEqual( self.humanPlayer.token, self.board.grid[0])

    def test_humanPlayer_play_grid_second(self):
        self.humanPlayer.play(self.board, 1)
        self.assertEqual( self.humanPlayer.token, self.board.grid[1])

    def test_humanPlayer_play_grid_third(self):
        self.humanPlayer.play(self.board, 2)
        self.assertEqual( self.humanPlayer.token, self.board.grid[2])

    def test_humanPlayer_play_grid_fourth(self):
        self.humanPlayer.play(self.board, 3)
        self.assertEqual( self.humanPlayer.token, self.board.grid[3])

    def test_humanPlayer_play_grid_fifth(self):
        self.humanPlayer.play(self.board, 4)
        self.assertEqual( self.humanPlayer.token, self.board.grid[4])

    def test_humanPlayer_play_grid_fifth(self):
        self.humanPlayer.play(self.board, 5)
        self.assertEqual( self.humanPlayer.token, self.board.grid[5])

    def test_humanPlayer_play_grid_sixth(self):
        self.humanPlayer.play(self.board, 6)
        self.assertEqual( self.humanPlayer.token, self.board.grid[6])

    def test_humanPlayer_play_grid_seventh(self):
        self.humanPlayer.play(self.board, 7)
        self.assertEqual( self.humanPlayer.token, self.board.grid[7])

    def test_humanPlayer_play_grid_eigth(self):
        self.humanPlayer.play(self.board, 8)
        self.assertEqual( self.humanPlayer.token, self.board.grid[8])

    def test_set_humanPlayer_token_X(self):
        self.humanPlayer.set_token('X')
        self.assertEqual( self.humanPlayer.token, 'X')

    def test_set_humanPlayer_token_O(self):
        self.humanPlayer.set_token('O')
        self.assertEqual( self.humanPlayer.token, 'O')

    def test_auto_assign_token_when_opponent_is_X(self):
        self.humanPlayer.auto_token('X')
        self.assertEqual( self.humanPlayer.token, 'O' )

    def test_auto_assign_token_when_opponent_is_O(self):
        self.humanPlayer.auto_token('O')
        self.assertEqual( self.humanPlayer.token, 'X' )


if __name__ == '__main__':
    unittest.main()

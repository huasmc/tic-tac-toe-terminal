import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_has_grid(self):
        self.assertEqual( len(self.board.grid), 9 )

    def test_board_has_win_combinations(self):
        self.assertEqual( len(self.board.win_combinations), 8)

    def test_board_first_win_combination(self):
        self.assertEqual( self.board.win_combinations[0], [0,1,2])

    def test_board_second_win_combination(self):
        self.assertEqual( self.board.win_combinations[1], [3,4,5])

    def test_board_third_win_combination(self):
        self.assertEqual( self.board.win_combinations[2], [6,7,8])

    def test_board_fourth_win_combination(self):
        self.assertEqual( self.board.win_combinations[3], [0,3,6])

    def test_board_fifth_win_combination(self):
        self.assertEqual( self.board.win_combinations[4], [1,4,7])

    def test_board_sixth_win_combination(self):
        self.assertEqual( self.board.win_combinations[5], [2,5,8])

    def test_board_seventh_win_combination(self):
        self.assertEqual( self.board.win_combinations[6], [0,4,8])

    def test_board_eigth_win_combination(self):
        self.assertEqual(self.board.win_combinations[7], [2,4,6])

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.testBoard = Board()

    def test_board_has_grid(self):
        self.assertEquals( len(self.testBoard.grid), 9 )

if __name__ == '__main__':
    unittest.main()

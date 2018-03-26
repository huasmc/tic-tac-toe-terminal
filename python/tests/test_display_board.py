import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from display_board import DisplayBoard

class TestDisplayBoard(unittest.TestCase):

    def setUp(self):
        self.displayBoard = DisplayBoard();

    def test_displayBoard_logs(self):
        self.assertEquals( self.displayBoard.logs, 0 )

if __name__ == '__main__':
    unittest.main()

import unittest
from models.display_board import DisplayBoard
from models.board import Board
import io

class TestDisplayBoard(unittest.TestCase):

    def setUp(self):
        self.displayBoard = DisplayBoard();
        self.board = Board();

    def test_displayBoard_logs(self):
        self.assertEqual( self.displayBoard.logs(self.board), " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (self.board.grid[0], self.board.grid[1], self.board.grid[2],
                 self.board.grid[3], self.board.grid[4], self.board.grid[5],
                 self.board.grid[6], self.board.grid[7], self.board.grid[8]))


if __name__ == '__main__':
    unittest.main()

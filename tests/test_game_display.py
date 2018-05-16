import unittest
import io
from io import StringIO
from unittest.mock import patch
from models.game_display import GameDisplay
from models.board import Board

class TestGameDisplay(unittest.TestCase):

    def setUp(self):
        self.gameDisplay = GameDisplay();
        self.board = Board();

    def test_gameDisplay_show_board(self):
        self.assertEqual( self.gameDisplay.show(self.board), " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (self.board.grid[0], self.board.grid[1], self.board.grid[2],
                 self.board.grid[3], self.board.grid[4], self.board.grid[5],
                 self.board.grid[6], self.board.grid[7], self.board.grid[8]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_gameDisplay_log_game_over(self, mock_stdout):
        self.gameDisplay.log('Game Over')
        self.assertEqual('Game Over\n', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

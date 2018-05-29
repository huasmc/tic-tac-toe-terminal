import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.game_display import GameDisplay
from models.board import Board
from pynput.keyboard import Key, Controller

class TestGameDisplay(unittest.TestCase):

    def setUp(self):
        self.gameDisplay = GameDisplay();
        self.board = Board();

    @patch('sys.stdout', new_callable=StringIO)
    def test_gameDisplay_show_board(self, mock_stdout):
        self.gameDisplay.show(self.board)
        self.assertEqual( mock_stdout.getvalue(), " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n\n" % \
            (self.board.grid[0], self.board.grid[1], self.board.grid[2],
                 self.board.grid[3], self.board.grid[4], self.board.grid[5],
                 self.board.grid[6], self.board.grid[7], self.board.grid[8]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_gameDisplay_log_game_over(self, mock_stdout):
        self.gameDisplay.log('Game Over')
        self.assertEqual( mock_stdout.getvalue(), 'Game Over\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_gameDisplay_log_as_list(self, mock_stdout):
        self.gameDisplay.log_as_list('Game')
        self.assertEqual( mock_stdout.getvalue(), 'G\na\nm\ne\n' )

    @patch('builtins.input', return_value='0')
    def test_prompt_input(self, mock_input):
        self.assertEqual( self.gameDisplay.prompt('Choose 0: '), '0' )

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='0')
    def test_prompt_output(self, mock_input, mock_stdout):
        keyboard = Controller()
        self.gameDisplay.prompt('Choose 0: ')
        self.assertEqual( mock_stdout.getvalue(), 'Choose 0: \n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_over(self, mock_stdout):
        self.gameDisplay.game_over()
        self.assertEqual( mock_stdout.getvalue(), 'Game Over\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_chosen_spot_token_X(self, mock_stdout):
        self.gameDisplay.chosen_spot('X', 4)
        self.assertEqual( mock_stdout.getvalue(), 'Player with token X has played in spot 4\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_chosen_spot_token_O(self, mock_stdout):
        self.gameDisplay.chosen_spot('O', 4)
        self.assertEqual( mock_stdout.getvalue(), 'Player with token O has played in spot 4\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_token_X(self, mock_stdout):
        self.gameDisplay.winner('X')
        self.assertEqual( mock_stdout.getvalue(), 'Player with token X won!\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_token_O(self, mock_stdout):
        self.gameDisplay.winner('O')
        self.assertEqual( mock_stdout.getvalue(), 'Player with token O won!\n' )

if __name__ == '__main__':
    unittest.main()

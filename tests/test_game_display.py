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
        self.gameDisplay.logAsList('Game')
        self.assertEqual( mock_stdout.getvalue(), 'G\na\nm\ne\n' )

    @patch('builtins.input', return_value='0')
    def test_prompt_input(self, input):
        self.assertEqual( self.gameDisplay.prompt('Choose 0: '), '0' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_output(self, mock_stdout):
        keyboard = Controller()
        keyboard.press(Key.enter)
        self.gameDisplay.prompt('Choose 0: ')
        keyboard.release(Key.enter)
        self.assertEqual( mock_stdout.getvalue(), 'Choose 0: ')

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.game_display import GameDisplay
from models.board import Board
from pynput.keyboard import Key, Controller

class TestGameDisplay(unittest.TestCase):

    def setUp(self):
        self.board = Board();

    @patch('sys.stdout', new_callable=StringIO)
    def test_gameDisplay_show_board(self, mock_stdout):
        GameDisplay.show(self.board)
        self.assertEqual( mock_stdout.getvalue(), " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n\n" % \
            (self.board.grid[0], self.board.grid[1], self.board.grid[2],
                 self.board.grid[3], self.board.grid[4], self.board.grid[5],
                 self.board.grid[6], self.board.grid[7], self.board.grid[8]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_over(self, mock_stdout):
        GameDisplay.game_over()
        self.assertEqual( mock_stdout.getvalue(), 'Game Over\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_chosen_spot_token_X(self, mock_stdout):
        GameDisplay.chosen_spot('X', 4)
        self.assertEqual( mock_stdout.getvalue(), 'Player with token X has played in spot 4\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_chosen_spot_token_O(self, mock_stdout):
        GameDisplay.chosen_spot('O', 4)
        self.assertEqual( mock_stdout.getvalue(), 'Player with token O has played in spot 4\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_token_X(self, mock_stdout):
        GameDisplay.winner('X')
        self.assertEqual( mock_stdout.getvalue(), 'Player with token X won!\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_token_O(self, mock_stdout):
        GameDisplay.winner('O')
        self.assertEqual( mock_stdout.getvalue(), 'Player with token O won!\n' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_tie(self, mock_stdout):
        GameDisplay.tie()
        self.assertEqual( mock_stdout.getvalue(), "It's a tie!\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_types(self, mock_stdout):
        GameDisplay.game_types()
        self.assertEqual( mock_stdout.getvalue(), "1. Human Vs Bot\n2. Human Vs Human\n3. Bot Vs Bot\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_spot(self, mock_stdout):
        available_spots = ['4', '5']
        GameDisplay.prompt_spot(available_spots)
        self.assertEqual( mock_stdout.getvalue(), "Choose one of these spots [4, 5]:\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_token(self, mock_stdout):
        GameDisplay.prompt_token()
        self.assertEqual( mock_stdout.getvalue(), "Choose your token! It can be either X or O:\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_first_player(self, mock_stdout):
        GameDisplay.prompt_first_player()
        self.assertEqual( mock_stdout.getvalue(), "Who plays first, X or O?\n" )

    @patch('builtins.input', return_value='0')
    def test_get_player_spot(self, input):
        self.assertEqual( GameDisplay.get_player_spot(GameDisplay, ['0', '1']), 0 )

    @patch('builtins.input', return_value='X')
    def test_get_player_token_X(self, input):
        self.assertEqual( GameDisplay.get_player_token(GameDisplay), 'X')

    @patch('builtins.input', return_value='O')
    def test_get_player_token_O(self, input):
        self.assertEqual( GameDisplay.get_player_token(GameDisplay), 'O')

    @patch('builtins.input', return_value='X')
    def test_get_first_player_X(self, input):
        self.assertEqual( GameDisplay.get_first_player(GameDisplay), 'X')

    @patch('builtins.input', return_value='O')
    def test_get_first_player_O(self, input):
        self.assertEqual( GameDisplay.get_first_player(GameDisplay), 'O')

    @patch('builtins.input', return_value='1')
    def test_get_game_type_human_vs_bot(self, input):
        self.assertEqual( GameDisplay.get_game_type(GameDisplay), 0 )

    @patch('builtins.input', return_value='2')
    def test_get_game_type_human_vs_human(self, input):
        self.assertEqual( GameDisplay.get_game_type(GameDisplay), 1 )

    @patch('builtins.input', return_value='3')
    def test_get_game_type_human_vs_bot(self, input):
        self.assertEqual( GameDisplay.get_game_type(GameDisplay), 2 )

    def test_handle_game_type_input_1(self):
        self.assertEqual( GameDisplay.handle_game_type_input(GameDisplay, '1'), 0 )

    def test_handle_game_type_input_2(self):
        self.assertEqual( GameDisplay.handle_game_type_input(GameDisplay, '2'), 1 )

    def test_handle_game_type_input_3(self):
        self.assertEqual( GameDisplay.handle_game_type_input(GameDisplay, '3'), 2 )


if __name__ == '__main__':
    unittest.main()

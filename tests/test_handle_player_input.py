import unittest
from io import StringIO
from unittest.mock import patch
from models.handle_player_input import HandlePlayerInput

class TestHandlePlayerInput(unittest.TestCase):

    def setUp(self):
        self.handlePlayerInput = HandlePlayerInput()

    @patch('builtins.input', return_value='0')
    def test_get_player_spot(self, input):
        self.assertEqual(self.handlePlayerInput.get_player_spot(['0', '1']), 0)

    @patch('builtins.input', return_value='X')
    def test_get_player_token_X(self, input):
        self.assertEqual(self.handlePlayerInput.get_player_token(), 'X')

    @patch('builtins.input', return_value='O')
    def test_get_player_token_O(self, input):
        self.assertEqual(self.handlePlayerInput.get_player_token(), 'O')

    @patch('builtins.input', return_value='X')
    def test_get_first_player_X(self, input):
        self.assertEqual(self.handlePlayerInput.get_first_player(), 'X')

    @patch('builtins.input', return_value='O')
    def test_get_first_player_O(self, input):
        self.assertEqual(self.handlePlayerInput.get_first_player(), 'O')

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_game_type_human_vs_bot(self, input, mock_stdout):
        self.assertEqual(self.handlePlayerInput.get_game_type(), 0)

    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_game_type_human_vs_human(self, input, mock_stdout):
        self.assertEqual(self.handlePlayerInput.get_game_type(), 1)

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_game_type_human_vs_bot(self, input, mock_stdout):
        self.assertEqual(self.handlePlayerInput.get_game_type(), 2)

    def test_handle_game_type_input_1(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('1'), 0)

    def test_handle_game_type_input_2(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('2'), 1)

    def test_handle_game_type_input_3(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('3'), 2)

if __name__ == '__main__':
    unittest.main()

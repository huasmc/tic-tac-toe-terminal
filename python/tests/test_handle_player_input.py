import unittest
from unittest.mock import patch
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from handle_player_input import HandlePlayerInput

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
    def test_get_game_type_human_vs_bot(self, input):
        self.assertEqual(self.handlePlayerInput.get_game_type(), '1')

    @patch('builtins.input', return_value='2')
    def test_get_game_type_human_vs_human(self, input):
        self.assertEqual(self.handlePlayerInput.get_game_type(), '2')
        
    @patch('builtins.input', return_value='2')
    def test_get_game_type_human_vs_human(self, input):
        self.assertEqual(self.handlePlayerInput.get_game_type(), '2')


    def test_handle_game_type_input_1(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('1'), 0)

    def test_handle_game_type_input_2(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('2'), 1)

    def test_handle_game_type_input_3(self):
        self.assertEqual(self.handlePlayerInput.handle_game_type_input('3'), 2)


    #
    # @patch('builtins.input', return_value='Soiuoiug')
    # def test_get_player_token_bad_input_letter(self, input):
    #     self.assertEqual(self.handlePlayerInput.get_player_token(), 'Please choose either X or O.')
    #
    # @patch('builtins.input', return_value='45')
    # def test_get_player_token_bad_input_number(self, input):
    #     self.assertEqual(self.handlePlayerInput.get_player_token(), 'Please choose either X or O.')

if __name__ == '__main__':
    unittest.main()



    # #
    # @patch('yourmodule.get_input', return_value='yes')
    # def test_answer_yes(self, input):
    #     self.assertEqual(answer(), 'you entered yes')

    # @patch('yourmodule.get_input', return_value='no')
    # def test_answer_no(self, input):
    #     self.assertEqual(answer(), 'you entered no')

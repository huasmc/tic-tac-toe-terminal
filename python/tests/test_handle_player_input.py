import unittest
from unittest.mock import patch
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from handle_player_input import HandlePlayerInput

class TestHandlePlayerInput(unittest.TestCase):

    def setUp(self):
        self.handlePlayerInput = HandlePlayerInput()

    @patch('builtins.input', return_value='0')
    def test_get_user_spot(self, input):
        self.assertEqual(self.handlePlayerInput.get_player_spot(), 0)

if __name__ == '__main__':
    unittest.main()



    # #
    # @patch('yourmodule.get_input', return_value='yes')
    # def test_answer_yes(self, input):
    #     self.assertEqual(answer(), 'you entered yes')

    # @patch('yourmodule.get_input', return_value='no')
    # def test_answer_no(self, input):
    #     self.assertEqual(answer(), 'you entered no')

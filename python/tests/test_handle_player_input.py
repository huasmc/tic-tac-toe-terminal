import unittest
import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/')
from handle_player_input import HandlePlayerInput

class TestHandlePlayerInput(unittest.TestCase):

    def setUp(self):
        self.handlePlayerInput = HandlePlayerInput()

if __name__ == '__main__':
    unittest.main()

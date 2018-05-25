import unittest
from io import StringIO
from models.game_types.human_vs_human import HumanVsHuman
from models.abstracts.game_type import GameType
from models.human_player import HumanPlayer
from unittest.mock import patch

class TestHumanVsHuman(unittest.TestCase):

    def setUp(self):
        self.game = HumanVsHuman()

    def test_game_type_subclass(self):
        self.assertTrue( issubclass( HumanVsHuman, GameType) )

    def test_inherits_board(self):
        self.assertIsNotNone( self.game.board )

    def test_inherits_game_state(self):
        self.assertIsNotNone( self.game.gameState )

    def test_inherits_handle_player_input(self):
        self.assertIsNotNone( self.game.handlePlayerInput )

    def test_inherits_handle_turns(self):
        self.assertIsNotNone( self.game.handleTurns )

    def test_inherits_play_method(self):
        self.assertIsNotNone( self.game.play )

    def test_inherits_end_game_method(self):
        self.assertIsNotNone( self.game.end_game )

    def test_inherits_set_up_method(self):
        self.assertIsNotNone( self.game.set_up )

    def test_inherits_start_method(self):
        self.assertIsNotNone( self.game.start )

    def test_inherits_handle_play_method(self):
        self.assertIsNotNone( self.game.handle_play )

    def test_has_player_one(self):
        self.assertIsNotNone( self.game.playerOne )

    def test_has_player_two(self):
        self.assertIsNotNone( self.game.playerTwo )

    def test_player_one_is_human_player_instance(self):
        self.assertTrue( isinstance( self.game.playerOne, HumanPlayer) )

    def test_player_two_is_human_player_instance(self):
        self.assertTrue( isinstance( self.game.playerTwo, HumanPlayer) )

    @patch('builtins.input', return_value='X')
    def test_can_set_up_first_player_X(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerOne.token, 'X' )
        self.assertEqual( self.game.playerTwo.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_can_set_up_first_player_O(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerOne.token, 'O' )
        self.assertEqual( self.game.playerTwo.token, 'X' )

    @patch('builtins.input', return_value='X')
    def test_can_set_up_second_player_O(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerTwo.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_can_set_up_second_player_X(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerTwo.token, 'X' )

    @patch('sys.stdout', new_callable=StringIO)
    def test_ends_game_with_tie(self, mock_stdout):
        self.game.board.grid = ["X", "O", "X",
                           "O", "X", "O",
                           "O", "X", "O"]
        self.game.end_game()
        self.assertEqual( mock_stdout.getvalue(), "It's a tie!\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_ends_game_when_token_O_wins(self, mock_stdout):
        self.game.board.grid = ["O", "O", "X",
                                "O", "X", "O",
                                "O", "X", "O"]
        self.game.end_game()
        self.assertEqual( mock_stdout.getvalue(), "Player with token O won!\n" )

    @patch('sys.stdout', new_callable=StringIO)
    def test_ends_game_when_token_X_wins(self, mock_stdout):
        self.game.board.grid = ["X", "O", "X",
                                "O", "X", "O",
                                "O", "O", "X"]
        self.game.end_game()
        self.assertEqual( mock_stdout.getvalue(), "Player with token X won!\n" )


if __name__ == '__main__':
    unittest.main()

import unittest
from models.game_types.human_vs_human import HumanVsHuman
from models.abstracts.game_type import GameType
from models.human_player import HumanPlayer
from unittest.mock import patch

class TestHumanVsHuman(unittest.TestCase):

    def setUp(self):
        self.game = HumanVsHuman()

    def test_human_vs_human_is_game_type_subclass(self):
        self.assertTrue( issubclass( HumanVsHuman, GameType) )

    def test_human_vs_human_inherits_board(self):
        self.assertIsNotNone( self.game.board )

    def test_human_vs_human_inherits_game_state(self):
        self.assertIsNotNone( self.game.gameState )

    def test_human_vs_human_inherits_handle_player_input(self):
        self.assertIsNotNone( self.game.handlePlayerInput )

    def test_human_vs_human_inherits_handle_turns(self):
        self.assertIsNotNone( self.game.handleTurns )

    def test_human_vs_human_inherits_play_method(self):
        self.assertIsNotNone( self.game.play )

    def test_human_vs_human_inherits_end_game_method(self):
        self.assertIsNotNone( self.game.end_game )

    def test_human_vs_human_inherits_set_up_method(self):
        self.assertIsNotNone( self.game.set_up )

    def test_human_vs_human_has_bot_player_one(self):
        self.assertIsNotNone( self.game.playerOne )

    def test_human_vs_human_has_bot_player_two(self):
        self.assertIsNotNone( self.game.playerTwo )

    def test_human_vs_human_player_one_is_human_player_instance(self):
        self.assertTrue( isinstance( self.game.playerOne, HumanPlayer) )

    def test_human_vs_human_player_two_is_human_player_instance(self):
        self.assertTrue( isinstance( self.game.playerTwo, HumanPlayer) )

    @patch('builtins.input', return_value='X')
    def test_human_vs_human_can_set_up_first_player_X(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerOne.token, 'X' )
        self.assertEqual( self.game.playerTwo.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_human_vs_human_can_set_up_first_player_O(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerOne.token, 'O' )
        self.assertEqual( self.game.playerTwo.token, 'X' )

    @patch('builtins.input', return_value='X')
    def test_human_vs_human_can_set_up_second_player_O(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerTwo.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_human_vs_human_can_set_up_second_player_X(self, input):
        self.game.set_up()
        self.assertEqual( self.game.playerTwo.token, 'X' )


if __name__ == '__main__':
    unittest.main()

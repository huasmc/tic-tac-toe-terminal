import unittest
from models.game_types.bot_vs_bot import BotVsBot
from unittest.mock import patch

class TestBotVsBot(unittest.TestCase):

    def setUp(self):
        self.game = BotVsBot()

    def test_bot_vs_bot_inherits_board(self):
        self.assertIsNotNone( self.game.board )

    def test_bot_vs_bot_inherits_game_state(self):
        self.assertIsNotNone( self.game.gameState )

    def test_bot_vs_bot_inherits_handle_player_input(self):
        self.assertIsNotNone( self.game.handlePlayerInput )

    def test_bot_vs_bot_inherits_handle_turns(self):
        self.assertIsNotNone( self.game.handleTurns )

    def test_bot_vs_bot_inherits_play_method(self):
        self.assertIsNotNone( self.game.play )

    def test_bot_vs_bot_inherits_end_game_method(self):
        self.assertIsNotNone( self.game.end_game )

    def test_bot_vs_bot_inherits_set_up_method(self):
        self.assertIsNotNone( self.game.set_up )

    def test_bot_vs_bot_has_bot_player_one(self):
        self.assertIsNotNone( self.game.botPlayer1 )

    def test_bot_vs_bot_has_bot_player_two(self):
        self.assertIsNotNone( self.game.botPlayer2 )

    @patch('builtins.input', return_value='X')
    def test_bot_vs_bot_can_set_tokens_first_player_X(self, input):
        self.game.set_tokens()
        self.assertEqual( self.game.botPlayer1.token, 'X' )
        self.assertEqual( self.game.botPlayer2.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_bot_vs_bot_can_set_tokens_first_player_O(self, input):
        self.game.set_tokens()
        self.assertEqual( self.game.botPlayer1.token, 'O' )
        self.assertEqual( self.game.botPlayer2.token, 'X' )

    @patch('builtins.input', return_value='X')
    def test_bot_vs_bot_can_set_tokens_second_player_O(self, input):
        self.game.set_tokens()
        self.assertEqual( self.game.botPlayer2.token, 'O' )

    @patch('builtins.input', return_value='O')
    def test_bot_vs_bot_can_set_tokens_second_player_X(self, input):
        self.game.set_tokens()
        self.assertEqual( self.game.botPlayer2.token, 'X' )


if __name__ == '__main__':
    unittest.main()

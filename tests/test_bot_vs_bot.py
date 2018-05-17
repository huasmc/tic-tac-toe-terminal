import unittest
from models.game_types.bot_vs_bot import BotVsBot

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

if __name__ == '__main__':
    unittest.main()

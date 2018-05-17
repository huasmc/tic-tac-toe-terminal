import unittest
from models.game_types.bot_vs_bot import BotVsBot

class TestBotVsBot(unittest.TestCase):

    def setUp(self):
        self.game = BotVsBot()

    def test_bot_vs_bot_inherits_board(self):
        self.assertIsNotNone( self.game.board )

    def test_bot_vs_bot_inherits_game_state(self):
        self.assertIsNotNone( self.game.gameState )

if __name__ == '__main__':
    unittest.main()

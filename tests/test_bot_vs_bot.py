import unittest
from models.game_types.bot_vs_bot import BotVsBot

class TestBotVsBot(unittest.TestCase):

    def setUp(self):
        self.game = BotVsBot()

    def test_bot_vs_bot_inherits_board(self):
        self.assertIsNotNone( self.game.board.grid )

if __name__ == '__main__':
    unittest.main()

import unittest
from models.game_types.bot_vs_bot import BotVsBot

class TestBotVsBot(unittest.TestCase):

    def setUp(self):
        self.game = BotVsBot()

if __name__ == '__main__':
    unittest.main()

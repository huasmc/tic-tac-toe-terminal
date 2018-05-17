from models.game_types.bot_vs_bot import BotVsBot
from models.game_types.human_vs_bot import HumanVsBot
from models.game_types.human_vs_human import HumanVsHuman
from models.handle_player_input import HandlePlayerInput

class Game:

    def __init__(self):
        self.bot_vs_bot = BotVsBot()
        self.huamn_vs_bot = HumanVsBot()
        self.human_vs_human = HumanVsHuman()
        self.handlePlayerInput = HandlePlayerInput()

    def start(self):
        game_type = self.handlePlayerInput.get_game_type()
        if(game_type == 0):
            self.huamn_vs_bot.play()
            return
        elif(game_type == 1):
            self.human_vs_human.play()
            return
        else:
            self.bot_vs_bot.play()
            return

if __name__ == '__main__':
  game = Game()
  game.start()

import copy
from ..bot_player import BotPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class BotVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne = BotPlayer()
    self.playerTwo = BotPlayer()

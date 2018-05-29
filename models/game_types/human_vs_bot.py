import copy
from ..bot_player import BotPlayer
from ..human_player import HumanPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class HumanVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne = HumanPlayer()
    self.playerTwo = BotPlayer()

  def set_up(self):
    self.playerOne.set_token(self.handlePlayerInput.get_player_token())
    self.playerTwo.auto_token(self.playerOne.token)
    first_player = self.handlePlayerInput.get_first_player()
    self.handleTurns.set_currentPlayerToken(first_player)

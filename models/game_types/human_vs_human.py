import copy
from ..human_player import HumanPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class HumanVsHuman(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne = HumanPlayer()
    self.playerTwo = HumanPlayer()

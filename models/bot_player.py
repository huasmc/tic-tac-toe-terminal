from .AI import MiniMax
from .abstracts.player import Player
from .game_display import GameDisplay

class BotPlayer(Player):

  def __init__(self):
      super().__init__()
      self.AI = None

  def play(self, board):
        GameDisplay.log("Wait, Computer is thinking..")
        spot = int(self.AI.get_best_spot(board))
        board.grid[spot] = self.token
        return spot

  def initialize_AI(self):
      if( self.token != None):
          self.AI = MiniMax(self.token)

  def set_token(self, token):
      self.token = token
      self.initialize_AI()

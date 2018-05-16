from .AI import MiniMax
from .abstracts.player import Player

class ComputerPlayer(Player):

  def __init__(self):
      super().__init__()
      self.AI = None

  def play(self, board):
        print('Computer: Wait Im thinking..')
        spot = int(self.AI.get_best_spot(board))
        board.grid[spot] = self.token
        return spot

  def auto_token(self, opponents_token):
     if ('O' != opponents_token != 'X' ):
      return 'Invalid opponents token'
     else:
          if (opponents_token == 'X'):
              self.set_token('O')
          else:
              self.set_token('X')


  def initialize_AI(self):
      if( self.token != None):
          self.AI = MiniMax(self.token)

  def set_token(self, token):
      self.token = token
      self.initialize_AI()

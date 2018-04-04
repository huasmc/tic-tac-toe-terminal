from .abstracts.player import Player
class HumanPlayer(Player):

  def __init__(self):
      super().__init__()
# Can create class that takes input from terminal
# pass input as argument for method. SOLID

  def play(self, board, spot):
    # spot = None
    # while spot is None:
    #   spot = int(raw_input())
      if board.grid[spot] != "X" and board.grid[spot] != "O":
        board.grid[spot] = self.token
      else:
        spot = None

  def set_token(self, token):
      self.token = token

  def auto_token(self, opponents_token):
      if(opponents_token == 'X'):
          self.set_token('O')
      else:
          self.set_token('X')

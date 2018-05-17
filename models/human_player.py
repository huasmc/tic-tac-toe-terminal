from .abstracts.player import Player
class HumanPlayer(Player):

  def __init__(self):
      super().__init__()

  def play(self, board, spot):
      if board.grid[spot] != "X" and board.grid[spot] != "O":
        board.grid[spot] = self.token
      else:
        spot = None

  def set_token(self, token):
      self.token = token

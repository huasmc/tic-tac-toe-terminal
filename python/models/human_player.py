class HumanPlayer:

  def __init__(self):
      self.token = 'X'

  def get_human_spot(self, board):
    spot = None
    while spot is None:
      spot = int(raw_input())
      if board.grid[spot] != "X" and board.grid[spot] != "O":
        board.grid[spot] = self.token
      else:
        spot = None

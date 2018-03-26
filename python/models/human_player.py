class HumanPlayer:
  def get_human_spot(self, board, token):
    spot = None
    while spot is None:
      spot = int(raw_input())
      if board.grid[spot] != "X" and board.grid[spot] != "O":
        board.grid[spot] = token
      else:
        spot = None

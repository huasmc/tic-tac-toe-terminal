class HumanPlayer:
  def get_human_spot(self, board, token):
    spot = None
    while spot is None:
      spot = int(raw_input())
      if board[spot] != "X" and board[spot] != "O":
        board[spot] = token
      else:
        spot = None

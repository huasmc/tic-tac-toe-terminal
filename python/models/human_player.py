class HumanPlayer:
  def get_human_spot(self):
    spot = None
    while spot is None:
      spot = int(raw_input())
      if self.board[spot] != "X" and self.board[spot] != "O":
        self.board[spot] = self.hum
      else:
        spot = None

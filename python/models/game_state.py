class GameState:
  def three_in_a_row(self, *args):
    return args[0] == args[1] == args[2] == "X" or \
        args[0] == args[1] == args[2] == "O"

  def game_is_over(self, b):
    return self.three_in_a_row(b[0], b[1], b[2]) == 1 or \
        self.three_in_a_row(b[3], b[4], b[5]) == 1 or \
        self.three_in_a_row(b[6], b[7], b[8]) == 1 or \
        self.three_in_a_row(b[0], b[3], b[6]) == 1 or \
        self.three_in_a_row(b[1], b[4], b[7]) == 1 or \
        self.three_in_a_row(b[2], b[5], b[8]) == 1 or \
        self.three_in_a_row(b[0], b[4], b[8]) == 1 or \
        self.three_in_a_row(b[2], b[4], b[6]) == 1

  def tie(self, b):
    return len([s for s in b if s == "X" or s == "O"]) == 9

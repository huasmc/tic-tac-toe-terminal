class HumanPlayer:

  def __init__(self):
      self.token = 'X'
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

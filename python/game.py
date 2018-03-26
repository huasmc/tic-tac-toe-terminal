class Game:
  def __init__(self):
    self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    self.com = "X" # the computer's marker
    self.hum = "O" # the user's marker

  def start_game(self):
    # start by printing the board
    print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
        (self.board[0], self.board[1], self.board[2],
             self.board[3], self.board[4], self.board[5],
             self.board[6], self.board[7], self.board[8])
    print "Enter [0-8]:"
    # loop through until the game was won or tied
    while not self.game_is_over(self.board) and not self.tie(self.board):
      self.get_human_spot()
      if not self.game_is_over(self.board) and not self.tie(self.board):
        self.eval_board()

      print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
          (self.board[0], self.board[1], self.board[2],
               self.board[3], self.board[4], self.board[5],
               self.board[6], self.board[7], self.board[8])

    print "Game over"

  def get_human_spot(self):
    spot = None
    while spot is None:
      spot = int(raw_input())
      if self.board[spot] != "X" and self.board[spot] != "O":
        self.board[spot] = self.hum
      else:
        spot = None

if __name__ == '__main__':
  game = Game()
  game.start_game()

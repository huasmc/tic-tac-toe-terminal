class ComputerPlayer:
    
  def eval_board(self):
    spot = None
    while spot is None:
      if self.board[4] == "4":
        spot = 4
        self.board[spot] = self.com
      else:
        spot = self.get_best_move(self.board, self.com)
        if self.board[spot] != "X" and self.board[spot] != "O":
          self.board[spot] = self.com
        else:
          spot = None

  def get_best_move(self, board, next_player, depth = 0, best_score = {}):
    available_spaces = [s for s in board if s != "X" and s != "O"]
    best_move = None

    for avail in available_spaces:
      board[int(avail)] = self.com
      if self.game_is_over(board):
        best_move = int(avail)
        board[int(avail)] = avail
        return best_move
      else:
        board[int(avail)] = self.hum
        if self.game_is_over(board):
          best_move = int(avail)
          board[int(avail)] = avail
          return best_move
        else:
          board[int(avail)] = avail

    if best_move:
      return best_move
    else:
      return int(available_spaces[0])

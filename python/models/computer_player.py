class ComputerPlayer:

  def eval_board(self, board, token, gameState):
    spot = None
    while spot is None:
      if board[4] == "4":
        spot = 4
        board[spot] = token
      else:
        spot = self.get_best_move(board, token, gameState)
        if board[spot] != "X" and board[spot] != "O":
          board[spot] = token
        else:
          spot = None

  def get_best_move(self, board, token, gameState):
    available_spaces = [s for s in board if s != "X" and s != "O"]
    best_move = None

    for avail in available_spaces:
      board[int(avail)] = token
      if gameState.game_is_over(board):
        best_move = int(avail)
        board[int(avail)] = avail
        return best_move
      else:
        board[int(avail)] = 'O'
        if gameState.game_is_over(board):
          best_move = int(avail)
          board[int(avail)] = avail
          return best_move
        else:
          board[int(avail)] = avail

    if best_move:
      return best_move
    else:
      return int(available_spaces[0])

class ComputerPlayer:

  def play(self, board, token, gameState):
    spot = None
    while spot is None:
      if board.grid[4] == "4":
        spot = 4
        board.grid[spot] = token
      else:
        spot = self.get_best_move(board, token, gameState)
        if board.grid[spot] != "X" and board.grid[spot] != "O":
          board.grid[spot] = token
        else:
          spot = None

  def get_best_move(self, board, token, gameState):
    available_spaces = [s for s in board.grid if s != "X" and s != "O"]
    best_move = None

    for avail in available_spaces:
      board.grid[int(avail)] = token
      if gameState.get_state(board):
        best_move = int(avail)
        board.grid[int(avail)] = avail
        return best_move
      else:
        board.grid[int(avail)] = 'O'
        if gameState.get_state(board):
          best_move = int(avail)
          board.grid[int(avail)] = avail
          return best_move
        else:
          board.grid[int(avail)] = avail

    if best_move:
      return best_move
    else:
      return int(available_spaces[0])

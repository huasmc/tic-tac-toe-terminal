class ComputerPlayer:
  def __init__(self):
      self.token = 'O'

  def play(self, board, gameState):
    spot = None
    while spot is None:
      if board.grid[4] == "4":
        spot = 4
        board.grid[spot] = self.token
      else:
        spot = self.get_best_move(board, gameState)
        if board.grid[spot] != "X" and board.grid[spot] != "O":
          board.grid[spot] = self.token
        else:
          spot = None

  def get_best_move(self, board, gameState):
    available_spaces = [s for s in board.grid if s != "X" and s != "O"]
    best_move = None

    for avail in available_spaces:
      board.grid[int(avail)] = self.token
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

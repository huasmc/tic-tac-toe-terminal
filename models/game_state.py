class GameState:

  def finished(self, board):
      return self.check_win(board)[0] or self.tie(board)

  def check_win(self, board):
      for combination in board.win_combinations:
        if self.check_combination_state(combination, board):
            return [True, board.grid[combination[0]]]
      return [False, None]

  def check_combination_state(self, combination, board):
      return board.grid[combination[0]] == board.grid[combination[1]] == board.grid[combination[2]] == 'X' or \
        board.grid[combination[0]] == board.grid[combination[1]] == board.grid[combination[2]] == 'O'

  def tie(self, board):
    return len([s for s in board.grid if s == "X" or s == "O"]) == 9

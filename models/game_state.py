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

  # def three_in_a_row(self, *args):
  #   return args[0] == args[1] == args[2] == "X" or \
  #       args[0] == args[1] == args[2] == "O"
  #
  # def game_is_over(self, board):
  #   return self.three_in_a_row(board.grid[0], board.grid[1], board.grid[2]) == 1 or \
  #       self.three_in_a_row(board.grid[3], board.grid[4], board.grid[5]) == 1 or \
  #       self.three_in_a_row(board.grid[6], board.grid[7], board.grid[8]) == 1 or \
  #       self.three_in_a_row(board.grid[0], board.grid[3], board.grid[6]) == 1 or \
  #       self.three_in_a_row(board.grid[1], board.grid[4], board.grid[7]) == 1 or \
  #       self.three_in_a_row(board.grid[2], board.grid[5], board.grid[8]) == 1 or \
  #       self.three_in_a_row(board.grid[0], board.grid[4], board.grid[8]) == 1 or \
  #       self.three_in_a_row(board.grid[2], board.grid[4], board.grid[6]) == 1

  def tie(self, board):
    return len([s for s in board.grid if s == "X" or s == "O"]) == 9
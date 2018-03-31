from AI import MiniMax

class ComputerPlayer:

  def __init__(self):
      self.token = None
      self.AI = None

  def play(self, board):
      # if ( board.grid[4] != "X" and board.grid[4] != "O" ):
      #   spot = int(4)
      #   board.grid[spot] = self.token
      # else:
        spot = int(self.AI.get_best_spot(board))
        board.grid[spot] = self.token
        print(f"Computer has played on position {spot}.")

  def set_token(self, opponents_token):
      if (opponents_token == 'X'):
          self.token = 'O'
      else:
            self.token = 'X'
      self.initialize_AI()

  def initialize_AI(self):
      if( self.token != None):
          self.AI = MiniMax(self.token)


      #
      #
      #
      # def play(self, board, gameState):
      # spot = None
      # while spot is None:
      #   if board.grid[4] == "4":
      #     spot = 4
      #     board.grid[spot] = self.token
      #   else:
      #     spot = self.get_best_move(board, gameState)
      #     if board.grid[spot] != "X" and board.grid[spot] != "O":
      #       board.grid[spot] = self.token
      #     else:
      #       spot = None
      #
      # def get_best_move(self, board, gameState):
      #   available_spots = board.get_available_spots()
      #   best_move = None
      #
      #   for spot in available_spots:
      #     board.grid[int(spot)] = self.token
      #     if gameState.get_state(board):
      #       best_move = int(spot)
      #       board.grid[int(spot)] = spot
      #       return best_move
      #     else:
      #       board.grid[int(spot)] = self.token
      #       if gameState.get_state(board):
      #         best_move = int(spot)
      #         board.grid[int(spot)] = spot
      #         return best_move
      #       else:
      #         board.grid[int(spot)] = spot
      #
      #   if best_move:
      #     return best_move
      #   else:
      #     return int(available_spots[0])

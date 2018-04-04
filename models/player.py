class Player(object):

 def __init__(self):
     self.token = None

 def play(self, board, spot):
     if board.grid[spot] != "X" and board.grid[spot] != "O":
       board.grid[spot] = self.token
       return spot
     else:
       spot = None
       return spot

 def set_token(self, token):
     self.token = token

 def auto_token(self, opponents_token):
     if(opponents_token == 'X'):
         self.set_token('O')
     else:
         self.set_token('X')

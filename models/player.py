from abc import ABCMeta, abstractmethod
class Player(metaclass=ABCMeta):

 def __init__(self):
     self.token = None

 @abstractmethod
 def play(self, board, spot):
     if board.grid[spot] != "X" and board.grid[spot] != "O":
       board.grid[spot] = self.token
       return spot
     else:
       spot = None
       return spot

 @abstractmethod
 def set_token(self, token):
     self.token = token

 @abstractmethod
 def auto_token(self, opponents_token):
     if(opponents_token == 'X'):
         self.set_token('O')
     else:
         self.set_token('X')

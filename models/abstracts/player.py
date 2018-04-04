from abc import ABCMeta, abstractmethod
class Player(metaclass=ABCMeta):

 def __init__(self):
     self.token = None

 @abstractmethod
 def play(self, board, spot):
     raise NotImplementedError

 @abstractmethod
 def set_token(self, token):
     raise NotImplementedError

 @abstractmethod
 def auto_token(self, opponents_token):
     raise NotImplementedError

from abc import ABCMeta, abstractmethod

class GameType(metaclass=ABCMeta):
    
 def __init__(self):
    self.board = Board()
    self.gameState = GameState()
    self.handlePlayerInput = HandlePlayerInput()
    self.handleTurns = HandleTurns()

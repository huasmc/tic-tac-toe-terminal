from abc import ABCMeta, abstractmethod
from ..game_state import GameState
from ..board import Board
from ..game_display import GameDisplay
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns

class GameType(metaclass=ABCMeta):

 def __init__(self):
    self.board = Board()
    self.gameState = GameState()
    self.handlePlayerInput = HandlePlayerInput()
    self.handleTurns = HandleTurns()

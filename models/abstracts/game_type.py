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

    def play(self):
        self.set_up()
        GameDisplay.show(self.board)
        self.start()
        GameDisplay.show(self.board)
        GameDisplay.log('Game Over')

    @abstractmethod
    def set_tokens(self):
        raise NotImplementedError

    def set_up(self):
        self.set_tokens()

    def end_game(self):
        if (self.gameState.check_win(self.board)[0]):
         winner = self.gameState.check_win(self.board)[1][0]
         GameDisplay.log(f"Player with token {winner} won!")
        elif (self.gameState.finished(self.board)):
         GameDisplay.log1("It's a tie!")

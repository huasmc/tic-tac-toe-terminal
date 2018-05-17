from abc import ABCMeta, abstractmethod
from ..game_state import GameState
from ..board import Board
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
from ..game_display import GameDisplay

class GameType(metaclass=ABCMeta):

    def __init__(self):
        self.board = Board()
        self.gameState = GameState()
        self.handlePlayerInput = HandlePlayerInput()
        self.handleTurns = HandleTurns()
        self.playerOne = None
        self.playerTwo = None

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
        self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()
        self.set_tokens()

    def end_game(self):
        if (self.gameState.check_win(self.board)[0]):
         winner = self.gameState.check_win(self.board)[1][0]
         GameDisplay.log(f"Player with token {winner} won!")
        elif (self.gameState.finished(self.board)):
         GameDisplay.log("It's a tie!")

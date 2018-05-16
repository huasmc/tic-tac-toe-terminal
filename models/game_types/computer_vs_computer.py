import copy
from ..game_state import GameState
from ..computer_player import ComputerPlayer
from ..board import Board
from ..game_display import GameDisplay
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class ComputerVsComputer:
  def __init__(self):
    self.board = Board()
    self.gameState = GameState()
    self.computerPlayer1 = ComputerPlayer()
    self.computerPlayer2 = ComputerPlayer()
    self.handlePlayerInput = HandlePlayerInput()
    self.gameState = GameState()
    self.handleTurns = HandleTurns()

  def play(self):
    self.set_up()
    GameDisplay.show(self.board)
    self.start()
    GameDisplay.show(self.board)
    GameDisplay.log('Game Over')

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.computerPlayer1.token):
             spot = self.computerPlayer1.play(self.board)
             GameDisplay.log(f"Computer {self.computerPlayer1.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.computerPlayer2.play(self.board)
             GameDisplay.log(f"Computer {self.computerPlayer2.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
     self.end_game()

  def set_up(self):
      self.set_tokens()

  def set_tokens(self):
      while self.computerPlayer2.token == None:
          player_token = self.handlePlayerInput.get_first_player()
          self.handleTurns.currentPlayerToken = player_token
          self.computerPlayer1.set_token(player_token)
          self.computerPlayer2.auto_token(self.computerPlayer1.token)

  def end_game(self):
      if (self.gameState.check_win(self.board)[0]):
        winner = self.gameState.check_win()[1][0]
        GameDisplay.log(f"Computer {winner} won!")
      elif (self.gameState.finished(self.board)):
        GameDisplay.log("It's a tie!")

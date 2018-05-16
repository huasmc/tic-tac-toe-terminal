import copy
from ..game_state import GameState
from ..human_player import HumanPlayer
from ..board import Board
from ..game_display import GameDisplay
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class HumanVsHuman:
  def __init__(self):
    self.board = Board()
    self.gameDisplay = GameDisplay()
    self.gameState = GameState()
    self.humanPlayer1 = HumanPlayer()
    self.humanPlayer2 = HumanPlayer()
    self.handlePlayerInput = HandlePlayerInput()
    self.gameState = GameState()
    self.handleTurns = HandleTurns()

  def play(self):
    self.set_up()
    self.gameDisplay.show(self.board)
    self.start()
    self.gameDisplay.show(self.board)
    print('Game Over')
    os.system("find . -name *.pyc -delete")

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.humanPlayer1.token):
             spot = self.let_humanPlayer_play(self.humanPlayer1)
             print(f"Human {self.humanPlayer1.token} has played in spot {spot}")
             self.gameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.let_humanPlayer_play(self.humanPlayer2)
             print(f"Human {self.humanPlayer2.token} has played in spot {spot}")
             self.gameDisplay.show(self.board)
             self.handleTurns.change()
         self.end_game()

  def let_humanPlayer_play(self, player):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      player.play(self.board, spot)
      return spot

  def set_up(self):
      self.set_tokens()
      self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()

  def set_tokens(self):
      while self.humanPlayer1.token == None and self.humanPlayer2.token == None:
          player1_token = self.handlePlayerInput.get_player_token()
          self.humanPlayer1.set_token(player1_token)
          self.humanPlayer2.auto_token(player1_token)

  def end_game(self):
     if (self.gameState.check_win(self.board)[0]):
       winner = self.gameState.check_win(self.board)[1][0]
       print(f"Human {winner} won!")
     elif (self.gameState.finished(self.board)):
       print("It's a tie!")

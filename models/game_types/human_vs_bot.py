import copy
from ..game_state import GameState
from ..human_player import HumanPlayer
from ..bot_player import BotPlayer
from ..board import Board
from ..game_display import GameDisplay
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class HumanVsBot:
  def __init__(self):
    self.board = Board()
    self.gameState = GameState()
    self.humanPlayer = HumanPlayer()
    self.botPlayer = BotPlayer()
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
         if(self.handleTurns.currentPlayerToken == self.humanPlayer.token):
             spot = self.let_humanPlayer_play()
             GameDisplay.log(f"Human {self.humanPlayer.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.botPlayer.play(self.board)
             GameDisplay.log(f"Bot {self.botPlayer.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         self.end_game()

  def let_humanPlayer_play(self):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      self.humanPlayer.play(self.board, spot)
      return spot

  def set_up(self):
      self.set_tokens()
      self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()

  def set_tokens(self):
      while self.botPlayer.token == None:
          player_token = self.handlePlayerInput.get_player_token()
          self.humanPlayer.set_token(player_token)
          self.botPlayer.auto_token(player_token)

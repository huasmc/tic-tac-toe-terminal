import copy
from ..bot_player import BotPlayer
from ..abstracts.game_type import GameType
import os

class BotVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.botPlayer1 = BotPlayer()
    self.botPlayer2 = BotPlayer()

  def play(self):
    self.set_up()
    GameDisplay.show(self.board)
    self.start()
    GameDisplay.show(self.board)
    GameDisplay.log('Game Over')

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.botPlayer1.token):
             spot = self.botPlayer1.play(self.board)
             GameDisplay.log(f"Bot {self.botPlayer1.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.botPlayer2.play(self.board)
             GameDisplay.log(f"Bot {self.botPlayer2.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
     self.end_game()

  def set_up(self):
      self.set_tokens()

  def set_tokens(self):
      while self.botPlayer2.token == None:
          player_token = self.handlePlayerInput.get_first_player()
          self.handleTurns.currentPlayerToken = player_token
          self.botPlayer1.set_token(player_token)
          self.botPlayer2.auto_token(self.botPlayer1.token)

  def end_game(self):
      if (self.gameState.check_win(self.board)[0]):
        winner = self.gameState.check_win()[1][0]
        GameDisplay.log(f"Bot {winner} won!")
      elif (self.gameState.finished(self.board)):
        GameDisplay.log("It's a tie!")

import copy
from ..bot_player import BotPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class BotVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.firstPlayer = BotPlayer()
    self.secondPlayer = BotPlayer()

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.firstPlayer.token):
             spot = self.firstPlayer.play(self.board)
             GameDisplay.log(f"Bot {self.firstPlayer.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.secondPlayer.play(self.board)
             GameDisplay.log(f"Bot {self.secondPlayer.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
     self.end_game()

  def set_tokens(self):
      while self.secondPlayer.token == None:
          self.firstPlayer.set_token(self.handleTurns.currentPlayerToken)
          self.secondPlayer.auto_token(self.firstPlayer.token)

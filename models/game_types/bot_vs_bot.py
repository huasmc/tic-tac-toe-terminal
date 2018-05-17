import copy
from ..bot_player import BotPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class BotVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.botPlayer1 = BotPlayer()
    self.botPlayer2 = BotPlayer()

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

  def set_tokens(self):
      while self.botPlayer2.token == None:
          self.botPlayer1.set_token(self.handleTurns.currentPlayerToken)
          self.botPlayer2.auto_token(self.botPlayer1.token)

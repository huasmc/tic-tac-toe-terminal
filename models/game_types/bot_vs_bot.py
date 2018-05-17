import copy
from ..bot_player import BotPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class BotVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne = BotPlayer()
    self.playerTwo = BotPlayer()

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.playerOne.token):
             spot = self.playerOne.play(self.board)
             GameDisplay.log(f"Bot {self.playerOne.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.playerTwo.play(self.board)
             GameDisplay.log(f"Bot {self.playerTwo.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
     self.end_game()

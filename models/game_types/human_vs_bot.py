import copy
from ..bot_player import BotPlayer
from ..human_player import HumanPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class HumanVsBot(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne = HumanPlayer()
    self.playerTwo = BotPlayer()

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.playerOne.token):
             spot = self.let_playerOne_play()
             GameDisplay.log(f"Human {self.playerOne.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.playerTwo.play(self.board)
             GameDisplay.log(f"Bot {self.playerTwo.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         self.end_game()

  def let_playerOne_play(self):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      self.playerOne.play(self.board, spot)
      return spot

  def set_tokens(self):
      while self.playerTwo.token == None:
          player_token = self.handlePlayerInput.get_player_token()
          self.playerOne.set_token(player_token)
          self.playerTwo.auto_token(player_token)

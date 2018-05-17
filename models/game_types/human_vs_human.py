import copy
from ..human_player import HumanPlayer
from ..abstracts.game_type import GameType
from ..game_display import GameDisplay

class HumanVsHuman(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne= HumanPlayer()
    self.playerTwo = HumanPlayer()

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.playerOne.token):
             spot = self.let_humanPlayer_play(self.playerOne)
             GameDisplay.log(f"Human {self.playerOne.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         else:
             spot = self.let_humanPlayer_play(self.playerTwo)
             GameDisplay.log(f"Human {self.playerTwo.token} has played in spot {spot}")
             GameDisplay.show(self.board)
             self.handleTurns.change()
         self.end_game()

  def let_humanPlayer_play(self, player):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      player.play(self.board, spot)
      return spot

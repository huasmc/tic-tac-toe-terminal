import copy
from ..human_player import HumanPlayer
from ..abstracts.game_type import GameType

class HumanVsHuman(GameType):
  def __init__(self):
    super().__init__()
    self.playerOne= HumanPlayer()
    self.playerTwo = HumanPlayer()

  def play(self):
    self.set_up()
    GameDisplay.show(self.board)
    self.start()
    GameDisplay.show(self.board)
    GameDisplay.log('Game Over')

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

  def set_up(self):
      self.set_tokens()
      self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()

  def set_tokens(self):
      while self.playerOne.token == None and self.playerTwo.token == None:
          player1_token = self.handlePlayerInput.get_player_token()
          self.playerOne.set_token(player1_token)
          self.playerTwo.auto_token(player1_token)

  def end_game(self):
     if (self.gameState.check_win(self.board)[0]):
       winner = self.gameState.check_win(self.board)[1][0]
       GameDisplay.log(f"Human {winner} won!")
     elif (self.gameState.finished(self.board)):
       GameDisplay.log("It's a tie!")

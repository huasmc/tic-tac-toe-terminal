import copy
from ..game_state import GameState
from ..human_player import HumanPlayer
from ..board import Board
from ..display_board import DisplayBoard
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class HumanVsHuman:
  def __init__(self):
    self.board = Board()
    self.displayBoard = DisplayBoard()
    self.gameState = GameState()
    self.humanPlayer1 = HumanPlayer()
    self.humanPlayer2 = HumanPlayer()
    self.handlePlayerInput = HandlePlayerInput()
    self.gameState = GameState()
    self.handleTurns = HandleTurns()

  def play(self):
    # Choose tokens.
    self.set_up()
    # Show board.
    self.displayBoard.logs(self.board)
    # Start the game.
    self.start()
    # Print the board when finished.
    self.displayBoard.logs(self.board)
    # Inform the player the game has finished.
    print('Game Over')
    # Delete compiled *.pyc files after game over to keep file structure clean.
    os.system("find . -name *.pyc -delete")

  def start(self):
    # Prevent the game from exit before finishing using 'while not' loop.
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.humanPlayer1.token):
             spot = self.let_humanPlayer_play(self.humanPlayer1)
             print(f"Human {self.humanPlayer1.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()
         else:
             spot = self.let_humanPlayer_play(self.humanPlayer2)
             print(f"Human {self.humanPlayer2.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()

  def let_humanPlayer_play(self, player):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      player.play(self.board, spot)
      return spot

  # Set tokens and first player
  def set_up(self):
      self.set_tokens()
      self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()

  # Set tokens
  def set_tokens(self):
      while self.humanPlayer1.token == None and self.humanPlayer2.token == None:
          player1_token = self.handlePlayerInput.get_player_token()
          self.humanPlayer1.set_token(player1_token)
          self.humanPlayer2.auto_token(player1_token)

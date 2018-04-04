import copy
from ..game_state import GameState
from ..computer_player import ComputerPlayer
from ..board import Board
from ..display_board import DisplayBoard
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class ComputerVsComputer:
  def __init__(self):
    self.board = Board()
    self.displayBoard = DisplayBoard()
    self.gameState = GameState()
    self.computerPlayer1 = ComputerPlayer()
    self.computerPlayer2 = ComputerPlayer()
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
         if(self.handleTurns.currentPlayerToken == self.computerPlayer1.token):
             spot = self.computerPlayer1.play(self.board)
             print(f"{self.computerPlayer1.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()
         else:
             spot = self.computerPlayer2.play(self.board)
             print(f"{self.computerPlayer2.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()

  # Set tokens and first player
  def set_up(self):
      self.set_tokens()

  # Set tokens
  def set_tokens(self):
      while self.computerPlayer2.token == None:
          # Asks viewer for the token that the first computer player is going to use.
          player_token = self.handlePlayerInput.get_first_player()
          self.handleTurns.currentPlayerToken = player_token
          # Sets this token to player one.
          self.computerPlayer1.set_token(player_token)
          self.computerPlayer2.auto_token(self.computerPlayer1.token)

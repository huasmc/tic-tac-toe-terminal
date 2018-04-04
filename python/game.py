import sys
import copy
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from game_state import GameState
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board
from display_board import DisplayBoard
from handle_player_input import HandlePlayerInput
import os


class Game:
  def __init__(self):
    self.board = Board()
    self.displayBoard = DisplayBoard()
    self.gameState = GameState()
    self.humanPlayer = HumanPlayer()
    self.computerPlayer = ComputerPlayer()
    self.handlePlayerInput = HandlePlayerInput()
    self.gameState = GameState()

  def play(self):
    # Choose tokens.
    self.set_up()
    # Put the board on table.
    self.displayBoard.logs(self.board)
    # Start the game.
    self.start()
    # Print the board when finished.
    self.displayBoard.logs(self.board)
    # Inform the player the game has finished.
    print('Game Over')
    # Delete compiled *.pyc files after game over to keep file structure clean.
    os.system("find . -name *.pyc -delete")

  # Start the game.
  def start(self):
    # Prevent the game from exit before finishing using 'while not' loop.
    while not self.gameState.finished(self.board):
        try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
        spot = copy.deepcopy(try_spot)
        self.humanPlayer.play(self.board, spot)

        if not self.gameState.finished(self.board):
            self.computerPlayer.play(self.board)
            self.displayBoard.logs(self.board)


  # Set tokens
  def set_up(self):
      while self.computerPlayer.token == None:
          player_token = self.handlePlayerInput.get_player_token()
          self.humanPlayer.set_token(player_token)
          self.computerPlayer.set_token(player_token)



if __name__ == '__main__':
  game = Game()
  game.play()

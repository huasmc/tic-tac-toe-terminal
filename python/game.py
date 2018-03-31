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

  def start_game(self):
    # start by printing the board
    self.displayBoard.logs(self.board)

    print('Enter [0-8]')

    # loop through until the game was won or tied
    while not self.gameState.finished(self.board):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      self.humanPlayer.play(self.board, spot)

      if not self.gameState.finished(self.board):
        self.computerPlayer.play(self.board)

        self.displayBoard.logs(self.board)
    self.displayBoard.logs(self.board)
    print('Game Over')

    # Delete compiled *.pyc files after game over to keep file structure clean.
    os.system("find . -name *.pyc -delete")


if __name__ == '__main__':
  game = Game()
  game.start_game()

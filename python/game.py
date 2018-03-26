import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from game_state import GameState
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board
from display_board import DisplayBoard

class Game:
  def __init__(self):
    self.board = Board()
    self.displayBoard = DisplayBoard();
    self.com = "X" # the computer's marker
    self.hum = "O" # the user's marker
    self.gameState = GameState()
    self.humanPlayer = HumanPlayer()
    self.computerPlayer = ComputerPlayer()

  def start_game(self):
    # start by printing the board
    self.displayBoard.logs(self.board)
    print "Enter [0-8]:"
    # loop through until the game was won or tied
    while not self.gameState.game_is_over(self.board) and not self.gameState.tie(self.board):
      self.humanPlayer.get_human_spot(self.board, self.hum)
      if not self.gameState.game_is_over(self.board) and not self.gameState.tie(self.board):
        self.computerPlayer.eval_board(self.board, self.com, self.gameState)

        self.displayBoard.logs(self.board)

    print "Game over"


if __name__ == '__main__':
  game = Game()
  game.start_game()

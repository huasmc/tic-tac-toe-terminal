import sys
sys.path.append('/Users/huascar/Projects/8th-light-tictactoe/solution/python/models')
from game_state import GameState
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from board import Board

class Game:
  def __init__(self):
    self.board = Board()
    self.com = "X" # the computer's marker
    self.hum = "O" # the user's marker
    self.gameState = GameState()
    self.humanPlayer = HumanPlayer()
    self.computerPlayer = ComputerPlayer()

  def start_game(self):
    # start by printing the board
    print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
        (self.board[0], self.board[1], self.board[2],
             self.board[3], self.board[4], self.board[5],
             self.board[6], self.board[7], self.board[8])
    print "Enter [0-8]:"
    # loop through until the game was won or tied
    while not self.gameState.game_is_over(self.board) and not self.gameState.tie(self.board):
      self.humanPlayer.get_human_spot(self.board, self.hum)
      if not self.gameState.game_is_over(self.board) and not self.gameState.tie(self.board):
        self.computerPlayer.eval_board(self.board, self.com, self.gameState)

      print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
          (self.board[0], self.board[1], self.board[2],
               self.board[3], self.board[4], self.board[5],
               self.board[6], self.board[7], self.board[8])

    print "Game over"


if __name__ == '__main__':
  game = Game()
  game.start_game()

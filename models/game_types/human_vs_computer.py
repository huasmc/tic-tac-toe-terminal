import copy
from ..game_state import GameState
from ..human_player import HumanPlayer
from ..computer_player import ComputerPlayer
from ..board import Board
from ..display_board import DisplayBoard
from ..handle_player_input import HandlePlayerInput
from ..handle_turns import HandleTurns
import os

class HumanVsComputer:
  def __init__(self):
    self.board = Board()
    self.displayBoard = DisplayBoard()
    self.gameState = GameState()
    self.humanPlayer = HumanPlayer()
    self.computerPlayer = ComputerPlayer()
    self.handlePlayerInput = HandlePlayerInput()
    self.gameState = GameState()
    self.handleTurns = HandleTurns()

  def play(self):
    self.set_up()
    self.displayBoard.logs(self.board)
    self.start()
    self.displayBoard.logs(self.board)
    print('Game Over')
    os.system("find . -name *.pyc -delete")

  def start(self):
     while not self.gameState.finished(self.board):
         if(self.handleTurns.currentPlayerToken == self.humanPlayer.token):
             spot = self.let_humanPlayer_play()
             print(f"Human {self.humanPlayer.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()
         else:
             spot = self.computerPlayer.play(self.board)
             print(f"Computer {self.computerPlayer.token} has played in spot {spot}")
             self.displayBoard.logs(self.board)
             self.handleTurns.change()
         self.end_game()

  def let_humanPlayer_play(self):
      try_spot = self.handlePlayerInput.get_player_spot(self.board.get_available_spots())
      spot = copy.deepcopy(try_spot)
      self.humanPlayer.play(self.board, spot)
      return spot
  
  def set_up(self):
      self.set_tokens()
      self.handleTurns.currentPlayerToken = self.handlePlayerInput.get_first_player()
  
  def set_tokens(self):
      while self.computerPlayer.token == None:
          player_token = self.handlePlayerInput.get_player_token()
          self.humanPlayer.set_token(player_token)
          self.computerPlayer.auto_token(player_token)

  def end_game(self):
      if (self.gameState.check_win(self.board)[0]):
        winner = self.gameState.check_win(self.board)[1][0]
        print(f"Player with token {winner} won!")
      elif (self.gameState.finished(self.board)):
        print("It's a tie!")

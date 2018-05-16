from .game_state import GameState
from .display_board import DisplayBoard
import copy
import random

class MiniMax:

    def __init__(self, token):
        self.token = token
        self.winner = None
        self.gameState = GameState()
        if self.token == 'X':
            self.opponenttoken = 'O'
        else:
            self.opponenttoken = 'X'

    def get_best_spot(self, board):
        if ( board.grid[4] != "X" and board.grid[4] != "O" ):
         return 4
        else:
            spot = self.maximized_spot(board)
            return spot[0]

    def maximized_spot(self, board):
        clone_board = copy.deepcopy(board)

        bestscore = None
        bestspot = None

        for spot in clone_board.get_available_spots():
            clone_board.grid[int(spot)] = self.token

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                spot_position,score = self.minimized_spot(clone_board)

            clone_board = copy.deepcopy(board)

            if bestscore == None or score > bestscore:
                bestscore = score
                bestspot = spot

        return [bestspot, bestscore]

    def minimized_spot(self, board):
        clone_board = copy.deepcopy(board)

        bestscore = None
        bestspot = None

        for spot in clone_board.get_available_spots():
            clone_board.grid[int(spot)] = self.opponenttoken

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                spot_position,score = self.maximized_spot(clone_board)


            clone_board = copy.deepcopy(board)

            if bestscore == None or score < bestscore:
                bestscore = score
                bestspot = spot

        return [bestspot, bestscore]

    def get_score(self, board):
        if self.gameState.finished(board):
            self.winner = self.gameState.check_win(board)[1]
            if self.winner  == self.token:
                return 1

            elif self.winner == self.opponenttoken:
                return -1

        return 0 

    def get_random_spot(self, board):
        available_spots = board.get_available_spots()
        return random.choice(available_spots)

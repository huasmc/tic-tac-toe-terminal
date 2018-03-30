from game_state import GameState
from display_board import DisplayBoard
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
        # Play in the middle if it's empty.
        if ( board.grid[4] != "X" and board.grid[4] != "O" ):
         return 4
        # Play random to avoid slow process if there's no risk of losing.
        # elif ( len(board.get_available_spots()) > 7):
        #  return int(self.get_random_spot(board))
        # Play smart if there's risk of losing.
        else:
            spot = self.maximized_spot(board)
            return spot[0]

    def maximized_spot(self, board):
        clone_board = copy.deepcopy(board)
        # find best spot to win

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
        # ''' Find the minimized spot'''

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
                return 1 # Won

            elif self.winner == self.opponenttoken:
                return -1 # Opponent won

        return 0 # Draw

    def get_random_spot(self, board):
        available_spots = board.get_available_spots()
        return random.choice(available_spots)

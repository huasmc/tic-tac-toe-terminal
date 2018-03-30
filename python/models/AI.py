from game_state import GameState
from display_board import DisplayBoard
import copy

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
            spot = self.maximized_move(board)
            return spot[0]

    def maximized_move(self, board):
        clone_board = copy.deepcopy(board)
        # find best move to win

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.token

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.minimized_move(clone_board)

            clone_board = copy.deepcopy(board)

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return [bestmove, bestscore]

    def minimized_move(self, board):
        clone_board = copy.deepcopy(board)
        # ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.opponenttoken

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.maximized_move(clone_board)


            clone_board = copy.deepcopy(board)

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return [bestmove, bestscore]

    def get_score(self, board):
        if self.gameState.finished(board):
            self.winner = self.gameState.check_win(board)[1]
            if self.winner  == self.token:
                return 1 # Won

            elif self.winner == self.opponenttoken:
                return -1 # Opponent won

        return 0 # Draw

    def get_random_spot(self, board)

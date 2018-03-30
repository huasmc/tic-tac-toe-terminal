import copy
from game_state import GameState

class minimax:

    def __init__(self, marker):
        self.marker = marker
        self.winner = None
        self.gameState = GameState()
        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def get_best_spot(self, board):
        if ( board.grid[4] != self.opponentmarker and board.grid[4] != self.marker ):
            return 4

        spot = self.maximized_move(board)
        return spot

    def maximized_move(self, board):
        if (board.grid[4] != self.opponentmarker):
            return 4, 1

        clone_board = copy.deepcopy(board)
        # find best move to win

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.marker

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.minimized_move(clone_board)

            clone_board = board

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def minimized_move(self,board):
        clone_board = copy.deepcopy(board)
        # ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.opponentmarker

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.maximized_move(clone_board)

            clone_board = board

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return int(bestmove), bestscore

    def get_score(self,board):
        if self.gameState.finished(board):
            if self.winner  == self.marker:
                return 1 # Won

            elif self.winner == self.opponentmarker:
                return -1 # Opponent won

        return 0 # Draw

from game_state import GameState
import copy

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
            spot = self.maximized_move(board)
            return spot[0]

    def maximized_move(self, board):
        clone_board = copy.deepcopy(board)
        clone_board_reset = copy.deepcopy(board)
        # find best move to win

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.marker

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.minimized_move(clone_board)

            clone_board = clone_board_reset

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return [bestmove, bestscore]

    def minimized_move(self,board):
        clone_board = copy.deepcopy(board)
        clone_board_reset = copy.deepcopy(board)
        # ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in clone_board.get_available_spots():
            clone_board.grid[int(m)] = self.opponentmarker

            if self.gameState.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                move_position,score = self.maximized_move(clone_board)

            clone_board = clone_board_reset

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return [bestmove, bestscore]

    def get_score(self,board):
        if self.gameState.finished(board):
            print self.gameState.check_win(board)
            self.winner = self.gameState.check_win(board)[1]
            if self.winner  == self.marker:
                return 1 # Won

            elif self.winner == self.opponentmarker:
                return -1 # Opponent won

        return 0 # Draw

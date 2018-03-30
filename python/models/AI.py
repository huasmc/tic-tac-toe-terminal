from game_state import GameState

class AI:

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

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

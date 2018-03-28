import copy
from board import Board
from game_state import GameState
from display_board import DisplayBoard

class Brain:

    def __init__(self):
        self.gameState = GameState()
        self.count = 0
        self.turn = 'O'
        self.displayBoard = DisplayBoard()

    #returns the best move according to the minimax method
    def bestMove(self, board):
        # if the game is not over.

        if self.gameState.finished(board):
            return
        self.count = 0
        spots_scores = []
        # get available spaces
        available_spots = board.get_available_spots()
        # get ALL scores given EACH availabe SPOT on board
        for spot in available_spots:
            spots_scores.append([self.miniMax(self.turn, board)])

        print spots_scores

        # Searchs for the available spot with the highest score.
        spots_max_score = spots_scores[self.max(spots_scores)]
        # Searchs for the available spot with the lowest score.
        spots_min_score = spots_scores[self.min(spots_scores)]
        self.displayBoard.logs(board)
        return [spots_max_score, spots_min_score]

        # if (self.originalBoard.getTurn() == self.originalBoard.State.x):
            # return moves[self.max(scores)]
        # else:
            # return moves[self.min(scores)]

    #classic minimax with alphabeta pruning
    def miniMax(self, turn, board, depth = 0) :
        # *** not needed
        # if first :
            # best = 0
            # *** not needed
            # self._copySquares = deepcopy(self._squares)
        # *** always start with initilisation of `best`, but with worst possible value
        #     for this player
            board_clone = copy.deepcopy(board)
            if turn == "O":
                best = -10
            else:
                best = 10
            # print self.gameState.finished(board_clone)
            if self.gameState.finished(board_clone):
                if turn == "X" :
                    # *** don't do this, you may still need the position to try other moves
                    # self._squares = self._copySquares
                    # *** value should be closer to zero for greater depth!
                    # *** expect tuple return value
                    return -10 + depth, None
                elif self.gameState.tie(board_clone) == "tie":
                    # self._squares = self._copySquares
                    # *** expect tuple return value
                    return 0, None
                elif turn == "O":
                    # self._squares = self._copySquares
                    # *** value should be closer to zero for greater depth!
                    # *** expect tuple return value
                    return 10 - depth, None
                # *** Execution can never get here
                # best = None
            available_spots = board_clone.get_available_spots()
            for move in available_spots:
                # *** don't increase depth in each iteration, instead pass depth+1 to
                #    the recursive call
                # depth += 1
                45444erfct
                self.fake_play(board_clone, move)
                print turn
                # *** pass depth+1, no need for passing `node` nor `first`.
                # *** expect tuple return value
                val, _ = self.miniMax(turn, board_clone, depth+1)
                # print best
                # *** undo last move

                self.fake_play(board_clone, move)
                if turn == "O" :
                    # print best
                    if val > best:

                        # *** Also keep track of the actual move
                        best, bestMove = val, move
                        # print best, bestMove
                else :
                    if val < best :
                        # *** Also keep track of the actual move
                        best, bestMove = val, move
                # *** don't interrupt the loop here!
                # return best
                # *** this is dead code:
                # print()
                # print()
            # *** Also keep track of the actual move
            return best, bestMove

    #helper method that returns the index of the highest number in a list
    def max(self, list):
        max = -1
        index = 0
        if list.__len__() == 1:
            return index

        for i in range (len(list)):
            if (list[i] > max):
                max = list[i]
                index = i
        return index

     #helper method that returns the index of the lowest number in a list
    def min(self, list):
        min = 1
        index = 0
        if list.__len__() == 1:
            return index

        for i in range (len(list)):
            if (list[i] < min):
                min = list[i]
                index = i
        return index

    def fake_play(self, board_clone, move):
        spot = int(move)
        board_clone.grid[spot] = self.turn
        self.take_fake_turn(board_clone)

    def take_fake_turn(self, board):
        if not self.gameState.finished(board):
            if self.turn == 'O':
                # print 'X'
                self.turn = 'X'
            else:
                # print 'O'
                self.turn = 'O'











                # def miniMax(self, board, spot, alpha = -1, beta = 1):
                #
                #     self.count += 1
                #     # Native module that copies objects. Similar to mock.
                #     board_clone = copy.deepcopy(board)
                #     # Play on spot(will create temporal method to change board here)
                #     spot = int(spot)
                #
                #     self.fake_play(board_clone, spot)
                #
                #     # if clone.gameOver:
                #     #     return clone.getWinner()
                #     # if self.gameState.finished(board_clone) == False:
                #     #     return 'over'
                #
                #
                #
                #     available_spots = board_clone.get_available_spots()
                #
                #     print self.turn
                #     # if it's the human player's turn
                #     if self.turn == 'O':
                #         print 'lol'
                #         for spot in available_spots:
                #             score = self.miniMax(board_clone, spot, alpha, beta)
                #             if score > alpha:
                #                 alpha += score
                #                 if alpha >= beta:
                #                     break
                #
                #                     return alpha
                #
                #                 else:
                #                     print 'it runs this ####loop'
                #                     for spot in available_spots:
                #                         score = self.miniMax(board_clone, spot, alpha, beta)
                #                         if score < beta:
                #                             beta += score
                #                             if alpha >= beta:
                #                                 break
                #                                 return beta

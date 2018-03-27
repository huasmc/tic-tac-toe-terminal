import copy
from board import Board

class Brain:

def __init__(self, board):
    self.originalBoard = board
    self.count = 0

#returns the best move according to the minimax method
def bestMove(self):
    if self.originalBoard.gameOver:
        return
    self.count = 0
    scores = []
    # get available spaces
    move = self.originalBoard.getMoves()
    # check scores for available spaces in board
    for m in moves:
        scores.append(self.miniMax(self.originalBoard, m))

    print(self.count)

    if (self.originalBoard.getTurn() == self.originalBoard.State.x):
        return moves[self.max(scores)]
    else:
        return moves[self.min(scores)]

#classic minimax with alphabeta pruning
def miniMax(self, board, move, alpha = -1, beta = 1):

    self.count += 1
    clone = copy.deepcopy(board) >now replaced as I said in the intro<
    clone.applyMove(move)

    if clone.gameOver:
        return clone.getWinner()

    availableMoves = board.getMoves()
    if clone.getTurn() == clone.State.x:

        for m in availableMoves:
            score = self.miniMax(clone, m, alpha, beta)
            if score > alpha:
                alpha = score
                if alpha >= beta:
                    break
        return alpha

    else:
        for m in availableMoves:
            score = self.miniMax(clone, m, alpha, beta)
            if score < beta:
                beta = score
                if alpha >= beta:
                    break
        return beta

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

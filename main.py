from Utils import *
import random
import timeit
def move(curBoard, preBoard, player, remain_time_x, remain_time_y):
        start = timeit.default_timer()
        depth = 3
        bestMove = Move(Position(-1, -1), Position(-1, -1))
        moves = getValidMoves(curBoard, preBoard, player)
        bestMoves = []
        bestValues = []
        #Initial game set preBoard equal None
        if isNewGame(curBoard, preBoard) | (depth == 0) :
            return random.choice(moves)
        if len(moves) == 0:
            return bestMove
        if len(moves) == 1:
            return moves[0]
        bestSoFar = - 100
        beta = 100
        # depth = self.depth
        for m in moves:
            clone = copy(curBoard)
            makeMove(clone, m, player)
            value = minSearch(clone, curBoard, depth - 1, bestSoFar, beta, player)
            if value >= bestSoFar:
                bestSoFar = value
                bestMoves.append(m)
                bestValues.append(value)
        # for move in bestMoves:
        #     print('(' + str(move.start.x) + ', ' + str(move.start.y) +
        #       ')->(' + str(move.end.x) + ', ' + str(move.end.y) + ')')
        # print(bestValues)
        if len(bestMoves) == 1:
            return bestMoves[0]
        finalBestMoves = []
        for i in range(0, len(bestMoves)):
            if bestValues[i] >= bestSoFar:
                finalBestMoves.append(bestMoves[i])
        bestMove = random.choice(finalBestMoves)
        stop = timeit.default_timer()
    
        time_step = stop - start
        if player == 1:
            remain_time_x -= time_step
        else:
            remain_time_y -= time_step
        return bestMove
def minSearch(curBoard, preBoard, depth, alpha, beta, player):
        moves = getValidMoves(curBoard, preBoard, -player)
        if (depth == 0) | (len(moves) == 0):
            return evaluate(curBoard, player)
        value = 100
        for m in moves:
            clone = copy(curBoard)
            makeMove(clone, m, -player)
            value = min(value, maxSearch(clone, curBoard, depth - 1, alpha, beta, player))
            if value <= alpha:
                return value
            beta = min(beta, value)
        # print("min", depth, value)
        return value
def maxSearch(curBoard, preBoard, depth, alpha, beta, player):
        moves = getValidMoves(curBoard, preBoard, player)
        if (depth == 0) | (len(moves) == 0):
            return evaluate(curBoard, player)
        value = -100
        for m in moves:
            clone = copy(curBoard)
            makeMove(clone, m, player)
            value = max(value, minSearch(clone, curBoard, depth - 1, alpha, beta, player))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        # print("max", depth, value)
        return value
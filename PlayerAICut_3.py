from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
from Displayer_3 import Displayer
import math
import sys


class PlayerAI(BaseAI):
    def __init__(self):
        self.counter = 0
        self.displayer = Displayer()
        self.depth = 0
    def getMove(self, grid):
        # sys.setrecursionlimit(1500)
        moves = grid.getAvailableMoves()
        copyGrid = grid.clone()
        self.depth = 0
        # move = self.decision(copyGrid)
        # return moves[randint(0, len(moves) - 1)] if moves else None
        self.counter += 1
        print("counter ", self.counter)
        result = self.decision(copyGrid)
        print("max utility", result[1])
        return result[0]



    def eval (self, grid):

        result =  self.findPairs(grid) #grid.getMaxTile() + len(grid.getAvailableCells()) + grid.getCellValue([0,0]) + self.meanOfFields(grid) + self.findPairs(grid)
        # print('eval ', result)
        return result

    #
    # def evaluate(self, grid):
    #
    #     # return grid.getcellValue([0,0])
    #     # print(type(grid))
    #
    #     return len(grid.getAvailableCells() * -1)
    def findPairs(self,grid):
        result = 0
        for i in range(grid.size):
            for j in range(grid.size):
                if i-1 >= 0 and grid.getCellValue([i,j])>0:
                    if grid.getCellValue([i,j]) == grid.getCellValue([i-1,j]):
                        result += 1
                if i+1 <= grid.size and grid.getCellValue([i,j])>0:
                    if grid.getCellValue([i,j]) == grid.getCellValue([i+1,j]):
                        result += 1
                if j+1 <= grid.size and grid.getCellValue([i,j])>0:
                    if grid.getCellValue([i,j]) == grid.getCellValue([i,j+1]):
                        result += 1
                if j-1 <= 0 and grid.getCellValue([i,j])>0:
                    if grid.getCellValue([i,j]) == grid.getCellValue([i,j-1]):
                        result += 1
        #print(f"result of below grid is {result}")
        #self.displayer.display(grid)
        return result
    def meanOfFields(self, grid):
        fieldsSum = 0
        result = 0
        for i in range(grid.size):
            for j in range(grid.size):
                fieldsSum += grid.getCellValue([i,j])
        return fieldsSum/(grid.size*grid.size)

    def decision(self, grid):
        maxState = self.maximize(grid, 800)
        return maxState

    def maximize(self, grid, maxDepth):
        if self.depth > maxDepth:
            return None, self.eval(grid)
        else:
            self.depth += 1
        if self.terminalTest(grid):
            return None, self.eval(grid)


        maxMove = None
        maxUtility = -math.inf
        availableMoves = grid.getAvailableMoves()
        for move in availableMoves:

            copyGrid = grid.clone()
            copyGrid.move(move)
            # minimum = self.minimize(copyGrid)
            # grid.move(move)
            minimum = self.minimize(copyGrid, maxDepth)

            if minimum[1] >= maxUtility:
                maxMove = move
                maxUtility = minimum[1]
           # if maxUtility >= beta:
            #    return maxMove, maxUtility
            #if maxUtility > alpha:
           #     alpha = maxUtility
        return maxMove, maxUtility

    def minimize(self, grid, maxDepth):
        if self.depth > maxDepth:
            return None, self.eval(grid)
        else:
            self.depth += 1
        if self.terminalTest(grid):
            print("terminal state reached with following grid")
            print(f'alpha {alpha} and beta {beta}')
            print("utility", self.eval(grid))
            self.displayer.display(grid)
            print("---------------------------------------------------------")
            return None, self.eval(grid)


        minMove = None
        minUtility = math.inf
        cells = grid.getAvailableCells()
        availableCells = grid.getAvailableCells()
        for cell in availableCells:
            copyGrid = grid.clone()
            copyGrid.setCellValue(cell,2)
            # grid.setCellValue(cell,2)
            maximum = self.maximize(copyGrid, maxDepth)
            if maximum[1] <= minUtility:
                minMove = cell
                minUtility = maximum[1]
           # if minUtility <= alpha:
           #     return minMove, minUtility
           # if minUtility < beta:
            #    beta = minUtility

            return minMove, minUtility

    def terminalTest(self, grid):
        availableMoves = grid.getAvailableMoves()
        if len(availableMoves) == 0:
            return True
        else:
            return False

def main():
    player = PlayerAI()
    testGrid = Grid()
    displayer = Displayer()
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([0,0],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([0,3],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([2,3],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([0,1],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([0,2],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
    testGrid.setCellValue([1,1],3)
    displayer.display(testGrid)
    print(player.findPairs(testGrid))
#main()
"""
                                N-Queens problem 
                                ----------------
    State-space representation:
        State: 
            Queen-Position list contain N 2-tuples: (row, col) with row and col in range from 0 to N-1
        Initial state: 
            Queen-Position list is empty
        Goal state: 
            List of all N queen's position such that no two are in the same row, column, or diagonal.
        Next step state: 
            Place position for one more queen and append to Queen-Position list.

    All using algorithm:
        DFS algorithm
        BrFS algorithm
        Heuristic algorithm: Our super-pro optimized algorithm (similar to hill climbing) for N = 100.000 in 10 -> 15 minutes
"""

import random
import time


class NQueens_Heuristic:
    def __init__(self, N):
        self.N = N
        self.queenPosSol = None

    ########################################################################################
    ''' Rule checker '''

    # check for row violate exists
    def checkRowViolate(self, queenPos, N):
        col = [0] * N
        for i in range(len(queenPos)):
            col[queenPos[i][0]] += 1
            if col[queenPos[i][1]] > 1:
                return True
        return False

    # check for Collumn violate exists
    def checkColViolate(self, queenPos, N):
        col = [0] * N
        for i in range(len(queenPos)):
            col[queenPos[i][1]] += 1
            if col[queenPos[i][1]] > 1:
                return True
        return False

    # check for positive diagonal violate exists
    def checkPosDiagViolate(self, queenPos, N):
        diag = [0] * (2*N - 1)
        for i in range(len(queenPos)):
            diag[queenPos[i][0] + queenPos[i][1]] += 1
            if diag[queenPos[i][0] + queenPos[i][1]] > 1:
                return True
        return False

    # check for negative diagonal violate exists
    def checkNegDiagViolate(self, queenPos, N):
        diag = [0] * (2*N - 1)
        for i in range(len(queenPos)):
            diag[queenPos[i][0] - queenPos[i][1]] += 1
            if diag[queenPos[i][0] - queenPos[i][1]] > 1:
                return True
        return False

    # return True if exists any violation
    def isNotSafe(self, queenPos):
        if self.checkRowViolate(queenPos, self.N):
            return True
        if self.checkColViolate(queenPos, self.N):
            return True
        if self.checkPosDiagViolate(queenPos, self.N):
            return True
        if self.checkNegDiagViolate(queenPos, self.N):
            return True
        return False

    # check right, wrong or no solution
    def checkSolution(self):
        if self.queenPosSol == None:
            print("Doesnt have solution")
        elif not self.isNotSafe(self.queenPosSol):
            print("Has right solution")
        else:
            print("Wrong solution")

    ###########################################################################################
    ''' Utility '''

    # prints out all positions of queens
    def printQueen(self):
        if self.queenPosSol == None:
            print("No solution")
            return

        for i in range(self.N):
            print((self.queenPosSol[i]))

    def print_solution(self, queens):
        print(queens)

    # print demo board for N < 50
    def printBoard(self):
        if self.queenPosSol == None:
            print("No solution")
            return

        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in self.queenPosSol:
                    print('Q ', end='')
                else:
                    print('. ', end='')
            print('\n', end='')

    ###########################################################################################
    ''' 
            Heuristic algorithm                                 
    Fast search algorithm (similar to hill climbing)     
    for N = 100.000 in 7 -> 15 minutes, belongs to configuration of processor   
    Plz stay calm and our algorithm won't let you down!!! :D

    The main ideas is to generate random queens with different row and col,
    this is done by keep the row number ascending, while shuffle the column number.

    Our task is to check collisions between queens via two diagonal slopes.

    If there are collisions, swap the queen involved with some random queen and check the result, 
    if the swap makes number of collisions smaller, then swap them by their column, 
    but if the swap is not good, then dont swap but choose another candidate queen for swapping.

    The procedure is finished if there is no collision detected (collision = 0).
    '''

    def calcCollision(self, queencol, dp, dn):
        for i in range(self.N):
            dp[i] = 0
            dn[i] = 0

        collision = 0

        for i in range(self.N):
            dp[i + queencol[i]] += 1
            dn[i - queencol[i]] += 1

        for i in range(self.N * 2 - 1):
            if dp[i] > 1:
                collision += dp[i] - 1
            if dn[i] > 1:
                collision += dn[i] - 1

        return collision

    def calcAttack(self, queencol, dp, dn, atk):
        num_of_atk = 0
        for i in range(len(queencol)):
            if dp[i + queencol[i]] > 1:
                atk[num_of_atk] = i
                num_of_atk += 1
            elif dn[i - queencol[i]] > 1:
                atk[num_of_atk] = i
                num_of_atk += 1

        return num_of_atk

    def isSwapOK(self, i, j, queencol, dp, dn):
        if i == j:
            return False

        # ori: i, q[i] and j, q[j]; new: j, q[i] and i, q[j]
        dpiiori = dp[i + queencol[i]]
        dpjjori = dp[j + queencol[j]]
        dniiori = dn[i - queencol[i]]
        dnjjori = dn[j - queencol[j]]

        dpijori = dp[i + queencol[j]]
        dpjiori = dp[j + queencol[i]]
        dnijori = dn[i - queencol[j]]
        dnjiori = dn[j - queencol[i]]

        oriarr = [dpiiori, dpjjori, dniiori, dnjjori,
                  dpijori, dpjiori, dnijori, dnjiori]

        dpiinew = dpiiori - 1
        dpjjnew = dpjjori - 1
        dniinew = dniiori - 1
        dnjjnew = dnjjori - 1

        dpijnew = dpijori + 1
        dpjinew = dpjiori + 1
        dnijnew = dnijori + 1
        dnjinew = dnjiori + 1

        newarr = [dpiinew, dpjjnew, dniinew, dnjjnew,
                  dpijnew, dpjinew, dnijnew, dnjinew]

        cori = self.collupd(oriarr, [])
        cnew = self.collupd(newarr, [])

        if cori > cnew:
            return True
        else:
            return False

    def makeSwap(self, i, j, queencol, dp, dn):
        dp[i + queencol[i]] -= 1
        dp[j + queencol[j]] -= 1
        dn[i - queencol[i]] -= 1
        dn[j - queencol[j]] -= 1

        dp[i + queencol[j]] += 1
        dp[j + queencol[i]] += 1
        dn[i - queencol[j]] += 1
        dn[j - queencol[i]] += 1

        buffer = queencol[i]
        queencol[i] = queencol[j]
        queencol[j] = buffer

        collision = self.collupd(dp, dn)
        return collision

    def collupd(self, dp, dn):
        r = 0
        for i in dp:
            if i > 1:
                r += i-1
        for i in dn:
            if i > 1:
                r += i-1
        return r

    # run for ~15 mins
    def queen_fast_search(self):
        C1 = 0.45
        C2 = 32
        collision = -1

        while collision != 0:
            # Initialize random queen collumn as a sample list
            queencol = random.sample(range(0, self.N), self.N)

            # Initiate arrays that stores number of queen in diagonal lines
            dp = [0] * (self.N * 2 - 1)
            dn = [0] * (self.N * 2 - 1)
            # Initiate array stores conflicting queen for faster performance
            atk = [0] * self.N

            # Check collision for the initial array and update to dp, dn
            # If there is no collision, then it is a solution, we should return it
            collision = self.calcCollision(queencol, dp, dn)
            if collision == 0:
                break

            # The limit for collision number, if it is smaller than the limit
            # then update the num_of_attack field to shorten the loop below.
            limit = C1 * collision

            # Check the number of queen conflicting with others 
            # and store them in atk array
            num_of_atk = self.calcAttack(queencol, dp, dn, atk)
            loopcount = 0

            # Main loop for searching for solution
            while loopcount <= C2 * self.N:

                for k in range(num_of_atk):

                    # Choose a candidate conflicting queen 
                    # and its swapping partner
                    i = atk[k]
                    j = random.choice(range(self.N))

                    # Check the swapping process, 
                    # if it makes the collision smaller
                    # then do the swapping
                    if self.isSwapOK(i, j, queencol, dp, dn):
                        collision = self.makeSwap(i, j, queencol, dp, dn)

                        # If the requirement is achieved, 
                        # then save the state to queenPosSol
                        # and return
                        if collision == 0:
                            self.queenPosSol = list(
                                zip(range(self.N), queencol))
                            return

                        # If the collision is smaller than the limit
                        # update the limit and the attacking queens
                        # to shorten the loop and make it faster
                        elif collision < limit:
                            limit = C1 * collision
                            num_of_atk = self.calcAttack(
                                queencol, dp, dn, atk)

                # If the loopcount is too big, 
                # then the initial randomize state is not good enough
                # we should start randomize it again
                loopcount = loopcount + num_of_atk

        self.queenPosSol = list(zip(range(self.N), queencol))


if __name__ == "__main__":
    N = int(input())
    q = NQueens_Heuristic(N)

    start_time = time.time()
    q.queen_fast_search()
    # q.dfs()
    #q.print_solution(q.queenPosSol)
    #q.printQueen()
    #q.printBoard()
    print(q.queenPosSol)

    q.checkSolution()
    end_time = time.time()
    print("Time elapsed: %s" % (end_time - start_time))
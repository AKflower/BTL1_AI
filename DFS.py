from queue import Queue

class NQueens_DFS:
    def __init__(self, size):
        self.size = size
    
    def DFS(self):
            if self.size < 1:
                return []
            solutions = []
            stack = [[]]
            while stack:
                solution = stack.pop()
                if self.conflict(solution):
                    continue
                row = len(solution)
                if row == self.size:
                    solutions.append(solution)
                    continue
                for col in range(self.size):
                    queen = (row, col)
                    queens = solution.copy()
                    queens.append(queen)
                    stack.append(queens)
            return solutions
    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False
    
    def print_solution(self, queens):
        print(queens)

def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    solutions = n_queens.DFS()

    if print_solutions:
        for i, solution in enumerate(solutions):
            print(f'Solution {i + 1}:')
            n_queens.print_solution(solution)

        print(f'Total solutions: {len(solutions)}')

if __name__ == '__main__':
    main()
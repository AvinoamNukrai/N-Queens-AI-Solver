from itertools import permutations

from NQueensSolverInterface import NQueensSolverInterface


class NaiveAlgorithm(NQueensSolverInterface):
    def __init__(self, n):
        self.n = n
        self.solution = None

    def solve(self):
        """Solve the N-Queens problem using a naive brute-force approach."""
        for perm in permutations(range(self.n)):
            if self.__is_valid_solution__(perm):
                self.solution = perm
                return perm
        return None

    def __is_valid_solution__(self, queens):
        """Check if a given permutation is a valid solution for N-Queens."""
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Check if two queens are in the same diagonal
                if abs(queens[i] - queens[j]) == abs(i - j):
                    return False
        return True

    def print_solution(self):
        """Print the solution to the console."""
        if self.solution:
            for row in range(self.n):
                line = ['Q' if self.solution[row] == col else '.' for col in range(self.n)]
                print(' '.join(line))

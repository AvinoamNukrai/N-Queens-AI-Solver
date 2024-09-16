import math
import random
import time
from collections import defaultdict
from statistics import median
from numpy.ma.extras import average
from tabulate import tabulate

from NQueensSolverInterface import NQueensSolverInterface


class MinConflictsAlgorithm(NQueensSolverInterface):
    """
    Min-Conflicts algorithm for solving the N-Queens problem
    the algorithm is based on the following steps:
    1. randomly initialize the board with n queens
    2. while the termination criteria is not met:
        a. get the most conflicted queen
        b. remove the queen
        c. get the best position for the queen
        d. place the queen in the best position
    3. return the solution

    The running time of the algorithm is O(t * n^3) where t is the number of steps and n is the size of the board.
    """

    def_max_steps = 1000

    def __init__(self, n, max_steps=def_max_steps, limit_steps=True):
        self.limit_steps = limit_steps
        self.max_steps = max_steps
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.steps = 0
        self.best_board = None
        self.best_board_conflicts = math.inf
        self.step_to_reach_best = math.inf

    # region conflicts calc
    def get_conflicts(self, row, col):
        """Calculate the number of conflicts for a given cell at (row, col)."""
        return (self.conflicts_per_row(row, col) +
                self.conflicts_per_col(row, col) +
                self.conflicts_per_main_diag(row, col) +
                self.conflicts_per_secondary_diag(row, col))

    def get_all_conflicts(self):
        """Calculate the total number of conflicts on the board."""
        conflicts = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    conflicts += self.get_conflicts(i, j)
        return conflicts // 2  # Each conflict is counted twice, so divide by 2

    def conflicts_per_row(self, row, col):
        """Count conflicts in the same row, excluding the current cell."""
        return sum(1 for i in range(self.n) if i != col and self.board[row][i] == 1)

    def conflicts_per_col(self, row, col):
        """Count conflicts in the same column, excluding the current cell."""
        return sum(1 for i in range(self.n) if i != row and self.board[i][col] == 1)

    def conflicts_per_main_diag(self, row, col):
        """Count conflicts in the main diagonal (top-left to bottom-right)."""
        count = 0
        # Check top-left to bottom-right direction
        for d in range(-self.n + 1, self.n):
            r, c = row + d, col + d
            if 0 <= r < self.n and 0 <= c < self.n and (r, c) != (row, col) and self.board[r][c] == 1:
                count += 1
        return count

    def conflicts_per_secondary_diag(self, row, col):
        """Count conflicts in the secondary diagonal (top-right to bottom-left)."""
        count = 0
        # Check top-right to bottom-left direction
        for d in range(-self.n + 1, self.n):
            r, c = row + d, col - d
            if 0 <= r < self.n and 0 <= c < self.n and (r, c) != (row, col) and self.board[r][c] == 1:
                count += 1
        return count

    # endregion

    def solve(self, max_steps=def_max_steps):
        """running time is O(t * n^3)"""
        self.__init_N_queens__()
        while not self.__termination_criteria__():
            i, j = self.__get_most_conflicted_queen__()
            self.board[i][j] = 0
            i, j = self.__get_best_position__()
            self.board[i][j] = 1
            self.steps += 1
            conflicts = self.get_all_conflicts()
            if conflicts < self.best_board_conflicts:
                self.best_board = [row[:] for row in self.board]
                self.best_board_conflicts = conflicts
                self.step_to_reach_best = self.steps
        self.board = self.best_board

    def __init_N_queens__(self):
        """ running time is O(n)"""
        count = 0
        s = set()
        while count < self.n:
            row = random.randint(0, self.n - 1)
            col = random.randint(0, self.n - 1)
            if frozenset([row, col]) not in s:
                s.add(frozenset([row, col]))
                self.board[row][col] = 1
                count += 1

    def __termination_criteria__(self):
        """running time is O(n^2)"""
        conflicts_sum = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    conflicts_sum += self.get_conflicts(i, j)
        return conflicts_sum == 0 or (self.limit_steps and self.steps >= self.max_steps)

    def __get_most_conflicted_queen__(self):
        """running time is O(n^2)"""
        max_conflicts = 0
        max_conflicts_queen = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    continue
                conflicts = self.get_conflicts(i, j)
                if conflicts > max_conflicts:
                    max_conflicts = conflicts
                    max_conflicts_queen = [(i, j)]
                elif conflicts == max_conflicts:
                    max_conflicts_queen.append((i, j))
        return random.choice(max_conflicts_queen)

    def __get_best_position__(self):
        """running time is O(n^3)"""
        min_conflicts = math.inf
        best_position = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    conflicts = self.get_conflicts(i, j)
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_position = [(i, j)]
                    elif conflicts == min_conflicts:
                        best_position.append((i, j))
        return random.choice(best_position)

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print('Q' if self.board[i][j] == 1 else '.', end=' ')
            print()
        print("nuber of steps: ", self.steps)
        print("number of conflicts: ", self.get_all_conflicts())

from abc import ABC, abstractmethod


class NQueensSolverInterface(ABC):
    @abstractmethod
    def solve(self):
        """
        This method should implement the algorithm to solve the N-Queens problem.
        """
        pass

    @abstractmethod
    def print_solution(self):
        """
        This method should print the solution to the N-Queens problem.
        """

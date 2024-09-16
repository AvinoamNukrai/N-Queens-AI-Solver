import random

from MutationRateModel import mutationRateFit

from MutationRateModel import mutationRateFit
from NQueensSolverInterface import NQueensSolverInterface


class GeneticAlgorithm(NQueensSolverInterface):
    """
    A class to represent a genetic algorithm for solving the N-Queens problem.

    Attributes:
    n (int): The number of queens and the size of the board (n x n).
    population_size (int): The size of the population.
    mutation_rate (float): The mutation rate.
    max_generations (int): The maximum number of generations.
    population (list): The current population of solutions.
    best_solution (list): The best solution found.
    generations (int): The number of generations evolved.
    """

    def __init__(self, n):
        """
        Initializes the genetic algorithm with the given parameters.

        Parameters:
        n (int): The number of queens and the size of the board (n x n).
        population_size (int): The size of the population.
        mutation_rate (float): The mutation rate.
        max_generations (int): The maximum number of generations.
        """
        self.n = n

        self.population_size = max(10, n)
        self.mutation_rate = mutationRateFit().get_best_mutation_rate(n)
        self.max_generations = 100 * (n ** 2)

        self.population = self.__init_population__()
        self.best_solution = None
        self.generations = 0
        self.tournament_size = 5

    def solve(self):
        """
        Evolves the population to find a solution to the N-Queens problem.
        running time is O(max_generations * population_size * n ^ 2)

        Returns:
        bool: True if a solution is found, False otherwise.
        """
        for generation in range(self.max_generations):  # O(max_generations)
            new_population = []
            for _ in range(self.population_size):  # O(population_size)
                parent1, parent2 = self.__select_parents__()  # O(tournament_size)
                child = self.__crossover__(parent1, parent2)  # O(n)
                child = self.__mutate__(child)  # O(1)
                new_population.append(child)

            self.population = new_population
            best_board = max(self.population, key=self.__fitness__)  # O(population_size* n^2)
            if self.__fitness__(best_board) == self.n * (self.n - 1) // 2:
                self.best_solution = best_board
                self.generations = generation + 1
                return True

        self.best_solution = max(self.population, key=self.__fitness__)
        self.generations = self.max_generations
        return False

    def __init_population__(self):
        """
        Initializes the population with random boards.

        Returns:
        list: A list of random boards.
        """
        return [self.__random_board__() for _ in range(self.population_size)]

    def __random_board__(self):
        """
        Generates a random board configuration.

        Returns:
        list: A random board configuration.
        """
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def __fitness__(self, board):
        """
        Calculates the fitness of a board configuration.

        Parameters:
        board (list): A board configuration.

        Returns:
        int: The fitness score of the board.
        """
        max_pairs = self.n * (self.n - 1) // 2
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return max_pairs - conflicts

    def __select_parents__(self):
        """
        Selects two parents from the population using tournament selection.

        Returns:
        list: A list containing two parent boards.
        """
        return [max(random.sample(self.population, self.tournament_size), key=self.__fitness__) for _ in range(2)]

    def __crossover__(self, parent1, parent2):
        """
        Performs crossover between two parent boards.

        Parameters:
        parent1 (list): The first parent board.
        parent2 (list): The second parent board.

        Returns:
        list: The child board resulting from the crossover.
        """
        crossover_point = random.randint(0, self.n - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    def __mutate__(self, board):
        """
        Mutates a board configuration with a given mutation rate.

        Parameters:
        board (list): The board configuration to mutate.

        Returns:
        list: The mutated board configuration.
        """
        if random.random() < self.mutation_rate:
            board[random.randint(0, self.n - 1)] = random.randint(0, self.n - 1)
        return board

    def __calculate_solution_conflicts__(self):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.best_solution[i] == self.best_solution[j] or abs(
                        self.best_solution[i] - self.best_solution[j]) == abs(i - j):
                    conflicts += 1
        return conflicts // 2

    def print_solution(self):
        print("Solution found in", self.generations, "generations.")
        print("Board:", self.best_solution)
        print("Conflicts:", self.__calculate_solution_conflicts__())
        for i in range(self.n):
            for j in range(self.n):
                print("Q" if self.best_solution[j] == i else ".", end=" ")
            print()

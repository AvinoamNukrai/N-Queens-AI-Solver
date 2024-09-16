import argparse
import time

from NaiveAlgorithm import NaiveAlgorithm as NaiveAlgorithmNQueens
from MinConflictsAlgorithm import MinConflictsAlgorithm as MinConflictsAlgorithmNQueens
from GeneticAlgorithm import GeneticAlgorithm as GeneticAlgorithmNQueens


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run N-Queens solver with different algorithms.")
    parser.add_argument("-Alg_Name", choices=["Naive", "MinConflicts", "GA"], required=True,
                        help="Algorithm to use for solving N-Queens.")
    parser.add_argument("-N", type=int, required=True, help="Size of the N-Queens board (N value).")
    return parser.parse_args()


def run_naive_algorithm(n):
    solver = NaiveAlgorithmNQueens(n)
    solver.solve()
    print(f"Naive Algorithm solution for {n}-Queens:")
    solver.print_solution()


def run_min_conflicts_algorithm(n):
    solver = MinConflictsAlgorithmNQueens(n)
    solver.solve()
    print(f"Min-Conflicts Algorithm solution for {n}-Queens:")
    solver.print_solution()


def run_genetic_algorithm(n):
    solver = GeneticAlgorithmNQueens(n)
    solver.solve()
    print(f"Genetic Algorithm solution for {n}-Queens:")
    solver.print_solution()


def main():
    args = parse_arguments()
    n = args.N

    if args.Alg_Name == "Naive":
        run_naive_algorithm(n)
    elif args.Alg_Name == "MinConflicts":
        run_min_conflicts_algorithm(n)
    elif args.Alg_Name == "GA":
        run_genetic_algorithm(n)
    else:
        print(f"Unknown algorithm {args.Alg_Name}")


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"Execution time: {time.time() - start:.8f} seconds.")

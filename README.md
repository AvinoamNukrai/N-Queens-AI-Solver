# N-Queens Problem Solver

This repository contains several algorithms to solve the N-Queens problem, including Genetic Algorithm, Min-Conflicts
Algorithm, and a Naive Approach.

## Requirements

To run the programs, Python 3 is required. Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

## included files

- main.py: The main entry point for the program.
- GeneticAlgorithm.py: Implements the genetic algorithm.
- MinConflictsAlgorithm.py: Implements the Min-Conflicts algorithm.
- NaiveAlgorithm.py: Implements a naive solution approach.
- NQueensSolverInterface.py: Interface for the solver implementations.
- MutationRateModel.py: Model to calculate mutation rates for the genetic algorithm.
- genetic algorithm results.xlsx: Excel file containing results data necessary for running the genetic algorithm
  mutation rate model.

## Usage

To run the programs, you need to include the genetic algorithm results.xlsx file in your project directory as it
contains essential data for the genetic algorithm.

**To run the Genetic Algorithm:**

```bash
python main.py -Alg_Name=GA -N={n}
```

**To run the Min-Conflicts Algorithm:**

```bash
python main.py -Alg_Name=MinConflicts -N={n}
```

**To run the Naive Algorithm:**

```bash
python main.py -Alg_Name=Naive -N={n}
```

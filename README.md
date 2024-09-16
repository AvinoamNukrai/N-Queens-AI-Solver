# N-Queens Problem Solver

The N-Queens problem, a classic example in combinatorial optimization and artificial
intelligence, challenges us to place N queens on an N×N chessboard such that no two
queens threaten each other. The complexity of the problem increases exponentially
with N, making it a significant testbed for various AI algorithms focused on constraint
satisfaction.
In our project, we explored two primary computational approaches to solve the N-Queens
problem: the Min-Conflict Heuristic and the Genetic Algorithm. These were selected over other methods like naive brute force, planning, and reinforcement learning approaches due to their suitability for handling the problem's constraints efficiently.

Min-Conflict Heuristic:
The Min-Conflict algorithm is a heuristic method that iteratively minimizes conflicts
by moving a queen to a position where it has fewest conflicts until no conflicts remain
or a preset number of steps is reached. Our implementation showed promising results,
particularly efficient for large N values, demonstrating the practical utility of heuristic
search methods in solving constraint satisfaction problems.

Genetic Algorithm:
The Genetic Algorithm, inspired by principles of evolution and natural selection, uses a population of solutions to evolve towards an optimal arrangement. By applying
genetic operations such as fitness-based parent selection, crossover, and mutation, this algorithm effectively explores the solution space. It particularly excels in scalability
and maintaining solution quality with increasing N, highlighting its quality in exploring large search spaces.

Results and Evaluation:
Our results indicate that both algorithms are highly effective but exhibit different strengths depending on the scenario. The Min-Conflict Heuristic excels in rapid
convergence to a solution with fewer computational resources for smaller to moderatesized boards. In contrast, the Genetic Algorithm stands out in its ability to handle
larger problem sizes due to its evolutionary search mechanisms that effectively explore more extensive search spaces.

![image](https://github.com/user-attachments/assets/d19fcea1-82d7-4ee4-a2a8-27f6ef78d80f)


Critique and Potential Improvements:
While our approaches are effective, they are not without limitations. The Min-Conflict Heuristic, for example, can struggle with certain board configurations that may lead to
local minima. The Genetic Algorithm, while powerful, requires careful tuning of parameters like mutation rate and population size to prevent premature convergence
or excessive computational overhead. Moreover, relaxing some of the inherent assumptions such as fixed board size or
incremental changes in queen position could open up new avenues for algorithmic enhancements. Exploring adaptive heuristic or meta-heuristic approaches could also
provide more dynamic solutions to the N-Queens problem across varied problem sizes and configurations.

In conclusion, our project demonstrates that while the Min-Conflict and Genetic algorithms are potent tools for tackling the N-Queens problem, there remains
significant scope for enhancing these approaches. Future work will aim to refine these algorithms, explore alternative methods, and potentially develop hybrid approaches
that combine the strengths of multiple strategies to address the complexities of the NQueens problem more comprehensively.





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

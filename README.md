# N-Queens Problem Solver

This repository contains several algorithms to solve the N-Queens problem, including Genetic Algorithm, Min-Conflicts
Algorithm, and a Naive Approach.




![image](https://github.com/user-attachments/assets/d19fcea1-82d7-4ee4-a2a8-27f6ef78d80f)

The N-Queens problem, a classic example in combinatorial optimization and artificial
intelligence, challenges us to place N queens on an N×N chessboard such that no two
queens threaten each other. The complexity of the problem increases exponentially
with N, making it a significant testbed for various AI algorithms focused on constraint
satisfaction.
In our project, we explored two primary computational approaches to solve the NQueens
problem: the Min-Conflict Heuristic and the Genetic Algorithm. These were
selected over other methods like naive brute force, planning, and reinforcement
learning approaches due to their suitability for handling the problem's constraints
efficiently.
Min-Conflict Heuristic
The Min-Conflict algorithm is a heuristic method that iteratively minimizes conflicts
by moving a queen to a position where it has fewest conflicts until no conflicts remain
or a preset number of steps is reached. Our implementation showed promising results,
particularly efficient for large N values, demonstrating the practical utility of heuristic
search methods in solving constraint satisfaction problems.
Genetic Algorithm
The Genetic Algorithm, inspired by principles of evolution and natural selection, uses
a population of solutions to evolve towards an optimal arrangement. By applying
genetic operations such as fitness-based parent selection, crossover, and mutation, this
algorithm effectively explores the solution space. It particularly excels in scalability
and maintaining solution quality with increasing N, highlighting its quality in exploring
large search spaces.
Results and Evaluation
Our results indicate that both algorithms are highly effective but exhibit different
strengths depending on the scenario. The Min-Conflict Heuristic excels in rapid
convergence to a solution with fewer computational resources for smaller to moderatesized
boards. In contrast, the Genetic Algorithm stands out in its ability to handle
larger problem sizes due to its evolutionary search mechanisms that effectively explore
more extensive search spaces.
Critique and Potential Improvements
While our approaches are effective, they are not without limitations. The Min-Conflict
Heuristic, for example, can struggle with certain board configurations that may lead to
local minima. The Genetic Algorithm, while powerful, requires careful tuning of
parameters like mutation rate and population size to prevent premature convergence
or excessive computational overhead.
Moreover, relaxing some of the inherent assumptions such as fixed board size or
incremental changes in queen position could open up new avenues for algorithmic
enhancements. Exploring adaptive heuristic or meta-heuristic approaches could also
provide more dynamic solutions to the N-Queens problem across varied problem sizes
and configurations.
In conclusion, our project demonstrates that while the Min-Conflict and Genetic
algorithms are potent tools for tackling the N-Queens problem, there remains
significant scope for enhancing these approaches. Future work will aim to refine these
algorithms, explore alternative methods, and potentially develop hybrid approaches
that combine the strengths of multiple strategies to address the complexities of the NQueens
problem more comprehensively.


Model Description
The algorithm built from the following building blocks:
1. Initialization: The algorithm begins by generating an initial population of 𝑃
random permutations, where each permutation represents a valid configuration
of queens on the board. Formally, let 𝑃 = {𝑝!, 𝑝", . . . , 𝑝/} be a population of size
𝑘, where 𝑝$ ∈ 𝑆# is a random permutation of {1, 2, . . . ,𝑁 − 1}.
2. Fitness Function: The fitness function evaluates how close a given solution is
to being conflict-free. The objective is to minimize the number of conflicts,
where a conflict occurs if two queens share the same row or diagonal.
Mathematically, for each permutation 𝑝, the fitness function 𝐹(𝑝) defined as:
𝐹(𝑝) = Σ$.!
#Σ0.$1!
# (𝛿(𝑝[𝑖], 𝑝[𝑗]) + 𝛿(|𝑝[𝑖] − 𝑝[𝑗]|, |𝑖 − 𝑗|))
Where:
● 𝑝[𝑖] is the row index of the queen in column 𝑖.
● 𝛿(𝑥, 𝑦) is the Kronecker delta, which is 1 if 𝑥 = 𝑦 and 0 otherwise.
The fitness function 𝐹(𝑝) returns the total number of attacking pairs of
queens in configuration 𝑝, where a value of 𝐹(𝑝) = 0 indicates a solution.
3. Parent Selection: Parents are selected by randomly choosing a batch from the
current generation. From this batch, the two solutions with the highest fitness
values are chosen to be the parents.
4. Crossover: Crossover combines two parent boards to create a new child board.
A crossover point is randomly chosen, and segments from each parent are
exchanged to produce the child board.
5. Mutation: Mutation introduces variability into the population. Each board may
be mutated by selecting randomly column and with a probability defined by the
mutation rate replace it. This process helps in exploring the solution space and
avoids premature convergence to suboptimal solutions.
6. Termination: The algorithm continues evolving the population through
generations until a conflict-free solution is found (zero fitness value) or the
maximum number of generations is reached.






Min-Conflict
To solve the N-Queens problem, we implemented a hybrid approach combining the
Min-Conflicts Heuristic with elements of local search. Our algorithm iteratively adjusts
the positions of the queens, aiming to minimize conflicts until a valid solution is found
or a preset limit of steps is reached.
Model Description
The algorithm built from the following building blocks:
1. Initialization: A random initial board configuration 𝑄 = {𝑞!, 𝑞", . . . , 𝑞#} of N
queens is placed on the board such that each queen 𝑞$ placed on a random cell
(𝑖, 𝑗) є {1,2, . . . ,𝑁}х{1,2, . . . ,𝑁} on the board.
2. Conflict Resolution Loop:
At each step:
● Let 𝑐(𝑞$) represent the number of conflicts for queen 𝑞$
● The algorithm selects the queen 𝑞%&' with the highest conflict value:
𝑞%&' = 𝑎𝑟𝑔𝑚𝑎𝑥(! 𝑐(𝑞$)
● 𝑞𝑚𝑎𝑥 is relocated to a row 𝑟′ in the same column 𝑖 minimizing its
conflicts:
𝑟′ = 𝑎𝑟𝑔𝑚𝑖𝑛, 𝑐(𝑞$ 𝑖𝑛 𝑟𝑜𝑤 𝑟)
This process repeats until one of the following is occurred:
● A solution with zero conflicts is found, i.e., Σ#
$.!𝑐(𝑞$) = 0.
● The predefined step limit 𝐿 is reached.
3. Termination:
The algorithm terminates when either a conflict-free configuration is found, or
the step limit 𝐿 is reached. If Σ#
$.!𝑐(𝑞$) = 0, the algorithm returns a valid
solution. Otherwise, it terminated.







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

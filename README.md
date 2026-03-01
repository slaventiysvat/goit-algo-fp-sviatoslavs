# goit-algo-fp-sviatoslavs
This is repo where is took a part in basic algortithms course from GoIT

#Task 1:
- Implemented a function to reverse a singly linked list, which changes the links between nodes. The code is executed.
- Implemented a sorting algorithm (function) for a singly linked list programmatically. The code is executed.
- Implemented a function that combines two sorted singly linked lists into one sorted list. The code is executed.

#Task 2:
- The code is executed. The program visualizes the fractal “Pythagorean tree”.
- The user has the ability to specify the level of recursion.

#Task 3:
- Implemented Dijkstra’s algorithm for finding the shortest path in a graph using a binary heap (pyramid).
- Within the framework of the task implementation, a graph was created, a pyramid was used to optimize the selection of vertices, and the shortest paths from the initial vertex to all others were calculated.

#Task 4:
- The code is executed. The function visualizes a binary heap.

#Task 5:
- DFS and BFS algorithms are implemented in software to visualize depth-first and breadth-first traversal of a tree. A stack and a queue are used.
- Node colors change from dark to light depending on the traversal order.

#Task 6:
- A function that uses the greedy algorithm principle is implemented in software. The code is executed and returns the names of dishes, maximizing the ratio of calories to cost, without exceeding a given budget.
- A function that uses the dynamic programming principle is implemented in software. The code is executed and returns the optimal set of dishes to maximize calories for a given budget.

#Task 7:
- An algorithm for modeling the rolling of two dice and constructing a table of sums and their probabilities using the Monte Carlo method is implemented in software.
- The code is executed and simulates a large number of dice rolls, calculates the sums of the numbers that fall on the dice, counts how many times each possible sum appears in the simulation, and determines the probability of each possible sum.
- A table or graph is created that displays the probabilities of each sum found using the Monte Carlo method.

### Task 7 — Monte Carlo vs Analytic: Conclusions

Simulation was run with **200 000 trials** (seed = 42).

| Sum | Monte-Carlo | Analytic | Abs Diff |
|:---:|------------:|---------:|---------:|
| 2   | 2.7925%     | 2.7778%  | 0.0147%  |
| 3   | 5.5430%     | 5.5556%  | 0.0126%  |
| 4   | 8.3475%     | 8.3333%  | 0.0142%  |
| 5   | 11.1180%    | 11.1111% | 0.0069%  |
| 6   | 13.9110%    | 13.8889% | 0.0221%  |
| 7   | 16.4995%    | 16.6667% | 0.1672%  |
| 8   | 13.9390%    | 13.8889% | 0.0501%  |
| 9   | 11.1720%    | 11.1111% | 0.0609%  |
| 10  | 8.2765%     | 8.3333%  | 0.0568%  |
| 11  | 5.6160%     | 5.5556%  | 0.0604%  |
| 12  | 2.7850%     | 2.7778%  | 0.0072%  |

**Key observations:**
- Sum **7** has the highest probability (~16.67%), as expected — it can be formed in 6 different ways out of 36.
- The maximum absolute deviation between Monte Carlo and the analytic result across all sums was **0.1672%** (observed at sum 7).
- All other sums deviate by less than **0.07%** from their theoretical values.
- The distribution is symmetric around sum 7, which is correctly reproduced by the simulation.
- These results confirm that at 200 000 trials the Monte Carlo method reliably converges to the theoretical probabilities. Increasing the number of trials further reduces the error according to the Law of Large Numbers.

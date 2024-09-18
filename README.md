
# N-Queens Solver

This project implements a solution to the **N-Queens Problem** using Constraint Satisfaction Problem (CSP) techniques and backtracking. It allows for finding all possible solutions to the problem where `N` queens are placed on an `N x N` chessboard in such a way that no two queens threaten each other.

## Table of Contents

1. [Overview](#overview)
2. [Problem Description](#problem-description)
3. [How It Works](#how-it-works)
4. [Files in the Project](#files-in-the-project)
5. [How to Run the Program](#how-to-run-the-program)
6. [Requirements](#requirements)
7. [Future Improvements](#future-improvements)
8. [License](#license)

## Overview

This project solves the N-Queens Problem, a classic computer science problem, using a CSP-based agent that performs backtracking to find all possible solutions. It uses object-oriented programming concepts such as **agents**, **environments**, and **perceptions** to represent the problem and its constraints.

## Problem Description

The **N-Queens Problem** is a well-known puzzle where the goal is to place `N` queens on an `N x N` chessboard such that:

- No two queens can be on the same row.
- No two queens can be on the same column.
- No two queens can be on the same diagonal.

The challenge is to find all configurations where the above conditions hold. For example, for `N = 4`, the chessboard is a 4x4 grid, and the solution should place 4 queens on the board without them threatening each other.

## How It Works

### Key Concepts

1. **Agents**: The agent (CSPAgent) is responsible for solving the problem using a backtracking algorithm. It selects variables (queen positions), assigns values (positions on the board), and checks constraints (no threats between queens).
   
2. **Environment**: The environment (NQueensEnvironment) interacts with the agent and provides the constraints of the problem (board size, valid positions). The environment also displays the solution visually as a board with queens placed.

3. **Backtracking Algorithm**: The backtracking algorithm used by the agent is designed to explore all possible combinations of queen placements, backtracking when a constraint is violated, and continuing until all solutions are found.

### Process Overview

- The environment initializes an empty board of size `N`.
- The agent starts assigning positions to each queen, ensuring no conflicts in rows, columns, or diagonals.
- If a conflict arises, the agent backtracks and tries a different position for the queen.
- Once all queens are placed correctly, the solution is stored and the agent continues searching for other valid configurations.
- The program terminates when all solutions have been found.

### Output

The program prints the total number of solutions found and displays each solution as an `N x N` board with queens marked as `Q` and empty spaces as `.`.

## Files in the Project

- **`Agent.py`**: Defines the base agent class which handles perceptions, actions, and status.
- **`CSPAgent.py`**: Defines a specialized agent that solves the N-Queens problem using backtracking.
- **`NQueensAgent.py`**: A more specific implementation of the CSP agent tailored for the N-Queens problem.
- **`Environment.py`**: Defines the base environment class which interacts with agents.
- **`NQueensEnvironment.py`**: The environment for the N-Queens problem that sets up the board, interacts with the agent, and displays the solutions.
- **`main.py`**: The main entry point for running the program. It prompts the user for the size of the board (`N`) and runs the N-Queens solution process.

## How to Run the Program

### Step-by-step Instructions

1. **Clone the Repository**

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/Ichurri/n-queens
   cd n-queens-solver
   ```

2. **Install the Required Dependencies**

   Ensure that you have Python installed. This project does not require any external libraries, so no further dependencies need to be installed.

3. **Run the Program**

   To execute the program, run the following command in your terminal:

   ```bash
   python3 main.py
   ```

   You will be prompted to enter the value of `N`, the size of the board:

   ```
   Enter the value of N:
   ```

   After entering a number (e.g., `8` for an 8x8 board), the program will display the solutions found:

   ```
   92 solutions were found:
   Solution 1: 
    Q . . . . . . .
    . . . . Q . . .
    . . . . . . Q .
    . Q . . . . . .
    . . . Q . . . .
    . . . . . Q . .
    . . Q . . . . .
    . . . . . . . Q
   ```

4. **Output**

   The program prints the number of solutions and then displays each solution as a chessboard with queens placed.

## Requirements

- **Python 3.x**: The program is written in Python, and it requires Python 3 or later.
- No additional libraries are required, as the project uses only standard Python modules.

## Future Improvements

- **Optimizations**: Introduce optimizations such as forward-checking and constraint propagation to improve the performance of the backtracking algorithm.
- **Graphical Interface**: Implement a graphical interface to visually display the board and allow users to interact with the program.
- **Benchmarking**: Add benchmarking to compare the efficiency of the algorithm for larger values of `N`.


## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as you see fit.

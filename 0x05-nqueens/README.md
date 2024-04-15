## N-Queens Problem Solver (Backtracking with Recursion)

This repository implements the N-Queens problem solver using the backtracking algorithm with recursion. The N-Queens problem involves placing N queens on an N x N chessboard such that no two queens threaten each other (no queens share the same row, column, or diagonal).

### Features

- Solves the N-Queens problem for any board size (N) greater than or equal to 4.
- Employs a backtracking approach with recursion for efficient exploration of possible solutions.
- Provides all valid solutions (if any) found for the given board size.

### Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mcakyerima/alx-interview/blob/main/0x05-nqueens/0-nqueens.py
   ```

2. **Install dependencies (no external dependencies required for this code).**

3. **Run the script:**

   ```bash
   python3 nqueens.py N
   ```

   where `N` is the size of the chessboard (number of queens).

### Example

```
python3 nqueens.py 4
```

This will output all valid solutions for a 4 x 4 chessboard:

```
[[0, 2], [1, 0], [2, 3], [3, 1]]
[[0, 3], [1, 1], [2, 0], [3, 2]]
```

### How it Works

The code utilizes a class named `NQueen` to represent the problem and its solution. The `solve_n_queens` function implements the backtracking algorithm with recursion. It iteratively tries placing queens in each column, ensuring no conflicts arise. If a placement is safe, it recursively explores subsequent columns until all queens are placed (a valid solution is found). If no safe placement exists in a branch, backtracking occurs to try different configurations.

### Additional Notes

- This implementation utilizes a list to represent the board state, with each element storing the row position of a queen in the corresponding column (0-based indexing for queens).
- The solutions are stored as a list of lists, where each inner list represents the row and column positions of the queens in a valid solution (also using 0-based indexing).

#!/usr/bin/python3

"""Solves the N-Queens problem using backtracking with recursion.

This code implements the N-Queens algorithm, which finds a placement of N
queens on an N x N chessboard such that no two queens threaten each other
(no two queens share the same row, column, or diagonal).

The solution employs backtracking with recursion. It starts by placing a
queen in the first column, then iterates through possible positions in the
second column, ensuring no queen is threatened. This process continues
recursively until all columns are filled, representing a valid solution. If
no solution is found in the current branch, backtracking occurs to try
different placements.

Usage:
  nqueens.py N

where N is the size of the chessboard (number of queens).
"""

import sys


class NQueen:
    """Class for solving the N-Queens problem."""

    def __init__(self, n):
        """
        Initializes the N-Queens problem with the board size (n).

        Args:
            n (int): The size of the chessboard (number of queens).
        """
        self.n = n
        self.board = [0] * (n + 1)  # Use a list to represent the board state
        self.solutions = []  # Store found solutions

    def is_safe(self, col, row):
        """
        Checks if a queen can be placed at (row, col) without threating
        existing queens.

        Args:
            col (int): The column to place the queen.
            row (int): The row to place the queen.

        Returns:
            bool: True if the placement is safe, False otherwise.
        """
        # Check for queens in the same row or diagonals
        for j in range(1, col):
            if self.board[j] == row or abs(self.board[j] - row) == abs(j - col):
                return False
        return True

    def solve_n_queens(self, col):
        """
        Solves the N-Queens problem using backtracking and recursion.

        Args:
            col (int): The current column to place the queen (starts from 1).
        """
        if col == self.n + 1:  # All queens placed (solution found)
            solution = []  # Create a new solution list
            for i in range(1, self.n + 1):
                solution.append([i - 1, self.board[i] - 1])  # Convert board to 0-based indexing
            self.solutions.append(solution)
            return

        # Try all possible positions in the current column
        for i in range(1, self.n + 1):
            if self.is_safe(col, i):
                self.board[col] = i  # Place the queen
                self.solve_n_queens(col + 1)  # Recur for next queen
                self.board[col] = 0  # Backtrack (remove queen)

    def get_solutions(self):
        """
        Returns the list of found solutions.

        Returns:
            list: A list of lists representing valid queen placements.
        """
        self.solve_n_queens(1)  # Start solving from the first column
        return self.solutions


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens.py N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
solutions = queen.get_solutions()

if solutions:
    for solution in solutions:
        print(solution)
else:
    print("No solution found for N=", N)

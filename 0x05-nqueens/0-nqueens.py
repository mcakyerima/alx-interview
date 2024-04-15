#!/usr/bin/python3
""" N QUEENS ALGORITHM USING BACKTRACKING (RECURSIVE APPROACH WITH LOOP) """
import sys


class NQueen:
    """ Class to solve the N Queen problem """

    def __init__(self, n):
        """ Initializes the problem with the given board size """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Determines if a queen can be placed at position (k, i)
        Returns True if the placement is possible without conflicts
        with other queens; otherwise, returns False.
        """

        # Check previous rows to see if placing the queen at (k, i) is valid
        for j in range(1, k):
            # Check for conflicts in the same column or diagonals
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        """ Attempts to place queens from row k onwards
        Args:
        k: The starting row for placing queens
        """
        # Loop through each column in the current row k
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # If queen can be placed in column i
                self.x[k] = i
                if k == self.n:
                    # All queens have been placed (found a valid solution)
                    solution = []
                    for j in range(1, self.n + 1):
                        # Append the position of the queen in a 0-indexed format
                        solution.append([j - 1, self.x[j] - 1])
                    self.res.append(solution)
                else:
                    # Continue to place queens in the next row
                    self.nQueen(k + 1)
        return self.res


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a numerical value")
    sys.exit(1)

if N < 4:
    print("N must be 4 or greater")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for solution in res:
    print(solution)

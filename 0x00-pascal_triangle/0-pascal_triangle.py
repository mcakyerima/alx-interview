#!/usr/bin/python3
"""
pascal_triangle.py: A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Each inner list represents a row of the triangle.

    Raises:
        ValueError: If n is not a positive integer.
    """
    triangle = []
    
    if not isinstance(n, int) or n <= 0:
        return triangle

    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)

    return triangle



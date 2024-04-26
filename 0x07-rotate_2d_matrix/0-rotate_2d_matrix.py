#!/usr/bin/python3

"""
Rotate a 2D Matrix 90 Degrees Clockwise
=========================================

This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_matrix_clockwise(matrix: list) -> None:
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A 2D list of integers representing the matrix to be rotated.

    Returns:
        None
    """
    num_rows = len(matrix[0])

    for row_index in range(num_rows - 1, -1, -1):
        for col_index in range(0, num_rows):
            matrix[col_index].append(matrix[row_index].pop(0))

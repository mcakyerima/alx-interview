# Rotate 2D Matrix 90 Degrees Clockwise
=========================================

## Overview
-----------

This module provides a function to rotate a 2D matrix 90 degrees clockwise in-place. The function takes a 2D list of integers as input and modifies it to achieve the rotation.

## Usage
-----

To use the module, simply call the `rotate_matrix_clockwise` function with a 2D list of integers as an argument. The function will modify the input list in-place.

## Example
-------

```python
from rotate_matrix import rotate_matrix_clockwise

# Define a 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix 90 degrees clockwise
rotate_matrix_clockwise(matrix)

# Print the rotated matrix
for row in matrix:
    print(row)
```

### Output

```
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

## Function Documentation
-------------------------
`rotate_matrix_clockwise(matrix: list) -> None`

Rotate a 2D matrix 90 degrees clockwise in-place.

**Args:**

- `matrix (list)`: A 2D list of integers representing the matrix to be rotated.

**Returns:**

- `None`

**Note:**

- The input matrix is modified in-place.
- The function assumes that the input matrix is a 2D list of integers.
- The function does not return anything.

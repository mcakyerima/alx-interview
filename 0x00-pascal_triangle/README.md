# Pascal's Triangle

This repository contains a Python script for generating Pascal's triangle and a main script to demonstrate its usage.

## Description

Pascal's triangle is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal. In the triangle, each number is the sum of the two directly above it. This Python script generates Pascal's triangle up to a specified number of rows and returns it as a list of lists.

## Contents

- `0-pascal_triangle.py`: Python script containing the implementation of the Pascal's triangle generator.
- `0-main.py`: Main script demonstrating the usage of the Pascal's triangle generator.
- `README.md`: This file, providing an overview of the repository and its contents.

## Usage

To use the Pascal's triangle generator, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/mcakyerima/alx-interview.git
```

2. Navigate to the `0x00-pascal_triangle` directory:

```
cd alx-interview/0x00-pascal_triangle
```

3. Run the `0-main.py` script and pass the number of rows you want in the Pascal's triangle as a command-line argument:

```
python 0-main.py <num_rows>
```

Replace `<num_rows>` with the desired number of rows for the Pascal's triangle.

## Example

To generate Pascal's triangle with 5 rows, run the following command:

```
python 0-main.py 5
```

This will produce the following output:

```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Author

This repository is maintained by Mohammed Kaka. Feel free to reach out with any questions or suggestions.

# ALX Making Change Challenge

## Tasks 📝

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

#### Prototype
```python
def makeChange(coins, total)
```

#### Return
- The fewest number of coins needed to meet total.
- If total is 0 or less, returns 0.
- If total cannot be met by any number of coins you have, returns -1.

#### Constraints
- `coins` is a list of the values of the coins in your possession.
- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.
- Your solution’s runtime will be evaluated in this task.

### Examples

```python
>>> makeChange([1, 2, 25], 37)
7
>>> makeChange([1256, 54, 48, 16, 102], 1453)
-1
```

## Additional Resources 📚

- [Mock Technical Interview](https://example.com/mock-technical-interview)

## Requirements 📋

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
```

# ALx Mock Interview - 0x0A. Prime Game 🎓

## Requirements 🛠️

Ensure compliance with the following guidelines:

- **General**:
  - Editors: Allowed editors include vi, vim, and emacs.
  - Execution Environment: All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
  - File Conventions: All files should end with a new line, and the first line of each file should be exactly `#!/usr/bin/python3`.
  - README: A README.md file at the root of the project folder is mandatory.
  - Coding Style: Your code should adhere to the PEP 8 style (version 1.7.x).
  - Executability: Ensure all your files are executable.
- **Tasks**:
  - Each task has specific requirements outlined within the task description.
  - Follow the provided prototype for function definitions.
  - Task solutions should meet the specified constraints and requirements.

## Tasks 📝

### 0. Prime Game

Maria and Ben are engaged in a strategic game involving prime numbers. Your task is to determine the winner of each game based on the rules provided. The prototype for the function is as follows:

```python
def isWinner(x, nums):
    pass
```

**Parameters**:
- `x`: Number of rounds.
- `nums`: An array of integers representing the range for each round.

**Return**:
- Name of the player that won the most rounds.
- If the winner cannot be determined, return None.

**Constraints**:
- The range and number of rounds will not exceed 10000.
- Prohibited from importing any packages.

**Example**:

```
x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
```

**Example Usage**:

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

```
Output:
Winner: Ben
```

## Repository Details 📁

- **GitHub Repository**: alx-interview
- **Directory**: 0x0A-primegame
- **File**: 0-prime_game.py


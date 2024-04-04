# UTF-8 Validation

This repository contains a Python method to determine if a given data set represents a valid UTF-8 encoding.

## Method

The method `validUTF8(data)` is designed to check if a data set is a valid UTF-8 encoding. It takes a list of integers as input, where each integer represents one byte of data (8 least significant bits), and returns True if the data set is valid UTF-8, otherwise False.

### Prototype

```python
def validUTF8(data) -> bool:
    pass
```

### Parameters

- `data`: List[int] - The data set represented by a list of integers.

### Return Value

- `True`: If the data set is a valid UTF-8 encoding.
- `False`: If the data set is not a valid UTF-8 encoding.

### Constraints

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- Only the 8 least significant bits of each integer are considered for UTF-8 validation.

## Usage

To use the `validUTF8` method, import it into your Python script and call it with a list of integers representing the data set.

Example:

```python
from utf8_validation import validUTF8

data = [65, 195, 169, 226, 130, 172]
print(validUTF8(data))  # Output: True
```

## Testing

To test the validity of the UTF-8 encoding method, you can use the provided test cases in the `test_utf8_validation.py` file. Run the tests using a Python test runner such as `pytest`.

---

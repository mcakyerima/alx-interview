#!/usr/bin/python3

""" A method that determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize a variable to keep track of the number of expected bytes
    # for a character
    expected_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # If no bytes are expected, determine the number of bytes needed
        # based on the current integer
        if expected_bytes == 0:
            if (num >> 7) == 0b0:
                expected_bytes = 0
            elif (num >> 5) == 0b110:
                expected_bytes = 1
            elif (num >> 4) == 0b111:
                expected_bytes = 2
            elif (num >> 3) == 0b11110:
                expected_bytes = 3
            else:
                return False

        else:
            if (num >> 6) == 0b10:
                expected_bytes -= 1
            else:
                return False

        # If there are more bytes expected but the data ends,
        # it's an invalid UTF-8 sequence
        if expected_bytes > 0 and (num >> 6) != 0b10:
            return False

    # Check if all expected bytes were consumed
    return expected_bytes == 0

#!/usr/bin/python3
'''
This module contains a function to compute the fewest number of
operations needed to result in exactly n H characters.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result in
    exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed.
    '''
    if not isinstance(n, int):
        return 0

    operations_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif clipboard > 0:
            done += clipboard
            operations_count += 1

    return operations_count


if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


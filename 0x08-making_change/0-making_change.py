#!/usr/bin/python3
"""
Module for generating change
"""


def makeChange(coins, total):
    """
    Generate the minimum number of coins needed to reach a total amount.

    Args:
        coins (list): List of available coin denominations.
        total (int): The target total amount.

    Returns:
        int: The minimum number of coins needed to reach the total. 
             Returns -1 if the total cannot be reached with the given coins.
    """
    # Check if the total amount is 0 or less
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy approach
    coins.sort(reverse=True)
    # Counter for the total number of coins used
    coins_count = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Counter for the number of coins of the current denomination
        coin_count_for_denomination = 0

        # Greedily use as many coins of the current denomination as possible
        while total >= coin:
            total -= coin
            coin_count_for_denomination += 1

        coins_count += coin_count_for_denomination

        # If the total amount is reached, return the total number of coins used
        if total == 0:
            return coins_count

    # If the total amount cannot be reached, return -1
    return -1

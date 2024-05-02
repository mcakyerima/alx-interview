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
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order for greedy approach
    coins_count = 0  # Counter for the total number of coins used

    # Iterate through each coin denomination
    for coin in coins:
        coin_count_for_denomination = 0  # Counter for the number of coins of the current denomination

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

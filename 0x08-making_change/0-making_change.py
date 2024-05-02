#!/usr/bin/python3
"""
Module for makeChange function
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to be met.
    Returns:
        int: Fewest number of coins needed to meet total. If total is 0 or less, returns 0.
        If total cannot be met by any number of coins you have, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort()  # Sort coins in ascending order

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

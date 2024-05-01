#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    # Base cases
    if total <= 0:
        return 0
    if min(coins) > total:
        return -1

    # Initialize a list to store the fewest number
    # of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array from current coin value to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

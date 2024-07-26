#!/usr/bin/python3
"""
The make change challenge is an attempt to use dynamic programming to
determine to smallest combination of denomination to make the total amount
"""


def makeChange(coins, total):
    """returns the lowest combination of denomination or -1"""
    if total <= 0:
        return 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for idx in range(coin, total + 1):
            dp[idx] = min(dp[idx], dp[idx - coin] + 1)
    return dp[total] if dp[total] != float("inf") else -1

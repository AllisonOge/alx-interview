#!/usr/bin/python3
"""
The make change challenge is an attempt to use dynamic programming to
determine to smallest combination of denomination to make the total amount
"""


def makeChange(coins, total):
    """returns the lowest combination of denomination or -1"""
    if total <= 0:
        return 0
    remaining_total = total
    num_coins = 0

    coins = sorted(coins, reverse=True)
    for coin in coins:
        if remaining_total == 0:
            break
        count = remaining_total // coin
        num_coins += count
        remaining_total -= coin * count

    if remaining_total:
        return -1
    return num_coins

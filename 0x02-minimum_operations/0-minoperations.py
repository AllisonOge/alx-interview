#!/usr/bin/python3
"""
Module that defines the function `minOperations` to calculate
the fewest number of operations needed to result in exactly `n`
`H` characters in the file
"""


def minOperations(n: int) -> int:
    """return an integer if n is possible else 0"""
    if n <= 1:  # edge case
        return 0

    operations = 0

    factor = 2  # smallest divisible factor greater than 1

    while factor <= n:  # while the operations haven't been exhausted
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations

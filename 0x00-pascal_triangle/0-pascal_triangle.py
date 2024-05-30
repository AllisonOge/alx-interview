#!/usr/bin/python3
"""
Module that creates the function pascal_triangle(n) that returns a list
of list of integers representing the Pascal triangle of n
"""

import math

def pascal_triangle(n):
    """
    computes the pascal triangle
    Parameters
    ----------
    n: int - size of pascal triangle

    Returns
    -------
    p_triangle: List of List of int
    """
    # if n = 1
    # [[1], [1, 1]]
    # if n = 2
    # [[1], [1, 1], [1, 2, 1]]
    # if n = 3
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    # if n = 4
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    # if n = k
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],...,[kC0, kC1, kC3, ..., kCk]]
    # where kCr = k!/(k-r)!r!

    if n <= 0:
        return []
    if n == 1:
        return [[1], [1, 1]]

    row = [int(math.factorial(n-1)/(math.factorial(n-1-i)*math.factorial(i))) for i in range(n)]
    return pascal_triangle(n-2) + [row]

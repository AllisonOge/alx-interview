#!/usr/bin/python3
"""
Module that creates the function pascal_triangle(n) that returns a list
of list of integers representing the Pascal triangle of n
"""


def factorial(n):
    """compute the factorial"""
    if n <= 0:
        return 1
    return n * factorial(n-1)


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
    # if n = 2
    # [[1], [1, 1]]
    # if n = 3
    # [[1], [1, 1], [1, 2, 1]]
    # if n = 4
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    # if n = 5
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    # if n = k
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
    # [1, 4, 6, 4, 1],...,[kC0, kC1, kC3, ..., kCk]]
    # where kCr = k!/(k-r)!r!

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    row = [int(factorial(n-1)/(factorial(n-1-i)*factorial(i))) \
           for i in range(n)]
    return pascal_triangle(n-1) + [row]

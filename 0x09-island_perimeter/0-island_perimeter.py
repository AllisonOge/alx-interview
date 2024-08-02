#!/usr/bin/python3
"""
Island Perimeter challenge
"""


def island_perimeter(grid):
    """
    find the perimeter of the island in a grid containing one or
    no island

    Args:
        grid (list) a list of list of 1s and 0s, a cell has a side length of 1

    Return:
        perimeter (int) perimeter of the island
    """
    perimeter = 0
    if grid is None:
        return perimeter
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter

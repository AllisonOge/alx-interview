#!/usr/bin/python3
"""
rotate 2D matrix challenge
"""


def rotate_2d_matrix(matrix):
    """
    Inplace 90 degree rotation of a 2D matrix

    matrix is nxn
    """
    if matrix is None:
        return
    # logic for inplace rotation is to traverse the matrix
    # one cycle at a time
    #
    # step one is to traverse the outer cycle
    # (path 1->5->9->13->14->15->16->12->8->4->3->2->1)
    # and rotate groups of 4 (there would be 3 groups of 4)
    # 1  2  3  4    4  2  3  16   4  8  3  16    4  8  12 16
    # 5  6  7  8 => 5  6  7  8 => 5  6  7  15 => 3  6  7  15
    # 9  10 11 12   9  10 11 12   2  10 11 12    2  10 11 14
    # 13 14 15 16   1  14 15 13   1  14 9  13    1  5  9  13
    #
    # next we traverse the inner cycle
    # 4  8  12 16    4  8  12 16
    # 3  6  7  15 => 3  7  11 15
    # 2  10 11 14    2  6  10 14
    # 1  5  9  13    1  5  9  13
    N = len(matrix)
    for x in range(N // 2):
        for y in range(x, N - x - 1):
            temp = matrix[N - y - 1][x]
            matrix[N - y - 1][x] = matrix[N - x - 1][N - y - 1]
            matrix[N - x - 1][N - y - 1] = matrix[y][N - x - 1]
            matrix[y][N - x - 1] = matrix[x][y]
            matrix[x][y] = temp

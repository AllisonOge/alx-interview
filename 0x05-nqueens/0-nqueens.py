#!/usr/bin/python3
"""N Queen puzzle program"""
import sys


def solve_n_queens(n):
    """initial board and solve N-Queen puzzle

    Args:
        n (integer): dimension of board
    """
    def is_safe(board, row, col):
        """check if it is a safe position for the queen

        Args:
            board (list): n by n grid matrix
            row (integer): row positon on the board
            col (integer): column position on the board

        Returns:
            (boolean): True is safe otherwise False
        """
        # Check if the current position is safe for the queen
        # Check the row
        for i in range(col):
            if (board[i][0] == col
                    or board[i][1] == row
                    or abs(board[i][0] - col) == abs(board[i][1] - row)):
                return False
        return True

    def solve(board, col, solutions):
        """recursively solve the N-queen puzzle

        Args:
            board (list): n by n grid matrix
            col (integer): column position on the board
            solutions (list): store all posible solutions
        """
        # Base case: If all queens are placed, return True
        if col >= n:
            solutions.append(board[:])
            return

        for i in range(n):
            if is_safe(board, i, col):
                # Place the queen
                board[col] = [col, i]

                # Recursively solve for the next column
                solve(board, col + 1, solutions)

    # Initialize an empty chessboard
    board = [[-1, -1]] * n

    # Collect all solutions
    solutions = []
    # Solve the puzzle
    solve(board, 0, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(int(sys.argv[1]))

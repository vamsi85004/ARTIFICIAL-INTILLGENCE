# Python Program to solve the 8-Queen Problem using Backtracking

N = 8  # Number of queens

# Function to print the chessboard
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

# Solve the problem using backtracking
def solve_queens(board, row):
    if row == N:  # All queens are placed
        print_solution(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_queens(board, row + 1) or res
            board[row][col] = 0  # Backtrack

    return res

# Main function
def solve_n_queens():
    board = [[0] * N for _ in range(N)]
    if not solve_queens(board, 0):
        print("No solution exists")

# Run the program
solve_n_queens()
S

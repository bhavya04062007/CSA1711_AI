# 8-Queen Problem using Backtracking

N = 8

# Function to print the board
def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
    print("\n")

# Function to check if placing queen is safe
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function
def solve_n_queen(board, row):
    if row == N:
        print_board(board)
        return True   # return False here if you want ALL solutions

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queen(board, row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Main
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_n_queen(board, 0):
    print("No solution exists")

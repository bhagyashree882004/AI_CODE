def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]

    # Helper arrays for bounding
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + n - 1

    def backtrack(row):
        if row == n:
            print_board(board)
            return True  # return False if you want all solutions

        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # Place queen
                board[row][col] = 1
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

                if backtrack(row + 1):
                    return True

                # Backtrack
                board[row][col] = 0
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

        return False

    if not backtrack(0):
        print("No solution exists.")

# Example usage
n = int(input("Enter the value of N: "))
solve_n_queens(n)


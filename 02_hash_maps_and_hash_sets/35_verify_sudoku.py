# Given a partially completed 9x9 Sudoku board, validate it.

# The point :
# We will use a hash set for each row, column, and square.
# ! The cell (j, i) belongs to row j, column i, and square [j // 3][i // 3] (i, j ∈ [0, 8]).

# We will create 9 hash sets for rows, 9 hash sets for columns, and 9 hash sets for squares.
# We will iterate over each cell and add the value to each corresponding hash set.
# If a value is already present in any hash set, we return False.

# We'll iterate over each cell:
# - Check if the number already exists in the respective row, column, or square.
# - If any duplicate is found, the Sudoku board is invalid.

# Complexity Analysis
#   Time  : O(n²)
#   Space : O(n²) :
# Because we iterate over each cell of the board once and perform operations on hash sets in O(1).
# We allocate three arrays (rows, cols, grids) of size n (9 here), each containing n (9 here) elements.


def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets: list[set[int]] = [set() for _ in range(9)]
    col_sets: list[set[int]] = [set() for _ in range(9)]
    grid_sets: list[list[set[int]]] = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            if num in row_sets[r] or num in col_sets[c] or num in grid_sets[r // 3][c // 3]:
                return False
            row_sets[r].add(num)
            col_sets[c].add(num)
            grid_sets[r // 3][c // 3].add(num)
    return True


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print(verify_sudoku_board(board))  # True


board = [
    [3, 0, 6, 0, 5, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 2, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0],
]

print(verify_sudoku_board(board))  # False

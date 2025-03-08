# For each 0 in an mxn matrix, set its entire row and col to 0 in place

# Brute force => O(m x n x (m + n))
# Because mn represents the number of zeros if we imagine the matrix consists only of zeros.
# m + n represents the number of cells in a row and a column combined.

# The point :
# Note that a cell in a row or column that contains a 0 will becomes a 0.
# We will create two hash sets with the indexes of rows and columns that contain zeros.
# We can then check in O(1) if a cell (j, i) belongs to a row or column that contains a 0.

# Complexity Analysis
#   Time  : O(mn)
#   Space : O(m+n) :
# O(mn) because we traverse the matrix twice and perform O(1) operations during each pass.
# O(m + n) because the hash sets grow with the number of rows and columns that contain zeros.


def zero_striping_hash_sets(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    # Pass 1 : identify rows and cols containing 0 storing he respective index
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    # Pass 2 : set any cell to 0 if its row (resp. col) is in zero_rows (resp. zero_cols)
    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0


board = [
    [1, 2, 3, 4, 5],
    [6, 0, 8, 9, 9],
    [9, 8, 7, 6, 5],
    [2, 4, 6, 8, 0],
]

print("\n".join("".join(map(str, row)) for row in board))
print()
zero_striping_hash_sets(board)
print("\n".join("".join(map(str, row)) for row in board))
print("\n\n\n")


# The point :
# If we absolutely want to perform operations in place, we can observe that a row or column containing a 0 will end up containing only zeros.
# Its content doesn't matter, so we can sacrifice it.
# We decide to set to 0 the cells in the first row whose column contains a 0.
# We decide to set to 0 the cells in the first column whose row contains a 0.
# We add two flags to track whether the first row and the first column initially contain any zeros.
#       If so, we will need to set the entire first row and first column to 0 at the end.

# Complexity Analysis
#   Time  : O(mn)
#   Space : O(1) :
# O(mn) because checking the first row takes O(m) and the first column takes O(n).
# Then, we perform two passes over the m x n matrix.
# Finally, we iterate over the first row (O(m)) and the first column (O(n)).
# Complexity = O(m) + O(n) + O(mn) + O(m) + O(n) = O(mn).
# O(1) space because we use the first row and the first column to store flags and zeros.


def zero_stripping(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])

    # Check if the 1st row and 1st col contain 0
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and first col as markers
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # Update the submatrix using the flags in the first row and first col
    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # if the first row had 0 initially set all elements in it to 0
    if first_row_has_zero:
        for c in range(n):
            matrix[0][c] = 0
    # if the first col had 0 initially set all elements in it to 0
    if first_col_has_zero:
        for r in range(m):
            matrix[r][0] = 0


board = [
    [1, 2, 0, 4, 5],
    [6, 0, 8, 9, 9],
    [9, 8, 7, 6, 5],
    [2, 4, 6, 8, 0],
]

print("\n".join("".join(map(str, row)) for row in board))
print()
zero_stripping(board)
print("\n".join("".join(map(str, row)) for row in board))

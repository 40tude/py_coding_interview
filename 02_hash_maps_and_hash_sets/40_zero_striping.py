# for each 0 in an mxn matrix, set its entire row and col to 0 in place

# Brute force => O(m x n x  (m+n))
# Car mn = le nb de 0 si on imagine que c'est une matrice que de 0
# m + n  = le nb de cellule dans une ligne et une colonne combinées

# Noter qu'une cellule dans une col ou une row qui contient un 0 va devenir un 0
# On va créer 2 hash sets avec les index des lignes et des colonnes qui contiennent des 0
# On pourra vérifier en O(1) si une cellule (j, i) appartient à une ligne ou une colonne contient un 0


# O(mn), O(m + n)
# En mxn car on va parcourir la matrice 2 fois et faire des opérations en 0(1) pendant chaque passe
# En m+n car les hash sets grossissent avec le nombre de lignes et de colonnes dans lesquels on trouve des 0
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


# Si on veut absolument faire les opération sur place, on peut remarquer qu'un ligne ou une colonne qui contient un 0 va contenir que des 0
# Son contenu n'a pas d'importance. On peu le sacrifier
# On décide sur la 1ere ligne de mettre à 0 les cellules dont la colonne contient un 0
# On décide sur la 1ere colonne de mettre à 0 les cellules dont la ligne contient un 0
# On ajoute 2 flags pour savoir si la 1ere ligne et la 1ere colonne contiennent des 0 au départ
#       Si tel est le cas faudra mettre à 0 toute la 1ere ligne et la 1ere colonne à la fin

# O(mn), O(1)
# En mn car vérifier la première ligne prend O(m) et la première colonne prend O(n)
# Ensuite y a 2 passes sur la matrice mxn
# Enfin on itère sur la première ligne (O(m)) et la première colonne (O(n))
# Complexité = O(m) + O(n) + O(mn) + O(m) + O(n) = O(mn)
# En O(1) car on utilise la première ligne et la première colonne pour stocker les flags et les 0


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

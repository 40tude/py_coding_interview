# Given a partially completed 9x9 Sudoku board, validate it.

# O(n²), O(n²)
# Car on itère sur chaque cellule du tableau une fois et qu'on fait des opérations sur des hash sets en O(1)
# On alloue des 3 tableaux (rows, cols, grids) de taille n (9 ici) qui sont chacun de taille n (9 ici)

# On va utiliser un hash set pour chaque ligne, colonne et carré
# La cellule j, i appartient à la ligne j, colonne i et au carré [j // 3]  [i // 3] (i,j € [0, 8])

# On va créer 9 hash sets pour les lignes, 9 hash sets pour les colonnes et 9 hash sets pour les carrés
# On va itérer sur chaque cellule et ajouter la valeur à chaque hash set
# Si on trouve une valeur déjà présente dans un hash set, on retourne False


def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    grid_sets = [[set() for _ in range(3)] for _ in range(3)]

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

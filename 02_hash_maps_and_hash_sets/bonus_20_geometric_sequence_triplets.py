# A geometric sequence triplet is a sequence of three numbers where each successive number is obtained by multiplying the preceding number by a constant called the common ratio.
# 1 2 4
# 5 15 45

# Given an array of integers and a common ratio r
# find all triplets of indexes (i, j, k) that follow a geometric sequence for i < j < k.
# It’s possible to encounter duplicate triplets in the array.

# Input: nums = [2, 1, 2, 4, 8, 8], r = 2
# Output: 5

# On cherche x, x·r, x·r²
# if we know one value of a triplet, we can calculate what the other two values should be
# Faut les retrouver dans l'ordre x, x·r, x·r² dans le tableau
# On va plutôt chercher x/r, x et xr car alors on cherche TOUJOURS x/r à gauche et xr à droite
# Pour faire des recherche en O(1) on va utiliser des hash maps (gauche et droite)
# Faut que x soit divisible par r
# Comme on peut avoir plusieurs fois la même valeur dans le tableau
# on aura sans doute le même nombre de x/r et de xr
# Résumé
#   Verifier x%r == 0
#   Compter le nombre de x/r à gauche et le nombre de xr à dte
#   On multiplie les 2 pour avoir le nombre de triplets


# BIEN VOIR L'EXEMPLE DE MISE EN OEUVRE p 23
# On met tout dans le hash map de droite au départ
# On prend le premier x à gauche du tableau
# Gestion dynamique des hash maps gauche et droite


# O(n), O(n)
# On parcourt le tableau 1 fois et on fait des operation en O(1) sur les hash map à chaque itération
# En O(n) car la hash map peut croître jusqu'à n


from collections import defaultdict


def geometric_sequence_triplets(nums: list[int], r: int) -> int:
    left_map = defaultdict(int)  # "defaultdict" ensures default value is 0 when accessing a key that doesn't exist
    right_map = defaultdict(int)
    count = 0

    # populate right_map
    for x in nums:
        right_map[x] += 1
    # search geom triplets
    for x in nums:
        # decrement freq of x in right_map
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        # increment freq of x in left_map since now it will be part of the "left" side of the array as we move to the right
        left_map[x] += 1
    return count


print(geometric_sequence_triplets([2, 1, 2, 4, 8, 8], 2))  # 5

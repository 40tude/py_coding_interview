# Given a string of lowercase English letters
# Rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order.
# If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that’s first in lexicographical order

# O(n), O(n)
# Car on parcourt la chaîne de n chars 2 fois
#       Une fois pour trouver le pivot et une fois pour trouver le rightmost successor
#       On fait aussi une inversion de la chaîne qui est en 0(n)
# Pour l'espace, on est en O(n) car on alloue letters[]


# Le mot clé c'est rearrange
# Input     : s = "abcd"
# Output    :     "abdc"

# Input     : s = "dcba"
# Output    :     "abcd"

# Le mieux c'est de donner des chiffres à chaque lettre : a = 1, b = 2, c= 3...
# l’accroissement minimal se fait en changent les lettres qui sont à droite (pas celles de gauche)
# suffixe
# En partant de la droite, on cherche le plus petit suffixe qu'on peut réarranger pour former une permutation plus grande
# On cherche le premier caractère qui est plus petit que le suivant (pivot)

# Si on trouve pas de pivot, la chaîne est déjà à sa "valeur" max.
# On retourne alors la chaîne inversée (se sera alors la première permutation lexicographique)

# Si on a un pivot, faut l’échanger avec le premier caractère à partir de la droite qui est plus grand que lui
# a b c e d d a où c est le pivot. On va l'échanger avec le 1er d de droite
# a b d e d c a

# Faut voir que le suffixe edca est "non-increasing"
# On peut minimiser le suffixe en l'inversant
# a b d a c d e


def next_lexicographical_seq(s: str) -> str:
    letters = list(s)

    # On cherche le pivot
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    # if pivot NOT found the string "value" is already max
    # return the reversed string
    if pivot == -1:
        return "".join(reversed(letters))

    # A partir de la droite, on cherche le 1er caractère plus grand que le pivot
    rightmost_successor = len(letters) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1

    # On échange le pivot avec le rightmost successor
    letters[pivot], letters[rightmost_successor] = letters[rightmost_successor], letters[pivot]

    # On inverse le suffixe
    letters[pivot + 1 :] = reversed(letters[pivot + 1 :])
    return "".join(letters)


print(next_lexicographical_seq("ynitsed"))  # ynsdeit

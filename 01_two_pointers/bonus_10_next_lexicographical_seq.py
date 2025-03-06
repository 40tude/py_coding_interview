# Given a string of lowercase English letters
# Rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order.
# If the given string is already the last lexicographical arrangement possible, return the first lexicographical arrangement.

# Complexity:
# Time: O(n), Space: O(n)
# Time is O(n) as we traverse the string a few times:
#   - Searching for pivot
#   - Finding rightmost successor
#   - Reversing the suffix
# Space complexity is O(n) due to the letters[] array allocation

# ! The keyword here is "rearrange"
# Input  : s = "abcd"
# Output :     "abdc"

# Input  : s = "dcba"
# Output :     "abcd"

# The best is to assign numbers to letters (a=1, b=2, c=3, etc.)
# We look for the smallest suffix (right hand side) that we can rearrange to get a greater permutation
# We focus on changing the smallest possible suffix that can produce a greater permutation
# We search for the first character that is smaller than the next one (pivot)

# If no pivot is found, the string is already at its maximum "value".
# Then, we return the reversed string (this will become the first lexicographical permutation).

# If a pivot is found, swap it with the next larger character to its right.

# Example:
# Input: s = "a b c e d"
# Pivot is 'c', as it's the first character smaller than its successor 'e':
# Swap pivot 'c' with the next larger character to its right ('e'):
# Result: "a b e c"

# Notice the suffix after the pivot is "non-increasing".
# To minimize the suffix, reverse it:
# Result: "a b d a c d e"


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

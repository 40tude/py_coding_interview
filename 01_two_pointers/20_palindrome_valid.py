# Given a string determine if it's a palindrome after removing all non-alphanumeric characters
# On utilise 2 pointeurs (debut, fin). Il doivent être egaux. On skip les non alpha numériques.
# On doit sur la meme lettre ou sur les 2 mêmes lettres avant que left> right

# O(n), O(1)
# Car on parcourt la chaîne de n char une fois et on alloue un nombre constant de variables


def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # skip non alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        # skip non alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1
        # if does'nt match return false otherwise go forward
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome_valid("abbabba"))
print(is_palindrome_valid("abbabbu"))

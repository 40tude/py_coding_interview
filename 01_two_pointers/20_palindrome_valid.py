# Given a string determine if it's a palindrome after removing all non-alphanumeric characters

# The point :
#   ! We use two pointers (start, end).
#   They must match. We skip non-alphanumeric characters.
#   We must land on the same character or two identical characters before left > right.

# Complexity Analysis
#   Time  : O(n)
#   Space : O(1)
# Because we traverse the n-character string once and allocate a constant number of variables.


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

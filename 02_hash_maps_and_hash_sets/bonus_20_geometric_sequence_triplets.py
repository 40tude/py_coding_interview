# A geometric sequence triplet is a sequence of three numbers where each successive number is obtained by multiplying the preceding number by a constant called the common ratio.
# 1 2 4
# 5 15 45

# Given an array of integers and a common ratio r
# Find all triplets of indexes (i, j, k) that follow a geometric sequence for i < j < k.
# It’s possible to encounter duplicate triplets in the array.

# Input: nums = [2, 1, 2, 4, 8, 8], r = 2
# Output: 5

# We are looking for x, x·r, x·r².
# If we know one value of a triplet, we can calculate what the other two values should be.
# We need to find them in order: x, x·r, x·r² in the array.

# The point :
# ! Instead, we search for x/r, x, and x·r because this way, we always look for x/r on the left and x·r on the right.
# To perform O(1) lookups, we use hash maps (left and right).
# x must be divisible by r.
# Since the same value can appear multiple times in the array, we may find the same number of x/r and x·r.

# Summary:
#   - Check if x % r == 0.
#   - Count the occurrences of x/r on the left and x·r on the right.
#   - Multiply these two counts to get the number of triplets.

# SEE THE IMPLEMENTATION EXAMPLE ON PAGE 23
# Initially, we store all values in the right hash map.
# We take the first x from the left side of the array.
# Dynamic management of the left and right hash maps.

# Complexity Analysis
#   Time  : O(n)
#   Space : O(n) :
# We traverse the array once and perform O(1) operations on the hash maps at each iteration.
# Space complexity is O(n) because the hash map can grow up to n elements.


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

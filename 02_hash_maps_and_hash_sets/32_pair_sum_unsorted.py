# see 01_two_pointers\12_pair_sum_sorted.py

# Given an array and a target sum, return the indexes of any pair of numbers that add up to the target sum.
# Avoid brute force with 2 nested loops O(n²) and use the two pointers technique
# Avoir sorting the array because 0(nlogn)

# The point :
# ! complement of x = y = target - x
# look for index NOT for the values by themselves

# pass 1 = fill a hash map with for each val its index
# ! pass 2 = look for each val, if it scomplement is in the hash map

# Complexity Analysis
#   Time  : O(n)
#   Space : O(n) :


def pair_sum_unsorted_two_pass(nums: list[int], target: int) -> list[int]:

    num_to_index = {}

    for i, num in enumerate(nums):
        num_to_index[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index and num_to_index[complement] != i:
            return [i, num_to_index[complement]]
    return []


print(pair_sum_unsorted_two_pass([1, 2, 3, 4, 5], 6))  # [0, 4]


# We can have only ONE pass filling the hash map and looking for the complement at the same time
# O(n), O(n)
# Because go through le list only once
# The hash map can grow up to n
def pair_sum_unsorted_one_pass(nums: list[int], target: int) -> list[int]:

    complement_to_index: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_to_index:
            return [complement_to_index[complement], i]
        complement_to_index[num] = i
    return []


print(pair_sum_unsorted_one_pass([1, 2, 3, 4, 5], 6))  # [1, 3]

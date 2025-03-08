# Given a sorted array and a target sum, return the indexes of any pair of numbers that add up to the target sum.
# Avoid brute force with 2 nested loops O(n²) and use the two pointers technique

# The point :
#    Leverage the fact that the numbers are sorted
#    Use 2 ptrs, one on the left the other on the right
#    Sum them up. If below move the left ptr inward. If above move the right ptr inward

# Complexity Analysis
#   Time  : O(n)
#   Space : O(1)


def pair_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right]
    return []


res_list = pair_sum_sorted([-5, -2, 3, 4, 6], 7)
print(res_list)

res_list = pair_sum_sorted([1, 1, 1], 2)
print(res_list)

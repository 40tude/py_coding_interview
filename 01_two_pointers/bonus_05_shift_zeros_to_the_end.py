# Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

# ! We use two staged pointers:
#   - 'left' points to the position where non-zero values should be placed
#   - 'right' points to non-zero values

# Both pointers start at the left
# Move 'right' to the first non-zero value
# Swap values
# Increment both pointers by +1
# Move 'right' forward to the next non-zero value and repeat

# Time complexity: O(n), Space complexity: O(1)
# Because we traverse the array once and shift values in place


# def shift_zeros_to_the_end(nums: list[int]) -> None:
#     left = 0
#     right = 0
#     while right < len(nums):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#         right += 1


def shift_zeros_to_the_end(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1


Bob = [0, 1, 0, 3, 12]
shift_zeros_to_the_end(Bob)
print(Bob)  # [1, 3, 12, 0, 0]

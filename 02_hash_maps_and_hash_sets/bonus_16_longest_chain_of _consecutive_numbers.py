# Find the longest chain of consecutive numbers in an array.
# Two numbers are consecutive if they have a difference of 1.

# I didn't realize that sorting was an option.

# Brute force 1:
#   We sort the array O(nlog(n)) and iterate through it.

# Brute force 2:
#   We can consider each value as the start of a sequence.
#   This leads to an O(n^3) solution, which is even worse.
#   O(n^3) because there is a for loop, a while loop, and inside the while loop, we perform "while (current_num + 1) in nums" in O(n).

# ! Optimized approach:
# 1 - Instead of performing a linear search, we use a hash set to achieve O(1) lookups.
# 2 - We eliminate false starts by skipping values where v-1 exists in the hash set.
# This reduces the complexity from O(n^3) to O(n).


# O(n), O(n)
# Even though there are two loops, the complexity is O(n) because the inner loop runs only on the start of sequences.
# Therefore, the combined number of iterations for both loops is O(n).
# The for loop runs n times, and the while loop runs n times.
# This results in O(n + n) = O(n).
# Space complexity is O(n) because we use a hash set to store the values.
def longest_chain_of_consecutive_numbers(nums: list[int]) -> int:
    if not nums:
        return 0
    num_set = set(nums)
    longest_chain = 0
    for num in num_set:
        # If the current number is the smallest in its chaine, search for the length of the chain
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    return longest_chain


print(longest_chain_of_consecutive_numbers([1, 6, 2, 5, 8, 7, 10, 3]))  # 4

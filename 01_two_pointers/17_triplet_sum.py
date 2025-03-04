# Given an array of int, return all triplets such that a+b+c =0
# 1 2 3 and 2 3 1 are considered duplicates

# O(n²), O(n)
# On trie le tableau => O(nlogn)
# Pour chaque élément du tableau on appelle pair_sum_sorted_all_pairs() qui tourne en  O(n)
# O(nlogn) + O(n²) = O(n²)
# O(n) pour space à cause de l'algo de tri Python
# ON NE TIENT PAS COMPTE DE L4ESPACE UTILISE POUR STOCKER LES TRIPLETS

# Ici log c'est bien log à base 2
# log2(128)     = 7
# log2(256)     = 8
# log2(512)     = 9
# log2(1024)    = 10
# log2(1MB)     = 20


#
# Sort the array
# b+c = -a for all values of a


def pair_sum_sorted_all_pairs(nums: list[int], start: int, target: int) -> list[list[int]]:
    pairs = []
    left, right = start, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # To avoid duplicate, skip "b" if it is same as previous number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs


def triplet_sum_(nums: list[int]) -> list[list[int]]:
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        # Triplet will never sum to 0
        if nums[i] > 0:
            break
        # To avoid duplicate, skip "a" if it is same as previous number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Find pair with sum = -a (meaning -num[i])
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets


res_list = triplet_sum_([0, -1, 2, -3, 1])
print(res_list)


res_list = triplet_sum_([0, 0, 1, -1, 1, -1])
print(res_list)

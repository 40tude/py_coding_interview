# Voir 01_two_pointers\12_pair_sum_sorted.py

# Given an array and a target sum, return the indexes of any pair of numbers that add up to the target sum.
# Avoid brute force with 2 nested loops O(n²) and use the two pointers technique
# Avoir sorting the array because 0(nlogn)

# complement of x = y = target - x
# on cherche les index PAS les valeurs elles-mêmes

# passe 1 = on rempli uen hash map avec pour chaque valeur, son index
# passe 2 = on cherche pour chaque valeur, si son complement est dans la hash map


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


# On peut faire 1 passe en remplissant la hash map et en cherchant les compléments en même temps
# O(n), O(n)
# Car on itère sur la liste une seule fois et que la hash map peut croître jusqu'à avoir une taille n
def pair_sum_unsorted_one_pass(nums: list[int], target: int) -> list[int]:

    complement_to_index: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_to_index:
            return [complement_to_index[complement], i]
        complement_to_index[num] = i
    return []


print(pair_sum_unsorted_one_pass([1, 2, 3, 4, 5], 6))  # [1, 3]

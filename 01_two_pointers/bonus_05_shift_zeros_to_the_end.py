# Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

# On utilise 2 pointers staged
#   - left pointe l'endroit où le valeurs non nulles doivent être placées
#   - right point sur les valeurs non nulles

# Les 2 pointeurs à gauche
# On met right sur la première valeur non nulle
# On échange les valeurs
# On avance les 2 pointeurs de +1
# On déplace right jusqu'à la prochaine valeur non nulle et on boucle


# O(n), O(1)
# Car on parcourt le tableau une fois et on shift les valeurs en place


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

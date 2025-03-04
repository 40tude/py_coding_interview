# You are given an array of numbers
# Each representing the height of a vertical line
# Return the amount of water which the largest container can hold

# Je suis pas sûr de comprendre l'énoncé
# On met les pointeurs au début et à la fin
# On va à l'intérieur, on calcule la surface
# On avance le plus petit des 2 pointeurs
# On continue jusqu'à ce que les pointeurs se rencontrent

# O(n), O(1)
# Car on parcourt le tableau une fois et on alloue un nombre constant de variables


def largest_container(heights: list[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while left < right:
        # calculate the water contained between the 2 lines
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        # move the pointer with the shorter line inward
        # move both inward in cas of equality
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water


print(largest_container([2, 7, 8, 3, 7, 6]))  # 24
print(largest_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

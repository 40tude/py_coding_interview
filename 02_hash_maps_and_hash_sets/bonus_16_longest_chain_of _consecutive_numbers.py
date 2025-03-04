# Find the longest chain of consecutive numbers in an array.
# Two numbers are consecutive if they have a difference of 1.

# j'avais pas compris qu'on pouvait trier
# Brute force 1
#   On trie O(nlog(n)) et on parcourt

# Brut force 2
#   On peut considérer chaque valeur comme le début d'une chaine
#   Du coup on a une solution en O(n^3) c'est pire
#   n^3 car y a une boucle for, une boucle while et qu'à chaque tour de la boucle while on fait un "while (current_num + 1) in nums" en O(n)

# 1 - Au lieu de faire une recherche lineaire on va faire une recherche en O(1) en utilisant un hash set
# 2 - On va supprimer tous les faux départ en supprimant les valeurs pour lesquelles v-1 est dans le hash set
# On passe de O(n^3) à O(n)


# O(n), O(n)
# Même si il y a 2 boucles on est en O(n) car la boucle interne s'execute uniquement sur les departs de chaines
# Donc le nombre combiné d'iteration pour les 2 boucles est O(n)
# La boucle for tourne n fois, le boucle while tourne n fois
# On est en O(n+n) = O(n)
# En O(n) car on utilise un hash set pour stocker les valeurs
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

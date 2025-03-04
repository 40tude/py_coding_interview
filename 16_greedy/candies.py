def candies(ratings: list[int]) -> int:
    n = len(ratings)
    # ensure each child has at least 1 candy
    candies = [1] * n
    # first pass : left to right. For each child ensure the child i has more candies than the child to the left (i+1) if the rating is higher
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    # second pass : right to left. For each child ensure the child i has more candies than the child to the right if the rating is higher
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # if current child has more candies than the child to the right, then keep the current value
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


print(f"{candies([1, 3, 3])}")

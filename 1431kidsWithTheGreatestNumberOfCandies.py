def kidsWithCandies(candies: list, extraCandies: int) -> list:
	max_candies = max(candies)
	greatest_candies = [False] * len(candies)
	for i in range(len(candies)):
		if candies[i] + extraCandies >= max_candies:
			greatest_candies[i] = True
	return greatest_candies

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

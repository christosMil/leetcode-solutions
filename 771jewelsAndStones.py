def numJewelsInStones(jewels: str, stones: str) -> int:
	result = 0
	for i in stones:
		if i in jewels:
			result += 1
	return result

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

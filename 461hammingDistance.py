def hammingDistance(x: int, y: int) -> int:
	dist = 0
	while x != 0 or y != 0:
		if x%2 != y%2:
			dist += 1
		x, y = x//2, y//2
	return dist

x, y = 1, 4
print(x, y, hammingDistance(x, y))

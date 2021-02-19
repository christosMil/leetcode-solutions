def sumZero(n: int) -> list:
	result = [0] * n
	for i in range(1, n):
		if i%2 == 1:
			result[i] = i
		else:
			result[i] = 1-i
	if n%2 == 0:
		result[0] = -result[-1]
	return result

n = 5
print(n, sumZero(n))

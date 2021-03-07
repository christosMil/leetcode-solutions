def xorOperation(n: int, start: int) -> int:
	res = 0
	nums = []
	for i in range(n):
		nums.extend([start + 2*i])
		res ^= nums[i]
	return res

n, start = 5, 0
print(n, start, xorOperation(n, start))

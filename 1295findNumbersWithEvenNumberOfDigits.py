def findNumbers(nums: list) -> int:
	res = 0
	for i in nums:
		digits = 1
		while i//10:
			digits += 1
			i //= 10
		if digits % 2 == 0:
			res += 1
	return res

nums = [12,345,2,6,7896]
print(nums, findNumbers(nums))

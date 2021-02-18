def sumOfUnique(nums: list) -> int:
	hash_nums = {}
	for i in nums:
		if i not in hash_nums:
			hash_nums[i] = 1
		else:
			hash_nums[i] += 1
	return sum(i for i in hash_nums if hash_nums.get(i) == 1)

nums = [1,2,3,2]
print(nums, sumOfUnique(nums))

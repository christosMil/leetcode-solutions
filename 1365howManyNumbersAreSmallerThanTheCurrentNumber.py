def smallerNumbersThanCurrent(nums: list) -> list:
	res = [0]*len(nums)
	for i in range(len(nums)):
		for j in nums:
			if j < nums[i]:
				res[i] += 1
	return res

nums = [8,1,2,2,3]
print(nums, smallerNumbersThanCurrent(nums))

def runningSum(nums) -> list:
	sum = 0
	for i in range(1, len(nums)):
		nums[i] = nums[i] + nums[i-1]
	return nums

nums = [3,1,2,10,1]
print(nums)
print(runningSum(nums))

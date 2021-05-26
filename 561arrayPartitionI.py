def arrayPairSum(nums: list) -> int:
	nums.sort()
	s = 0
	for i in range(0, len(nums), 2):
		s += nums[i]
	return s

nums = [1,4,3,2]
print(nums, arrayPairSum(nums))

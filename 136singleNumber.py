def singleNumber(nums) -> int:
	nums.sort()
	if len(nums) == 1:
		return nums[0]
	if nums[0] != nums[1]:
		return nums[0]
	for i in range (0,len(nums)-1,2):
		if nums[i] != nums[i+1]:
			return nums[i]
	return nums[len(nums)-1]
        
nums = [4,4,2,2,1,1,3,3,5,5,18,81,18,99,103,81]
solution = singleNumber(nums)
print(nums)
print(solution)

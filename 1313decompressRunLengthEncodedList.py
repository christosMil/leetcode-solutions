def decompressRLElist(nums: list) -> list:
	result = []
	for i in range(0, len(nums), 2):
		for j in range(nums[i]):
			result.append(nums[i+1])
	return result

nums = [1,2,3,4]
print(nums, decompressRLElist(nums))

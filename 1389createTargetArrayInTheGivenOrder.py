def createTargetArray(nums: list, index: list) -> list:
	target = []
	for i in range(len(index)):
		if index[i] == i:
			target.extend([nums[index[i]]])
		else:
			target.extend([0])
			for j in range(len(target) - 1, index[i], -1):
				target[j] = target[j-1]
			target[index[i]] = nums[i]
	return target

nums, index = [0,1,2,3,4], [0,1,2,2,1]
print(nums, index, createTargetArray(nums, index))

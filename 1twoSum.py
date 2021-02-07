def twoSum(nums, target):
	for iIndex, iValue in enumerate(nums):
		for jIndex, jValue in enumerate(nums[iIndex+1:]):
			if iValue + jValue == target:
				return iIndex, jIndex+iIndex+1


testingList = [3,2,4]
testingTarget = 6
print(twoSum(testingList, testingTarget))

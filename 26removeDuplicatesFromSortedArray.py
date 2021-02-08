def removeDuplicates(nums) -> int:
	i = 0
	loop_termination = len(nums)-1
	while i < loop_termination:
		if nums[i] == nums[i+1]:
			nums.pop(i)
			loop_termination -= 1
		else:
			i += 1
	return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
print(removeDuplicates(nums))

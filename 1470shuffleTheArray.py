def shuffle(nums, n) -> list:
	x = nums[:n]
	y = nums[n:]
	for i in range(2*n):
		if i%2 == 0:
			nums[i] = x[int(i/2)]
		else:
			nums[i] = y[int((i-1)/2)]
	return nums

nums = [2,5,1,3,4,7]
n = 3
print(nums)
print(shuffle(nums, n))

def sumOddLengthSubarrays(arr: list) -> int:
	s = 0
	for i in range(1, len(arr) + 1, 2):
		for j in range(len(arr) + 1 - i):
			s +=  sum(arr[j:i+j])
	return s

arr = [1,4,2,5,3]
print(arr, sumOddLengthSubarrays(arr))

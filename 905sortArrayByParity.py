def sortArrayByParity(A: list) -> list:
	i, j = 0, len(A)-1
	while i < j:
		if A[i]%2 == 1:
			popped = A.pop(i)
			A.extend([popped])
			j -= 1
		else:
			i += 1
	return A

A = [3,1,2,4]
print(A, sortArrayByParity(A))

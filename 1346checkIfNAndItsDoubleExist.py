def checkIfExist(arr: list) -> bool:
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
				return True
	return False

arr = [10,2,5,3]
print(arr, checkIfExist(arr))

def replaceElements(arr: list) -> list:
	for i in range(len(arr)-1):
		arr[i] = max(arr[i+1:])
	arr[-1] = -1
	return arr

arr = [17,18,5,4,6,1]
print(arr, replaceElements(arr))

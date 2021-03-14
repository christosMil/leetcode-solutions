def oddCells(m: int, n: int, indices: list) -> int:
	arr = [[0] * n for i in range(m)]
	for i in indices:
		for j in range(n):
			arr[i[0]][j] += 1
		for j in range(m):
			arr[j][i[1]] += 1
	return sum(1 for i in arr for j in i if j%2 == 1)

m, n, indices = 2, 3, [[0,1],[1,1]]
print(m, n, indices, oddCells(m, n, indices))

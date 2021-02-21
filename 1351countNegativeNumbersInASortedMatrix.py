def countNegatives(grid: list) -> int:
	res = 0
	for i in range(len(grid) - 1, -1, -1):
		for j in range(len(grid[0]) -1, -1, -1):
			if grid[i][j] < 0:
				res += 1
			else:
				break;
		if j == len(grid[0]):
			break
	return res

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(grid, countNegatives(grid))

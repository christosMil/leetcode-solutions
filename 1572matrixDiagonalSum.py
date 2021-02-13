def diagonalSum(mat: list) -> int:
	result = 0
	for i in range(len(mat)):
		print(mat[i][i])
		result += mat[i][i]
		if i < len(mat)//2 and i != len(mat) - 1 - i:
			print(mat[i][len(mat)-1], mat[len(mat)-1][i])
			result += mat[i][len(mat)-1-i] + mat[len(mat)-1-i][i]
	return result

mat = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
print(diagonalSum(mat))

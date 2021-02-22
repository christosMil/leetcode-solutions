def countBalls(lowLimit: int, highLimit: int) -> int:
	digits = 0
	max_digits = [0] * (6*9 + 1)
	for i in range(lowLimit, highLimit + 1):
		digits = (i//100000) + ((i%100000)//10000) + ((i%10000)//1000) + ((i%1000)//100) + ((i%100)//10) + i%10
		max_digits[digits] += 1
	return max(max_digits)

lowLimit = 1
highLimit = 10
print(countBalls(lowLimit, highLimit))

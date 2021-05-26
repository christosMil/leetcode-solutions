from math import sqrt

def checkPerfectNumber(num: int) -> bool:
	if num == 1:
		return False
	s = 0
	for i in range(1, int(sqrt(num)) + 1):
		if num%i == 0:
			s += i + num//i
	return s - num == num

num = 28
print(num, checkPerfectNumber(num))

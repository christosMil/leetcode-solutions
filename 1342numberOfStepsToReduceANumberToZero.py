def numberOfSteps (num: int) -> int:
	i = 0
	while num != 0:
		i += 1
		if num%2 == 0:
			num //= 2
		else:
			num -= 1
	return i

num = 14
print(num, numberOfSteps(num))

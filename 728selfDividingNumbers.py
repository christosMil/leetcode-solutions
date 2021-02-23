def selfDividingNumbers(left: int, right: int) -> list:
	res = []
	digit = 0
	for i in range(left, right + 1):
		digit_counter = 0
		is_self_dividing_counter = 0
		for j in range(1, 4 + 1):
			if i >= 10**(j-1):
				digit_counter += 1
				digit = (i%(10**j))//(10**(j-1))
				if digit == 0 or i%digit != 0:
					break
				else:
					is_self_dividing_counter += 1
		if digit_counter == is_self_dividing_counter:
			res.extend([i])
	return res

left = 1
right = 22
print(left, right, selfDividingNumbers(left, right))

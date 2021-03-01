def subtractProductAndSum(n: int) -> int:
	n = list(str(n)) # it would have worked only with str casting, but list appers to be faster
	product = 1
	s = 0
	for i in n:
		s += int(i)
		product *= int(i)
	return product - s

n = 234
print(n, subtractProductAndSum(n))

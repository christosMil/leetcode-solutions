def balancedStringSplit(s: str) -> int:
	count = 0
	c_R = 0
	c_L = 0
	test_s = ""
	for i in s:
		test_s += i
		if i == "R":
			c_R += 1
		else:
			c_L += 1
		if c_R == c_L:
			count += 1
			c_R = c_L = 0
			test_s = ""
	return count

s = "RLRRLLRLRL"
print(s, balancedStringSplit(s))

def generateTheString(n: int) -> str:
	return "a"*(n - 1) + "a"*(n%2) + "b"*((n+1)%2)

n = 4
print(n, generateTheString(n))

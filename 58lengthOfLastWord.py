def lengthOfLastWord(s: str) -> int:
	length = 0
	if s.count(" ") == len(s):
		return 0
	while s[-1] == " ":
		s = s[:-1]
	for i in range(len(s) - 1, -1, -1):
		if s[i] != " ":
			length += 1
		else:
			break
	return length

s = "Hello World"
print(s, lengthOfLastWord(s))

def toLowerCase(string: str) -> str:
	my_set = set(string)
	for i in my_set:
		if 65 <= ord(i) <= 90:
			string = string.replace(i, chr(ord(i) + 32))
	return string

string = "Hello"
print(string, toLowerCase(string))

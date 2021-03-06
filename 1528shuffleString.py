def restoreString(s: str, indices: list) -> str:
	my_dict = {}
	for i, j in enumerate(s):
		my_dict[indices[i]] = j
	s = ""
	for i in range(len(indices)):
		s += my_dict[i]
	return s

s, indices = "codeleet", [4,5,6,7,0,2,1,3]
print(s, indices, restoreString(s, indices))

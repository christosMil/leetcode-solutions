def countConsistentStrings(allowed: str, words: list) -> int:
	res = 0
	for i in words:
		my_set = set(i)
		flag = True
		for s in my_set:
			if s not in allowed:
				flag = False
				break
		if flag:
			res += 1
	return res

allowed, words =  "ab", ["ad","bd","aaab","baa","badab"]
print(allowed, words, countConsistentStrings(allowed, words))

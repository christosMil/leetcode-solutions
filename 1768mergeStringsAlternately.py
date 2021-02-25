from itertools import zip_longest

def mergeAlternately(word1: str, word2: str) -> str:
	word3 = []
	for i, j in zip_longest(list(word1), list(word2)):
		if i != None:
			word3.extend([i])
		if j != None:
			word3.extend([j])
	return ''.join(word3)

word1, word2 =  "abc", "pqr"
print(word1, word2, mergeAlternately(word1, word2))

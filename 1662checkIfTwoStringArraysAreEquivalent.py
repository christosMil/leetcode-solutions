def arrayStringsAreEqual(word1: list, word2: list) -> bool:
	return ''.join(word1) == ''.join(word2)

word1, word2 = ["ab", "c"], ["a", "bc"]
print(word1, word2, arrayStringsAreEqual(word1, word2))

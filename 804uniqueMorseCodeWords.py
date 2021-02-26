from string import ascii_lowercase

def uniqueMorseRepresentations(words: list) -> int:
	morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	english_letters = list(ascii_lowercase)
	letter_to_code = dict(zip(english_letters, morse_code))
	res = [""]*len(words)
	for i in range(len(words)):
		word = list(words[i])
		coded = ""
		for j in word:
			coded += letter_to_code[j]
		res[i] = coded
	return len(set(res))

words = ["gin", "zen", "gig", "msg"]
print(words, uniqueMorseRepresentations(words))

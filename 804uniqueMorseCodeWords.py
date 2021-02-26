from string import ascii_lowercase

def uniqueMorseRepresentations(words: list) -> int:
	morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	english_letters = list(ascii_lowercase)
	letter_to_code = dict(zip(english_letters, morse_code))
	res = []
	for i in words:
		coded = ""
		for j in i:
			coded += letter_to_code[j]
		res.extend([coded])
	return len(set(res))

words = ["gin", "zen", "gig", "msg"]
print(words, uniqueMorseRepresentations(words))

def halvesAreAlike(s: str) -> bool:
	my_list_1 = list(s)
	my_list_2, my_list_1 = my_list_1[len(my_list_1)//2:], my_list_1[:len(my_list_1)//2]
	vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	s_1, s_2 = 0, 0
	for i in range(len(my_list_1)):
		if my_list_1[i] in vowels_list:
			s_1 += 1
		if my_list_2[i] in vowels_list:
			s_2 += 1
	return s_1 == s_2

s = "book"
print(s, halvesAreAlike(s))

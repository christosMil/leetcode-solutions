def diStringMatch(S: str) -> list:
	my_list, low, high = [], 0, len(S)
	for i in range(len(S)):
		if S[i] == "D":
			my_list.append(high)
			high -= 1
		else:
			my_list.append(low)
			low += 1
	my_list.append(low) # low should be equal to high at this point
	return my_list

S = "IDID"
print(S, diStringMatch(S))

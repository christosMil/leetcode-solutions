def decrypt(code: list, k: int) -> list:
	new_code = [0]*len(code)
	if k == 0:
		return new_code        
	for i in range(len(code)):
		if k > 0:
			if i+k+1 <= len(code):
				new_code[i] = sum(code[i+1:i+k+1])
			else:
				if i+1 <= len(code):
					new_code[i] = sum(code[i+1:]) + sum(code[:k-(len(code)-(i+1))])
				else:
					new_code[i] = sum(code[:k+1])
		else:
			if i+k >= 0:
				new_code[i] = sum(code[i+k:i])
			else:
				if i == 0:
					new_code[i] = sum(code[len(code)+k:])
				else:
					new_code[i] = sum(code[:i]) + sum(code[len(code)+k+i:])
	return new_code

code = [5,2,3,2,3,1]
k = 3
print(decrypt(code, k))

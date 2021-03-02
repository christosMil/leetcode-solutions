def decode(encoded: list, first: int) -> list:
	decoded = [first]
	for i in range(1, len(encoded) + 1):
		decoded.extend([decoded[i-1] ^ encoded[i-1]])
	return decoded

encoded, first = [1,2,3], 1
print(encoded, first, decode(encoded, first))

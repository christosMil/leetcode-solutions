def defangIPaddr(address: str) -> str:
	address = list(address)
	for i in range(len(address)):
		if address[i] == ".":
			address[i] = "[.]"
	return ''.join(address)

address = "1.1.1.1"
print(address, defangIPaddr(address))

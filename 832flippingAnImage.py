def flipAndInvertImage(image: list) -> list:
	for i in range(len(image)):
		for j in range(len(image)//2):
			image[i][j], image[i][len(image)-1-j] = image[i][len(image)-1-j] ^ 1, image[i][j] ^ 1
	if len(image) % 2 == 1:
		for i in range(len(image)):
			image[i][len(image)//2] ^= 1
	return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(image)
print(flipAndInvertImage(image))

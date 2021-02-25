def largestAltitude(gain) -> int:
	height_sum = 0
	highest = 0
	for i in range (len(gain)):
		height_sum += gain[i]
		if height_sum > highest:
			highest = height_sum
	return highest

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

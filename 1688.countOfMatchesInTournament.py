import math

def numberOfMatches(n: int) -> int:
	matches = 0
	teams = n
	for i in range(int(math.log(n,2))+1):
		if teams % 2 == 0:
			matches += int(teams/2)
			teams = int(teams/2)
		else:
			matches += int((teams-1)/2)
			teams = int((teams-1)/2 + 1)
	return matches

n = 5
print(numberOfMatches(n))

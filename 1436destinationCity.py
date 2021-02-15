def destCity(paths: list) -> str:
	for i in range(len(paths)):
		for j in range(len(paths)):
			if paths[i][1] == paths[j][0]:
				j -= 1 # use j as flag (decrement by 1 in case the destination city was not of the last pair)
				break
		if j == len(paths) - 1:
			return paths[i][1]

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))

def solution(myList) -> int:
	myList.sort()
	if len(myList) >= 2:
		result = myList[-1] - myList[-2]
		myList.remove(myList[-1])
		if result == 0:
			myList.remove(myList[-1])
		else:
			myList[-1] = result
		solution(myList)
	if len(myList) == 1:
		return myList[0]
	else:
		return 0




myList = [2,7,4,1,8,1]
myList.sort()
print (solution(myList))

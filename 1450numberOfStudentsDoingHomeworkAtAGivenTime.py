def busyStudent(startTime: list, endTime: list, queryTime: int) -> int:
	result = 0
	for i in range(len(startTime)):
		if startTime[i] <= queryTime <= endTime[i]:
			result += 1
	return result

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
print(busyStudent(startTime, endTime, queryTime))

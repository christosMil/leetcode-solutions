def countGoodRectangles(rectangles: list) -> int:
	max_len = 0
	max_count = 0
	for i in rectangles:
		if max_len < min(i):
			max_len = min(i)
			max_count = 1
		elif max_len == min(i):
			max_count += 1
	return max_count

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(rectangles, countGoodRectangles(rectangles))

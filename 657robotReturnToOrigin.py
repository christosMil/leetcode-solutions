def judgeCircle(moves: str) -> bool:
	move_dict = {"R": 0, "L": 0, "U": 0, "D": 0}
	for i in moves:
		move_dict[i] += 1
	if move_dict["R"] == move_dict["L"] and move_dict["U"] == move_dict["D"]:
		return True
	return False

moves = "LDRRLRUULR"
print(judgeCircle(moves))

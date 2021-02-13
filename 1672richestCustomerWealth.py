def maximumWealth(accounts: list) -> int:
	max_wealth = 0
	for i in accounts:
		if max_wealth < sum(i):
			max_wealth = sum(i)
	return max_wealth

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(accounts))

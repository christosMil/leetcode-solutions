def countMatches(items: list, ruleKey: str, ruleValue: str) -> int:
	count = 0
	if ruleKey == "type":
		ruleKey = 0
	elif ruleKey == "color":
		ruleKey = 1
	else:
		ruleKey = 2
	for i in items:
		if i[ruleKey] == ruleValue:
			count += 1
	return count

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey, ruleValue = "color", "silver"
print(items, ruleKey, ruleValue, countMatches(items, ruleKey, ruleValue))

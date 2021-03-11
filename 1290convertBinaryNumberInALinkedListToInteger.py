class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class Solution:
	def getDecimalValue(self, head: ListNode) -> int:
		my_list, s = [head.val], 0
		while head.next != None:
			my_list.append(head.next.val)
			head = head.next
		for i in range(len(my_list) - 1):
			s += (2*my_list[i])**(len(my_list) - 1 - i)
		return s + my_list[len(my_list) - 1]

head = ListNode(1, ListNode(0, ListNode(1)))
print(Solution().getDecimalValue(head))

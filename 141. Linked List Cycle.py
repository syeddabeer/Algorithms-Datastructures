#141. Linked List Cycle
class ListNode:
	def __init__(self, val, tail=None):
		self.val = val
		self.next = tail 

class Solution:
	def hasCycle(self, head):
		if head is None:
			return False

		seen = set()
		while head is not None:
			if head not in seen:
				seen.add(head)
			else:
				return True
			head = head.next
		return False
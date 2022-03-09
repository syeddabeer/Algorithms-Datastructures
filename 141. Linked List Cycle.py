#141. Linked List Cycle
class ListNode:
	def __init__(self, val, tail=None):
		self.val = val
		self.next = tail 

class Solution:
	def hasCycle(self, head):
# Reverse Linked List II
"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""
# class ListNode:
# 	def __init__(self, val=0, next=None):
# 		self.val = val 
# 		self.next = next
class Solution:
	def reverseBetween(self, head, m, n):
		if not head:
			return None
		# Move the two pointers until they reach the proper starting point
        # in the list.

        cur, prev = head, None

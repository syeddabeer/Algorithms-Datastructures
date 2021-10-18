"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

"""
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val=val
		self.left=left
		self.right=right
"""

class Solution:
	# determines the height recursively using 1+max(func(root.left), func(root.right))
	def height(self, root):
		if not root:
			return -1
		return 1+max(self.height(root.left), self.height(root.right))

	def isBalanced(self, root):
		if not root:
			return True

		return abs(self.height(root.left) - self.height(root.right)) < 2 \
				and self.isBalanced(root.left) \
				and self.isBalanced(root.right)



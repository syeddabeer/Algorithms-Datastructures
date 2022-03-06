#655. Print Binary Tree
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val 
		self.left = left 
		self.right = right
class Solution:
	def printTree(self, root):
		if root is None:
			return None

		def maxDepth(node):
			if node is None:
				return 0
			else:
				leftDepth = maxDepth(node.left)
				rightDepth = maxDepth(node.right)
				depthIncludingNode = max(leftDepth, rightDepth)+1
				return depthIncludingNode

		height = maxDepth(root)-1
		cols = pow(2, height+1)-1
		res = [["" for _ in range(cols)] for _ in range(height+1)]

		def dfs(node, row, col):
			if node is None: return
			res[int(row)][int(col)] = str(node.val)
			dfs(node.left, row+1, (col - pow(2, height-row-1)))
			dfs(node.right, row+1, (col+pow(2, height-row-1)))

		dfs(root, 0, (cols-1)/2)
		return res 

"""
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]

 Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
"""

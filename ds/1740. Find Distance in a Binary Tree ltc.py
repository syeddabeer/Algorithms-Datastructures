#1740. Find Distance in a Binary Tree

class Solution:
	def findDistance(self, root, p, q):
		# here we use concept of lowest common ancestor and distance between p, q and lca
		def dfs(node):
			if node is None or node.val == p or node.val == q:
				return node 
			left = dfs(node.left)
			right = dfs(node.right)
			if left and right:
				return node 
			else:
				return left or right

		def dist(node, target):
			if node is None:
				return float('inf')
			if node.val == target:
				return 0
			return 1 + min((dist(node.left, target)), (dist(node.right, target)))

		lca = dfs(root)
		return dist(lca, p) + dist(lca, q)
"""
Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.
The distance between two nodes is the number of edges on the path from one to the other.
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.
Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.
"""
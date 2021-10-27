#Boundary of a binary tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def __init__(self):
		# initializing the arrays to concat at the final stage
		self.left=[]
		self.right=[]
		self.children=[]

	def left_boundary(self, root):
		if not root:
			return

		if root.left is None and root.right is None:
			return

		# if one of above condition fails
		self.left.append(root.val)

		if root.left:
			self.left_boundary(root.left)
		else:
			self.left_boundary(root.right)

	def right_boundary(self, root):
		if not root:
			return

		if root.left is None and root.right is None:
			return

		self.right.append(root.val)

		if root.right:
			self.right_boundary(root.right)

		else:
			self.right_boundary(root.left)

	def children_boundary(self, root, head):
		if not root:
			return

		if root!=head and root.left is None and root.right is None: #leaf node
			self.children.append(root.val)
			return

		self.children_boundary(root.left, head)
		self.children_boundary(root.right, head)

	def boundaryOfBinaryTree(self, root):
		res = []
		res.append(root.val)
		self.left_boundary(root.left)
		self.children_boundary(root, root)
		self.right_boundary(root.right)

		res += self.left + self.children + self.right[::-1]
		return res
		

"""
The boundary of a binary tree is the concatenation of the root, 
the left boundary, the leaves ordered from left-to-right, and 
the reverse order of the right boundary.
The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a 
left child, then the left boundary is empty. If a node in the left boundary and 
has a left child, then the left child is in the left boundary. If a node is in 
the left boundary, has no left child, but has a right child, then the right 
child is in the left boundary.The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side 
 the root's right subtree. Again, the leaf is not part of the right boundary, 
 and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, 
the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
"""
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None 

	def __contains__(self, target):
		if self.left and target < self.value :
			return self.left.__contains__(target)
		elif self.right and target > self.value:
			return self.right.__contains__(target)
		else:
			print("Found it")
			return self
		print("value is not in the tree.")        
		return False

	def traversePreorder(self):
		# preorder: Root -> Left -> Right
		# print("in preorder loop")
		print(self.value)
		if self.left:
			self.left.traversePreorder()
		if self.right:
			self.right.traversePreorder()

	def traverseInorder(self):
		# inorder: Left -> Root -> Right
		if self.left:
			self.left.traverseInorder()
		print(self.value)
		if self.right:
			self.right.traverseInorder()

	def traversePostorder(self):
		# postorder: Left -> Right -> Root
		if self.left:
			self.left.traversePostorder()
		if self.right:
			self.right.traversePostorder()
		print(self.value)

	#function associated with problem statement
	def getNodesAtDepth(self, depth, nodes=[]):
		# boundary condition. 
		# Also, reference condition for recursion
		if depth == 0:
			nodes.append(self.value)
			return nodes

		if self.left:
			self.left.getNodesAtDepth(depth-1, nodes)
		else:
			nodes.extend([None]*2**(depth-1))
		if self.right:
			self.right.getNodesAtDepth(depth-1, nodes)
		else:
			nodes.extend([None]*2**(depth-1))
		return nodes

	def height(self, h=0):
		leftHeight = self.left.height(h+1) if self.left else h
		rightHeight = self.right.height(h+1) if self.right else h
		return max(leftHeight, rightHeight)


class Tree:
	def __init__(self, root, name=''):
		self.root = root
		self.name = name 
	def __contains__(self, target):
		return self.root.__contains__(target)

	def traversePreorder(self):
		# print("preorder wrapper")
		self.root.traversePreorder()

	def traverseInorder(self):
		self.root.traverseInorder()

	def traversePostorder(self):
		self.root.traversePostorder()

	def height(self):
		return self.root.height()

	def getNodesAtDepth(self, depth):
		return self.root.getNodesAtDepth(depth, [])

#driver code
node=Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left=Node(13)
node.right.right=Node(10000)

myTree=Tree(node, 'Dab\'s tree')
print(myTree.root.left.value)
print(myTree.root.right.right.value)

# found=myTree.__contains__(10000)
# print(found.value)

print("traverse Preorder")
myTree.traversePreorder()

print("traverse Inorder")
myTree.traverseInorder()

print("traverse Postorder")
myTree.traversePostorder()


#LLearning


print("myTree.root.height(): ", myTree.root.height())

tree2=Tree(Node(50), 'A very short tree')
print("tree2.root.height(): ", tree2.root.height())


tree3=Tree(Node(50), 'Get all nodes at Depth')
tree3.root.left = Node(25)
tree3.root.right = Node(75)
tree3.root.left.left = Node(13)
tree3.root.left.right = Node(35)
tree3.root.left.right.right = Node(37)
tree3.root.right.left = Node(55)
tree3.root.right.right = Node(103)
tree3.root.left.left.left = Node(2)
tree3.root.left.left.right = Node(20)
tree3.root.right.right.left = Node(55)
tree3.root.right.right.right = Node(256)
print(tree3.getNodesAtDepth(2))
print(tree3.getNodesAtDepth(3))








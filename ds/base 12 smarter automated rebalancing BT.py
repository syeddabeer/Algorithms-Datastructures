# print the tree in the terminal
# display all nodes in the tree, display connections between them.
# handle depth of 5
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

	#function associated with problem statement
	def add(self, value):
		if value < self.value :
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.add(value)
				#change associated with problem statement
				self.left = self.left.fixImbalanceIfExists()
		elif value > self.value :
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.add(value)
				#change associated with problem statement
				self.right = self.right.fixImbalanceIfExists()
		else:
			return 

	
	def findMin(self):
		if self.left:
			return self.left.findMin()
		return self.value

	#function associated with problem statement
	def delete(self, target):
		if self.value == target:
			#do the deletion here
			if self.left and self.right:
				#RTFM Right tree find minimum
				minValue = self.right.findMin()
				self.value = minValue
				self.right = self.right.delete(minValue)
				return self
			else:
				return self.left or self.right

		if self.right and target > self.value:
			self.right = self.right.delete(target)

		if self.left and target < self.value:
			self.left = self.left.delete(target)
		return self.fixImbalanceIfExists()

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

	def getNodesAtDepth(self, depth, nodes=[]):
		# boundary condition. 
		# Also, reference condition for recursion
		if depth == 0:
			#nodes.append(self.value)
			nodes.append(self)
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

	
	def isBalanced(self):
		leftHeight = self.left.height()+1 if self.left else 0
		rightHeight = self.right.height()+1 if self.right else 0
		return abs(leftHeight - rightHeight)<2

	def getLeftRightHeightDifference(self):
		leftHeight = self.left.height()+1 if self.left else 0
		rightHeight = self.right.height()+1 if self.right else 0
		return leftHeight - rightHeight

	def fixImbalanceIfExists(self):
		if self.getLeftRightHeightDifference() > 1:
			#left imbalance
			if self.left.getLeftRightHeightDifference() > 0:
				# left left imbalance
				return rotateRight(self)
			else:
				# left right imbalance
				self.left = rotateLeft(self.left)
				return rotateRight(self)
		elif self.getLeftRightHeightDifference() < -1:
			# right imbalance
			if self.right.getLeftRightHeightDifference() < 0:
				#right right imbalance
				return rotateLeft(self)
			else:
				#right left imbalance
				self.right = rotateRight(self.right)
				return rotateLeft(self)
		return self

	def rebalance(self):
		if self.left:
			self.left.rebalance()
			self.left = self.left.fixImbalanceIfExists()

		if self.right:
			self.right.rebalance()
			self.right = self.right.fixImbalanceIfExists()

	def toStr(self):
		if not self.isBalanced():
			return str(self.value)+'*'
		return str(self.value)


class Tree:
	def __init__(self, root, name=''):
		self.root = root
		self.name = name

	def __contains__(self, target):
		return self.root.__contains__(target)

	#function associated with problem statement
	def add(self, value):
		self.root.add(value)	
		#change
		self.root = self.root.fixImbalanceIfExists()	

	#function associated with problem statement
	def delete(self, target):
		self.root = self.root.delete(target)

	def traversePreorder(self):
		# print("preorder wrapper")
		self.root.traversePreorder()

	def traverseInorder(self):
		self.root.traverseInorder()

	def traversePostorder(self):
		self.root.traversePostorder()

	def getNodesAtDepth(self, depth):
		return self.root.getNodesAtDepth(depth, [])

	def height(self):
		return self.root.height()
	
	def _nodeToChar(self, n, spacing):
		if n is None:
			return '_'+(' '*spacing)
		#spacing = spacing-len(str(n))+1
		spacing = spacing-len(n.toStr())+1
		return n.toStr()+(' '*spacing)
	
	def print(self, label=''):
		print(self.name+' '+label)
		height=self.root.height()
		spacing=3
		width=int((2**height-1)*(spacing+1)+1)
		#Root ofset
		offset = int((width-1)/2)
		for depth in range(0, height+1):
			if depth>0:
				#print directional lines
				print(' '*(offset+1) + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
			row = self.root.getNodesAtDepth(depth, [])
			print((' '*(offset) + ''.join([self._nodeToChar(n, spacing) for n in row])))
			spacing = offset+1
			offset = int(offset/2)-1
		print('')	

	
	def rebalance(self):
		self.root.rebalance()
		self.root = self.root.fixImbalanceIfExists()

def rotateRight(root):
	pivot = root.left
	reattachNode = pivot.right
	root.left = reattachNode
	pivot.right = root
	return pivot

def rotateLeft(root):
	pivot = root.right
	reattachNode = pivot.left
	root.right = reattachNode
	pivot.left = root
	return pivot

#driver code
unbalancedLeftLeft = Tree(Node(30), 'UNBALANCED LEFT LEFT')
unbalancedLeftLeft.root.left = Node(20)
unbalancedLeftLeft.root.left.right = Node(21)
unbalancedLeftLeft.root.left.left = Node(10)
unbalancedLeftLeft.root.left.left.left = Node(9)
unbalancedLeftLeft.root.left.left.right = Node(11)
unbalancedLeftLeft.print()
unbalancedLeftLeft.root = rotateRight(unbalancedLeftLeft.root)
unbalancedLeftLeft.print()

#driver code
unbalancedRightRight = Tree(Node(10), 'UNBALANCED Right Right')
unbalancedRightRight.root.right = Node(20)
unbalancedRightRight.root.right.left = Node(19)
unbalancedRightRight.root.right.right = Node(30)
unbalancedRightRight.root.right.right.left = Node(29)
unbalancedRightRight.root.right.right.right = Node(31)
unbalancedRightRight.print()
unbalancedRightRight.root = rotateLeft(unbalancedRightRight.root)
unbalancedRightRight.print()

unbalancedLeftRight = Tree(Node(30), 'UNBALANCED LEFT Right')
unbalancedLeftRight.root.right = Node(31)
unbalancedLeftRight.root.left = Node(10)
unbalancedLeftRight.root.left.right = Node(20)
unbalancedLeftRight.root.left.left = Node(9)
unbalancedLeftRight.root.left.right.left = Node(19)
unbalancedLeftRight.root.left.right.right = Node(21)
unbalancedLeftRight.print()
unbalancedLeftRight.root.left = rotateLeft(unbalancedLeftRight.root.left)
unbalancedLeftRight.root = rotateRight(unbalancedLeftRight.root)
unbalancedLeftRight.print()

unbalancedRightLeft = Tree(Node(30), 'UNBALANCED Right LEFT')
unbalancedRightLeft.root.left = Node(31)
unbalancedRightLeft.root.right = Node(10)
unbalancedRightLeft.root.right.left = Node(20)
unbalancedRightLeft.root.right.right = Node(9)
unbalancedRightLeft.root.right.left.right = Node(19)
unbalancedRightLeft.root.right.left.left = Node(21)
unbalancedRightLeft.print()
unbalancedRightLeft.root.right = rotateRight(unbalancedRightLeft.root.right)
unbalancedRightLeft.root = rotateLeft(unbalancedRightLeft.root)
unbalancedRightLeft.print()


treeImbalanced = Tree(Node(50), 'UNBALANCED')
treeImbalanced.root.left = Node(25)
treeImbalanced.root.right = Node(75)
treeImbalanced.root.left.left = Node(10)
treeImbalanced.root.left.right = Node(35)
treeImbalanced.root.left.right.left = Node(30)
treeImbalanced.root.left.left.left = Node(5)
treeImbalanced.root.left.left.right = Node(13)
treeImbalanced.root.left.left.left.left = Node(2)
treeImbalanced.root.left.left.left.left.left = Node(1)
treeImbalanced.print()
treeImbalanced.rebalance()
treeImbalanced.print()

#drivernode
Autotree = Tree(Node(50))
Autotree.add(25)
Autotree.print()
Autotree.add(75)
Autotree.print()
Autotree.add(10)
Autotree.print()
Autotree.add(35)
Autotree.print()
Autotree.add(30)
Autotree.print()
Autotree.add(5)
Autotree.print()
Autotree.add(2)
Autotree.print()
Autotree.add(1)
Autotree.print()
Autotree.delete(50)
Autotree.print()
Autotree.delete(75)
Autotree.print()

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

tree3.print()

# tree3.add(10)
# tree3.print()

tree3.delete(75)
tree3.print()

print(f"is Balanced yes or no: {tree3.root.isBalanced()}")
print(f"is Balanced yes or no: {tree3.root.left.isBalanced()}")




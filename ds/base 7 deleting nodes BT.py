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

	def add(self, value):
		if value < self.value :
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.add(value)
		elif value > self.value :
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.add(value)
		else:
			return 

	#function associated with problem statement
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
		return self

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

	def add(self, value):
		self.root.add(value)		

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
		spacing = spacing-len(str(n))+1
		return str(n)+(' '*spacing)
	
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

tree3.print()

# tree3.add(10)
# tree3.print()

tree3.delete(75)
tree3.print()




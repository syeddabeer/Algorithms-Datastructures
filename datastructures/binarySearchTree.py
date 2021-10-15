# binary search tree
"""
Binary Search Tree (BST) on the other hand, is a special form of Binary Tree data structure 
where each node has a comparable value, and smaller valued children attached to left and 
larger valued children attached to the right.
"""

"""
O(log n) - for search, remove, add
O(n) - for iteration
"""

"""
	Author: Dabeeruddin Syed
    Code based on class of George Heineman
    The code uses recursion a lot.
    root, left, right are pointers. 
"""
class BinaryNode:

	# first function
    def __init__(self, value):
        """Create binary node."""
        self.value   = value
        # left and right are pointers here. Also, root is a pointer.
        self.left    = None
        self.right   = None

    # IV function - when self.root.add function is called.
    def add(self, val):
        """
        Add a new node to the tree with value. Respond based on Set semantics, less equal or greater than.
        """
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
        elif val > self.value:
            self.right = self.addToSubTree(self.right, val)

    # V function - when self.root.add function is called.
    def addToSubTree(self, parent, val):
        """Add val to parent subtree (if exists) and return root of that subtree."""
        if parent is None:
            return BinaryNode(val)

        parent.add(val)
        return parent

    # VII function - when self.root.remove function is called.
    # add the element with the largest value from the left sub tree
    def remove(self, val):
        """
         Remove val of self from BinaryTree. 
        """
        if val < self.value:
            self.left = self.removeFromParent(self.left, val)
        elif val > self.value:
            self.right = self.removeFromParent(self.right, val)
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right
            
            childKey = child.value;
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey;
        
        return self

    # VIII function
    def removeFromParent(self, parent, val):
        """Helper method for remove. Ensures proper behavior when removing node that 
        has children."""
        if parent:
            return parent.remove(val)
        return None

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
        if self.right:
            rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"

    def inorder(self):
        """In order traversal generator of tree rooted at given node."""
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

class BinaryTree:
	# II function
    def __init__(self):
        """Create empty binary tree."""
        self.root = None
   	
   	# III function
    def add(self, value):
        """Insert value into proper location in Binary Tree."""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    # VI function
    def remove(self, val):
        """Remove value from tree."""
        if self.root:
            self.root = self.root.remove(val)

    def getMin(self):
        """Returns minimum value."""
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.left != None:
            n = n.left
        return n.value

    def getMax(self):
        """Returns maximum value."""
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        n = self.root
        while n.right != None:
            n = n.right
        return n.value
    
    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if target < node.value :
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
                
        return False

    def closest(self, target):
        """
        Return value closest to target. If there are several, then
        return one of them.
        """
        if self.root is None:
            return None
        
        best = node = self.root
        distance = abs(self.root.value - target)
        while node:
            if abs(node.value - target) < distance:
                distance = abs(node.value - target)
                best = node
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return target

        return best.value

    def __iter__(self):
        """In order traversal of elements in the tree."""
        if self.root:
            for e in self.root.inorder():
                yield e

    def __repr__(self):
        if self.root is None:
            return "binary:()"
        return "binary:" + str(self.root)

"""
Change Log:
-----------

"""

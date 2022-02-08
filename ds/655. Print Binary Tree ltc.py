class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        
class Solution:
    def printTree(self, root):
        def height(node):
            if not node:
                return -1
            return max(height(node.left), height(node.right))+1
        
        self.ht = height(root)
        #rows
        m = self.ht + 1
        # columns
        n = 2**(self.ht+1) - 1
        
        self.matrix = [["" for j in range(n)] for i in range(m)]
        def tre(root, c, i):
            if root:
                self.matrix[i][c] = str(root.val)
                tre(root.left, c-2**(self.ht-i-1), i+1)
                tre(root.right, c+2**(self.ht-i-1), i+1))
        tre(root, n//2, 0)
        return self.matrix
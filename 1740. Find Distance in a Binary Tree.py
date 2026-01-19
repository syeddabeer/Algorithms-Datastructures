# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if not root:
            return 0
        def ancestor(root, p, q):
            if not root:
                return 0
            if root.val==p or root.val==q:
                return root
            left = ancestor(root.left, p, q)
            right = ancestor(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        def dfs(node, target, distance):
            if not node:
                return 0
            if node.val==target:
                return distance
            left = dfs(node.left, target, distance+1)
            right = dfs(node.right, target, distance+1)
            return left if left else right
        node = ancestor(root, p, q)
        return dfs(node, p , 0) + dfs(node, q, 0)

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
Constraints:
The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
All Node.val are unique.
p and q are values in the tree.
"""
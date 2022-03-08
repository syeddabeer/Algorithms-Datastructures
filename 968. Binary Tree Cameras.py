#968. Binary Tree Cameras

class Solution(object):
    def minCameraCover(self, root):
        self.result = 0
        covered={None}
        
        def dfs(node, par=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if ((par is None and node not in covered) or 
                    (node.left not in covered) or (node.right not in covered)):
                    self.result+=1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.result

"""
Complexity Analysis: (O(N), O(H))

Time Complexity: O(N), where NN is the number of nodes in the given tree.

Space Complexity: O(H), where HH is the height of the given tree.
"""
"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
"""
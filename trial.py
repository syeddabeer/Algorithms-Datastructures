class Solution:
    def findDistance(self, root, p, q):
        def dfs(node): # lowest common ancestor
            if node is None or node.val==p or node.val==q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node 
            else:
                return left or right

        def dist(node, target):
            if not node:
                return float('inf')
            if node.val==target:
                return 0
            return 1+min(dist(node.left, target), dist(node.right, target))
            
        lca = dfs(root)
        return dist(lca, p) + dist(lca, q)

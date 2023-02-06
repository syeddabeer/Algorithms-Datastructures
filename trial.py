<<<<<<< HEAD
import pandas as pd

df = pd.Dataframe(index=range(0,10,1))
=======
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


class Tree:
    def zigzagLevelOrder(self, root):
        if root is None:
            return

        results = []

        def dfs(node, level):
            if node is None:
                return
            elif level>=len(results):
                results.append([node.val])
            elif level%2==0: # even left to right
                results[level].extend([node.val])
            elif level%2!=0:
                results[level].insert(0, node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)


        dfs(root, 0)
        return results
>>>>>>> e132628f3693ed40c5ea9055a6c79f8266196bae

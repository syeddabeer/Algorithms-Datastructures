from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        i=1

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()
            print("i=", i, ":", "curr_node: ", curr_node, "\n")

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret


# [3,9,20,null,null,15,7]
# node_queue at the start:  
#  deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}, None]) 

# i= 1 : curr_node:  
#  TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}} 

# node_queue:  deque([None]) 

# j= 1 : level_list:  deque([3]) 
#  curr_node:  TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}} 

# node_queue:  deque([None, TreeNode{val: 9, left: None, right: None}, TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}]) 

# i= 2 : curr_node:  
#  None 

# node_queue:  deque([TreeNode{val: 9, left: None, right: None}, TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}]) 

# goes to else block, node_queue gets appended with none

# i= 3 : curr_node:  
#  TreeNode{val: 9, left: None, right: None} 

# node_queue:  deque([TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, None]) 

# j= 2 : level_list:  deque([9]) 
#  curr_node:  TreeNode{val: 9, left: None, right: None} 

# node_queue:  deque([TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, None]) 

# i= 4 : curr_node:  
#  TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}} 

# node_queue:  deque([None]) 

# j= 3 : level_list:  deque([20, 9]) 
#  curr_node:  TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}} 

# node_queue:  deque([None, TreeNode{val: 15, left: None, right: None}, TreeNode{val: 7, left: None, right: None}]) 

# i= 5 : curr_node:  
#  None 

# node_queue:  deque([TreeNode{val: 15, left: None, right: None}, TreeNode{val: 7, left: None, right: None}]) 

# i= 6 : curr_node:  
#  TreeNode{val: 15, left: None, right: None} 

# node_queue:  deque([TreeNode{val: 7, left: None, right: None}, None]) 

# j= 4 : level_list:  deque([15]) 
#  curr_node:  TreeNode{val: 15, left: None, right: None} 

# node_queue:  deque([TreeNode{val: 7, left: None, right: None}, None]) 

# i= 7 : curr_node:  
#  TreeNode{val: 7, left: None, right: None} 

# node_queue:  deque([None]) 

# j= 5 : level_list:  deque([15, 7]) 
#  curr_node:  TreeNode{val: 7, left: None, right: None} 

# node_queue:  deque([None]) 

# i= 8 : curr_node:  
#  None 

# node_queue:  deque([]) 


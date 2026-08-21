# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if root is None:
            return []
        queue = [root]
        def bfs(root):
            while queue:
                level_store = []
                size = len(queue) # these need to reset every time
                for _ in range(size): # we need this to make sure the inner arrays are correct; allows us to cut off even when we're continually adding to the queue

                    current_node = queue.pop(0) # keep the node to check left and right later, remove now so we don't read the size wrong
                    level_store.append(current_node.val)

                    if current_node.left: # this is in the for loop before we want to get all the children of the nodes within the size boundry before doing this again
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)

                res.append(level_store)
        
        bfs(root)

        return res



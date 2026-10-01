# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(log n)?
# BST Inorder DFS gives sorted order
# run dfs until k iterations

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val
        def dfs(node):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            if count == 0: # for bubbling up the answer
                return
            count -= 1
            if count == 0: # we found the node!
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res


            

            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []

        def dfs(root, original_list):
            if not root:
                original_list.append(None)
                return
            
            original_list.append(root.val)
            dfs(root.right, original_list)
            dfs(root.left, original_list)

        dfs(p, p_list)
        dfs(q, q_list)
        
        if p_list == q_list:
            return True
        else:
            return False
            
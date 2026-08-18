# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the lowest common ancestor is when we split up trying to find the p or q
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val: # p and q are bigger than current root, then we just have to look in the right subtree and then make the left node the curr root
                curr = curr.right
            
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else: # if we need to split up at ANY moment or end up finding the value p or q
                return curr

        

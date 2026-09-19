# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use the same level technique but just process only the last node of the current queue/level
#bfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(root):
            if root is None:
                return res

            queue = [root]
            while queue:
                n = len(queue)
                res.append(queue[-1].val)
                for _ in range(n):
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)

                    queue.pop(0)
        
        bfs(root)

        return res

q = [1]
n = 1
i = 0
res = [1]
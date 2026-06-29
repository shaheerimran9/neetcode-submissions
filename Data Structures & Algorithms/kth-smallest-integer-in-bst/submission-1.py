# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = 0

        def dfs(node):
            if not node or self.count < 1:
                return

            dfs(node.left)

            if self.count == 1:
                self.res = node.val
                self.count = 0
                return
                
            self.count -= 1
            dfs(node.right)
        dfs(root)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float("-inf")
        def dfs(root = root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, root.val + left, root.val + right, root.val, root.val + right + left)
            return max(0, root.val, left + root.val, right + root.val)
        
        dfs()
        return self.res
            
        
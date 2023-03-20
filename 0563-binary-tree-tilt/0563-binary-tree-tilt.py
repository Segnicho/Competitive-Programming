# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root = root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            temp = root.val  + left + right
            root.val = abs(right - left)
            self.res += root.val
            return temp
        dfs(root)
        return self.res
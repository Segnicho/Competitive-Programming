# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(rt1 = root1, rt2 = root2):
            if not rt1 or not rt2:
                return rt1 == rt2 == None
            return rt1.val == rt2.val and (dfs(rt1.left, rt2.left) and            dfs(rt1.right, rt2.right) or dfs(rt1.left, rt2.right) and             dfs(rt1.right, rt2.left))
        
        return dfs()
    
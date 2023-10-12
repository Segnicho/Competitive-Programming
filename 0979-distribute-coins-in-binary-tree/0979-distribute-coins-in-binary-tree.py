# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def recur(node):
            if not node:
                return 0
        
            left = recur(node.left)
            right = recur(node.right)
            self.res += abs(left) + abs(right)
            return node.val -1 + left + right
        
        recur(root)
        return self.res
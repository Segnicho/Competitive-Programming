# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            left, right = dfs(node.left), dfs(node.right)
            
            robNode = node.val + left[1] + right[1]
            donRobNode = max(left) +  max(right)
            return (robNode, donRobNode)
        
        return max(dfs(root))
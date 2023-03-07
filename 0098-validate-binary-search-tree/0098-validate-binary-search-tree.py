# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validBST(node):
            if not node:
                return True
            if not validBST(node.right):
                return False
            if node.val >= self.prev:
                return False
            self.prev = node.val
            return validBST(node.left) 
        self.prev = float("inf")
        return validBST(root)

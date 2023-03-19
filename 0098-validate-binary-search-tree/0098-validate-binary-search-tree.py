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
            if not validBST(node.left):
                return False
            if self.prev >= node.val:
                return False
            self.prev = node.val
            return validBST(node.right) 
        self.prev = float("-inf")
        return validBST(root)
    
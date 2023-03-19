# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.currSum  = 0
        def convert(node = root):
            
            if not node:
                return 0
            convert(node.right)
            self.currSum += node.val
            node.val = self.currSum
            convert(node.left)
        convert()
        return root
    
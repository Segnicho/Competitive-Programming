# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def recur(root):
            if not root:
                return [0, 0]
            
            left = recur(root.left)
            right = recur(root.right) 
            
            avg = (left[0] + right[0] + root.val)//(left[1] + right[1] + 1)
            if avg  == root.val:
                self.res += 1
            return [left[0] + right[0] + root.val, left[1] + right[1] + 1]
        
        self.res = 0
        recur(root)
        return self.res
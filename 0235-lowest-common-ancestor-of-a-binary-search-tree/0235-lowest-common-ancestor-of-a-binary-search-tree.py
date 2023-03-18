# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recur(root):
            if q.val < root.val and p.val < root.val:
                return recur(root.left)
            elif q.val > root.val and p.val > root.val:
                return recur(root.right)
            else:
                return root
            
        return  recur(root)
    
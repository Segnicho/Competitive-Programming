# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recur( root, p, q):
            if q.val < root.val and p.val < root.val:
                return recur(root.left, p, q)
            elif q.val > root.val and p.val > root.val:
                return recur(root.right, p, q)
            else:
                return root
        return  recur(root, p, q)